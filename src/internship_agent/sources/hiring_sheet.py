"""Startups from a "startups hiring last week" spreadsheet (e.g. textbackdoor.com's list).

Columns: #, Startup, Industry, Example opening, Role location, Experience, Posting age,
Listed roles, Job listing, Company jobs, Website. The three link columns are
=HYPERLINK("url","label") formulas. Each startup becomes a company lead with no contact
yet, to cold-email for an internship; the usual people and email lookups fill in who.
"""

import re
from typing import Any

from internship_agent.leads.schemas import Lead, LeadKind
from internship_agent.sources.regions import region_from_text

_HYPERLINK = re.compile(r'^=HYPERLINK\("(https://[^"]+)"', re.I)
HEADER = (
    "#",
    "Startup",
    "Industry",
    "Example opening",
    "Role location",
    "Experience",
    "Posting age",
    "Listed roles",
    "Job listing",
    "Company jobs",
    "Website",
)


def link(cell: Any) -> str | None:
    """The https URL of a HYPERLINK formula, or of a cell holding a bare URL."""
    text = str(cell or "").strip()
    match = _HYPERLINK.match(text)
    if match:
        return match.group(1)
    return text if text.startswith("https://") else None


def _text(cell: Any) -> str:
    if isinstance(cell, float) and cell.is_integer():
        return str(int(cell))
    return " ".join(str(cell or "").split())


def to_lead(row: list[Any], checked_on: str) -> Lead | None:
    """One sheet row as a company lead; None for a row without a startup or a job link."""
    cells = [*row, *[None] * (len(HEADER) - len(row))]
    company, industry, role, location, experience, age, count = map(_text, cells[1:8])
    role_url, jobs_url, website = link(cells[8]), link(cells[9]), link(cells[10])
    source = role_url or jobs_url
    if not company or not source:
        return None
    hiring = f"Hiring a {role}" if role else "Hiring"
    details = ", ".join(
        x for x in (experience, f"posted {age} before {checked_on}" if age else "") if x
    )
    signals = [f"{hiring} ({details})" if details else hiring]
    if count:
        signals.append(f"{count} open role(s): {jobs_url or source}")
    if industry:
        signals.append(f"Industry: {industry}")
    return Lead(
        kind=LeadKind.FOUNDER,
        company=company,
        company_url=website,
        location=location,
        region=region_from_text(location),
        source_url=source,
        hiring_signals=signals,
    )


def to_leads(rows: list[list[Any]], checked_on: str) -> list[Lead]:
    """Leads from every data row after the header row, one per company."""
    start = next(
        (
            i + 1
            for i, row in enumerate(rows)
            if [_text(c) for c in row[: len(HEADER)]] == list(HEADER)
        ),
        0,
    )
    leads: dict[str, Lead] = {}
    for row in rows[start:]:
        lead = to_lead(row, checked_on)
        if lead is not None:
            leads.setdefault(lead.company.casefold(), lead)
    return list(leads.values())
