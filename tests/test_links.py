from datetime import UTC, date, datetime

import pytest

from internship_agent import pipeline
from internship_agent.links import page_url
from internship_agent.opportunities import run
from internship_agent.opportunities.schemas import Opportunity

BASE = "http://100.76.57.23:8765"
TODAY = date(2026, 10, 21)


def test_page_urls_open_a_view_or_one_item() -> None:
    assert page_url(BASE, "jobs") == f"{BASE}/#/jobs"
    assert page_url(BASE + "/", "picked", "https://a.dev/x?y=1") == (
        f"{BASE}/#/picked/https%3A%2F%2Fa.dev%2Fx%3Fy%3D1"
    )
    assert page_url(BASE, "jobs", "acme/jane-doe") == f"{BASE}/#/jobs/acme%2Fjane-doe"
    assert page_url(None, "jobs") is None


def hack(title: str, **kw: object) -> Opportunity:
    return Opportunity.model_validate(
        {
            "kind": "hackathon",
            "title": title,
            "url": f"https://{title.lower()}.dev",
            "source": "t",
            "online": True,
            **kw,
        }
    )


def test_event_application_push_opens_the_event_or_the_plans_list() -> None:
    def tried(title: str) -> Opportunity:
        return hack(
            title,
            application={
                "status": "needs_you",
                "detail": "CAPTCHA",
                "at": datetime.now(UTC).isoformat(),
            },
        )

    one = run.applied_push([tried("LarpHacks")], BASE)
    assert one.click == f"{BASE}/#/plans/https%3A%2F%2Flarphacks.dev"
    many = run.applied_push([tried("LarpHacks"), tried("Mergetober")], BASE)
    assert many.click == f"{BASE}/#/plans"


def test_opportunity_push_opens_what_it_is_mostly_about() -> None:
    picked = hack("Nebius", picked="Fit 84", status="interested")
    due = hack(
        "Taskforge",
        status="interested",
        deadline=date(2026, 10, 24),
        deadline_label="Submissions close",
    )
    only_pick = run.summary_push([picked], [picked], TODAY, BASE, picked=[picked])
    assert only_pick is not None and only_pick.click == f"{BASE}/#/picked/https%3A%2F%2Fnebius.dev"
    only_due = run.summary_push([], [due], TODAY, BASE)
    assert only_due is not None and only_due.click == f"{BASE}/#/calendar"
    mixed = run.summary_push([picked], [picked, due], TODAY, BASE, picked=[picked])
    assert mixed is not None and mixed.click == f"{BASE}/#/today"


def test_job_pipeline_push_opens_the_company_or_the_board() -> None:
    def event(key: str) -> pipeline.InboxEvent:
        return pipeline.InboxEvent(
            message_id=key,
            inbox="me@gmail.com",
            received_at=datetime.now(UTC),
            sender="a@b.com",
            sender_name="",
            subject="Interview",
            stage="interview",
            company=key,
            lead_key=key,
            snippet="",
        )

    one = pipeline.push_for([event("acme/jane")], BASE)
    assert one is not None and one.click == f"{BASE}/#/jobs/acme%2Fjane"
    two = pipeline.push_for([event("acme/jane"), event("nova/sam")], BASE)
    assert two is not None and two.click == f"{BASE}/#/jobs"


@pytest.mark.parametrize(
    "view", ["home", "today", "jobs", "picked", "plans", "calendar", "hackathons", "big", "applied"]
)
def test_every_linked_view_exists_in_the_dashboard(view: str) -> None:
    from importlib.resources import files

    page = files("internship_agent.dashboard").joinpath("index.html").read_text(encoding="utf-8")
    assert f"  {view}:" in page or f"\n  {view}: " in page
