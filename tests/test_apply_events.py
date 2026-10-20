from collections.abc import Iterator
from contextlib import contextmanager
from datetime import date
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.opportunities import apply, run
from internship_agent.opportunities.apply import Element, Snapshot
from internship_agent.opportunities.schemas import BrowserStep, Opportunity, StepAction
from internship_agent.opportunities.store import OpportunityStore

EVENT = Opportunity(
    kind="hackathon",
    title="Hack Western 13",
    url="https://hack-western-13.devpost.com",
    source="devpost",
    starts_on=date(2099, 11, 20),
)
BANK = {"full name": "Aarav Modi", "email": "aarav@example.com"}


class FakePage:
    """A scripted browser: each click moves to the next page."""

    def __init__(self, pages: list[Snapshot]) -> None:
        self.pages, self.at, self.acts = pages, 0, []

    def open(self, url: str) -> None:
        self.at = 0

    def snapshot(self) -> Snapshot:
        return self.pages[self.at]

    def act(self, action: StepAction, value: str, resume: Path) -> None:
        self.acts.append((action.kind, action.element, value))
        if action.kind == "click":
            self.at = min(self.at + 1, len(self.pages) - 1)

    def screenshot(self, path: Path) -> None:
        path.write_bytes(b"png")


def landing(**kw: object) -> Snapshot:
    data: dict = {
        "url": "https://hack-western-13.devpost.com/",
        "text": "Hack Western 13. Join us!",
        "elements": [Element(0, "button", label="Join hackathon")],
    }
    return Snapshot(**{**data, **kw})


FORM = Snapshot(
    "https://hack-western-13.devpost.com/register",
    "Register for Hack Western",
    [
        Element(0, "input", "text", "Full name", required=True),
        Element(1, "textarea", "", "Why do you want to come?", required=True),
        Element(2, "input", "checkbox", "I agree to the MLH Code of Conduct", required=True),
        Element(3, "input", "checkbox", "Send me the sponsor newsletter"),
        Element(4, "button", label="Submit registration"),
    ],
)
DONE = Snapshot(
    "https://hack-western-13.devpost.com/thanks", "You're registered for Hack Western 13!", []
)


def steps(*scripted: BrowserStep):
    queue = list(scripted)
    return lambda snapshot, history: queue.pop(0)


def step(
    outcome: str = "continue", *actions: tuple[str, int, str], reason: str = ""
) -> BrowserStep:
    return BrowserStep(
        page="a page",
        outcome=outcome,
        reason=reason,
        actions=[StepAction(kind=k, element=e, value=v) for k, e, v in actions],
    )


def test_registers_from_saved_answers_and_keeps_proof(tmp_path: Path) -> None:
    page = FakePage([landing(), FORM, DONE])
    script = steps(
        step("continue", ("click", 0, "")),
        step(
            "continue",
            ("fill", 0, "@bank:Full Name"),
            ("fill", 1, "To build with my robotics telemetry work."),
            ("check", 2, ""),
            ("check", 3, ""),
            ("click", 4, ""),
        ),
    )
    result = apply.run(page, EVENT, BANK, script, Path("resume.pdf"), tmp_path / "proof.png")
    assert (result.status, result.proof) == ("submitted", True)
    assert result.detail == 'Confirmed: "You\'re registered for Hack Western 13!"'
    assert ("fill", 0, "Aarav Modi") in page.acts  # the saved answer, filled in locally
    assert ("check", 3, "") not in page.acts  # the newsletter box stayed unticked
    assert not any("Aarav Modi" in s for s in result.steps)  # personal values stay out of the log
    assert (tmp_path / "proof.png").exists()


@pytest.mark.parametrize(
    ("pages", "script", "status", "detail"),
    [
        (
            [landing(elements=[Element(0, "button", label="Pay $25 and register")])],
            [step("continue", ("click", 0, ""))],
            "blocked",
            "Stopped before a payment button",
        ),
        (
            [
                landing(),
                Snapshot(
                    "https://hack-western-13.devpost.com/r",
                    "Hack Western",
                    [Element(0, "input", "text", "Card number")],
                ),
            ],
            [step("continue", ("click", 0, ""))],
            "blocked",
            "The form asks for payment details",
        ),
        (
            [landing(elements=[Element(0, "input", "password", "Password")])],
            [],
            "needs_you",
            "Sign in to devpost.com",
        ),
        (
            [landing(url="https://evil.example/")],
            [],
            "blocked",
            "Left the event's sites for evil.example",
        ),
        (
            [landing(text="Some other event")],
            [],
            "blocked",
            "The event page doesn't name the event",
        ),
        ([landing(captcha=True)], [], "needs_you", "A CAPTCHA"),
        (
            [landing(text="Just a moment...\nPerforming security verification", elements=[])],
            [],
            "needs_you",
            "A CAPTCHA or 'verify you're human' check",
        ),
        (
            [landing(), FORM],
            [step("continue", ("click", 0, "")), step("continue", ("fill", 0, "@bank:phone"))],
            "needs_you",
            "No saved answer for 'phone'",
        ),
        ([landing()], [step("submitted")], "uncertain", "The agent thought it was done"),
        (
            [landing()],
            [step("blocked", reason="High-school students only")],
            "blocked",
            "High-school students only",
        ),
    ],
)
def test_safety_rules_stop_the_run(
    tmp_path: Path, pages: list[Snapshot], script: list[BrowserStep], status: str, detail: str
) -> None:
    result = apply.run(
        FakePage(pages), EVENT, BANK, steps(*script), Path("r.pdf"), tmp_path / "p.png"
    )
    assert result.status == status
    assert result.detail.startswith(detail)
    assert not result.proof


