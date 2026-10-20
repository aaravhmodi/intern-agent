import time
from datetime import date
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.opportunities import feeds, run
from internship_agent.opportunities.ai import EventFinding
from internship_agent.opportunities.schemas import (
    Opportunity,
    OpportunityAssessment,
    OpportunityKind,
    OpportunityStatus,
)
from internship_agent.opportunities.store import OpportunityStore

TODAY = date(2026, 10, 20)


def _settings(tmp_path: Path) -> Settings:
    return Settings(data_dir=tmp_path, database_url=None, openai_api_key="test")


def _opp(**kw: object) -> Opportunity:
    data: dict[str, object] = {
        "kind": "hackathon",
        "title": "Hack",
        "url": "https://hack.example.com",
        "source": "test",
        "starts_on": date(2026, 11, 1),
    }
    return Opportunity.model_validate({**data, **kw})


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Aug 31 - Oct 23, 2026", (date(2026, 8, 31), date(2026, 10, 23))),
        ("Oct 05 - 27, 2026", (date(2026, 10, 5), date(2026, 10, 27))),
        ("Dec 28, 2026 - Jan 05, 2027", (date(2026, 12, 28), date(2027, 1, 5))),
        ("Dec 28 - Jan 05, 2027", (date(2026, 12, 28), date(2027, 1, 5))),
        ("Oct 23, 2026", (date(2026, 10, 23), date(2026, 10, 23))),
        ("soon", None),
    ],
)
def test_devpost_dates(text: str, expected: tuple[date, date] | None) -> None:
    assert feeds.devpost_dates(text) == expected


def test_devpost_parses_and_skips_invite_only() -> None:
    hackathons = [
        {
            "title": "Build North ",
            "url": "https://buildnorth.devpost.com/",
            "displayed_location": {"location": "Toronto"},
            "submission_period_dates": "Oct 16 - 26, 2026",
            "themes": [{"name": "AI"}],
            "prize_amount": "$<span data-currency-value>5,000</span>",
            "organization_name": "Build North",
        },
        {
            **{"title": "Secret", "url": "https://x.devpost.com/"},
            "invite_only": True,
            "submission_period_dates": "Oct 16 - 26, 2026",
        },
    ]
    [h] = feeds.devpost(hackathons)
    assert (h.title, h.deadline, h.online, h.topics) == (
        "Build North",
        date(2026, 10, 26),
        False,
        ["AI"],
    )
    assert "$5,000 in prizes" in h.details


MLH_CARD = """<a href="x" itemScope="" itemType="https://schema.org/Event">
<meta itemProp="url" content="https://{slug}.io/"/>
<meta itemProp="eventAttendanceMode" content="https://schema.org/OfflineEventAttendanceMode"/>
<meta itemProp="startDate" content="2026-11-07T17:00:00Z"/>
<meta itemProp="endDate" content="2026-11-08T19:00:00Z"/>
<div itemProp="location"><meta itemProp="addressLocality" content="{city}"/>
<meta itemProp="addressRegion" content="{region}"/>
<meta itemProp="addressCountry" content="{country}"/></div><h4 class="t">{name} </h4></a>"""


def test_mlh_parses_cards_and_never_reads_india_as_indiana(tmp_path: Path) -> None:
    page = MLH_CARD.format(
        slug="biohacks", city="Hamilton", region="Ontario", country="CA", name="BioHacks"
    )
    page += MLH_CARD.format(
        slug="hackcbs", city="New Delhi", region="Delhi", country="IN", name="hackCBS"
    )
    bio, cbs = feeds.mlh(page)
    assert (bio.title, bio.starts_on, bio.location) == (
        "BioHacks",
        date(2026, 11, 7),
        "Hamilton, Ontario, Canada",
    )
    assert run.keep([bio, cbs], _settings(tmp_path), TODAY) == [bio]


