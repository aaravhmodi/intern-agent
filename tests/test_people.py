from pathlib import Path
from typing import Any

import pytest

from internship_agent import workflows
from internship_agent.ai import PeopleFindings, PersonFinding, search_people
from internship_agent.config import Settings
from internship_agent.leads.schemas import Lead, Person, Segment
from internship_agent.leads.store import LeadStore
from internship_agent.sources import people as people_source
from internship_agent.sources.people import source_names, to_people
from tests.test_ai import fake_client

LEAD = Lead.model_validate(
    {
        "contact_name": "Jane Doe",
        "contact_role": "Co-founder & CEO",
        "company": "Acme",
        "round": "series-a",
        "announced_on": "2026-09-20",
        "source_url": "https://example.com",
    }
)


def person(**overrides: Any) -> PersonFinding:
    data: dict[str, Any] = {
        "name": "Sam Lee",
        "role": "Engineering Manager",
        "linkedin_url": "https://www.linkedin.com/in/samlee",
        "source_url": "https://acme.com/team",
    }
    return PersonFinding.model_validate({**data, **overrides})


def test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact() -> None:
    found = [
        person(),
        person(name="sam  lee", role="Duplicate"),
        person(name="Jane Doe", role="Co-founder & CEO"),
        person(name="Recruiting", role="Team inbox"),
        person(name="Ana Ruiz", role="Recruiter", source_url="https://acme.com/404"),
        person(name="Raj Patel", role="Engineer", linkedin_url="https://linkedin.com/company/acme"),
    ]
    kept = to_people(
        "Acme", found, skip="Jane Doe", confirm=lambda c, f: not f.source_url.endswith("404")
    )
    assert [(p.name, p.role, p.linkedin_url) for p in kept] == [
        ("Sam Lee", "Engineering Manager", "https://www.linkedin.com/in/samlee"),
        ("Raj Patel", "Engineer", None),  # not a profile URL: the dashboard searches instead
    ]


def test_a_linkedin_source_passes_without_being_fetched(monkeypatch: pytest.MonkeyPatch) -> None:
    fetched: list[str] = []
    monkeypatch.setattr(people_source, "page_names", lambda url, *a: fetched.append(url) or False)
    assert source_names("Acme", person(source_url="https://ca.linkedin.com/in/samlee"))
    assert fetched == []
    assert not source_names("Acme", person(source_url="https://notlinkedin.com/in/samlee"))
    assert not source_names("Acme", person(source_url="javascript://linkedin.com/x"))
    assert len(fetched) == 2


def test_search_people_asks_for_roles_that_suit_the_company_size() -> None:
    client, responses = fake_client(PeopleFindings(people=[person()]))

    found = search_people(client, "m", LEAD, Segment.MID)

    system = responses.kwargs["input"][0]["content"]
    assert "engineering manager" in system and "recruiter" in system
    assert "leave out the CEO and the co-founders" in system
    assert "Do not include Jane Doe" in system
    assert found == [person()]

    search_people(client, "m", LEAD, Segment.EARLY)
    assert "the founders, the CTO" in responses.kwargs["input"][0]["content"]


def test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = Settings(data_dir=tmp_path, openai_api_key="test", _env_file=None)  # type: ignore[call-arg]
    LeadStore(tmp_path / "leads.json").save([LEAD])
    found = [person(), person(name="Ana Ruiz"), person(name="Raj Patel")]
    monkeypatch.setattr(workflows, "search_people", lambda *a: found)
    monkeypatch.setattr(people_source, "page_names", lambda *a: True)

    lead = workflows.find_people(settings, LEAD.key)
    assert [p.name for p in lead.people] == ["Sam Lee", "Ana Ruiz", "Raj Patel"]

    found.clear()
    again = workflows.find_people(settings, LEAD.key)
    assert again.people == lead.people and isinstance(again.people[0], Person)