def test_dry_run_only_says_what_it_would_do(tmp_path: Path) -> None:
    page = FakePage([landing()])
    result = apply.run(
        page,
        EVENT,
        BANK,
        steps(step("continue", ("click", 0, ""))),
        Path("r"),
        tmp_path / "p",
        dry_run=True,
    )
    assert (result.status, result.detail, page.acts) == (
        "ready",
        "Dry run: would click [0] on the first page",
        [],
    )


@pytest.mark.parametrize(
    ("url", "ok"),
    [
        ("https://hack-western-13.devpost.com/register", True),
        ("https://www.calhacks.io/apply", True),  # the event's own site, from https://calhacks.io
        ("https://my.mlh.io/oauth/authorize", True),
        ("https://docs.google.com/forms/d/e/x/viewform", True),
        ("https://luma.com/abc", True),
        ("http://calhacks.io/apply", False),
        ("https://calhacks.io.evil.com/", False),
    ],
)
def test_allowed_sites(url: str, ok: bool) -> None:
    assert apply.allowed(url, "https://calhacks.io") is ok


def _event(**kw: object) -> Opportunity:
    return Opportunity.model_validate({**EVENT.model_dump(), **kw})


def _settings(tmp_path: Path) -> Settings:
    return Settings(
        _env_file=None,
        data_dir=tmp_path,
        database_url=None,
        openai_api_key="test",
        application_browser_dir=tmp_path / "browser",
    )


def test_to_apply_takes_interested_untried_open_events() -> None:
    def opp(title: str, **kw: object) -> Opportunity:
        fields = {"title": title, "url": f"https://{title}.dev", "status": "interested"}
        return _event(**{**fields, **kw})

    picked = run.to_apply(
        [
            opp("yes"),
            opp("new", status="new"),
            opp("conference", kind="conference"),
            opp("started", starts_on=date(2020, 1, 1)),
            opp(
                "tried",
                application={"status": "uncertain", "detail": "", "at": "2026-10-20T00:00:00Z"},
            ),
        ],
        date(2026, 10, 20),
    )
    assert [o.title for o in picked] == ["yes"]


def test_apply_events_saves_the_result_and_marks_it_submitted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = _settings(tmp_path)
    store = OpportunityStore(settings)
    store.add_new([_event(status="interested")])
    monkeypatch.setattr(run, "_candidate", lambda s: ("resume", "context"))
    monkeypatch.setattr(
        run, "answer_bank", lambda s: type("Bank", (), {"load": lambda self: BANK})()
    )
    script = steps(
        step("continue", ("click", 0, "")),
        step("continue", ("fill", 0, "@bank:full name"), ("click", 4, "")),
    )
    monkeypatch.setattr(
        run, "next_step", lambda client, model, text, page, history: script(None, history)
    )

    @contextmanager
    def fake_browser() -> Iterator[FakePage]:
        yield FakePage([landing(), FORM, DONE])

    done = run.apply_events(settings, page_factory=fake_browser)
    assert [(o.status, o.application.status) for o in done if o.application] == [
        ("submitted", "submitted")
    ]
    stored = store.get(EVENT.key)
    assert stored.application is not None and stored.application.proof
    assert run.applied_push(done, None).message == "✓ Applied: Hack Western 13"
    assert run.apply_events(settings, page_factory=fake_browser) == []  # never applied twice


def test_dashboard_apply_rules(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    store = OpportunityStore(_settings(tmp_path))
    talk = Opportunity(kind="conference", title="PyCon", url="https://pycon.org", source="t")
    tried = _event(application={"status": "uncertain", "detail": "x", "at": "2026-10-20T00:00:00Z"})
    store.add_new([talk, tried])
    client = TestClient(dashboard.app)
    assert client.post("/api/opportunities/apply", json={"key": talk.key}).status_code == 400
    reopened = client.post("/api/opportunities/apply/retry", json={"key": tried.key}).json()
    assert reopened["opportunity"]["application"] is None
    assert client.get("/api/opportunities/proof", params={"key": tried.key}).status_code == 404


def test_typed_urls_find_their_event() -> None:
    assert run._keys(["https://www.hacktrent.ca/?utm_source=mlh"]) == {"https://www.hacktrent.ca"}
