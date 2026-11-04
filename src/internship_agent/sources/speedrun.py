"""Intern roles at a16z speedrun and portfolio startups (public speedrun talent-network feed).

Ported from career-ops' providers/a16z-speedrun-talent.mjs. The feed is public and
paginated 50 per page; `q` runs its full-text search, so asking for "intern" keeps the
scan to a few pages.
"""

from datetime import datetime
from typing import Any
from urllib.parse import urlencode, urlsplit

from pydantic import BaseModel

from internship_agent.leads.schemas import Lead, LeadKind, Region
from internship_agent.leads.store import normalize_url
from internship_agent.sources.http import get_json
from internship_agent.sources.regions import region_from_text, wanted_location
from internship_agent.sources.startup_jobs import is_intern_engineering

FEED_URL = "https://speedrun-talent-network.com/api/v1/jobs"
_HOST = "speedrun-talent-network.com"


class SpeedrunJob(BaseModel):
    title: str
    company: str
    location: str
    url: str
    published_at: datetime | None = None


def parse_page(data: dict[str, Any]) -> list[SpeedrunJob]:
    jobs: list[SpeedrunJob] = []
    for j in data.get("jobs") or []:
        title = (j.get("title") or "").strip()
        company = (j.get("company") or "").strip()
        url = (j.get("url") or "").strip()
        parts = urlsplit(url)
        if not title or not company or parts.scheme != "https" or parts.hostname != _HOST:
            continue
        location = ", ".join(
            x for x in ((j.get("location") or "").strip(), "Remote" if j.get("remote") else "") if x
        )
        published = None
        if isinstance(j.get("published_at"), str):
            try:
                published = datetime.fromisoformat(j["published_at"].replace("Z", "+00:00"))
            except ValueError:
                pass
        jobs.append(
            SpeedrunJob(
                title=title, company=company, location=location, url=url, published_at=published
            )
        )
    return jobs


def fetch(query: str = "intern", max_pages: int = 4) -> list[SpeedrunJob]:
    jobs: list[SpeedrunJob] = []
    for page in range(max_pages):
        params = urlencode({"q": query, "page": page, "source": "internship-agent"})
        data = get_json(f"{FEED_URL}?{params}")
        found = parse_page(data)
        jobs.extend(found)
        total_pages = data.get("total_pages")
        if not found or (isinstance(total_pages, int) and page + 1 >= total_pages):
            break
    return jobs


def matching(jobs: list[SpeedrunJob], regions: set[Region]) -> list[SpeedrunJob]:
    return [
        j for j in jobs if is_intern_engineering(j.title) and wanted_location(j.location, regions)
    ]


def to_lead(job: SpeedrunJob) -> Lead:
    return Lead(
        kind=LeadKind.POSTING,
        company=job.company,
        posting_title=job.title,
        posting_url=normalize_url(job.url),
        source_url=job.url,
        location=job.location,
        region=region_from_text(job.location),
        hiring_signals=["a16z speedrun / portfolio company"],
    )
