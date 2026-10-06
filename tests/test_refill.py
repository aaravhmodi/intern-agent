# ruff: noqa: E501
from typing import Any

from internship_agent.leads.refill import open_postings, refill
from internship_agent.leads.schemas import Lead, LeadStatus
from internship_agent.leads.store import merge, normalize_url
from internship_agent.sources import simplify

MARKDOWN = """
## 💻 Software Engineering Internship Roles
<table>
<thead><tr><th>Company</th><th>Role</th><th>Location</th><th>Terms</th><th>Application</th><th>Age</th></tr></thead>
<tbody>
<tr><td><strong><a href="https://simplify.jobs/c/Acme">Acme</a></strong></td><td>SWE Intern</td>
<td>Toronto, ON, Canada</td><td>Winter 2027</td>
<td><a href="https://jobs.ashbyhq.com/acme/1/application?utm_source=Simplify&ref=Simplify"><img alt="Apply"></a>
<a href="https://simplify.jobs/p/1"><img alt="Simplify"></a></td><td>3d</td></tr>
<tr><td>↳</td><td>Backend Intern</td><td>Remote in Canada</td><td>Winter 2027, Spring 2027</td>
<td><a href="https://jobs.ashbyhq.com/acme/2"><img alt="Apply"></a></td><td>1mo</td></tr>
<tr><td>🔥 Bigco</td><td>SWE Intern</td><td>Toronto, ON</td><td>Winter 2027</td><td>🔒</td><td>2d</td></tr>
<tr><td>Faraway</td><td>SWE Intern</td><td>Austin, TX</td><td>Winter 2027</td>
<td><a href="https://faraway.com/jobs/9">Apply</a></td><td>1d</td></tr>
<tr><td>Later</td><td>SWE Intern</td><td>Toronto, ON</td><td>Fall 2027</td>
<td><a href="https://later.com/jobs/1">Apply</a></td><td>1d</td></tr>
</tbody></table>
## 🔧 Hardware Engineering Internship Roles
<table><tbody>
<tr><td>Gradco</td><td>ML Researcher Intern 🎓</td><td>Toronto, ON</td><td>Winter 2027</td>
<td><a href="https://gradco.com/1">Apply</a></td><td>1d</td></tr>
<tr><td>Chipco</td><td>FPGA Intern</td><td>Toronto, ON</td><td>Winter 2027</td>
<td><a href="https://chipco.com/1">Apply</a></td><td>1d</td></tr>
</tbody></table>
"""


def posting(company: str, url: str, **overrides: Any) -> Lead:
    data = {
        "kind": "posting",
        "company": company,
        "posting_title": "SWE Intern",
        "posting_url": url,
        "source_url": url,
    }
    return Lead.model_validate({**data, **overrides})


def test_parse_handles_continuation_rows_closed_rows_and_sections() -> None:
    rows = simplify.parse(MARKDOWN)

    assert [(r.company, r.role, r.closed) for r in rows] == [
        ("Acme", "SWE Intern", False),
        ("Acme", "Backend Intern", False),
        ("Bigco", "SWE Intern", True),
        ("Faraway", "SWE Intern", False),
        ("Later", "SWE Intern", False),
        ("Gradco", "ML Researcher Intern 🎓", False),
        ("Chipco", "FPGA Intern", False),
    ]
    assert rows[0].url.startswith("https://jobs.ashbyhq.com/acme/1")
    assert rows[1].age_days == 30


def test_matching_filters_term_location_section_and_closed() -> None:
    found = simplify.matching(simplify.parse(MARKDOWN))
    assert [(p.company, p.role) for p in found] == [
        ("Acme", "SWE Intern"),
        ("Acme", "Backend Intern"),
    ]


def test_to_lead_strips_role_markers() -> None:
    row = simplify.Posting(
        section="Software Engineering",
        company="A",
        role="SWE Intern 🛂",
        location="Toronto",
        terms="Winter 2027",
        url="https://a.com/1",
        closed=False,
        age="1d",
    )
    assert simplify.to_lead(row).posting_title == "SWE Intern"


def test_to_lead_normalizes_url() -> None:
    lead = simplify.to_lead(simplify.matching(simplify.parse(MARKDOWN))[0])
    assert lead.posting_url == "https://jobs.ashbyhq.com/acme/1"
    assert lead.status is LeadStatus.NEW


def test_normalize_url_keeps_meaningful_query() -> None:
    assert normalize_url("https://Stripe.com/jobs/search?gh_jid=81&utm_source=x&ref=Simplify") == (
        "https://stripe.com/jobs/search?gh_jid=81"
    )
    assert (
        normalize_url("http://jobs.ashbyhq.com/a/1/application/") == "https://jobs.ashbyhq.com/a/1"
    )


def test_merge_dedupes_same_posting_with_different_key() -> None:
    existing = [posting("Acme", "https://jobs.ashbyhq.com/acme/1", contact_name="Jane Doe")]
    incoming = [posting("Acme", "https://jobs.ashbyhq.com/acme/1/application?utm_source=x")]
    _, added = merge(existing, incoming)
    assert added == 0


def test_refill_tops_up_and_never_readds_applied_or_skipped() -> None:
    leads = [
        posting("Applied", "https://a.com/1", status=LeadStatus.APPLIED),
        posting("Skipped", "https://s.com/1", status=LeadStatus.SKIPPED),
        posting("Open", "https://o.com/1"),
    ]
    candidates = [
        posting("Applied", "https://a.com/1"),
        posting("Skipped", "https://s.com/1?utm_source=x"),
        posting("New1", "https://n.com/1"),
        posting("New2", "https://n.com/2"),
        posting("New3", "https://n.com/3"),
    ]

    all_leads, added = refill(leads, candidates, target_open=3)

    assert [x.company for x in added] == ["New1", "New2"]
    assert len(open_postings(all_leads)) == 3


def test_refill_noop_when_enough_open() -> None:
    leads = [posting("Open", "https://o.com/1")]
    assert refill(leads, [posting("New", "https://n.com/1")], target_open=1) == (leads, [])


def test_matching_by_region_includes_us_and_europe() -> None:
    from internship_agent.leads.schemas import Region

    rows = [
        simplify.Posting(
            section="Software Engineering",
            company=c,
            role="SWE Intern",
            location=loc,
            terms="Winter 2027",
            url=f"https://{c}.com/1",
            closed=False,
            age="1d",
        )
        for c, loc in [
            ("us", "Austin, TX"),
            ("eu", "London, UK"),
            ("ca", "Toronto, ON"),
            ("asia", "Tokyo, Japan"),
        ]
    ]
    found = simplify.matching(rows, locations=(), regions={Region.USA, Region.EUROPE})
    assert sorted(p.company for p in found) == ["eu", "us"]
    assert simplify.to_lead(found[0]).region in {Region.USA, Region.EUROPE}


def test_software_role_filter_and_company_cap() -> None:
    assert simplify.is_software_role("Software Engineer Intern - AI Tooling")
    assert simplify.is_software_role("Machine Learning Engineering Co-op")
    assert not simplify.is_software_role("Solar Hardware Engineer Intern")
    assert not simplify.is_software_role("GIS Intern - Fire Department")
    assert not simplify.is_software_role("Technology Co-op - Northeastern University")
    rows = [
        simplify.Posting(
            section="Software Engineering",
            company="T",
            role=f"SWE Intern {i}",
            location="Palo Alto, CA",
            terms="Winter 2027",
            url=f"https://t.com/{i}",
            closed=False,
            age=f"{i}d",
        )
        for i in range(5)
    ]
    assert len(simplify.cap_per_company(rows, per_company=3)) == 3
