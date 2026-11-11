"""Which companies get their LinkedIn network checked next, and storing what was found."""

from datetime import datetime, timedelta

from internship_agent.leads.contacts import company_key
from internship_agent.leads.schemas import Lead, LeadStatus, NetworkPerson

# A network changes slowly; look again after this long.
RECHECK_AFTER = timedelta(days=21)


def companies_due(leads: list[Lead], now: datetime, limit: int) -> list[str]:
    """Up to `limit` companies to check, never-checked first, then the longest ago.

    One search covers every lead at a company. Companies whose every lead is skipped, or that
    were checked within RECHECK_AFTER, are left out.
    """
    last: dict[str, datetime | None] = {}
    names: dict[str, str] = {}
    for lead in leads:
        key = company_key(lead.company)
        if lead.status is LeadStatus.SKIPPED or not key:
            continue
        names.setdefault(key, lead.company)
        times = [t for t in (last.get(key), lead.network_checked_at) if t is not None]
        last[key] = max(times) if times else None
    due = [k for k, at in last.items() if at is None or now - at >= RECHECK_AFTER]
    due.sort(key=lambda k: (last[k] is not None, last[k] or now))
    return [names[k] for k in due[:limit]]


def apply_network(
    leads: list[Lead], company: str, people: list[NetworkPerson], now: datetime
) -> list[Lead]:
    """Store the people found on every lead at `company`; returns the leads changed."""
    key = company_key(company)
    changed = [lead for lead in leads if company_key(lead.company) == key]
    for lead in changed:
        lead.network = people
        lead.network_checked_at = now
    return changed