def test_ccfddl_keeps_upcoming_editions_and_next_deadline() -> None:
    venues = [
        {
            "title": "CHI",
            "sub": "HI",
            "rank": {"core": "A*"},
            "description": "HCI",
            "confs": [
                {
                    "year": 2026,
                    "link": "https://chi2026.acm.org/",
                    "opening": "2026-04-13 08:00:00",
                    "timeline": [],
                },
                {
                    "year": 2027,
                    "link": "https://chi2027.acm.org/",
                    "opening": "2027-05-10 08:00:00",
                    "timeline": [{"deadline": "2026-09-10 23:59:59"}],
                    "timezone": "AoE",
                    "date": "May 10 - 14, 2027",
                },
            ],
        },
        {
            "title": "ACL",
            "sub": "AI",
            "rank": {"core": "A*"},
            "confs": [
                {
                    "year": 2027,
                    "link": "https://acl2027.org/",
                    "timeline": [
                        {"abstract_deadline": "TBD", "deadline": "2027-01-04 23:59:59"},
                        {"deadline": "2026-12-01 23:59:59"},
                    ],
                },
            ],
        },
        {
            "title": "SOSP",
            "sub": "DS",
            "confs": [{"year": 2027, "link": "https://sosp.org/", "timeline": []}],
        },
        {
            "title": "OLD",
            "sub": "AI",
            "confs": [
                {
                    "year": 2026,
                    "link": "https://old.org/",
                    "timeline": [{"deadline": "2026-01-01 00:00:00"}],
                }
            ],
        },
    ]
    chi, acl = feeds.ccfddl(venues, ["AI", "HI"], TODAY)
    assert (chi.title, chi.deadline, chi.rank, chi.starts_on) == (
        "CHI 2027",
        None,
        "CORE A*",
        date(2027, 5, 10),
    )
    assert chi.deadline_label.startswith("Main deadline passed")
    assert (acl.deadline, acl.deadline_label) == (date(2026, 12, 1), "Paper deadline")


def test_confs_tech_normalizes_country() -> None:
    [c] = feeds.confs_tech(
        [
            {
                "name": "PyConf",
                "url": "https://pyconf.dev",
                "startDate": "2027-03-01",
                "endDate": "2027-03-02",
                "city": "San Francisco, CA",
                "country": "U.S.A.",
                "cfpUrl": "https://pyconf.dev/cfp",
                "cfpEndDate": "2026-12-01",
            }
        ],
        "python",
    )
    assert (c.location, c.deadline, c.deadline_label) == (
        "San Francisco, CA, USA",
        date(2026, 12, 1),
        "Talk proposals close",
    )


