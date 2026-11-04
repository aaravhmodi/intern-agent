from datetime import date

from internship_agent.leads.schemas import Lead, LeadKind, Region
from internship_agent.leads.store import new_companies
from internship_agent.sources.hiring_sheet import HEADER, link, to_leads

ROWS: list[list[object]] = [
    ["Looking to work at a startup?"],
    [None],
    list(HEADER),
    [1.0, "Asendia AI", "B2B", "Product Engineer", "Remote, OR, US / CA / DE", "3+ years",
     "3 days", 4.0,
     '=HYPERLINK("https://www.ycombinator.com/companies/asendia-ai/jobs/euK3IzX-pe","Open role")',
     '=HYPERLINK("https://www.ycombinator.com/companies/asendia-ai/jobs","View all jobs")',
     '=HYPERLINK("https://asendia.ai/","Company website")'],
    [2.0, "Beam", "B2B", "Chief of Staff", "Toronto, ON", "Any (new grads ok)", "1 month", 2.0,
     None, '=HYPERLINK("https://www.ycombinator.com/companies/beam/jobs","View all jobs")', None],
    [3.0, "No Link", "B2B", "Engineer", "NYC", "", "", None, None, None, None],
    [4.0, "asendia ai", "B2B", "Duplicate", "", "", "", None,
     '=HYPERLINK("https://www.ycombinator.com/companies/x/jobs/1","Open role")', None, None],
]  # fmt: skip


def test_link() -> None:
    assert link('=HYPERLINK("https://a.io/x","Open")') == "https://a.io/x"
    assert link("https://a.io") == "https://a.io"
    assert link('=HYPERLINK("javascript:alert(1)","x")') is None
    assert link(None) is None


def test_rows_become_company_leads() -> None:
    leads = to_leads(ROWS, "Nov 3 2026")
    assert [lead.company for lead in leads] == ["Asendia AI", "Beam"]
    asendia, beam = leads
    assert asendia.kind is LeadKind.FOUNDER
    assert asendia.announced_on is None and asendia.contact_name == ""
    assert asendia.company_url == "https://asendia.ai/"
    assert asendia.source_url == "https://www.ycombinator.com/companies/asendia-ai/jobs/euK3IzX-pe"
    assert asendia.region is Region.USA
    assert asendia.hiring_signals == [
        "Hiring a Product Engineer (3+ years, posted 3 days before Nov 3 2026)",
        "4 open role(s): https://www.ycombinator.com/companies/asendia-ai/jobs",
        "Industry: B2B",
    ]
    assert asendia.key == "asendia-ai/team"
    # No single role link: the company's jobs page is the source.
    assert beam.source_url == "https://www.ycombinator.com/companies/beam/jobs"
    assert beam.company_url is None and beam.region is Region.CANADA


def test_import_skips_companies_already_stored() -> None:
    stored = Lead(
        company="Asendia AI, Inc.",
        contact_name="Jane Doe",
        announced_on=date(2026, 10, 1),
        source_url="https://techcrunch.com/x",
    )
    incoming = to_leads(ROWS, "Nov 3 2026")
    assert [lead.company for lead in new_companies([stored], incoming)] == ["Beam"]
