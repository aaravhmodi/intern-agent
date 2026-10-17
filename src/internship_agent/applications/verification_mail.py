"""Read a fresh Greenhouse application code from the configured Gmail inbox."""

import email
import imaplib
import re
import time
from datetime import UTC, datetime, timedelta
from email.header import decode_header, make_header
from email.utils import parseaddr, parsedate_to_datetime
from html import unescape

from pydantic import BaseModel, Field, ValidationError


class VerificationCode(BaseModel):
    value: str = Field(pattern=r"^[A-Za-z0-9]{8}$")


_CODE = re.compile(
    r"(?:verification|security)\s+code(?:\s+is|\s*:)?[^A-Za-z0-9]{0,30}"
    r"([A-Za-z0-9]{8})\b",
    re.I,
)
_GREENHOUSE_CODE = re.compile(
    r"code field on your application:\s*([A-Za-z0-9]{8})\b",
    re.I,
)


def _message_text(message: email.message.Message) -> str:
    parts = message.walk() if message.is_multipart() else [message]
    chunks: list[str] = []
    for part in parts:
        if part.get_content_maintype() != "text":
            continue
        payload = part.get_payload(decode=True)
        if not isinstance(payload, bytes):
            continue
        decoded = payload.decode(part.get_content_charset() or "utf-8", errors="replace")
        if part.get_content_subtype() == "html":
            decoded = re.sub(r"<[^>]+>", " ", decoded)
        chunks.append(unescape(decoded))
    return re.sub(r"\s+", " ", " ".join(chunks))


def _extract_code(raw: bytes, since: datetime, recipient: str, company: str = "") -> str | None:
    message = email.message_from_bytes(raw)
    sender = parseaddr(message.get("From", ""))[1].lower()
    if not (
        sender.endswith("@greenhouse.io")
        or sender.endswith(".greenhouse.io")
        or sender.endswith("@greenhouse-mail.io")
        or sender.endswith(".greenhouse-mail.io")
    ):
        return None
    recipients = " ".join(
        value
        for header in ("To", "Delivered-To", "X-Original-To")
        for value in message.get_all(header, [])
    ).lower()
    if recipient.lower() not in recipients:
        return None
    try:
        received = parsedate_to_datetime(message.get("Date", ""))
        if received is None or received.astimezone(UTC) < since - timedelta(seconds=30):
            return None
    except (TypeError, ValueError, OverflowError):
        return None
    subject = str(make_header(decode_header(message.get("Subject", ""))))
    if company and re.sub(r"[^a-z0-9]+", " ", company.lower()).strip() not in re.sub(
        r"[^a-z0-9]+", " ", subject.lower()
    ):
        return None
    body = _message_text(message)
    match = _GREENHOUSE_CODE.search(body) or _CODE.search(body) or _CODE.search(subject)
    if match is None:
        return None
    try:
        return VerificationCode(value=match.group(1)).value
    except ValidationError:
        return None


def wait_for_greenhouse_code(
    address: str,
    password: str,
    since: datetime,
    *,
    company: str = "",
    timeout_seconds: int = 180,
) -> str | None:
    """Poll Gmail read-only. Code and message contents never enter logs or persistent storage."""
    deadline = time.monotonic() + timeout_seconds
    seen: set[bytes] = set()
    with imaplib.IMAP4_SSL("imap.gmail.com", 993, timeout=15) as inbox:
        inbox.login(address, password)
        status, _ = inbox.select("INBOX", readonly=True)
        if status != "OK":
            return None
        while time.monotonic() < deadline:
            inbox.noop()
            status, result = inbox.search(None, "SINCE", since.strftime("%d-%b-%Y"))
            if status == "OK" and result and result[0]:
                for message_id in reversed(result[0].split()[-30:]):
                    if message_id in seen:
                        continue
                    seen.add(message_id)
                    status, parts = inbox.fetch(message_id, "(BODY.PEEK[])")
                    if status != "OK":
                        continue
                    for part in parts:
                        if isinstance(part, tuple) and isinstance(part[1], bytes):
                            if code := _extract_code(
                                part[1], since - timedelta(minutes=1), address, company
                            ):
                                return code
            time.sleep(min(5, max(0, deadline - time.monotonic())))
    return None
