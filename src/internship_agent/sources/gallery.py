"""Intern and co-op roles at the startups on https://startups.gallery/jobs.

The page is server-rendered with each job's application link, so the companies' job boards are
read from those links and checked for intern roles with the same readers the startup search uses.
"""

import re
import urllib.request
from collections.abc import Callable

from internship_agent.leads.schemas import Lead, LeadKind
from internship_agent.sources.regions import region_from_text
from internship_agent.sources.startup_jobs import (
    OpenRole,
    _ashby,
    _greenhouse,
    _lever,
    intern_roles,
)

URL = "https://startups.gallery/jobs"
_LINK = re.compile(
    r"https?://(?:jobs\.ashbyhq\.com/(?P<ashby>[\w.-]+)/[0-9a-f-]{36}"
    r"|(?:job-boards|boards)\.greenhouse\.io/(?P<greenhouse>[\w.-]+)/jobs/\d+"
    r"|jobs\.lever\.co/(?P<lever>[\w.-]+)/[0-9a-f-]{36})",
    re.I,
)
_READERS = {"ashby": _ashby, "greenhouse": _greenhouse, "lever": _lever}


def fetch() -> str:
    request = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body: bytes = response.read()
    return body.decode("utf-8", "ignore")


def boards(html: str) -> list[tuple[str, str]]:
    """(job-board kind, slug) for every distinct company board the page links to."""
    found: dict[tuple[str, str], None] = {}
    for match in _LINK.finditer(html):
        kind = next(k for k, v in match.groupdict().items() if v)
        found[(kind, match.group(kind).lower())] = None
    return list(found)


def to_lead(slug: str, role: OpenRole) -> Lead:
    company = slug.replace("-", " ").replace("_", " ").title()
    return Lead(
        kind=LeadKind.POSTING,
        company=company,
        posting_title=role.title,
        posting_url=role.url,
        source_url=URL,
        location=role.location,
        region=region_from_text(role.location),
        hiring_signals=["Listed on startups.gallery"],
    )


def postings(log: Callable[[str], None] = lambda _: None) -> list[Lead]:
    """Intern/co-op leads from every board linked on startups.gallery/jobs."""
    found = boards(fetch())
    leads: list[Lead] = []
    for kind, slug in found:
        try:
            leads += [to_lead(slug, r) for r in intern_roles(_READERS[kind](slug))]
        except Exception as error:  # one broken board must not stop the rest
            log(f"startups.gallery {slug}: {error}")
    log(f"{len(leads)} role(s) from {len(found)} startups.gallery board(s)")
    return leads
