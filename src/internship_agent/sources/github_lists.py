"""Intern roles from community-kept GitHub lists other than SimplifyJobs: markdown tables with a
company, role, location and an apply link (negarprh's Canadian list, speedyapply's USA and
international lists).
"""

import re
import urllib.request
from collections.abc import Callable

from internship_agent.leads.schemas import Lead, LeadKind
from internship_agent.sources.regions import region_from_text
from internship_agent.sources.simplify import is_software_role

LISTS = (
    ("negarprh/Canadian-Tech-Internships-2027", "README.md"),
    ("speedyapply/2027-SWE-College-Jobs", "README.md"),  # USA
    ("speedyapply/2027-SWE-College-Jobs", "INTERN_INTL.md"),  # includes Canada
)
RAW = "https://raw.githubusercontent.com/{repo}/main/{file}"
_LINK = re.compile(r"""(?:href="|\]\()(https?://[^")\s]+)""")
# The "Apply" button is itself an image link; its picture is not the job.
_IMAGE = re.compile(r"img\.shields\.io|imgur\.com|\.(?:png|svg|gif)\b", re.I)
_TAG = re.compile(r"<[^>]+>|\*\*|\[|\]\([^)]*\)")


def _cell(text: str) -> str:
    return _TAG.sub("", text).strip()


def parse(markdown: str, source: str) -> list[Lead]:
    """One lead per open row; closed rows (no apply link) and badge-only images are dropped."""
    leads: list[Lead] = []
    header: list[str] = []
    company = ""
    for line in markdown.splitlines():
        if not line.startswith("|"):
            header = [] if not line.strip() else header
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        names = [_cell(c).lower() for c in cells]
        if "company" in names:
            header = names
            continue
        if not header or set(line) <= set("|-: "):
            continue
        row = dict(zip(header, cells, strict=False))
        name = _cell(row.get("company", ""))
        company = company if name in ("↳", "") else name
        apply = row.get("apply") or row.get("posting") or row.get("application") or ""
        link = next((u for u in _LINK.findall(apply) if not _IMAGE.search(u)), "")
        title = _cell(row.get("role") or row.get("position") or "")
        if not link or not company or not title:
            continue
        location = _cell(row.get("location", ""))
        leads.append(
            Lead(
                kind=LeadKind.POSTING,
                company=company,
                posting_title=title,
                posting_url=link,
                source_url=source,
                location=location,
                region=region_from_text(location),
                hiring_signals=[f"Listed on {source.split('/')[3]}'s GitHub internship list"],
            )
        )
    return leads


def postings(log: Callable[[str], None] = lambda _: None) -> list[Lead]:
    """SWE intern leads from every list. One list down is skipped."""
    leads: list[Lead] = []
    for repo, file in LISTS:
        url = RAW.format(repo=repo, file=file)
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=30) as response:
                markdown = response.read().decode("utf-8", "ignore")
        except Exception as error:
            log(f"{repo}/{file}: {error}")
            continue
        found = [lead for lead in parse(markdown, url) if is_software_role(lead.posting_title)]
        log(f"{len(found)} role(s) from {repo}/{file}")
        leads += found
    return leads
