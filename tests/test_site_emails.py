import random

import pytest

from internship_agent.leads import patterns
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, LeadStatus
from internship_agent.sources import site_emails

PAGES = {
    "https://acme.ai/": '<a href="mailto:hello@acme.ai">Say hi</a> press@acme.ai',
    "https://acme.ai/careers": "Apply: careers@acme.ai or jobs@acme.ai. Not you@gmail.com",
    "https://acme.ai/team": "Jane Doe, CEO (jane.d@acme.ai). sales@acme.ai",
}


def test_published_addresses_are_read_from_the_company_pages(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(site_emails, "_fetch", lambda url: (url, PAGES.get(url, "")))
    found = site_emails.published("https://acme.ai/", "acme.ai")
    assert "you@gmail.com" not in found and found["careers@acme.ai"] == "https://acme.ai/careers"
    assert site_emails.personal(found, "Jane Doe") == ("jane.d@acme.ai", "https://acme.ai/team")
    assert site_emails.personal(found, "Al Smith") is None  # "al" is in "sales"; too short
    assert site_emails.generic(found) == ("careers@acme.ai", "https://acme.ai/careers")
    assert site_emails.generic({"press@acme.ai": "x", "sales@acme.ai": "y"}) is None


def lead(**more: object) -> Lead:
    data = {
        "kind": LeadKind.FOUNDER,
        "company": "Acme",
        "company_url": "https://acme.ai/",
        "source_url": "https://www.sec.gov/x/",
        "contact_name": "Jane Doe",
        "announced_on": "2026-10-01",
        "company_email": "careers@acme.ai",
    }
    return Lead.model_validate({**data, **more})


def test_the_company_inbox_takes_over_after_two_bounces() -> None:
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    one = lead(bounced_emails=["jane@acme.ai"])
    assert patterns.next_guess(one, "acme.ai", counts, random.Random(0)) != "careers@acme.ai"
    two = lead(
        bounced_emails=["jane@acme.ai"],
        sent_to="jane.doe@acme.ai",
        followups_stopped="bounced",
        status=LeadStatus.CONTACTED,
    )
    assert patterns.next_guess(two, "acme.ai", counts, random.Random(0)) == "careers@acme.ai"
    patterns.point_at(two, "careers@acme.ai")
    assert (two.email, two.email_status) == ("careers@acme.ai", EmailStatus.PUBLISHED)
    assert two.bounced_emails == ["jane@acme.ai", "jane.doe@acme.ai"]
