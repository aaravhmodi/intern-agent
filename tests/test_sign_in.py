from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime, timedelta
from email.message import EmailMessage
from pathlib import Path
from typing import Any

import pytest
from fastapi.testclient import TestClient

from internship_agent.applications.verification_mail import extract_sign_in
from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.opportunities import apply, run
from internship_agent.opportunities.apply import Element, Snapshot
from internship_agent.opportunities.schemas import BrowserStep, Opportunity, StepAction

NOW = datetime(2026, 10, 20, 18, 0, tzinfo=UTC)


def mail(
    sender: str, body: str, at: datetime = NOW, subject: str = "Sign in", html: str = ""
) -> bytes:
    message = EmailMessage()
    message["From"], message["To"], message["Subject"] = sender, "me@gmail.com", subject
    message["Date"] = at.strftime("%a, %d %b %Y %H:%M:%S %z")
    message.set_content(body)
    if html:
        message.add_alternative(html, subtype="html")
    return message.as_bytes()


def test_reads_a_fresh_code_only_from_the_site() -> None:
    raw = mail("Luma <noreply@luma-mail.com>", "Your sign in code is 482913. It expires soon.")
    assert extract_sign_in(raw, NOW, "luma", "code") == "482913"
    assert extract_sign_in(mail("x@phish.com", "code 482913"), NOW, "luma", "code") is None
    old = mail("noreply@luma-mail.com", "code 482913", at=NOW - timedelta(minutes=10))
    assert extract_sign_in(old, NOW, "luma", "code") is None
    subject_only = mail("hello@mlh.io", "Welcome!", subject="739201 is your MLH code")
    assert extract_sign_in(subject_only, NOW, "mlh", "code") == "739201"


def test_reads_the_sign_in_link_from_html() -> None:
    html = (
        '<a href="https://www.mlh.com/help">Help</a> '
        '<a href="https://www.mlh.com/auth/verify?token=abc123">Sign in</a>'
    )
    raw = mail("MLH <hello@mlh.io>", "Click the link to sign in.", html=html)
    assert (
        extract_sign_in(raw, NOW, "mlh", "link") == "https://www.mlh.com/auth/verify?token=abc123"
    )


class FakePage:
    def __init__(self, pages: list[Snapshot]) -> None:
        self.pages, self.at, self.acts, self.opened = pages, 0, [], []

    def open(self, url: str) -> None:
        self.opened.append(url)
        if self.opened[1:]:  # a sign-in link moves on
            self.at += 1

    def snapshot(self) -> Snapshot:
        return self.pages[self.at]

    def act(self, action: StepAction, value: str, resume: Path) -> None:
        self.acts.append((action.kind, action.element, value))
        if action.kind == "click":
            self.at += 1

    def screenshot(self, path: Path) -> None:
        path.write_bytes(b"png")

    def wait_for_human(self) -> bool:
        self.at += 1  # the person ticked the box
        return True

    def sessions(self) -> dict[str, Any]:
        return {
            "cookies": [
                {"name": "s", "value": "v", "domain": ".luma.com", "path": "/"},
                {"name": "j", "value": "v", "domain": "jobs.ashbyhq.com", "path": "/"},
            ]
        }


LUMA = Opportunity(kind="networking", title="Luma", url="https://luma.com/signin", source="sign-in")
EMAIL_PAGE = Snapshot(
    "https://luma.com/signin",
    "Welcome to Luma",
    [Element(0, "input", "email", "Email"), Element(1, "button", label="Continue with Email")],
)
CODE_PAGE = Snapshot(
    "https://luma.com/signin",
    "Luma: enter the code we sent",
    [Element(0, "input", "text", "Code"), Element(1, "button", label="Verify")],
)
HOME = Snapshot("https://luma.com/home", "Luma · Your events · Sign out", [])


def scripted(*steps: BrowserStep):
    queue = list(steps)
    return lambda snapshot, history: queue.pop(0)


def step(*actions: tuple[str, int, str]) -> BrowserStep:
    return BrowserStep(
        page="p",
        outcome="continue",
        reason="",
        actions=[StepAction(kind=k, element=e, value=v) for k, e, v in actions],
    )


def test_signs_in_with_the_emailed_code(tmp_path: Path) -> None:
    page = FakePage([EMAIL_PAGE, CODE_PAGE, HOME])
    asked = []
    result = apply.run(
        page,
        LUMA,
        {},
        scripted(
            step(("fill", 0, "me@gmail.com"), ("click", 1, "")),
            step(("fill", 0, "@inbox_code"), ("click", 1, "")),
        ),
        Path("r"),
        tmp_path / "p.png",
        confirmed=apply.SIGNED_IN,
        inbox=lambda want: asked.append(want) or "482913",
    )
    assert result.status == "submitted" and result.detail.startswith("Confirmed")
    assert ("fill", 0, "482913") in page.acts and asked == ["code"]
    assert not any("482913" in s for s in result.steps)  # the code never goes in the log


