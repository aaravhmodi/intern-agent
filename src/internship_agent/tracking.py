"""Deterministic classification of recruiting emails and calendar events."""

import re
from enum import StrEnum

from pydantic import BaseModel

from internship_agent.outlook.schemas import CalendarEvent, MailMessage

# KQL query used to pull candidate recruiting emails from Outlook.
RECRUITING_QUERY = (
    "internship OR intern OR co-op OR application OR interview OR assessment OR offer"
)


class Stage(StrEnum):
    OFFER = "offer"
    REJECTED = "rejected"
    INTERVIEW = "interview"
    ASSESSMENT = "assessment"
    APPLIED = "applied"
    OTHER = "other"


# Checked in order; the first stage with a matching pattern wins.
_STAGE_PATTERNS: list[tuple[Stage, re.Pattern[str]]] = [
    (Stage.OFFER, re.compile(r"\b(offer letter|pleased to offer|extend (you )?an offer)\b")),
    (
        Stage.REJECTED,
        re.compile(
            r"\b(unfortunately|not (to )?(be )?mov(e|ing) forward|other candidates"
            r"|no longer under consideration|regret to inform|position has been filled)\b"
        ),
    ),
    (
        Stage.INTERVIEW,
        re.compile(r"\b(interview|phone screen|schedule (a|your) (call|chat)|next round)\b"),
    ),
    (
        Stage.ASSESSMENT,
        re.compile(
            r"\b(online assessment|coding (challenge|assessment)|hackerrank|codesignal"
            r"|take-home|codility)\b"
        ),
    ),
    (
        Stage.APPLIED,
        re.compile(
            r"\b(thank(s| you) for (applying|your application|your interest)"
            r"|application (received|submitted)|we('ve| have) received your application)\b"
        ),
    ),
]

_INTERNSHIP_HINT = re.compile(r"\b(intern(ship)?s?|co-?op|winter 2027|student)\b")
_GENERIC_DOMAINS = {
    "gmail.com",
    "outlook.com",
    "hotmail.com",
    "uwaterloo.ca",
    "myworkday.com",
    "greenhouse.io",
    "lever.co",
    "ashbyhq.com",
    "smartrecruiters.com",
    "icims.com",
    "workablemail.com",
    "successfactors.com",
    "jobvite.com",
}


class ApplicationUpdate(BaseModel):
    message_id: str
    company: str
    stage: Stage
    subject: str
    received_at: str
    link: str


def classify_text(text: str) -> Stage:
    lowered = text.lower()
    for stage, pattern in _STAGE_PATTERNS:
        if pattern.search(lowered):
            return stage
    return Stage.OTHER


def guess_company(message: MailMessage) -> str:
    """Prefer the sender's display name; fall back to a non-ATS email domain."""
    name = message.sender_name.strip()
    for suffix in (" Recruiting", " Careers", " Talent Acquisition", " Hiring Team", " Jobs"):
        if name.endswith(suffix):
            return name[: -len(suffix)].strip()
    domain = message.sender_address.rpartition("@")[2].lower()
    parts = domain.split(".")
    root = ".".join(parts[-2:]) if len(parts) >= 2 else domain
    if root and root not in _GENERIC_DOMAINS:
        return parts[-2].capitalize()
    return name or "Unknown"


def to_update(message: MailMessage) -> ApplicationUpdate | None:
    text = f"{message.subject}\n{message.body_preview}"
    stage = classify_text(text)
    if stage is Stage.OTHER and not _INTERNSHIP_HINT.search(text.lower()):
        return None
    return ApplicationUpdate(
        message_id=message.id,
        company=guess_company(message),
        stage=stage,
        subject=message.subject,
        received_at=message.received_at.isoformat() if message.received_at else "",
        link=message.web_link,
    )


def application_updates(messages: list[MailMessage]) -> list[ApplicationUpdate]:
    return [u for m in messages if (u := to_update(m)) is not None]


_INTERVIEW_EVENT = re.compile(
    r"\b(interview|phone screen|technical screen|recruiter (call|chat)|onsite|super ?day)\b"
)


def interview_events(events: list[CalendarEvent]) -> list[CalendarEvent]:
    return [e for e in events if _INTERVIEW_EVENT.search(f"{e.subject} {e.body_preview}".lower())]
