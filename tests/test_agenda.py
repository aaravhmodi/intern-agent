from datetime import UTC, date, datetime
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from internship_agent import agenda
from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.leads.schemas import Lead, LeadStatus
from internship_agent.leads.store import LeadStore
from internship_agent.opportunities.schemas import Opportunity, OpportunityAssessment
from internship_agent.opportunities.store import OpportunityStore

TODAY = date(2026, 10, 20)


def _assessment(**kw: object) -> OpportunityAssessment:
    data: dict[str, object] = {
        "format": "in person",
        "location": "London, ON",
        "apply_by": date(2026, 11, 1),
        "travel": "partial",
        "travel_details": "Reimbursed after the event.",
        "travel_source_url": "https://hack.dev/faq",
        "cost": "free",
        "effort": "moderate",
        "effort_details": "36 hours",
        "fit_score": 60,
        "fit": [],
        "highlights": [],
        "summary": "Go.",
    }
    return OpportunityAssessment.model_validate({**data, **kw})


def _opp(**kw: object) -> Opportunity:
    data: dict[str, object] = {
        "kind": "hackathon",
        "title": "Hack Western",
        "url": "https://hack.dev",
        "source": "test",
        "starts_on": date(2026, 11, 20),
        "ends_on": date(2026, 11, 22),
        "deadline": date(2026, 11, 22),
        "deadline_label": "Submissions close",
        "location": "London, Canada",
    }
    return Opportunity.model_validate({**data, **kw})


def _emailed(**kw: object) -> Lead:
    data: dict[str, object] = {
        "kind": "posting",
        "company": "Acme",
        "posting_url": "https://acme.com/jobs/1",
        "source_url": "https://acme.com/jobs/1",
        "contact_name": "Jane Doe",
        "sent_at": datetime(2026, 10, 18, 15, tzinfo=UTC),
        "sent_to": "jane@acme.com",
        "status": "contacted",
    }
    return Lead.model_validate({**data, **kw})


def test_an_opportunity_gives_apply_deadline_and_event_items() -> None:
    found = agenda.opportunity_items(_opp(assessment=_assessment()))
    assert [(i.kind, i.day, i.end, i.title) for i in found] == [
        ("apply", date(2026, 11, 1), None, "Apply: Hack Western"),
        ("deadline", date(2026, 11, 22), None, "Submissions close: Hack Western"),
        ("event", date(2026, 11, 20), date(2026, 11, 22), "Hack Western"),
    ]
    assert all(i.mine for i in found)  # partial travel paid makes it promising


def test_mine_means_planned_or_promising() -> None:
    def mine(o: Opportunity) -> bool:
        return agenda.opportunity_items(o)[0].mine

    assert not mine(_opp())
    assert mine(_opp(status="interested"))
    assert mine(_opp(assessment=_assessment(fit_score=80, travel="none")))
    assert mine(_opp(assessment=_assessment(fit_score=40, travel="covered")))
    assert not mine(_opp(assessment=_assessment(fit_score=40, travel="none")))
    assert agenda.opportunity_items(_opp(status="skipped")) == []


def test_follow_ups_land_on_their_due_day_or_today_if_overdue() -> None:
    [due] = agenda.lead_items(_emailed(), followup_days=5, today=TODAY)
    assert (due.kind, due.day, due.title) == (
        "followup",
        date(2026, 10, 23),
        "Follow up: Jane Doe (Acme)",
    )
    [overdue] = agenda.lead_items(
        _emailed(sent_at=datetime(2026, 10, 1, tzinfo=UTC)), followup_days=5, today=TODAY
    )
    assert overdue.day == TODAY
    replied = _emailed(replied_at=datetime(2026, 10, 19, tzinfo=UTC))
    assert agenda.lead_items(replied, followup_days=5, today=TODAY) == []


def test_a_posting_deadline_shows_until_you_apply() -> None:
    lead = _emailed(
        sent_at=None,
        sent_to="",
        deadline=date(2026, 11, 5),
        posting_title="SWE Intern",
        status="scored",
    )
    [item] = agenda.lead_items(lead, followup_days=5, today=TODAY)
    assert (item.kind, item.title) == ("apply", "Apply: Acme (SWE Intern)")
    lead.status = LeadStatus.APPLIED
    assert agenda.lead_items(lead, followup_days=5, today=TODAY) == []


def test_ics_is_valid_all_day_events() -> None:
    long_title = "Deadline: " + "Very, long; title " * 8
    found = [
        agenda.Item(
            day=date(2026, 11, 20),
            end=date(2026, 11, 22),
            kind="event",
            title="Hack, Western",
            key="https://hack.dev",
            url="https://hack.dev",
            mine=True,
        ),
        agenda.Item(day=date(2026, 11, 1), kind="deadline", title=long_title, key="k", mine=True),
    ]
    ics = agenda.to_ics(found, datetime(2026, 10, 20, 12, tzinfo=UTC))
    lines = ics.split("\r\n")
    assert ics.endswith("END:VCALENDAR\r\n") and lines[0] == "BEGIN:VCALENDAR"
    assert "DTSTART;VALUE=DATE:20261120" in lines and "DTEND;VALUE=DATE:20261123" in lines
    assert "SUMMARY:Hack\\, Western" in lines
    assert all(len(line.encode()) <= 75 for line in lines)
    unfolded = ics.replace("\r\n ", "")
    assert "SUMMARY:Deadline: Very\\, long\\; title" in unfolded
    assert unfolded.count("BEGIN:VEVENT") == 2


def test_dashboard_exports_only_your_items_unless_asked(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    settings = Settings(data_dir=tmp_path, database_url=None)
    OpportunityStore(settings).add_new(
        [_opp(), _opp(title="Planned", url="https://p.dev", status="interested")]
    )
    LeadStore(tmp_path / "leads.json").save([_emailed()])
    client = TestClient(dashboard.app)
    assert {i["kind"] for i in client.get("/api/calendar").json()["items"]} == {
        "deadline",
        "event",
        "followup",
    }
    response = client.get("/api/calendar.ics")
    assert response.headers["content-type"].startswith("text/calendar")
    assert "Planned" in response.text and "Hack Western" not in response.text
    assert "Hack Western" in client.get("/api/calendar.ics?everything=true").text
