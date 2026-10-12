"""A read-only look at the Gmail mailbox: did someone write back, and what was sent to them.

Used before any follow-up goes out. Folders are opened read-only, so nothing is marked
read, moved or deleted. It signs in with the same Gmail app password used for sending.
"""

import email
import imaplib
import re
from datetime import UTC, datetime, timedelta
from email.header import decode_header, make_header
from types import TracebackType
from typing import Protocol, Self

from pydantic import BaseModel

from internship_agent.leads.followups import company_domain

GMAIL_IMAP = "imap.gmail.com"
# Bounce notices come from the mail system, not the person.
_BOUNCE_SENDER = "mailer-daemon"


class MailboxError(RuntimeError):
    pass


class SentMessage(BaseModel):
    """The headers of an email already sent, enough to reply in the same thread."""

    message_id: str
    subject: str
    references: str = ""


class Mailbox(Protocol):
    def heard_from(self, address: str, since: datetime) -> datetime | None:
        """When this person, or anyone at their company, first wrote after `since`."""

    def bounced(self, address: str, since: datetime) -> bool:
        """Whether mail to this address was returned as undeliverable after `since`."""

    def first_email(self, address: str, since: datetime) -> SentMessage | None:
        """The email sent to this address at about `since`."""


def _imap_date(moment: datetime) -> str:
    # IMAP's SINCE takes a day, not a time; results are narrowed by time afterwards.
    return f"{moment.day:02d}-{moment:%b-%Y}"


def _quoted(text: str) -> str:
    return '"' + text.replace("\\", "").replace('"', "") + '"'


class GmailMailbox:
    def __init__(self, address: str, app_password: str) -> None:
        self.address = address.strip().lower()
        try:
            self.connection = imaplib.IMAP4_SSL(GMAIL_IMAP, timeout=30)
            self.connection.login(address, app_password.replace(" ", ""))
        except (imaplib.IMAP4.error, OSError) as exc:
            # Never include the server's words: they can echo the login.
            raise MailboxError(
                f"Could not sign in to Gmail to check for replies: {type(exc).__name__}"
            ) from exc
        self._folders: dict[str, str] = {}

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        kind: type[BaseException] | None,
        error: BaseException | None,
        trace: TracebackType | None,
    ) -> None:
        try:
            self.connection.logout()
        except (imaplib.IMAP4.error, OSError):
            pass

    def _folder(self, flag: str) -> str:
        """The folder Gmail marks with a special-use flag such as \\All or \\Sent."""
        if not self._folders:
            status, lines = self.connection.list()
            if status != "OK":
                raise MailboxError("Gmail would not list its folders")
            for line in lines:
                text = line.decode("utf-8", "replace") if isinstance(line, bytes) else str(line)
                match = re.match(r'\((?P<flags>[^)]*)\) "[^"]*" (?P<name>.+)$', text)
                if match:
                    for found in match.group("flags").split():
                        self._folders[found.lower()] = match.group("name").strip()
        try:
            return self._folders[flag.lower()]
        except KeyError as exc:
            raise MailboxError(f"Gmail has no {flag} folder") from exc

    def _search(self, folder_flag: str, *criteria: str) -> list[bytes]:
        try:
            status, _ = self.connection.select(self._folder(folder_flag), readonly=True)
            if status != "OK":
                raise MailboxError(f"Gmail would not open its {folder_flag} folder")
            status, data = self.connection.search(None, *criteria)
        except (imaplib.IMAP4.error, OSError) as exc:
            raise MailboxError(f"Searching Gmail failed: {type(exc).__name__}") from exc
        if status != "OK" or not data or not data[0]:
            return []
        return list(data[0].split())

    def _received(self, ids: list[bytes]) -> list[datetime]:
        if not ids:
            return []
        status, data = self.connection.fetch(b",".join(ids).decode(), "(INTERNALDATE)")
        if status != "OK":
            raise MailboxError("Gmail would not give message dates")
        times = []
        for part in data:
            raw = part if isinstance(part, bytes) else part[0] if isinstance(part, tuple) else b""
            parsed = imaplib.Internaldate2tuple(raw)
            if parsed:
                times.append(datetime(*parsed[:6]).astimezone(UTC))
        return times

    def heard_from(self, address: str, since: datetime) -> datetime | None:
        senders = [address.strip().lower()]
        domain = company_domain(address)
        if domain:
            senders.append(f"@{domain}")
        arrived: list[datetime] = []
        for sender in senders:
            ids = self._search("\\All", "FROM", _quoted(sender), "SINCE", _imap_date(since))
            arrived += [time for time in self._received(ids) if time > since]
        return min(arrived) if arrived else None

    def bounced(self, address: str, since: datetime) -> bool:
        ids = self._search(
            "\\All",
            "FROM",
            _quoted(_BOUNCE_SENDER),
            "SINCE",
            _imap_date(since),
            "BODY",
            _quoted(address.strip().lower()),
        )
        return any(time > since for time in self._received(ids))

    def first_email(self, address: str, since: datetime) -> SentMessage | None:
        day_before = since - timedelta(days=1)
        ids = self._search(
            "\\Sent", "TO", _quoted(address.strip().lower()), "SINCE", _imap_date(day_before)
        )
        if not ids:
            return None
        status, data = self.connection.fetch(
            ids[0].decode(), "(BODY.PEEK[HEADER.FIELDS (MESSAGE-ID SUBJECT REFERENCES)])"
        )
        if status != "OK":
            return None
        raw = next((part[1] for part in data if isinstance(part, tuple)), b"")
        headers = email.message_from_bytes(raw)
        message_id = " ".join(str(headers.get("Message-ID", "")).split())
        if not message_id:
            return None
        subject = str(make_header(decode_header(str(headers.get("Subject", "")))))
        return SentMessage(
            message_id=message_id,
            subject=" ".join(subject.split()),
            references=" ".join(str(headers.get("References", "")).split()),
        )
