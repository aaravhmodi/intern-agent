from datetime import UTC, datetime, timedelta
from email.message import EmailMessage, Message
from email.utils import format_datetime
from pathlib import Path
from typing import Any

import pytest
from fastapi.testclient import TestClient

from internship_agent import db, pipeline
from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.leads.schemas import Lead
from internship_agent.leads.store import LeadStore

NOW = datetime.now(UTC)


def lead(company: str, **kw: object) -> Lead:
    data: dict[str, object] = {
        "kind": "posting",
        "company": company,
        "posting_url": f"https://boards.greenhouse.io/{company.lower()}/jobs/1",
        "source_url": "https://x.dev",
        "posting_title": "SWE Intern",
    }
    return Lead.model_validate({**data, **kw})


ACME = lead("Acme Robotics", status="applied")
NOVA = lead(
    "Nova",
    status="contacted",
    sent_to="jane@nova.ai",
    sent_at=NOW - timedelta(days=3),
    email="jane@nova.ai",
    email_status="published",
    contact_name="Jane Doe",
)
LEADS = [ACME, NOVA]


def mail(sender: str, subject: str, body: str, at: datetime = NOW, mid: str = "") -> Message:
    m = EmailMessage()
    m["From"], m["To"], m["Subject"] = sender, "me@gmail.com", subject
    m["Date"] = format_datetime(at)
    m["Message-ID"] = mid or f"<{abs(hash((sender, subject)))}@x>"
    m.set_content(body)
    return m


@pytest.mark.parametrize(
    ("message", "stage", "company"),
    [
        (
            mail(
                "Acme Robotics <no-reply@greenhouse.io>",
                "Thank you for applying to Acme Robotics",
                "We have received your application.",
            ),
            "applied",
            "Acme Robotics",
        ),
        (
            mail(
                "Acme Robotics Recruiting <no-reply@greenhouse.io>",
                "Your application to Acme Robotics",
                "Unfortunately we will not be moving forward.",
            ),
            "rejected",
            "Acme Robotics",
        ),
        (
            mail("Jane Doe <jane@nova.ai>", "Re: 15 min chat?", "Happy to chat, how's Thursday?"),
            "reply",
            "Nova",
        ),
        (
            mail(
                "Sam <sam@nova.ai>", "Interview with Nova", "We'd like to schedule a phone screen."
            ),
            "interview",
            "Nova",
        ),
        (
            mail(
                "Mail Delivery Subsystem <mailer-daemon@googlemail.com>",
                "Delivery Status Notification",
                "Address not found: jane@nova.ai could not be delivered",
            ),
            "bounced",
            "Nova",
        ),
        (
            mail(
                "CodeSignal <noreply@codesignal.com>",
                "Your Acme Robotics assessment",
                "Please complete the coding assessment within 7 days.",
            ),
            "assessment",
            "Acme Robotics",
        ),
    ],
)
def test_classifies_and_matches_pipeline_mail(message: Message, stage: str, company: str) -> None:
    event = pipeline.to_event("me@gmail.com", message, LEADS)
    assert event is not None
    assert (event.stage, event.company) == (stage, company)
    assert event.lead_key is not None and len(event.snippet) <= 240


@pytest.mark.parametrize(
    "message",
    [
        mail("Deals <news@shop.com>", "Big sale", "Unfortunately this sale ends soon."),
        mail("Friend <pal@gmail.com>", "dinner?", "Are we still on?"),
        mail(
            "Mail Delivery Subsystem <mailer-daemon@googlemail.com>",
            "Undeliverable",
            "bob@unknown.com could not be delivered",
        ),
    ],
)
def test_ignores_mail_that_isnt_about_the_search(message: Message) -> None:
    assert pipeline.to_event("me@gmail.com", message, LEADS) is None


def test_only_new_recruiting_headers_are_downloaded() -> None:
    known = {"<seen@x>"}

    def headers(sender: str, subject: str, mid: str = "<new@x>") -> Message:
        return mail(sender, subject, "", mid=mid)

    assert pipeline.worth_reading(headers("no-reply@greenhouse.io", "Hi"), LEADS, known)
    assert pipeline.worth_reading(
        headers("sam@nova.ai", "Hello"), LEADS, known
    )  # contacted company
    assert pipeline.worth_reading(headers("x@y.com", "Your interview"), LEADS, known)
    assert not pipeline.worth_reading(headers("news@shop.com", "Sale"), LEADS, known)
    assert not pipeline.worth_reading(
        headers("no-reply@greenhouse.io", "Hi", "<seen@x>"), LEADS, known
    )


