from datetime import date

from internship_agent.leads.contacts import (
    ContactType,
    company_key,
    contact_type,
    contacts_at,
    contacts_from_leads,
    to_vcard,
    uid,
)
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, Person


def _leads() -> list[Lead]:
    founder = Lead(
        company="Acme, Inc.",
        contact_name="Jane Doe",
        contact_role="Co-founder & CEO",
        email="jane@acme.ai",
        email_status=EmailStatus.PUBLISHED,
        announced_on=date(2026, 10, 1),
        source_url="https://techcrunch.com/acme",
        people=[Person(name="Raj Patel", role="Technical Recruiter")],
    )
    posting = Lead(
        kind=LeadKind.POSTING,
        company="acme",
        posting_title="SWE Intern",
        posting_url="https://jobs.ashbyhq.com/acme/1",
        source_url="https://jobs.ashbyhq.com/acme/1",
        contact_name="jane  doe",
        linkedin_url="https://www.linkedin.com/in/janedoe",
        people=[Person(name="Li Wei", role="Senior Software Engineer")],
    )
    other = Lead(
        company="Acme Robotics",
        contact_name="Sam Roe",
        announced_on=date(2026, 10, 1),
        source_url="https://techcrunch.com/acme-robotics",
    )
    return [founder, posting, other]


def test_company_key() -> None:
    assert company_key("Acme, Inc.") == company_key("acme") == "acme"
    assert company_key("Acme Robotics") != "acme"


def test_contact_type() -> None:
    assert contact_type("Technical Recruiter") is ContactType.RECRUITER
    assert contact_type("Co-founder & CEO") is ContactType.FOUNDER
    assert contact_type("Engineering Manager") is ContactType.HIRING_MANAGER
    assert contact_type("Senior Software Engineer") is ContactType.ENGINEER
    assert contact_type("") is ContactType.OTHER


def test_contacts_merge_across_leads_of_one_company() -> None:
    found = contacts_at(_leads(), "ACME")
    assert [c.name for c in found] == ["Jane Doe", "Raj Patel", "Li Wei"]
    jane = found[0]
    assert jane.email == "jane@acme.ai"
    assert jane.linkedin_url == "https://www.linkedin.com/in/janedoe"
    assert jane.type is ContactType.FOUNDER
    assert len(jane.lead_keys) == 2
    assert len(contacts_from_leads(_leads())) == 4


def test_vcard_is_stable_escaped_and_folded() -> None:
    contacts = contacts_from_leads(_leads())
    card = to_vcard(contacts)
    assert card.count("BEGIN:VCARD") == 4
    assert "\r\n" in card and "\n" not in card.replace("\r\n", "")
    assert "ORG:Acme\\, Inc." in card
    assert "N:Doe;Jane;;;" in card
    assert uid(contacts[0]) == uid(contacts_from_leads(_leads())[0])

    long = contacts[0].model_copy(update={"role": "é" * 80})
    for line in to_vcard([long]).split("\r\n"):
        assert len(line.encode("utf-8")) <= 75
