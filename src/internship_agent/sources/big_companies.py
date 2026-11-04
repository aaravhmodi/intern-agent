"""Intern and co-op roles straight from big companies' own career sites, which the
SimplifyJobs list can lag behind (MongoDB, Amazon, Microsoft and other Greenhouse companies).

Google, Meta, Apple and Netflix are not here: their career sites have no public job feed that
works without a script-rendered page or a login.
"""

import json
import re
import urllib.error
import urllib.request
from collections.abc import Callable
from typing import Any
from urllib.parse import quote

from internship_agent.leads.schemas import Lead, LeadKind, Region
from internship_agent.sources.regions import region_from_text, regions_of
from internship_agent.sources.startup_jobs import OpenRole, _greenhouse, intern_roles

# Company name -> Greenhouse board. A wrong slug just returns nothing.
GREENHOUSE = {
    "MongoDB": "mongodb",
    "Stripe": "stripe",
    "Databricks": "databricks",
    "Airbnb": "airbnb",
    "Cloudflare": "cloudflare",
    "Datadog": "datadog",
    "Figma": "figma",
    "Dropbox": "dropbox",
    "Pinterest": "pinterest",
    "Reddit": "reddit",
    "Coinbase": "coinbase",
    "Instacart": "instacart",
    "Twilio": "twilio",
    "Elastic": "elastic",
    "Samsara": "samsara",
    "Anthropic": "anthropic",
}
AMAZON = (
    "https://www.amazon.jobs/en/search.json?base_query={q}&result_limit=100&offset={n}&sort=recent"
)
MICROSOFT = "https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query={q}&start={n}&num=20"
PAGES = 4  # most pages read per company site


def _get(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read())


_CLOSED = re.compile(
    # Not "position is filled": that's in Jobvite's fine print on every live job.
    r"no longer available|no longer accepting|position has been filled|"
    r"posting is closed|job not found|no current openings",
    re.I,
)
_ASHBY_JOB = re.compile(r"https://jobs\.ashbyhq\.com/(?P<slug>[^/?#]+)/(?P<id>[0-9a-f-]{36})", re.I)
# A page cut off at the read limit can end inside a script, hence the "or the end".
_SCRIPT = re.compile(r"<script\b.*?(?:</script>|\Z)", re.I | re.S)
ASHBY_BOARD = "https://api.ashbyhq.com/posting-api/job-board/{slug}"


def posting_is_gone(url: str) -> bool:
    """True when the posting page is a 404/410 or says the role is closed.

    Greenhouse sends a closed job to its board with ?error=true. Ashby serves the same page for
    any job id, so an Ashby job is gone when its board's public feed no longer lists it. Any
    other failure (timeout, 5xx, script-rendered page) counts as still open, so a hiccup never
    hides a live role.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        if ashby := _ASHBY_JOB.match(url):
            board = _get(ASHBY_BOARD.format(slug=ashby["slug"]))
            return all(job.get("id") != ashby["id"] for job in board.get("jobs", []))
        with urllib.request.urlopen(request, timeout=20) as response:
            if "error=true" in response.geturl():
                return True
            page = response.read(300_000).decode("utf-8", "ignore")
            # Sites like Keysight ship their "no longer available" message in every page's script.
            return bool(_CLOSED.search(_SCRIPT.sub("", page)))
    except urllib.error.HTTPError as error:
        return error.code in (404, 410)
    except Exception:
        return False


def amazon_roles(pages: list[dict[str, Any]]) -> list[OpenRole]:
    return intern_roles(
        [
            OpenRole(
                title=job["title"].strip(),
                url="https://www.amazon.jobs" + job["job_path"],
                location=job.get("location", ""),
                board="amazon.jobs",
            )
            for page in pages
            for job in page.get("jobs", [])
        ]
    )


def microsoft_roles(pages: list[dict[str, Any]]) -> list[OpenRole]:
    return intern_roles(
        [
            OpenRole(
                title=p["name"].strip(),
                url="https://apply.careers.microsoft.com" + p["positionUrl"],
                location="; ".join(p.get("standardizedLocations") or []),
                board="microsoft careers",
            )
            for page in pages
            for p in page.get("data", {}).get("positions", [])
        ]
    )


def to_lead(company: str, role: OpenRole) -> Lead:
    return Lead(
        kind=LeadKind.POSTING,
        company=company,
        posting_title=role.title,
        posting_url=role.url,
        source_url=role.url,
        location=role.location,
        region=region_from_text(role.location),
        posted_on=role.posted_on,
        hiring_signals=[f"Open role on {company}'s own {role.board} site"],
    )


def postings(regions: set[Region], log: Callable[[str], None] = lambda _: None) -> list[Lead]:
    """Intern/co-op leads in `regions` from each company's career site. One site down is skipped."""
    found: list[tuple[str, OpenRole]] = []
    for company, slug in GREENHOUSE.items():
        try:
            found += [(company, r) for r in intern_roles(_greenhouse(slug))]
        except Exception as error:  # a missing board or a hiccup must not stop the rest
            log(f"{company}: {error}")
    for company, url, build in (
        ("Amazon", AMAZON, amazon_roles),
        ("Microsoft", MICROSOFT, microsoft_roles),
    ):
        try:
            pages = [
                _get(url.format(q=quote("intern"), n=n * (100 if company == "Amazon" else 20)))
                for n in range(PAGES)
            ]
            found += [(company, r) for r in build(pages)]
        except Exception as error:
            log(f"{company}: {error}")
    leads = [
        to_lead(company, role) for company, role in found if regions_of(role.location) & regions
    ]
    log(f"{len(leads)} role(s) from big companies' own career sites")
    return leads
