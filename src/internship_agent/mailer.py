"""Send one email through Gmail SMTP. Called only from an explicit dashboard click."""

import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

GMAIL_SMTP = ("smtp.gmail.com", 465)


class MailError(RuntimeError):
    pass


def build_message(
    sender: str,
    to: str,
    subject: str,
    body: str,
    attachment: Path | None = None,
) -> EmailMessage:
    if not to or "@" not in to:
        raise MailError("A recipient address is required")
    if not subject.strip() or not body.strip():
        raise MailError("Subject and body are required")
    message = EmailMessage()
    message["From"] = sender
    message["To"] = to
    message["Subject"] = subject.strip()
    message.set_content(body)
    if attachment is not None:
        message.add_attachment(
            attachment.read_bytes(),
            maintype="application",
            subtype="pdf",
            filename="Aarav_Modi_Resume.pdf",
        )
    return message


def send(message: EmailMessage, sender: str, app_password: str) -> None:
    host, port = GMAIL_SMTP
    try:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context(), timeout=30) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(message)
    except smtplib.SMTPAuthenticationError as exc:
        # Never include the password or server response details that could echo it.
        raise MailError("Gmail rejected the login. Check GMAIL_APP_PASSWORD in .env.") from exc
    except (smtplib.SMTPException, OSError) as exc:
        raise MailError(f"Sending failed: {type(exc).__name__}") from exc
