"""Deterministic filtering and ordering of leads."""

from datetime import date, timedelta

from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus, Round

# Early-stage teams are the most likely to take an intern from a cold message.
_ROUND_PRIORITY = {
    Round.SEED: 0,
    Round.PRE_SEED: 1,
    Round.SERIES_A: 2,
    Round.SERIES_B: 3,
    Round.OTHER: 4,
}


def is_open(lead: Lead, today: date, days: int) -> bool:
    """Founder raises must be recent; postings must not be past their deadline."""
    if lead.kind is LeadKind.POSTING:
        return lead.deadline is None or lead.deadline >= today
    return lead.announced_on is not None and lead.announced_on >= today - timedelta(days=days)


def rank(leads: list[Lead], today: date, days: int = 90) -> list[Lead]:
    active = [
        lead
        for lead in leads
        if lead.status is not LeadStatus.SKIPPED and is_open(lead, today, days)
    ]
    return sorted(
        active,
        key=lambda lead: (
            -(lead.fit.score if lead.fit else -1),
            _ROUND_PRIORITY[lead.round] if lead.kind is LeadKind.FOUNDER else 0,
            -(lead.announced_on or today).toordinal(),
        ),
    )
