"""Public feeds of hackathons, conferences and research deadlines.

Structured feeds come first because they cannot invent an event: Devpost's JSON API, MLH's
season page (schema.org Event markup), confs.tech's conference data on GitHub, and
ccfddl's research deadlines. Parsers are pure; `collect_*` fetch and parse.
"""

import html
import json
import re
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from typing import Any

from internship_agent.opportunities.schemas import Opportunity, OpportunityKind

DEVPOST = "https://devpost.com/api/hackathons?status[]=upcoming&status[]=open&page={page}"
MLH = "https://www.mlh.com/seasons/{season}/events"
CONFS_TECH = (
    "https://raw.githubusercontent.com/tech-conferences/conference-data/main/"
    "conferences/{year}/{topic}.json"
)
CCFDDL = "https://ccfddl.com/conference/allconf.json"

# ccfddl's area codes.
AREAS = {
    "AI": "Artificial intelligence",
    "SE": "Software engineering",
    "HI": "Human-computer interaction",
    "DB": "Databases and data mining",
    "MX": "Interdisciplinary",
    "NW": "Networking",
    "SC": "Security",
    "DS": "Systems and architecture",
    "CT": "Theory",
    "CG": "Graphics and multimedia",
}
# shortcut: only these MLH country codes become names regions_of() understands; others are
# dropped as not nearby. Add codes if you start travelling further for hackathons.
_COUNTRIES = {"US": "USA", "CA": "Canada", "GB": "United Kingdom", "IE": "Ireland"}


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        body: bytes = response.read()
    return body


def _day(text: str | None) -> date | None:
    try:
        return date.fromisoformat((text or "")[:10])
    except ValueError:  # "TBD" and the like
        return None


def devpost_dates(text: str) -> tuple[date, date] | None:
    """Parse "Aug 31 - Oct 23, 2026", "Oct 05 - 27, 2026" or "Dec 28, 2026 - Jan 05, 2027"."""
    try:
        left, _, right = text.partition(" - ")
        right = right or left
        if not right[0].isalpha():  # "27, 2026" is in the start's month
            right = f"{left.split()[0]} {right}"
        end = datetime.strptime(right, "%b %d, %Y").date()
        start_text = left if "," in left else f"{left}, {end.year}"
        start = datetime.strptime(start_text, "%b %d, %Y").date()
    except (ValueError, IndexError):
        return None
    return (start.replace(year=start.year - 1) if start > end else start), end


def devpost(hackathons: list[dict[str, Any]]) -> list[Opportunity]:
    found = []
    for h in hackathons:
        dates = devpost_dates(h.get("submission_period_dates", ""))
        if dates is None or h.get("invite_only"):
            continue
        location = h.get("displayed_location", {}).get("location", "")
        prize = html.unescape(re.sub(r"<[^>]+>", "", h.get("prize_amount", "")))
        details = [h.get("organization_name") or "", f"{prize} in prizes" if prize else ""]
        found.append(
            Opportunity(
                kind=OpportunityKind.HACKATHON,
                title=h["title"].strip(),
                url=h["url"],
                source="devpost",
                starts_on=dates[0],
                ends_on=dates[1],
                deadline=dates[1],
                deadline_label="Submissions close",
                location=location,
                online=location == "Online",
                topics=[t["name"] for t in h.get("themes", [])],
                details=" · ".join(d for d in details if d),
            )
        )
    return found


def _meta(card: str, prop: str) -> str:
    match = re.search(rf'itemProp="{prop}" content="([^"]*)"', card)
    return html.unescape(match.group(1)) if match else ""


def mlh(page: str) -> list[Opportunity]:
    """Events from MLH's season page, one schema.org Event per card."""
    found = []
    for card in page.split('itemType="https://schema.org/Event"')[1:]:
        name = re.search(r"<h4[^>]*>(.*?)</h4>", card, re.S)
        start, end = _day(_meta(card, "startDate")), _day(_meta(card, "endDate"))
        url = _meta(card, "url")
        if not (name and start and url.startswith("http")):
            continue
        code = _meta(card, "addressCountry")
        # "(IN)" rather than ", IN", which would read as Indiana.
        country = _COUNTRIES.get(code, f"({code})")
        place = ", ".join(
            filter(None, [_meta(card, "addressLocality"), _meta(card, "addressRegion")])
        )
        online = "Online" in _meta(card, "eventAttendanceMode")
        found.append(
            Opportunity(
                kind=OpportunityKind.HACKATHON,
                title=html.unescape(re.sub(r"<[^>]+>", "", name.group(1))).strip(),
                url=url,
                source="mlh",
                starts_on=start,
                ends_on=end,
                location="Online"
                if online
                else f"{place}, {country}"
                if code in _COUNTRIES
                else f"{place} {country}",
                online=online,
                details="Major League Hacking member event: student-run, free, travel "
                "reimbursement is sometimes offered.",
            )
        )
    return found


