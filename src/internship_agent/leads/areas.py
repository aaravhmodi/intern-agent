"""Which email batch a lead belongs to: a hub city, Europe, or everywhere else."""

import re
from itertools import zip_longest

from internship_agent.leads.schemas import Lead, Region

AREAS = ("toronto", "europe", "new-york", "sf", "others")

_CITY = {
    "toronto": r"toronto|mississauga|markham|vaughan|brampton|etobicoke|north york|scarborough",
    "new-york": r"new york|nyc|brooklyn|manhattan|queens|, ny\b",
    "sf": (
        r"san francisco|\bsf\b|bay area|palo alto|mountain view|menlo park|redwood city|"
        r"san mateo|sunnyvale|san jose|oakland|berkeley|cupertino|santa clara"
    ),
}


def hub(lead: Lead) -> str | None:
    """The hub city the lead's location names, if any."""
    where = lead.location.lower()
    return next((city for city, found in _CITY.items() if re.search(found, where)), None)


def in_area(lead: Lead, area: str) -> bool:
    if area not in AREAS:
        raise ValueError(f"unknown area {area!r}; expected one of {AREAS}")
    city = hub(lead)
    if area == "europe":
        return city is None and lead.region is Region.EUROPE
    if area == "others":
        return city is None
    return city == area


def spread(leads: list[Lead]) -> list[Lead]:
    """Interleave Europe, Canada and the USA so any prefix is split evenly between them.

    Each region keeps the order it came in (best fit first), and a region that runs out
    simply stops taking turns. shortcut: no region means the USA (Form D, the main source
    without one, is US-only); revisit if another no-region source is added.
    """
    lanes: dict[Region, list[Lead]] = {r: [] for r in (Region.EUROPE, Region.CANADA, Region.USA)}
    for lead in leads:
        lanes[lead.region or Region.USA].append(lead)
    return [lead for turn in zip_longest(*lanes.values()) for lead in turn if lead is not None]
