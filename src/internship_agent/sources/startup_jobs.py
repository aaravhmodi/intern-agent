"""Look for open intern/co-op roles on a startup's public job board.

Boards: Ashby, Greenhouse, Lever, Workable, Recruitee and SmartRecruiters, all public
no-auth APIs (the last three ported from career-ops' providers).
"""

import re
from datetime import date, datetime
from typing import Any
from urllib.parse import quote, urlsplit

from pydantic import BaseModel

from internship_agent.sources.http import get_json

_INTERN = re.compile(r"\b(intern|interns|internship|co-?op|student)\b", re.I)
_ENGINEERING = re.compile(
    r"\b(software|engineer\w*|developer|data|machine learning|ml|ai|platform|backend|"
    r"front-?end|full[- ]?stack|infrastructure|research|robotics)\b",
    re.I,
)


class OpenRole(BaseModel):
    title: str
    url: str
    location: str
    board: str
    posted_on: date | None = None


def _day(stamp: str | None) -> date | None:
    """The date of a board's ISO timestamp; None when missing or unreadable."""
    try:
        return datetime.fromisoformat(stamp).date() if stamp else None
    except ValueError:
        return None


def _json(url: str) -> Any:
    return get_json(url)


def board_slugs(company: str, company_url: str | None) -> list[str]:
    """Likely job-board slugs: the website's name, then the company name."""
    slugs: list[str] = []
    if company_url:
        host = urlsplit(company_url if "//" in company_url else f"https://{company_url}").netloc
        stem = host.lower().removeprefix("www.").split(".")[0]
        if stem:
            slugs.append(stem)
    name = re.sub(r"\b(inc|ltd|labs?|ai|technologies|corp)\b\.?", "", company.lower())
    for slug in (re.sub(r"[^a-z0-9]", "", name), re.sub(r"[^a-z0-9]+", "-", name).strip("-")):
        if len(slug) >= 3 and slug not in slugs:
            slugs.append(slug)
    return slugs


def _ashby(slug: str) -> list[OpenRole]:
    data = _json(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
    return [
        OpenRole(
            title=j["title"],
            url=j["jobUrl"],
            location=j.get("location", ""),
            board="ashby",
            posted_on=_day(j.get("publishedAt")),
        )
        for j in data.get("jobs", [])
        if j.get("isListed", True)
    ]


def _greenhouse(slug: str) -> list[OpenRole]:
    data = _json(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    return [
        OpenRole(
            title=j["title"],
            url=j["absolute_url"],
            location=(j.get("location") or {}).get("name", ""),
            board="greenhouse",
            posted_on=_day(j.get("first_published")),
        )
        for j in data.get("jobs", [])
    ]


def _lever(slug: str) -> list[OpenRole]:
    data = _json(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    return [
        OpenRole(
            title=j["text"],
            url=j["hostedUrl"],
            location=(j.get("categories") or {}).get("location", ""),
            board="lever",
            posted_on=date.fromtimestamp(j["createdAt"] / 1000) if j.get("createdAt") else None,
        )
        for j in data
    ]


def _join(*parts: object) -> str:
    return ", ".join(p.strip() for p in parts if isinstance(p, str) and p.strip())


def _https(*candidates: object) -> str:
    return next((c for c in candidates if isinstance(c, str) and c.startswith("https://")), "")


def parse_workable(data: dict[str, Any]) -> list[OpenRole]:
    roles: list[OpenRole] = []
    for j in data.get("jobs") or []:
        url = _https(j.get("url"), j.get("shortlink"))
        if not j.get("title") or not url:
            continue
        location = _join(j.get("city"), j.get("country")) or (
            "Remote" if j.get("telecommuting") else ""
        )
        roles.append(
            OpenRole(
                title=j["title"],
                url=url,
                location=location,
                board="workable",
                posted_on=_day(j.get("published_on")),
            )
        )
    return roles


def _workable(slug: str) -> list[OpenRole]:
    return parse_workable(_json(f"https://apply.workable.com/api/v1/widget/accounts/{slug}"))


def parse_recruitee(data: dict[str, Any]) -> list[OpenRole]:
    roles: list[OpenRole] = []
    for j in data.get("offers") or []:
        url = _https(j.get("careers_url"), j.get("url"))
        if not j.get("title") or not url:
            continue
        location = j.get("location") or _join(j.get("city"), j.get("country"))
        if j.get("remote") and "remote" not in location.lower():
            location = _join(location, "Remote")
        roles.append(
            OpenRole(
                title=j["title"],
                url=url,
                location=location,
                board="recruitee",
                posted_on=_day((j.get("published_at") or "")[:10] or None),
            )
        )
    return roles


def _recruitee(slug: str) -> list[OpenRole]:
    return parse_recruitee(_json(f"https://{slug}.recruitee.com/api/offers/"))


def parse_smartrecruiters(data: dict[str, Any], slug: str) -> list[OpenRole]:
    """Postings, linked to the public jobs.smartrecruiters.com page (the API ref 404s there)."""
    roles: list[OpenRole] = []
    for j in data.get("content") or []:
        if not j.get("name") or not j.get("id"):
            continue
        loc = j.get("location") or {}
        location = loc.get("fullLocation") or _join(
            loc.get("city"), loc.get("region"), loc.get("country")
        )
        if loc.get("remote"):
            location = _join(location, "Remote")
        url = f"https://jobs.smartrecruiters.com/{slug}/{quote(str(j['id']), safe='')}"
        roles.append(
            OpenRole(
                title=j["name"],
                url=url,
                location=location,
                board="smartrecruiters",
                posted_on=_day((j.get("releasedDate") or "")[:10] or None),
            )
        )
    return roles


def _smartrecruiters(slug: str) -> list[OpenRole]:
    data = _json(f"https://api.smartrecruiters.com/v1/companies/{slug}/postings?limit=100")
    return parse_smartrecruiters(data, slug)


BOARDS = (_ashby, _greenhouse, _lever, _workable, _recruitee, _smartrecruiters)


def is_intern_engineering(title: str) -> bool:
    return bool(_INTERN.search(title) and _ENGINEERING.search(title))


def intern_roles(roles: list[OpenRole]) -> list[OpenRole]:
    return [r for r in roles if is_intern_engineering(r.title)]


def find_intern_roles(company: str, company_url: str | None) -> list[OpenRole]:
    """Open intern/co-op roles from the first public job board found for the company."""
    for slug in board_slugs(company, company_url):
        for fetch in BOARDS:
            try:
                roles = fetch(slug)
            except Exception:
                continue
            if roles:
                return intern_roles(roles)
    return []