class FakeBox:
    def __init__(self, messages: list[Message]) -> None:
        self.messages = messages
        self.fetched: list[bytes] = []

    def __enter__(self) -> "FakeBox":
        return self

    def __exit__(self, *a: Any) -> None:
        pass

    def inbox_headers(self, since: datetime) -> list[tuple[bytes, Message]]:
        return [(str(i).encode(), m) for i, m in enumerate(self.messages)]

    def message(self, number: bytes) -> Message:
        self.fetched.append(number)
        return self.messages[int(number)]


def _settings(tmp_path: Path) -> Settings:
    return Settings(
        _env_file=None,
        data_dir=tmp_path,
        database_url=None,
        gmail_address="me@gmail.com",
        gmail_app_password="pw",
        outreach_gmail_address="out@gmail.com",
        outreach_gmail_app_password="pw2",
    )


def test_sync_reads_both_inboxes_and_never_stores_an_email_twice(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    boxes = {
        "me@gmail.com": FakeBox(
            [
                mail(
                    "no-reply@greenhouse.io",
                    "Thank you for applying to Acme Robotics",
                    "Application received",
                    mid="<a@x>",
                ),
                mail("news@shop.com", "Sale", "Unfortunately...", mid="<n@x>"),
            ]
        ),
        "out@gmail.com": FakeBox(
            [mail("Jane Doe <jane@nova.ai>", "Re: chat", "Sure, Friday works", mid="<r@x>")]
        ),
    }
    added = pipeline.sync(settings, LEADS, open_mailbox=lambda address, pw: boxes[address])
    assert sorted((e.inbox, e.stage) for e in added) == [
        ("me@gmail.com", "applied"),
        ("out@gmail.com", "reply"),
    ]
    assert boxes["me@gmail.com"].fetched == [b"0"]  # the newsletter was never downloaded
    assert pipeline.sync(settings, LEADS, open_mailbox=lambda address, pw: boxes[address]) == []
    assert len(pipeline.events(settings)) == 2


def test_board_columns_follow_the_latest_email(tmp_path: Path) -> None:
    def event(
        stage: str, key: str | None, days_ago: int, company: str = "X"
    ) -> pipeline.InboxEvent:
        return pipeline.InboxEvent(
            message_id=f"{stage}{days_ago}",
            inbox="me@gmail.com",
            received_at=NOW - timedelta(days=days_ago),
            sender="a@b.com",
            sender_name="",
            subject=stage,
            stage=stage,
            company=company,
            lead_key=key,
            snippet="",
        )

    cards = {
        c["company"]: c
        for c in pipeline.board(
            [ACME, NOVA, lead("Idle")],
            [
                event("applied", ACME.key, 5),
                event("interview", NOVA.key, 4),
                event("rejected", NOVA.key, 1),
                event("offer", None, 2, company="Mystery Co"),
            ],
        )
    }
    assert cards["Acme Robotics"]["column"] == "waiting"  # a confirmation doesn't move it
    assert (
        cards["Nova"]["column"] == "rejected" and cards["Nova"]["emails"][0]["stage"] == "rejected"
    )
    assert cards["Mystery Co"]["column"] == "offer" and cards["Mystery Co"]["key"] is None
    assert "Idle" not in cards  # never applied to or emailed


def test_first_scan_is_quiet_then_pushes_what_needs_you(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = _settings(tmp_path).model_copy(update={"ntfy_topic": "t"})
    sent: list[Any] = []
    monkeypatch.setattr(pipeline.notify, "send", lambda server, topic, push: sent.append(push))
    interview = pipeline.InboxEvent(
        message_id="i",
        inbox="me@gmail.com",
        received_at=NOW,
        sender="s@nova.ai",
        sender_name="Sam",
        subject="Interview with Nova",
        stage="interview",
        company="Nova",
        lead_key=NOVA.key,
        snippet="",
    )
    monkeypatch.setattr(pipeline, "sync", lambda *a: [interview])
    pipeline.scan(settings)
    assert sent == []  # first scan: backfill, no push
    db.append(settings, "pipeline", interview.model_dump(mode="json"))
    pipeline.scan(settings)
    assert sent[0].message == "Interview: Nova: Interview with Nova"


def test_dashboard_shows_the_board(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    LeadStore(tmp_path / "leads.json").save([ACME])
    data = TestClient(dashboard.app).get("/api/pipeline").json()
    assert [(c["company"], c["column"]) for c in data["cards"]] == [("Acme Robotics", "waiting")]
