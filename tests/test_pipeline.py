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


def mail(
    sender: str, subject: str, body: str, at: datetime = NOW, mid: str = "", **headers: str
) -> Message:
    m = EmailMessage()
    m["From"], m["To"], m["Subject"] = sender, "me@gmail.com", subject
    m["Date"] = format_datetime(at)
    m["Message-ID"] = mid or f"<{abs(hash((sender, subject, body)))}@x>"
    for name, value in headers.items():
        m[name.replace("_", "-")] = value
    m.set_content(body)
    return m


# Your own email quoted under theirs: the call asked for there is yours, not theirs.
QUOTE = "\n\nOn Mon, Oct 19, 2026 at 2:31 PM <me@gmail.com> wrote:\n> Could we schedule a call?"


@pytest.mark.parametrize(
    ("body", "subject", "stage"),
    [
        # Founders saying no in their own words (TDAA, SafeWorld, NorBot, Lendavo).
        (
            "Thanks. We don't have any internship opportunities at this time." + QUOTE,
            "Re: x",
            "rejected",
        ),
        (
            "We’re focused on full-time hiring and aren’t pursuing winter internships.",
            "Re: x",
            "rejected",
        ),
        (
            "We currently looking for someone immediate and local. Thanks for your interest.",
            "Re: x",
            "rejected",
        ),
        ("Opt out\n-----Original Message-----\nFrom: me\nSent: Thursday\nHi", "RE: x", "rejected"),
        # Asking for or booking a call (DeepMorph, Settle, Nodal, Optain).
        (
            "Do you have a 1-hour slot? We want to do a quick interview with you.",
            "Re: x",
            "interview",
        ),
        ("Thanks for reaching out! Let's chat next week.", "Re: x", "interview"),
        (
            "Join Zoom Meeting https://zoom.us/j/7523940762",
            "Invitation: Jane <> Aarav",
            "interview",
        ),
        # What you wrote, quoted below their answer, isn't theirs.
        ("Are you a US citizen? This is required to work here." + QUOTE, "Re: x", "reply"),
    ],
)
def test_a_founders_answer_is_read_without_the_quoted_thread(
    body: str, subject: str, stage: str
) -> None:
    event = pipeline.to_event("me@gmail.com", mail("Jane <jane@nova.ai>", subject, body), LEADS)
    assert event is not None and event.stage == stage


def test_newsletters_and_auto_replies_are_not_pipeline_mail() -> None:
    newsletter = mail(
        "speedrun <speedrun@substack.com>",
        "Still thinking about applying to speedrun?",
        "We extend an offer to 30 teams.",
        List_Unsubscribe="<https://x/unsub>",
    )
    away = mail(
        "Jane <jane@nova.ai>", "Automatic reply", "I'm away.", Auto_Submitted="auto-replied"
    )
    assert pipeline.to_event("me@gmail.com", newsletter, LEADS) is None
    assert pipeline.to_event("me@gmail.com", away, LEADS) is None


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

    # fJscaler: the interview was set up, then the Teams invite came in as a plain reply.
    # And a guess that bounced before the address that got through isn't a bounce now.
    sol = lead("Sol", sent_to="a@sol.ai", sent_at=NOW - timedelta(days=2))
    bo = lead("Bo", sent_to="b@bo.ai", sent_at=NOW - timedelta(days=2))
    later = {
        c["company"]: c["column"]
        for c in pipeline.board(
            [sol, bo],
            [
                event("bounced", sol.key, 6),
                event("interview", sol.key, 4),
                event("reply", sol.key, 1),
                event("bounced", bo.key, 5),
            ],
        )
    }
    assert later == {"Sol": "interview", "Bo": "waiting"}


