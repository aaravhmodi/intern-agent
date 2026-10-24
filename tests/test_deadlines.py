from datetime import date

from internship_agent.leads.deadlines import find_deadline
from internship_agent.leads.refill import expire_postings
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus


def posting(name: str, deadline: date | None, status: LeadStatus = LeadStatus.NEW) -> Lead:
    return Lead(
        kind=LeadKind.POSTING,
        company=name,
        source_url="https://example.com",
        posting_title="SWE Intern",
        posting_url=f"https://jobs.example.com/{name}",
        deadline=deadline,
        status=status,
    )


def test_finds_a_stated_deadline() -> None:
    assert find_deadline("Apply by November 30, 2026. Great team.") == date(2026, 11, 30)
    assert find_deadline("Application deadline: Dec 5th, 2026") == date(2026, 12, 5)
    assert find_deadline("Closing date - 2026-11-02") == date(2026, 11, 2)


def test_ignores_text_without_a_full_dated_deadline() -> None:
    assert find_deadline("Apply by November 30. We started in 2019.") is None
    assert find_deadline("Rolling applications, join us in January 2027") is None


def test_expire_postings_skips_only_open_postings_past_deadline() -> None:
    today = date(2026, 10, 21)
    late = posting("late", date(2026, 10, 1))
    live = posting("live", date(2026, 11, 1))
    undated = posting("undated", None)
    applied = posting("applied", date(2026, 10, 1), LeadStatus.APPLIED)
    expired = expire_postings([late, live, undated, applied], today)
    assert expired == [late]
    assert late.status is LeadStatus.SKIPPED and "Expired" in late.notes[-1].text
    assert [live.status, undated.status, applied.status] == [
        LeadStatus.NEW,
        LeadStatus.NEW,
        LeadStatus.APPLIED,
    ]


def test_expire_closed_skips_open_postings_that_are_gone() -> None:
    from internship_agent.leads.refill import expire_closed

    gone, live = posting("gone", None), posting("live", None)
    gone.posting_url, live.posting_url = "https://x.test/gone", "https://x.test/live"
    assert expire_closed([gone, live], lambda url: url.endswith("gone")) == [gone]
    assert gone.status is LeadStatus.SKIPPED and live.status is LeadStatus.NEW
