from datetime import UTC, datetime, timedelta
from email.message import EmailMessage
from pathlib import Path

from internship_agent.applications import verification_mail
from internship_agent.applications.verification_mail import _extract_code
from internship_agent.config import Settings
from internship_agent.leads.schemas import FormQuestion, PreparedAnswer
from internship_agent.workflows import _use_gmail_for_applications, answer_bank


def message(
    sender: str, recipient: str, at: datetime, body: str, subject: str = "Verify your application"
) -> bytes:
    mail = EmailMessage()
    mail["From"] = sender
    mail["To"] = recipient
    mail["Date"] = at.strftime("%a, %d %b %Y %H:%M:%S %z")
    mail["Subject"] = subject
    mail.set_content(body)
    return mail.as_bytes()


def test_extracts_only_fresh_greenhouse_code_for_the_application_inbox() -> None:
    now = datetime.now(UTC)
    body = "Your security code is H5bGteWa. Enter it to submit your application."
    raw = message("Greenhouse <no-reply@greenhouse.io>", "candidate@gmail.com", now, body)
    assert _extract_code(raw, now, "candidate@gmail.com") == "H5bGteWa"
    assert _extract_code(raw, now, "someone@gmail.com") is None
    assert _extract_code(raw, now + timedelta(minutes=2), "candidate@gmail.com") is None
    spoof = message("Other <no-reply@example.com>", "candidate@gmail.com", now, body)
    assert _extract_code(spoof, now, "candidate@gmail.com") is None


def test_application_email_uses_configured_gmail(tmp_path: Path) -> None:
    settings = Settings(
        _env_file=None,
        data_dir=tmp_path,
        gmail_address="candidate@gmail.com",
        gmail_app_password="app-password",
    )
    answers = [
        PreparedAnswer(question=FormQuestion(label="Email Address"), answer="old@example.com")
    ]
    _use_gmail_for_applications(settings, answers)
    assert answers[0].answer == "candidate@gmail.com"
    assert answer_bank(settings).load()["email"] == "candidate@gmail.com"


def test_extracts_greenhouse_mail_code_after_application_label() -> None:
    now = datetime.now(UTC)
    body = (
        "Copy and paste this code into the Security code field on your application: "
        "H5bGteWa After you enter the code, submit your application."
    )
    raw = message(
        "Greenhouse <verify@us.greenhouse-mail.io>",
        "candidate@gmail.com",
        now,
        body,
        "Security code for your application to Bot Auto",
    )
    assert _extract_code(raw, now, "candidate@gmail.com", "Bot Auto") == "H5bGteWa"
    assert _extract_code(raw, now, "candidate@gmail.com", "Another Company") is None
    # Boards often use a short name: "Kodiak" in the subject for the "Kodiak Robotics" lead.
    short = message(
        "Greenhouse <verify@us.greenhouse-mail.io>",
        "candidate@gmail.com",
        now,
        body,
        "Security code for your application to Kodiak",
    )
    assert _extract_code(short, now, "candidate@gmail.com", "Kodiak Robotics") == "H5bGteWa"
    # A list called Figure AI's posting "FightCamp"; its Greenhouse board still names Figure.
    figure = message(
        "Greenhouse <verify@us.greenhouse-mail.io>",
        "candidate@gmail.com",
        now,
        body,
        "Security code for your application to Figure",
    )
    assert _extract_code(figure, now, "candidate@gmail.com", "FightCamp", "figureai") == "H5bGteWa"
    assert _extract_code(figure, now, "candidate@gmail.com", "FightCamp", "bose") is None


def test_mail_poll_refreshes_inbox_until_new_code_arrives(monkeypatch) -> None:
    now = datetime.now(UTC)
    raw = message(
        "Greenhouse <verify@us.greenhouse-mail.io>",
        "candidate@gmail.com",
        now,
        "Use the Security code field on your application: H5bGteWa",
        "Security code for your application to Bot Auto",
    )

    class Inbox:
        searches = 0
        refreshes = 0

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return None

        def login(self, *_args):
            return None

        def select(self, *_args, **_kwargs):
            return "OK", []

        def noop(self):
            self.refreshes += 1

        def search(self, *args):
            # A UTC date can be a day ahead of Gmail's mailbox date (evening in the Americas).
            assert args[-1] == (now - timedelta(days=1)).strftime("%d-%b-%Y")
            self.searches += 1
            return "OK", [b"" if self.searches == 1 else b"42"]

        def fetch(self, *_args):
            return "OK", [(b"42", raw)]

    inbox = Inbox()
    monkeypatch.setattr(verification_mail.imaplib, "IMAP4_SSL", lambda *_args, **_kw: inbox)
    monkeypatch.setattr(verification_mail.time, "sleep", lambda _seconds: None)
    code = verification_mail.wait_for_greenhouse_code(
        "candidate@gmail.com", "secret", now, company="Bot Auto", timeout_seconds=2
    )
    assert code == "H5bGteWa"
    assert inbox.refreshes >= 2
