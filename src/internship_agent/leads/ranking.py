"""Deterministic filtering and ordering of founder leads."""

from datetime import date, timedelta

from internship_agent.leads.schemas import FounderLead, LeadStatus, Round

# Early-stage teams are the most likely to take an intern from a cold message.
_ROUND_PRIORITY = {
    Round.SEED: 0,
    Round.PRE_SEED: 1,
    Round.SERIES_A: 2,
    Round.SERIES_B: 3,
    Round.OTHER: 4,
}


def is_recent(lead: FounderLead, today: date, days: int) -> bool:
    return lead.announced_on >= today - timedelta(days=days)


def rank(leads: list[FounderLead], today: date, days: int = 90) -> list[FounderLead]:
    active = [
        lead
        for lead in leads
        if lead.status is not LeadStatus.SKIPPED and is_recent(lead, today, days)
    ]
    return sorted(
        active,
        key=lambda lead: (
            -(lead.fit.score if lead.fit else -1),
            _ROUND_PRIORITY[lead.round],
            -lead.announced_on.toordinal(),
        ),
    )
