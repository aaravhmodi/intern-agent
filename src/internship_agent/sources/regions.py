"""Map free-text job locations to regions."""

import re

from internship_agent.leads.schemas import Region

_PROVINCES = {"ON", "QC", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "PE", "YT", "NT", "NU"}
_EUROPE = (
    "United Kingdom",
    "UK",
    "England",
    "Scotland",
    "Ireland",
    "Germany",
    "France",
    "Netherlands",
    "Belgium",
    "Luxembourg",
    "Switzerland",
    "Austria",
    "Spain",
    "Portugal",
    "Italy",
    "Denmark",
    "Sweden",
    "Norway",
    "Finland",
    "Iceland",
    "Poland",
    "Czech",
    "Estonia",
    "Latvia",
    "Lithuania",
    "Greece",
    "Romania",
    "Hungary",
    "Europe",
    "London",
    "Berlin",
    "Munich",
    "Paris",
    "Amsterdam",
    "Zurich",
    "Dublin",
    "Stockholm",
    "Copenhagen",
    "Madrid",
    "Barcelona",
    "Lisbon",
    "Milan",
    "Warsaw",
    "Helsinki",
    "Oslo",
    "Vienna",
    "Prague",
    "Tallinn",
    "EMEA",
)
_EUROPE_RE = re.compile(r"\b(" + "|".join(re.escape(x) for x in _EUROPE) + r")\b")
_US_STATES = set(
    "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ "
    "NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC".split()
)
_STATE_RE = re.compile(r",\s*([A-Z]{2})\b")


def regions_of(location: str) -> set[Region]:
    """All regions a location string mentions (a posting may list several offices)."""
    found: set[Region] = set()
    if "Canada" in location or any(code in _PROVINCES for code in _STATE_RE.findall(location)):
        found.add(Region.CANADA)
    if re.search(r"\b(USA|United States|US)\b", location) or any(
        code in _US_STATES for code in _STATE_RE.findall(location)
    ):
        found.add(Region.USA)
    if _EUROPE_RE.search(location):
        found.add(Region.EUROPE)
    return found


def region_from_text(text: str) -> Region | None:
    """Best single region for a startup's location text, if any."""
    found = regions_of(text)
    for region in (Region.CANADA, Region.USA, Region.EUROPE):
        if region in found:
            return region
    return None
