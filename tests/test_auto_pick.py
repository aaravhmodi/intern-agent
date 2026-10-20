from datetime import date
from pathlib import Path

import pytest

from internship_agent.config import Settings
from internship_agent.opportunities import run
from internship_agent.opportunities.schemas import Opportunity, OpportunityAssessment
from internship_agent.opportunities.store import OpportunityStore

TODAY = date(2026, 10, 20)
CITIES = ["Toronto", "Waterloo"]


def check(**kw: object) -> OpportunityAssessment:
    data: dict[str, object] = {
        "format": "online",
        "location": "Online",
        "apply_by": date(2026, 11, 1),
        "travel": "none",
        "travel_details": "",
        "travel_source_url": "",
        "cost": "free",
        "effort": "moderate",
        "effort_details": "a weekend",
        "fit_score": 82,
        "fit": [],
        "highlights": [],
        "eligible": "yes",
        "sponsors": ["Amazon"],
        "prizes": "$10,000",
        "recognition": "Judged demos",
        "summary": "Go.",
    }
    return OpportunityAssessment.model_validate({**data, **kw})


def hack(assessment: OpportunityAssessment | None = None, **kw: object) -> Opportunity:
    data: dict[str, object] = {
        "kind": "hackathon",
        "title": "Build Something",
        "url": "https://build.devpost.com",
        "source": "devpost",
        "starts_on": date(2026, 11, 5),
        "online": True,
        "location": "Online",
    }
    return Opportunity.model_validate({**data, **kw, "assessment": assessment})


def reason(o: Opportunity) -> str | None:
    return run.pick_reason(o, TODAY, CITIES, 70)


def test_picks_sponsored_online_hackathons_with_recognition() -> None:
    assert reason(hack(check())) == "Fit 82, moderate effort, online; sponsored: Amazon"
    assert reason(hack(check(sponsors=[], prizes="$5,000 in cash"))) == (
        "Fit 82, moderate effort, online; sponsored: $5,000 in cash"
    )


@pytest.mark.parametrize(
    ("opportunity", "picked"),
    [
        (hack(check(format="in person"), online=False, location="Toronto, ON"), "nearby"),
        (
            hack(
                check(format="in person", travel="partial"),
                online=False,
                location="Berlin, Germany",
            ),
            "travel paid",
        ),
        (hack(check(format="in person"), online=False, location="Berlin, Germany"), None),
        (hack(check(eligible="no")), None),
        (hack(check(eligible="unclear")), None),
        (hack(check(effort="heavy")), None),
        (hack(check(fit_score=60)), None),
        (hack(check(apply_by=date(2026, 10, 1))), None),
        (hack(check(), deadline=date(2026, 10, 10)), None),
        (hack(check(sponsors=[], prizes="none stated")), None),
        (hack(check(recognition="none stated")), None),
        (hack(check(), status="skipped"), None),
        (hack(check(), status="registered"), None),
        (hack(None), None),
        (hack(check(), kind="conference"), None),
    ],
)
def test_only_realistic_reachable_sponsored_hackathons(
    opportunity: Opportunity, picked: str | None
) -> None:
    got = reason(opportunity)
    assert (got is None) == (picked is None)
    if picked:
        assert got is not None and picked in got


def test_checks_saved_before_these_fields_are_never_picked() -> None:
    old = OpportunityAssessment.model_validate(
        {
            k: v
            for k, v in check().model_dump().items()
            if k not in ("eligible", "sponsors", "prizes", "recognition")
        }
    )
    assert (old.eligible, old.prizes) == ("unclear", "not checked")
    assert reason(hack(old)) is None


def test_auto_pick_marks_interested_and_says_why(tmp_path: Path) -> None:
    settings = Settings(_env_file=None, data_dir=tmp_path, database_url=None, event_cities=CITIES)
    store = OpportunityStore(settings)
    store.add_new([hack(check()), hack(check(fit_score=50), title="Meh", url="https://meh.dev")])
    picked = run.auto_pick(settings, TODAY)
    assert [o.title for o in picked] == ["Build Something"]
    stored = {o.title: o for o in store.load()}
    assert stored["Build Something"].status == "interested" and stored["Build Something"].picked
    assert stored["Meh"].status == "new" and not stored["Meh"].picked
    assert run.auto_pick(settings, TODAY) == []  # once picked it's yours, never re-picked
    off = settings.model_copy(update={"auto_pick_hackathons": False})
    assert run.auto_pick(off, TODAY) == []


def test_push_names_what_was_picked() -> None:
    o = hack(
        check(), status="interested", picked="Fit 82, moderate effort, online; sponsored: Amazon"
    )
    push = run.summary_push([], [], TODAY, None, picked=[o])
    assert push is not None
    assert (
        push.message
        == "Picked for you: Build Something (Fit 82, moderate effort, online; sponsored: Amazon)"
    )
