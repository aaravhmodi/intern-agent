from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

import pytest

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads.network import RECHECK_AFTER, apply_network, companies_due
from internship_agent.leads.schemas import Lead, LeadStatus, NetworkPerson
from internship_agent.leads.store import LeadStore
from internship_agent.sources import linkedin_network
from internship_agent.sources.linkedin_network import people_from_cards, search_url

NOW = datetime(2026, 11, 11, tzinfo=UTC)

# Result cards as the browser reads them from LinkedIn's people search (mock fixtures).
CARDS: list[dict[str, Any]] = [
    {
        "text": "Sam Lee\nView Sam Lee’s profile\n • 3rd+\n3rd+ degree connection\n"
        "Backend Engineer at Acme\nToronto, Ontario, Canada\nConnect",
        "href": "https://www.linkedin.com/in/samlee?miniProfileUrn=abc",
    },
    {
        "text": "Ana Ruiz • 2nd\n2nd degree connection\nRecruiter | Hiring interns\n"
        "Waterloo, Ontario\nCurrent: Technical Recruiter at Acme Inc\n"
        "Priya Shah is a mutual connection\nMessage",
        "href": "https://ca.linkedin.com/in/anaruiz/",
    },
    {  # matched "acme" somewhere else on the profile; does not work there
        "text": "Raj Patel\n • 2nd\nEngineer at Acmetech\nPast: Intern at Acme\nConnect",
        "href": "https://www.linkedin.com/in/rajpatel",
    },
    {"text": "LinkedIn Member\n • 3rd+\nEngineer at Acme", "href": "https://www.linkedin.com/in/x"},
    {"text": "Bo Chen\nEngineer at Acme\nConnect", "href": "https://www.linkedin.com/in/bochen"},
    {  # the same person again (a nested list item)
        "text": "Ana Ruiz • 2nd\nCurrent: Technical Recruiter at Acme Inc",
        "href": "https://ca.linkedin.com/in/anaruiz/",
    },
    {"text": "Ed Wu\n • 2nd\nCTO at Acme", "href": "https://www.linkedin.com/company/acme"},
]


def lead(company: str = "Acme", **overrides: Any) -> Lead:
    data: dict[str, Any] = {
        "company": company,
        "contact_name": "Jane Doe",
        "source_url": f"https://example.com/{company}",
    }
    return Lead.model_validate({**data, **overrides})


def test_search_url_limits_to_second_and_third_degree() -> None:
    query = parse_qs(urlsplit(search_url("Acme, Inc.")).query)
    assert query["keywords"] == ["Acme, Inc."]
    assert query["network"] == ['["S","O"]']


def test_people_from_cards_keeps_only_people_at_the_company_second_degree_first() -> None:
    people = people_from_cards(CARDS, "Acme")
    assert [(p.name, p.degree, p.profile_url) for p in people] == [
        ("Ana Ruiz", 2, "https://ca.linkedin.com/in/anaruiz/"),
        ("Sam Lee", 3, "https://www.linkedin.com/in/samlee"),
    ]
    ana, sam = people
    assert ana.headline == "Technical Recruiter at Acme Inc"
    assert ana.mutual == "Priya Shah is a mutual connection"
    assert sam.headline == "Backend Engineer at Acme" and sam.mutual == ""


def test_companies_due_puts_unchecked_first_and_skips_recent_and_skipped() -> None:
    leads = [
        lead("Old", network_checked_at=NOW - RECHECK_AFTER - timedelta(days=5)),
        lead("Older", network_checked_at=NOW - RECHECK_AFTER - timedelta(days=9)),
        lead("Recent", network_checked_at=NOW - timedelta(days=2)),
        lead("Fresh"),
        lead("fresh, inc.", contact_name="Other Person"),  # the same company
        lead("Dropped", status=LeadStatus.SKIPPED),
        # A second lead at Recent that was never checked: the company still was.
        lead("Recent", contact_name="Someone Else"),
    ]
    assert companies_due(leads, NOW, limit=10) == ["Fresh", "Older", "Old"]
    assert companies_due(leads, NOW, limit=1) == ["Fresh"]


def test_apply_network_stores_on_every_lead_at_the_company() -> None:
    leads = [lead("Acme"), lead("acme inc", contact_name="Other"), lead("Beta")]
    found = [NetworkPerson(name="Sam", profile_url="https://linkedin.com/in/sam", degree=2)]
    changed = apply_network(leads, "Acme", found, NOW)
    assert len(changed) == 2
    assert all(x.network == found and x.network_checked_at == NOW for x in changed)
    assert leads[2].network == [] and leads[2].network_checked_at is None


def test_network_person_rejects_non_profile_urls() -> None:
    with pytest.raises(ValueError):
        NetworkPerson(name="X", profile_url="https://evil.example/in/x", degree=2)


def _settings(tmp_path: Path) -> Settings:
    return Settings(  # type: ignore[call-arg]
        data_dir=tmp_path,
        linkedin_cdp_url="http://browser:9223",
        linkedin_network_pause_seconds=0,
        _env_file=None,
    )


def test_find_networks_checks_each_company_once_and_survives_one_failing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    LeadStore(tmp_path / "leads.json").save(
        [lead("Acme"), lead("Acme", contact_name="Other"), lead("Broken"), lead("Gamma")]
    )
    searched: list[str] = []

    def fake_cards(cdp_url: str, company: str) -> list[dict[str, Any]]:
        searched.append(company)
        if company == "Broken":
            raise TimeoutError
        return CARDS

    monkeypatch.setattr(linkedin_network, "cards", fake_cards)
    logs: list[str] = []
    assert workflows.find_networks(_settings(tmp_path), log=logs.append) == 2
    assert searched == ["Acme", "Broken", "Gamma"]
    stored = LeadStore(tmp_path / "leads.json").load()
    assert [len(x.network) for x in stored] == [2, 2, 0, 0]
    assert stored[2].network_checked_at is None  # tried again next run
    assert "Broken: LinkedIn search failed (TimeoutError)" in logs


def test_find_networks_stops_at_the_sign_in_wall(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    LeadStore(tmp_path / "leads.json").save([lead("Acme"), lead("Beta")])
    calls: list[str] = []

    def signed_out(cdp_url: str, company: str) -> list[dict[str, Any]]:
        calls.append(company)
        raise linkedin_network.SignInRequired("sign in")

    monkeypatch.setattr(linkedin_network, "cards", signed_out)
    with pytest.raises(linkedin_network.SignInRequired):
        workflows.find_networks(_settings(tmp_path))
    assert calls == ["Acme"]


def test_find_network_needs_a_browser(tmp_path: Path) -> None:
    LeadStore(tmp_path / "leads.json").save([lead("Acme")])
    settings = Settings(data_dir=tmp_path, _env_file=None)  # type: ignore[call-arg]
    with pytest.raises(ValueError, match="CDP_URL"):
        workflows.find_network(settings, lead("Acme").key)
