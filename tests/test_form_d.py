from datetime import date

import pytest

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
    assert filing.officers == ["Dmitry Kafidov"]


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


def test_the_site_must_name_someone_on_the_filing_or_its_legal_name(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    filing = form_d.parse_filing(FILING, URL, date(2026, 10, 16))
    assert filing is not None
    sites = {
        # A same-name company that names nobody from the filing.
        "https://vernex.com/": "<title>Vernex</title> Wire harnesses",
        "https://vernex.ai/": '<meta name="description" content="AI tools"> Vernex',
        "https://vernex.ai/team": "Dmitry Kafidov, CEO. Write to dmitry.k@vernex.ai",
        "https://vernex.io/": "Vernex. (c) 2026 Vernex, Inc.",
    }
    monkeypatch.setattr(form_d, "_fetch", lambda url: (url, sites.get(url, "")))
    site = form_d.find_site(filing)
    assert site is not None and site.url == "https://vernex.ai/"
    assert site.what_they_build == "AI tools"

    lead = form_d.to_lead(filing, site)
    assert (lead.email, lead.email_status) == ("dmitry.k@vernex.ai", EmailStatus.PUBLISHED)
    assert lead.email_source == "https://vernex.ai/team"
    assert lead.segment is Segment.EARLY and lead.source_url == URL
    other = form_d.to_lead(filing, site, "Ana Ruiz")
    assert (other.contact_name, other.contact_role) == ("Ana Ruiz", "Executive Officer")
    assert other.email == "ana@vernex.ai" and other.company == lead.company

    # Only the legal name: still theirs, but no published address, so a guess. The site
    # redirects to its web host, on a port; the email stays on the domain they own.
    del sites["https://vernex.ai/"]
    monkeypatch.setattr(
        form_d,
        "_fetch",
        lambda url: (url.replace("vernex.io", "x.azurestaticapps.net:443"), sites.get(url, "")),
    )
    site = form_d.find_site(filing)
    assert site is not None and site.url == "https://vernex.io/"
    lead = form_d.to_lead(filing, site)
    assert (lead.email, lead.email_status) == ("dmitry@vernex.io", EmailStatus.PATTERN)

    del sites["https://vernex.io/"]
    assert form_d.find_site(filing) is None
