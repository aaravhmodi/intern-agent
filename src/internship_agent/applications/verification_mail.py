"""Read fresh codes from the configured Gmail inbox: Greenhouse's application code, and the
sign-in codes or links event sites (Luma, MLH, Eventbrite) email."""

import email
import imaplib
import re
import time
from collections.abc import Callable
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
    # Subjects use the board's short name ("Kodiak" for "Kodiak Robotics"), so match the first word.
    first_word = re.sub(r"[^a-z0-9]+", " ", company.lower()).split()[:1]
    if first_word and first_word[0] not in re.sub(r"[^a-z0-9]+", " ", subject.lower()).split():
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
    return _poll(
        address,
        password,
        since,
        timeout_seconds,
        lambda raw: _extract_code(raw, since - timedelta(minutes=1), address, company),
    )


def _poll(
    address: str,
    password: str,
    since: datetime,
    timeout_seconds: int,
    extract: Callable[[bytes], str | None],
) -> str | None:
    """Read new Gmail messages (read-only) until `extract` finds something or time runs out."""
    deadline = time.monotonic() + timeout_seconds
    seen: set[bytes] = set()
    with imaplib.IMAP4_SSL("imap.gmail.com", 993, timeout=15) as inbox:
        inbox.login(address, password)
        status, _ = inbox.select("INBOX", readonly=True)
        if status != "OK":
            return None
        while time.monotonic() < deadline:
            inbox.noop()
            # IMAP SINCE uses Gmail's timezone, not UTC; the extractor checks the exact time.
            day = (since - timedelta(days=1)).strftime("%d-%b-%Y")
            status, result = inbox.search(None, "SINCE", day)
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
                            if found := extract(part[1]):
                                return found
            time.sleep(min(5, max(0, deadline - time.monotonic())))
    return None


# A sign-in code: 4-8 characters with at least one digit, next to the word "code".
_SIGN_IN_CODE = re.compile(
    r"\bcode\b[^A-Za-z0-9]{0,40}(?:is[^A-Za-z0-9]{0,10})?(?=[A-Za-z0-9]*\d)([A-Za-z0-9]{4,8})\b|"
    r"\b(?=[A-Za-z0-9]*\d)([A-Za-z0-9]{4,8})\b(?=[^A-Za-z0-9]{0,20}is your\b)",
    re.I,
)
_LINK = re.compile(r"https://[^\s\"'<>]+")
_SIGN_IN_PATH = re.compile(r"sign|log.?in|auth|verify|magic|token|confirm|session", re.I)


def extract_sign_in(raw: bytes, since: datetime, site: str, want: str) -> str | None:
    """A sign-in code (want="code") or link (want="link") from `site`, sent after `since`.

    `site` is the brand in the sender's domain ("luma", "mlh", "eventbrite", "devpost").
    """
    message = email.message_from_bytes(raw)
    sender = parseaddr(message.get("From", ""))[1].lower()
    if site.lower() not in sender.rpartition("@")[2]:
        return None
    try:
        received = parsedate_to_datetime(message.get("Date", ""))
        if received is None or received.astimezone(UTC) < since - timedelta(seconds=30):
            return None
    except (TypeError, ValueError, OverflowError):
        return None
    subject = str(make_header(decode_header(message.get("Subject", ""))))
    if want == "code":
        match = _SIGN_IN_CODE.search(subject) or _SIGN_IN_CODE.search(_message_text(message))
        return (match.group(1) or match.group(2)) if match else None
    links = [u.rstrip(".,)") for u in _LINK.findall(_raw_text(message))]
    return next((u for u in links if site.lower() in u.lower() and _SIGN_IN_PATH.search(u)), None)


def _raw_text(message: email.message.Message) -> str:
    """Every text part as sent, HTML included, so link targets (hrefs) survive."""
    chunks = []
    for part in message.walk() if message.is_multipart() else [message]:
        payload = part.get_payload(decode=True)
        if part.get_content_maintype() == "text" and isinstance(payload, bytes):
            chunks.append(
                unescape(payload.decode(part.get_content_charset() or "utf-8", "replace"))
            )
    return " ".join(chunks)


def wait_for_sign_in(
    address: str,
    password: str,
    since: datetime,
    site: str,
    want: str,
    timeout_seconds: int = 150,
) -> str | None:
    """The newest sign-in code or link `site` emailed after `since`, read-only from Gmail."""
    return _poll(
        address,
        password,
        since,
        timeout_seconds,
        lambda raw: extract_sign_in(raw, since, site, want),
    )
