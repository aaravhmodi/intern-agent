"""Keep a target number of open postings: once you apply, new ones take their place."""

from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus
from internship_agent.leads.store import merge

DONE = {LeadStatus.APPLIED, LeadStatus.CONTACTED, LeadStatus.SKIPPED}


def is_workday(lead: Lead) -> bool:
    """Workday-hosted application forms are intentionally left for manual handling."""
    url = (lead.posting_url or "").lower()
    return "myworkdayjobs.com" in url or "workday.com" in url


def open_postings(leads: list[Lead]) -> list[Lead]:
    return [
        lead
        for lead in leads
        if lead.kind is LeadKind.POSTING and lead.status not in DONE and not is_workday(lead)
    ]


def refill(
    leads: list[Lead], candidates: list[Lead], target_open: int
) -> tuple[list[Lead], list[Lead]]:
    """Add candidates (in order) until there are `target_open` open postings.

    Candidates already present (same key or posting URL), including ones you applied to or
    skipped, are never re-added. Returns (all leads, newly added leads).
    """
    candidates = [candidate for candidate in candidates if not is_workday(candidate)]
    needed = target_open - len(open_postings(leads))
    if needed <= 0:
        return leads, []
    added: list[Lead] = []
    for candidate in candidates:
        if len(added) == needed:
            break
        merged, count = merge([*leads, *added], [candidate])
        if count:
            added.append(merged[-1])
    return [*leads, *added], added