def test_waits_for_a_person_at_a_human_check_then_follows_the_emailed_link(tmp_path: Path) -> None:
    check = Snapshot(
        "https://www.mlh.com/signin",
        "MLH Welcome Back",
        [Element(0, "input", "email", "Email")],
        captcha=True,
    )
    ticked = Snapshot(
        "https://www.mlh.com/signin",
        "MLH Welcome Back",
        [Element(0, "input", "email", "Email"), Element(1, "button", label="Sign In")],
    )
    sent = Snapshot("https://www.mlh.com/signin", "MLH: check your email for a sign-in link", [])
    home = Snapshot("https://www.mlh.com/account", "MLH · My Profile · Sign out", [])
    page = FakePage([check, ticked, sent, home])
    mlh = Opportunity(
        kind="networking", title="MLH", url="https://www.mlh.com/signin", source="sign-in"
    )
    result = apply.run(
        page,
        mlh,
        {},
        scripted(step(("fill", 0, "me@gmail.com"), ("click", 1, "")), step(("email_link", 0, ""))),
        Path("r"),
        tmp_path / "p.png",
        confirmed=apply.SIGNED_IN,
        wait_for_human=page.wait_for_human,
        inbox=lambda want: "https://www.mlh.com/auth/verify?token=x",
    )
    assert result.status == "submitted"
    assert page.opened[-1] == "https://www.mlh.com/auth/verify?token=x"
    assert "you cleared a 'verify you're human' check" in " ".join(result.steps)


def test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(tmp_path: Path) -> None:
    passkey = Snapshot(
        "https://luma.com/home",
        "Create a Passkey · Create Event",
        [
            Element(0, "button", label="Create Passkey"),
            Element(1, "button", label="Not Now"),
            Element(2, "a", label="Create Event"),
        ],
    )
    said_done = BrowserStep(page="p", actions=[], outcome="submitted", reason="")
    signed = apply.run(
        FakePage([EMAIL_PAGE, passkey]),
        LUMA,
        {},
        scripted(step(("fill", 0, "me@gmail.com"), ("click", 1, "")), said_done),
        Path("r"),
        tmp_path / "a.png",
        confirmed=apply.SIGNED_IN,
    )
    assert (signed.status, signed.detail) == (
        "submitted",
        "Signed in: no sign-in form or link left on the page",
    )
    early = apply.run(
        FakePage([EMAIL_PAGE, CODE_PAGE]),
        LUMA,
        {},
        scripted(step(("fill", 0, "me@gmail.com"), ("click", 1, "")), said_done),
        Path("r"),
        tmp_path / "b.png",
        confirmed=apply.SIGNED_IN,
    )
    assert early.status == "uncertain"  # the code field is still there


def test_no_email_link_means_needs_you(tmp_path: Path) -> None:
    page = FakePage([EMAIL_PAGE])
    result = apply.run(
        page,
        LUMA,
        {},
        scripted(step(("email_link", 0, ""))),
        Path("r"),
        tmp_path / "p",
        confirmed=apply.SIGNED_IN,
        inbox=lambda want: None,
    )
    assert (result.status, result.detail) == ("needs_you", "No sign-in link arrived by email")


def test_sign_in_returns_only_those_sites_cookies_and_hands_back_unfinished(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = Settings(
        _env_file=None,
        data_dir=tmp_path,
        database_url=None,
        openai_api_key="k",
        gmail_address="me@gmail.com",
        gmail_app_password="pw",
        application_browser_dir=tmp_path / "b",
    )
    monkeypatch.setattr(run, "answer_bank", lambda s: type("B", (), {"load": lambda self: {}})())
    page = FakePage([EMAIL_PAGE])

    @contextmanager
    def fake() -> Iterator[FakePage]:
        yield page

    monkeypatch.setattr(
        run,
        "next_step",
        lambda *a: BrowserStep(page="p", actions=[], outcome="needs_you", reason="Only a password"),
    )
    handed: list[list[str]] = []
    results, cookies = run.sign_in(
        settings, ["luma"], page_factory=fake, finish_by_hand=handed.append
    )
    assert results["luma"].status == "needs_you" and handed == [["Luma"]]
    assert [c["domain"] for c in cookies] == [".luma.com"]  # job-site cookies stay on the laptop

    def closed() -> dict[str, Any]:
        raise RuntimeError("Target page, context or browser has been closed")

    page.sessions = closed  # type: ignore[method-assign]
    said: list[str] = []
    _, cookies = run.sign_in(settings, ["luma"], page_factory=fake, log=said.append)
    assert cookies == [] and said[-1].startswith("The browser window was closed")


def test_server_takes_only_event_site_cookies(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    taken: list[list[dict[str, Any]]] = []
    import internship_agent.opportunities.browser as browser

    monkeypatch.setattr(
        browser, "import_sessions", lambda d, cookies: taken.append(cookies) or len(cookies)
    )
    client = TestClient(dashboard.app)
    response = client.post(
        "/api/browser-sessions",
        json={
            "cookies": [
                {"name": "s", "value": "v", "domain": ".mlh.com", "path": "/", "secure": True},
                {"name": "x", "value": "v", "domain": "bank.example.com", "path": "/"},
            ]
        },
    )
    assert response.json() == {"added": 1}
    assert [c["domain"] for c in taken[0]] == [".mlh.com"] and taken[0][0]["secure"] is True
