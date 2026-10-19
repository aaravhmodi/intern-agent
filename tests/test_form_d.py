from datetime import date

import pytest

from internship_agent.ai import CompanySite
from internship_agent.leads.schemas import EmailStatus, Segment
from internship_agent.sources import form_d

# Trimmed from a real filing (Vernex, Inc., October 16, 2026).
FILING = """<?xml version="1.0"?>
<edgarSubmission>
  <primaryIssuer>
    <entityName>Vernex, Inc.</entityName>
    <issuerAddress><city>NEWARK</city><stateOrCountry>DE</stateOrCountry></issuerAddress>
    <yearOfInc><withinFiveYears>true</withinFiveYears><value>2026</value></yearOfInc>
  </primaryIssuer>
  <relatedPersonsList>
    <relatedPersonInfo>
      <relatedPersonName><firstName>JANE</firstName><lastName>ADVISOR</lastName></relatedPersonName>
      <relatedPersonRelationshipList><relationship>Director</relationship></relatedPersonRelationshipList>
    </relatedPersonInfo>
    <relatedPersonInfo>
      <relatedPersonName><firstName>Dmitry</firstName><lastName>Kafidov</lastName></relatedPersonName>
      <relatedPersonRelationshipList>
        <relationship>Executive Officer</relationship><relationship>Director</relationship>
      </relatedPersonRelationshipList>
    </relatedPersonInfo>
  </relatedPersonsList>
  <offeringData>
    <industryGroup><industryGroupType>Other Technology</industryGroupType></industryGroup>
    <typeOfFiling>
      <newOrAmendment><isAmendment>false</isAmendment></newOrAmendment>
      <dateOfFirstSale><value>2026-09-15</value></dateOfFirstSale>
    </typeOfFiling>
    <offeringSalesAmounts>
      <totalOfferingAmount>Indefinite</totalOfferingAmount>
      <totalAmountSold>1400000</totalAmountSold>
    </offeringSalesAmounts>
    <signatureBlock><signature>
      <nameOfSigner>Dmitry Kafidov</nameOfSigner>
      <signatureTitle>Chief Executive Officer</signatureTitle>
    </signature></signatureBlock>
  </offeringData>
</edgarSubmission>"""
URL = "https://www.sec.gov/Archives/edgar/data/2160116/000216011626000001/"


def test_a_young_tech_company_raise_becomes_a_filing() -> None:
    filing = form_d.parse_filing(FILING, URL, date(2026, 10, 16))
    assert filing is not None
    assert filing.company == "Vernex" and filing.location == "Newark, DE"
    assert filing.amount_usd == 1_400_000 and filing.first_sale == "2026-09-15"
    # The officer who signed is the contact; a director who isn't an officer is not.
    assert filing.contact_name == "Dmitry Kafidov"
    assert filing.contact_role == "Chief Executive Officer"
    assert filing.people == ["Jane Advisor", "Dmitry Kafidov"]


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("Other Technology", "Real Estate"),
        ("<isAmendment>false", "<isAmendment>true"),
        ("<withinFiveYears>true", "<withinFiveYears>false"),
        ("<totalAmountSold>1400000", "<totalAmountSold>1585000000"),
        ("<totalAmountSold>1400000", "<totalAmountSold>50000"),
        ("<relationship>Executive Officer</relationship>", ""),
    ],
)
def test_funds_old_companies_and_odd_sizes_are_left_out(old: str, new: str) -> None:
    assert form_d.parse_filing(FILING.replace(old, new), URL, date(2026, 10, 16)) is None


def test_daily_index_lists_new_filings_only() -> None:
    index = (
        "Form Type   Company Name   CIK   Date Filed  File Name\n"
        "D           Vernex, Inc.  2160116  20261016  edgar/data/2160116/0002160116-26-000001.txt\n"
        "D/A         Old Co         1        20261016  edgar/data/1/0000000001-26-000001.txt\n"
        "10-K        Big Co         2        20261016  edgar/data/2/0000000002-26-000001.txt\n"
    )
    assert form_d.form_d_paths(index) == ["edgar/data/2160116/0002160116-26-000001.txt"]
    assert form_d.index_url(date(2026, 10, 16)).endswith("/2026/QTR4/form.20261016.idx")


def test_an_email_is_published_only_if_the_page_shows_it(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    filing = form_d.parse_filing(FILING, URL, date(2026, 10, 16))
    assert filing is not None
    site = CompanySite(
        company_url="https://www.vernex.io/",
        what_they_build="Tools",
        email="dmitry@vernex.io",
        email_source="https://vernex.io/team",
    )
    monkeypatch.setattr(form_d, "page_text", lambda url: "Contact dmitry@vernex.io")
    lead = form_d.to_lead(filing, site)
    assert (lead.email, lead.email_status) == ("dmitry@vernex.io", EmailStatus.PUBLISHED)
    assert lead.segment is Segment.EARLY and lead.source_url == URL

    # The model claimed an address the page doesn't show: fall back to an unverified guess.
    monkeypatch.setattr(form_d, "page_text", lambda url: "no emails here")
    lead = form_d.to_lead(filing, site)
    assert (lead.email, lead.email_status) == ("dmitry@vernex.io", EmailStatus.PATTERN)

    # A shared inbox on the page is not the founder's address.
    monkeypatch.setattr(form_d, "page_text", lambda url: "Press: media@vernex.io")
    lead = form_d.to_lead(filing, site.model_copy(update={"email": "media@vernex.io"}))
    assert (lead.email, lead.email_status) == ("dmitry@vernex.io", EmailStatus.PATTERN)
