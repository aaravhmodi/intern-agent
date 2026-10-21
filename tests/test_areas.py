from datetime import date

import pytest

from internship_agent.leads.areas import in_area, spread
from internship_agent.leads.schemas import Lead, Region


def founder(name: str, location: str, region: Region | None) -> Lead:
    return Lead(
        company=name,
        location=location,
        region=region,
        source_url="https://example.com",
        contact_name="Pat Lee",
        announced_on=date(2026, 10, 1),
    )


def test_hub_cities_and_europe_are_separate_batches() -> None:
    toronto = founder("a", "Toronto, ON", Region.CANADA)
    nyc = founder("b", "Brooklyn, NY", Region.USA)
    sf = founder("c", "San Francisco, CA", Region.USA)
    berlin = founder("d", "Berlin, Germany", Region.EUROPE)
    austin = founder("e", "Austin, TX", Region.USA)
    vancouver = founder("f", "Vancouver, BC", Region.CANADA)
    assert in_area(toronto, "toronto") and not in_area(toronto, "others")
    assert in_area(nyc, "new-york") and in_area(sf, "sf")
    assert in_area(berlin, "europe") and in_area(berlin, "others")
    assert not in_area(austin, "europe") and in_area(austin, "others")
    assert in_area(vancouver, "others") and not in_area(vancouver, "toronto")


def test_unknown_area_is_rejected() -> None:
    with pytest.raises(ValueError):
        in_area(founder("a", "Toronto", Region.CANADA), "mars")


def test_spread_splits_evenly_and_keeps_fit_order() -> None:
    eu = [founder(f"eu{i}", "Paris", Region.EUROPE) for i in range(2)]
    ca = [founder(f"ca{i}", "Calgary", Region.CANADA) for i in range(5)]
    us = [founder(f"us{i}", "Austin", Region.USA) for i in range(5)]
    names = [lead.company for lead in spread([*us, *ca, *eu])]
    assert names[:6] == ["eu0", "ca0", "us0", "eu1", "ca1", "us1"]
    assert names[6:] == ["ca2", "us2", "ca3", "us3", "ca4", "us4"]  # Europe ran out