def test_keep_drops_past_and_far_away_events(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    toronto = _opp(title="A", url="https://a.dev", location="Toronto")
    online = _opp(title="B", url="https://b.dev", location="Online", online=True)
    past = _opp(title="C", url="https://c.dev", location="Toronto", starts_on=date(2026, 10, 1))
    far = _opp(title="D", url="https://d.dev", location="Bengaluru")
    research = _opp(kind="research", title="E", url="https://e.dev", location="Seoul, Korea")
    assert run.keep([toronto, online, past, far, research], settings, TODAY) == [
        toronto,
        online,
        research,
    ]


def test_add_new_dedupes_and_never_overwrites_status(tmp_path: Path) -> None:
    store = OpportunityStore(_settings(tmp_path))
    store.add_new([_opp()])
    item = store.get("https://hack.example.com")
    item.status = OpportunityStatus.REGISTERED
    store.upsert(item)
    again = [_opp(details="changed"), _opp(url="https://mlh.io/hack?utm_source=x", title="HACK")]
    assert store.add_new(again) == []
    assert [o.status for o in store.load()] == [OpportunityStatus.REGISTERED]


def test_next_date_uses_open_deadline_else_start() -> None:
    assert run.next_date(_opp(deadline=date(2026, 10, 25)), TODAY) == date(2026, 10, 25)
    assert run.next_date(_opp(deadline=date(2026, 9, 1)), TODAY) == date(2026, 11, 1)


def test_summary_push_lists_new_and_planned_deadlines_this_week() -> None:
    due = _opp(
        title="Planned",
        deadline=date(2026, 10, 24),
        deadline_label="Submissions close",
        status="interested",
    )
    unplanned = _opp(title="Unplanned", url="https://u.dev", deadline=date(2026, 10, 22))
    later = _opp(
        title="Later", url="https://l.dev", deadline=date(2026, 11, 20), status="interested"
    )
    push = run.summary_push([unplanned], [due, unplanned, later], TODAY, None)
    assert push is not None
    assert push.message == "New: 1 hackathon\nDue Oct 24: Planned (Submissions close)"
    assert run.summary_push([], [unplanned, later], TODAY, None) is None


def test_find_events_keeps_only_dated_events_whose_page_names_them(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def finding(title: str, url: str, day: date) -> EventFinding:
        return EventFinding(
            title=title,
            url=url,
            starts_on=day,
            location="Toronto",
            organizer="TechTO",
            kind="networking",
            why="Founders and engineers.",
        )

    findings = [
        finding("TechTO Together", "https://luma.com/real", date.today()),
        finding("Invented Mixer", "https://luma.com/fake", date.today()),
        finding("Last Year", "https://luma.com/old", date(2025, 1, 1)),
    ]
    monkeypatch.setattr(run, "search_events", lambda *a: findings)
    monkeypatch.setattr(run, "page_names", lambda url, *_: url.endswith("real"))
    added = run.find_events(_settings(tmp_path))
    assert [(o.title, o.kind, o.details) for o in added] == [
        ("TechTO Together", OpportunityKind.NETWORKING, "TechTO: Founders and engineers.")
    ]


def test_dashboard_lists_and_marks_opportunities(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    store = OpportunityStore(_settings(tmp_path))
    store.add_new(
        [
            _opp(starts_on=date(2099, 1, 1)),
            _opp(title="Gone", url="https://g.dev", starts_on=date(2020, 1, 1)),
        ]
    )
    client = TestClient(dashboard.app)
    [item] = client.get("/api/opportunities").json()["opportunities"]
    assert item["key"] == "https://hack.example.com"
    response = client.post(
        "/api/opportunities/status", json={"key": item["key"], "status": "interested"}
    )
    assert response.json()["opportunity"]["status"] == "interested"
    assert (
        client.post(
            "/api/opportunities/status", json={"key": "https://nope.dev", "status": "interested"}
        ).status_code
        == 404
    )


def test_without_citations_strips_inline_links_only() -> None:
    from internship_agent.opportunities.schemas import SubmissionStrategy

    cite = " ([chi2027.acm.org](https://chi2027.acm.org/authors/posters/?utm_source=openai))"
    s = SubmissionStrategy(
        verdict="realistic",
        summary=f"Posters fit (a non-archival track).{cite}",
        tracks=[],
        what_to_submit="StudyAgent",
        plan=[f"Submit by Jan 20.{cite}"],
        funding=[],
        risks=[],
    )
    clean = run.without_citations(s)
    assert clean.summary == "Posters fit (a non-archival track)."
    assert clean.plan == ["Submit by Jan 20."]


def _assessment(**kw: object) -> OpportunityAssessment:
    data: dict[str, object] = {
        "format": "in person",
        "location": "Hamilton, ON",
        "travel": "covered",
        "travel_details": "Free bus from Waterloo. ([site](https://hack.example.com/faq))",
        "travel_source_url": "https://hack.example.com/faq",
        "cost": "free",
        "effort": "moderate",
        "effort_details": "36-hour weekend",
        "fit_score": 140,
        "fit": ["Ship a FastAPI backend"],
        "highlights": ["Recruiters attend"],
        "summary": "Go.",
    }
    return OpportunityAssessment.model_validate({**data, **kw})


def _fake_ai(monkeypatch: pytest.MonkeyPatch, found: object, confirmed: bool) -> None:
    monkeypatch.setattr(run, "assess", lambda *a: found)
    monkeypatch.setattr(run, "page_names", lambda *a: confirmed)
    monkeypatch.setattr(run, "_candidate", lambda s: ("resume", "context"))


def test_check_keeps_confirmed_travel_and_cleans_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _fake_ai(monkeypatch, _assessment(), confirmed=True)
    a = run.checked(None, _settings(tmp_path), "r", "c", _opp())  # type: ignore[arg-type]
    assert (a.travel, a.fit_score, a.travel_details) == ("covered", 100, "Free bus from Waterloo.")


def test_check_marks_unconfirmed_travel_unknown(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _fake_ai(monkeypatch, _assessment(), confirmed=False)
    a = run.checked(None, _settings(tmp_path), "r", "c", _opp())  # type: ignore[arg-type]
    assert a.travel == "unknown"
    assert a.travel_details.startswith("Not confirmed on the event's pages:")


def test_worth_checking_puts_nearby_hackathons_first_and_research_last() -> None:
    def opp(title: str, **kw: object) -> Opportunity:
        return _opp(title=title, url=f"https://{title.lower()}.dev", **kw)

    picked = run.worth_checking(
        [
            opp("Research", kind="research", location="Toronto", starts_on=date(2026, 10, 21)),
            opp(
                "Rome conf", kind="conference", location="Rome, Italy", starts_on=date(2026, 10, 22)
            ),
            opp("Toronto conf", kind="conference", location="Toronto", starts_on=date(2026, 12, 1)),
            opp("Online hack", online=True, location="Online", starts_on=date(2026, 10, 22)),
            opp("SF hack", location="San Francisco, CA, USA", starts_on=date(2026, 10, 23)),
            opp(
                "Hamilton hack later",
                location="Hamilton, Ontario, Canada",
                starts_on=date(2026, 12, 1),
            ),
            opp("Toronto hack", location="Toronto", starts_on=date(2026, 11, 1)),
            opp("Checked", location="Toronto", assessment=_assessment(prizes="$1,000")),
            opp(
                "Old check",
                location="Toronto",
                assessment=_assessment(),
                starts_on=date(2027, 1, 9),
            ),
        ],
        TODAY,
        10,
        ["Toronto", "Waterloo"],
    )
    assert [o.title for o in picked] == [
        "Online hack",  # online and nearby come first, soonest first
        "Toronto hack",
        "Hamilton hack later",
        "Old check",  # checked before sponsors/prizes were recorded: checked again
        "SF hack",  # far away in person comes last
        "Toronto conf",
        "Rome conf",
        "Research",
    ]


def test_check_events_saves_results_and_survives_one_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = _settings(tmp_path)
    store = OpportunityStore(settings)
    store.add_new(
        [_opp(title="Good", url="https://good.dev"), _opp(title="Bad", url="https://bad.dev")]
    )

    def fake(client: object, s: object, r: str, c: str, event: Opportunity) -> object:
        if event.title == "Bad":
            raise RuntimeError("search timed out")
        return _assessment()

    monkeypatch.setattr(run, "checked", fake)
    monkeypatch.setattr(run, "_candidate", lambda s: ("resume", "context"))
    done = run.check_events(settings, limit=5)
    assert [o.title for o in done] == ["Good"]
    assert {o.title: o.assessment is not None for o in store.load()} == {"Good": True, "Bad": False}


def test_a_finished_check_is_saved_before_the_run_is_killed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = _settings(tmp_path)
    store = OpportunityStore(settings)
    store.add_new(
        [_opp(title="Fast", url="https://fast.dev"), _opp(title="Slow", url="https://slow.dev")]
    )

    def fake(client: object, s: object, r: str, c: str, event: Opportunity) -> object:
        if event.title == "Slow":  # a deploy restarts the server once Fast is on disk
            deadline = time.monotonic() + 5
            while not store.get("https://fast.dev").assessment and time.monotonic() < deadline:
                time.sleep(0.01)
            raise SystemExit("restarted")
        return _assessment()

    monkeypatch.setattr(run, "checked", fake)
    monkeypatch.setattr(run, "_candidate", lambda s: ("resume", "context"))
    with pytest.raises(SystemExit):
        run.check_events(settings, limit=5)
    assert store.get("https://fast.dev").assessment is not None


def test_summary_push_announces_paid_trips() -> None:
    trip = _opp(title="BioHacks", assessment=_assessment(travel="covered"))
    nothing = _opp(title="Meh", url="https://m.dev", assessment=_assessment(travel="none"))
    push = run.summary_push([], [], TODAY, None, [trip, nothing])
    assert push is not None
    assert push.message == "Travel paid: BioHacks (2026-11-01, Hamilton, ON)"


def test_dashboard_checks_one_event(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    OpportunityStore(_settings(tmp_path)).add_new([_opp(starts_on=date(2099, 1, 1))])
    _fake_ai(monkeypatch, _assessment(), confirmed=True)
    client = TestClient(dashboard.app)
    response = client.post("/api/opportunities/check", json={"key": "https://hack.example.com"})
    assert response.json()["checked"][0]["assessment"]["travel"] == "covered"
    [stored] = client.get("/api/opportunities").json()["opportunities"]
    assert stored["assessment"]["fit_score"] == 100
