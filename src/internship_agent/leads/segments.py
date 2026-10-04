"""Deterministic segment rules: early/mid-stage startups vs big companies."""

import re

from internship_agent.leads.schemas import Lead, LeadKind, Round, Segment

ROUND_SEGMENT = {
    Round.PRE_SEED: Segment.EARLY,
    Round.SEED: Segment.EARLY,
    Round.SERIES_A: Segment.MID,
    Round.SERIES_B: Segment.MID,
}


def effective_segment(lead: Lead) -> Segment | None:
    """An explicit segment wins; founders fall back to their round; otherwise unknown."""
    if lead.segment is not None:
        return lead.segment
    if lead.kind is LeadKind.FOUNDER:
        return ROUND_SEGMENT.get(lead.round, Segment.MID)
    return None


def parse_round(text: str) -> Round:
    """Map free text such as 'Seed - $3 million' or 'Series A' to a Round."""
    lowered = text.lower()
    if re.search(r"pre[- ]?seed", lowered):
        return Round.PRE_SEED
    if "seed" in lowered:
        return Round.SEED
    if re.search(r"series\s*a\b", lowered):
        return Round.SERIES_A
    if re.search(r"series\s*[b-d]\b", lowered):
        return Round.SERIES_B
    return Round.OTHER
