from datetime import UTC, datetime, timedelta
from email.message import EmailMessage
from pathlib import Path

from internship_agent.applications.verification_mail import _extract_code
from internship_agent.config import Settings
from internship_agent.leads.schemas import FormQuestion, PreparedAnswer
from internship_agent.workflows import _use_gmail_for_applications, answer_bank


def message(sender: str, recipient: str, at: datetime, body: str) -> bytes:
    mail = EmailMessage()
    mail["From"] = sender
    mail["To"] = recipient
    mail["Date"] = at.strftime("%a, %d %b %Y %H:%M:%S %z")
    mail["Subject"] = "Verify your application"
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
    raw = message("Greenhouse <verify@us.greenhouse-mail.io>", "candidate@gmail.com", now, body)
    assert _extract_code(raw, now, "candidate@gmail.com") == "H5bGteWa"
