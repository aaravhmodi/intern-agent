import random
from datetime import UTC, datetime
from pathlib import Path

import pytest

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads import followups, patterns
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, LeadStatus
from internship_agent.leads.store import LeadStore
from internship_agent.sources import site_emails

NOW_UTC = datetime(2026, 10, 20, tzinfo=UTC)

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


def test_a_published_address_proves_the_company_format() -> None:
    known = patterns.by_domain(
        [lead(email="willem@acme.ai", email_status=EmailStatus.PUBLISHED, contact_name="Willem J")],
        datetime.now(UTC),
    )
    assert known == {"acme.ai": {"first": True}}


def test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(tmp_path: Path) -> None:
    LeadStore(tmp_path / "leads.json").save(
        [
            lead(company="Info Co", company_url="https://info.co", company_email="info@info.co"),
            lead(),  # Acme, careers@acme.ai
            lead(company="Replied", company_email="jobs@replied.io", replied_at=NOW_UTC),
            lead(company="Done", company_email="hello@done.ai", sent_to="hello@done.ai"),
        ]
    )
    picked = workflows.inbox_send(Settings(_env_file=None, data_dir=tmp_path), 10)
    assert [inbox.email for inbox in picked] == ["careers@acme.ai", "info@info.co"]
    assert picked[0].key == "acme/team" and followups.first_name(picked[0]) == "Acme team"


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
