from datetime import date
from typing import Any

import pytest

from internship_agent import x_search
from internship_agent.ai import StartupFinding
from internship_agent.leads.schemas import Region, Segment
from internship_agent.sources.startups import to_leads
from internship_agent.x_search import post_confirms, post_id

TODAY = date(2026, 10, 12)
POST = "https://x.com/zerosetinc/status/2107512024452493548"


def finding(**changes: Any) -> StartupFinding:
    data: dict[str, Any] = {
        "company": "Zeroset",
        "founder_name": "William Zhang",
        "founder_role": "Founder",
        "round": "Pre-Seed",
        "amount_usd": 5_200_000,
        "announced_on": date(2026, 10, 6),
        "source_url": POST,
        "company_url": None,
        "what_they_build": "World models of enterprise work.",
        "location": "San Francisco, United States",
        "social_url": POST,
        "x_handle": "zerosetinc",
    }
    return StartupFinding.model_validate({**data, **changes})


def test_only_a_link_to_a_post_has_a_post_id() -> None:
    assert post_id(POST) == "2107512024452493548"
    assert post_id("https://twitter.com/i/status/42") == "42"
    assert post_id("https://x.com/zerosetinc") is None
    assert post_id("https://betakit.com/zeroset-raises") is None
    assert post_id(None) is None


def test_a_post_counts_when_it_exists_and_is_about_raising(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    posts = {
        POST: "Today, we're announcing Zeroset's $5.2M pre-seed round to deploy world models.",
        "https://x.com/zerosetinc/status/2": "Great weekend hiking with the team!",
    }
    monkeypatch.setattr(x_search, "post_text", posts.get)

    assert post_confirms(finding())
    # A real post that isn't about funding, and a link to no post at all.
    assert not post_confirms(finding(social_url="https://x.com/zerosetinc/status/2"))
    assert not post_confirms(finding(social_url="https://x.com/zerosetinc/status/999"))


def test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() -> None:
    by_company = finding(founder_name="", founder_role="")

    assert to_leads([by_company], TODAY, 60, [Segment.EARLY], confirm=lambda f: True) == []
    (lead,) = to_leads(
        [by_company],
        TODAY,
        60,
        [Segment.EARLY],
        confirm=lambda f: True,
        region=Region.USA,
        require_founder=False,
    )
    assert (lead.company, lead.contact_name, lead.x_handle) == ("Zeroset", "", "zerosetinc")
    assert lead.hiring_signals == [f"Announcement post: {POST}"]
    assert lead.source_url == POST