def confs_tech(entries: list[dict[str, Any]], topic: str) -> list[Opportunity]:
    found = []
    for c in entries:
        country = c.get("country", "").replace("U.S.A.", "USA").replace("U.K.", "UK")
        cfp = c.get("cfpUrl", "")
        found.append(
            Opportunity(
                kind=OpportunityKind.CONFERENCE,
                title=c["name"].strip(),
                url=c["url"],
                source="confs.tech",
                starts_on=_day(c.get("startDate")),
                ends_on=_day(c.get("endDate")),
                deadline=_day(c.get("cfpEndDate")),
                deadline_label="Talk proposals close" if c.get("cfpEndDate") else "",
                location="Online"
                if c.get("online") and not c.get("city")
                else ", ".join(filter(None, [c.get("city", ""), country])),
                online=bool(c.get("online")),
                topics=[topic],
                details=f"Call for talks: {cfp}" if cfp else "",
            )
        )
    return found


def ccfddl(venues: list[dict[str, Any]], areas: list[str], today: date) -> list[Opportunity]:
    """Each venue's newest edition that has not happened yet.

    An edition whose main deadline has passed is kept: workshops, posters and student
    tracks usually close months later, and the strategy step looks those up.
    """
    found = []
    for v in venues:
        if v.get("sub") not in areas or not v.get("confs"):
            continue
        conf = max(v["confs"], key=lambda c: c.get("year", 0))
        opening = _day(conf.get("opening"))
        deadlines = sorted(
            d
            for step in conf.get("timeline", [])
            for k in ("abstract_deadline", "deadline")
            if (d := _day(step.get(k))) and d >= today
        )
        if (opening and opening < today) or (not opening and not deadlines):
            continue
        rank = v.get("rank") or {}
        found.append(
            Opportunity(
                kind=OpportunityKind.RESEARCH,
                title=f"{v['title']} {conf.get('year', '')}".strip(),
                url=conf["link"],
                source="ccfddl",
                starts_on=opening,
                deadline=deadlines[0] if deadlines else None,
                deadline_label="Paper deadline"
                if deadlines
                else "Main deadline passed: check workshops, posters and student tracks",
                location=conf.get("place", ""),
                topics=[AREAS.get(v["sub"], v["sub"])],
                details=f"{v.get('description', '')}. {conf.get('date', '')}; deadlines in "
                f"{conf.get('timezone', 'the venue timezone')}.",
                rank=f"CORE {rank['core']}"
                if rank.get("core") not in (None, "N")
                else (f"CCF {rank['ccf']}" if rank.get("ccf") not in (None, "N") else ""),
            )
        )
    return found


def collect_devpost(online_pages: int = 4, in_person_pages: int = 12) -> list[Opportunity]:
    found = []
    for query, pages in (("", online_pages), ("&challenge_type[]=in-person", in_person_pages)):
        for page in range(1, pages + 1):
            data = json.loads(get(DEVPOST.format(page=page) + query))
            found += devpost(data.get("hackathons", []))
            if not data.get("hackathons"):
                break
            time.sleep(0.5)  # be polite to an undocumented API
    return found


def collect_mlh(today: date) -> list[Opportunity]:
    # MLH seasons are named for the year they end in (the 2027 season runs mid-2026 to mid-2027).
    season = today.year + 1 if today.month >= 7 else today.year
    return mlh(get(MLH.format(season=season)).decode("utf-8", "ignore"))


def collect_confs_tech(today: date, topics: list[str]) -> list[Opportunity]:
    found = []
    for year in (today.year, today.year + 1):
        for topic in topics:
            try:
                entries = json.loads(get(CONFS_TECH.format(year=year, topic=topic)))
            except urllib.error.HTTPError as exc:
                if exc.code == 404:  # no file for that topic and year yet
                    continue
                raise
            found += confs_tech(entries, topic)
    return found


def collect_ccfddl(today: date, areas: list[str]) -> list[Opportunity]:
    return ccfddl(json.loads(get(CCFDDL)), areas, today)