def test_reclassify_corrects_stored_mail_with_todays_rules(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    no = mail(
        "Jane <jane@nova.ai>", "Re: chat", "We don't have any internship roles.", mid="<no@x>"
    )
    news = mail(
        "Inspirit <a@inspirit.ai>",
        "Ambassador Program Application Open!",
        "We are excited to invite you to the program.",
        mid="<ad@x>",
        List_Unsubscribe="<https://x/unsub>",
    )
    for message, stage in ((no, "reply"), (news, "interview")):
        old = pipeline.to_event(
            "out@gmail.com", mail("Jane <jane@nova.ai>", "Re: chat", "ok"), LEADS
        )
        assert old is not None
        db.append(
            settings,
            "pipeline",
            {**old.model_dump(mode="json"), "message_id": message["Message-ID"], "stage": stage},
        )
    boxes = {"me@gmail.com": FakeBox([]), "out@gmail.com": FakeBox([no, news])}
    assert pipeline.reclassify(settings, LEADS, open_mailbox=lambda a, pw: boxes[a]) == 2
    assert [(e.message_id, e.stage) for e in pipeline.events(settings)] == [("<no@x>", "rejected")]


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
    assert [t["label"] for t in data["insights"]["tiles"]][:3] == [
        "Emailed",
        "Delivered",
        "Replies",
    ]


def _event(stage: str, lead: Lead, days_ago: int = 1) -> pipeline.InboxEvent:
    return pipeline.InboxEvent(
        message_id=f"{stage}-{lead.key}",
        inbox="me@gmail.com",
        received_at=NOW - timedelta(days=days_ago),
        sender="x@y.com",
        sender_name="",
        subject=stage,
        stage=stage,
        company=lead.company,
        lead_key=lead.key,
        snippet="",
    )


def test_insights_count_funnels_and_say_what_they_mean() -> None:
    sent = NOW - timedelta(days=4)

    def emailed(name: str, status: str = "pattern") -> Lead:
        return lead(
            name,
            status="contacted",
            sent_to=f"a@{name.lower()}.com",
            sent_at=sent,
            email=f"a@{name.lower()}.com",
            email_status=status,
            segment="early",
        )

    guessed = [emailed(f"Co{i}") for i in range(10)]
    applied = lead(
        "Acme Robotics",
        status="applied",
        application={
            "prepared_at": NOW.isoformat(),
            "source": "form",
            "answers": [],
            "submission_status": "uncertain",
        },
    )
    found = [_event("bounced", g) for g in guessed[:4]] + [
        _event("reply", guessed[4]),
        _event("interview", guessed[5]),
        _event("applied", applied),
    ]
    ins = pipeline.insights([*guessed, applied], found, None, NOW.date())

    tiles = {t["label"]: t for t in ins["tiles"]}
    assert tiles["Emailed"]["value"] == 10 and tiles["Emailed"]["sub"] == "4 bounced"
    assert tiles["Delivered"]["value"] == "60%" and tiles["Replies"]["value"] == 2
    assert ins["funnels"]["outreach"] == [
        ["Emailed", 10],
        ["Delivered", 6],
        ["Replied", 2],
        ["Interview", 1],
    ]
    assert ins["funnels"]["applications"][:2] == [["Applied", 1], ["Confirmed by email", 1]]
    assert ins["sources"] == [{"label": "Guessed address", "sent": 10, "bounced": 4, "heard": 2}]
    assert (
        sum(d["bounced"] for d in ins["daily"]) == 4 and sum(d["sent"] for d in ins["daily"]) == 10
    )
    notes = " | ".join(n["text"] for n in ins["notes"])
    assert "40% of emails to guessed addresses bounced (4 of 10)" in notes
    assert "2 of 6 delivered emails got a reply from a person (33%)" in notes
    assert "did reach the employer, who emailed back: Acme Robotics" in notes
    assert "Needs you: Co5." in notes  # a company name, never an internal key
    assert ins["median_reply_days"] == 3


def test_replies_are_not_pushed_twice() -> None:
    reply = _event("reply", NOVA)
    assert pipeline.push_for([reply], None) is None  # n8n and followups already push replies


@pytest.mark.parametrize(
    ("subject", "company"),
    [
        ("Thank you for applying to Astranis", "Astranis"),
        ("Thank you for applying to Vercel!", "Vercel"),
        ("Thank you for applying to Legend Biotech US", "Legend Biotech US"),
        ("Your application to Kodiak Robotics for Software Intern", "Kodiak Robotics"),
        ("Astranis: Thank You for Launching Your Application", "Astranis"),
        ("Weekly digest", "us.greenhouse-mail.io"),  # nothing to go on: keep what was stored
    ],
)
def test_unmatched_mail_is_named_by_its_subject(subject: str, company: str) -> None:
    event = pipeline.InboxEvent(
        message_id="m",
        inbox="me@gmail.com",
        received_at=NOW,
        sender="no-reply@us.greenhouse-mail.io",
        sender_name="",
        subject=subject,
        stage="applied",
        company="us.greenhouse-mail.io",
        lead_key=None,
        snippet="",
    )
    assert pipeline.display_company(event) == company


def test_confirmation_closes_the_open_posting_it_names() -> None:
    apps = lead("Solink", status="applied", posting_title="Software Engineer Co-op - Apps")
    agents = lead(
        "Solink",
        status="scored",
        posting_title="Software Engineer Co-op - Agents",
        posting_url="https://jobs.ashbyhq.com/solink/agents",
    )
    winter = lead("Vercel", posting_title="Software Engineering Intern - Winter '27")
    summer = lead(
        "Vercel",
        posting_title="Software Engineering Intern - Summer '27",
        posting_url="https://boards.greenhouse.io/vercel/jobs/2",
    )
    unsure = lead(
        "Atoms",
        status="scored",
        application={
            "prepared_at": NOW,
            "source": "form",
            "answers": [],
            "submission_status": "uncertain",
        },
    )
    leads = [apps, agents, winter, summer, unsure]

    def confirms(sender: str, subject: str, body: str) -> list[str]:
        event = pipeline.to_event("me@gmail.com", mail(sender, subject, body), leads)
        assert event is not None
        return event.confirms

    body = "Thank you for your interest in Solink for the Software Engineer Co-Op- Agents position!"
    assert confirms("Solink <no-reply@ashbyhq.com>", "Solink Application Confirmation", body) == [
        agents.key
    ]
    body = "We received your application for the Software Engineering Intern - Winter '27 role."
    assert confirms(
        "Vercel <no-reply@greenhouse.io>", "Thank you for applying to Vercel!", body
    ) == [winter.key]
    body = "Your application is in the queue."
    assert confirms("Atoms <no-reply@greenhouse.io>", "Thank you for applying to Atoms!", body) == [
        unsure.key
    ]
    # Naming only a company with no unconfirmed submit closes nothing.
    assert (
        confirms("Vercel <no-reply@greenhouse.io>", "Thank you for applying to Vercel!", "Hi") == []
    )
