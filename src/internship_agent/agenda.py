"""One calendar for both agents: deadlines, events and follow-ups, and an .ics export."""

import hashlib
from datetime import date, datetime, timedelta
from typing import Literal

from pydantic import BaseModel

from internship_agent.leads.followups import next_followup
from internship_agent.leads.refill import DONE
from internship_agent.leads.schemas import Lead
from internship_agent.opportunities.run import PLANNED
from internship_agent.opportunities.schemas import Opportunity, OpportunityStatus

ItemKind = Literal["apply", "deadline", "event", "followup"]


class Item(BaseModel):
    day: date
    end: date | None = None  # last day of a multi-day event
    kind: ItemKind
    title: str
    detail: str = ""
    key: str  # the lead's or opportunity's key, to open it
    url: str = ""
    # Planned by you, or promising (fit 75+ or travel paid): shown by default and exported.
    mine: bool


def _promising(o: Opportunity) -> bool:
    a = o.assessment
    return o.status in PLANNED or bool(
        a and (a.fit_score >= 75 or a.travel in ("covered", "partial"))
    )


def opportunity_items(o: Opportunity) -> list[Item]:
    if o.status is OpportunityStatus.SKIPPED:
        return []
    base = {"key": o.key, "url": o.url, "mine": _promising(o)}
    found = []
    if o.assessment and o.assessment.apply_by:
        found.append(
            Item(day=o.assessment.apply_by, kind="apply", title=f"Apply: {o.title}", **base)
        )
    if o.deadline:
        found.append(
            Item(
                day=o.deadline,
                kind="deadline",
                title=f"{o.deadline_label or 'Deadline'}: {o.title}",
                **base,
            )
        )
    if o.starts_on:
        where = "Online" if o.online else o.location
        found.append(
            Item(day=o.starts_on, end=o.ends_on, kind="event", title=o.title, detail=where, **base)
        )
    return found


def lead_items(lead: Lead, followup_days: int, today: date) -> list[Item]:
    found = []
    if lead.deadline and lead.status not in DONE:
        title = f"Apply: {lead.company}" + (
            f" ({lead.posting_title})" if lead.posting_title else ""
        )
        found.append(
            Item(
                day=lead.deadline,
                kind="apply",
                title=title,
                key=lead.key,
                url=lead.posting_url or "",
                mine=True,
            )
        )
    if due := next_followup(lead, followup_days):
        who = lead.contact_name or lead.sent_to or lead.company
        found.append(
            Item(
                day=max(due.date(), today),  # an overdue one is still to do today
                kind="followup",
                title=f"Follow up: {who} ({lead.company})",
                detail=f"Last emailed {due.date() - timedelta(days=followup_days)}",
                key=lead.key,
                mine=True,
            )
        )
    return found


def items(
    leads: list[Lead], opportunities: list[Opportunity], followup_days: int, today: date
) -> list[Item]:
    found = [i for o in opportunities for i in opportunity_items(o)]
    found += [i for lead in leads for i in lead_items(lead, followup_days, today)]
    return sorted(found, key=lambda i: (i.day, i.kind, i.title))


def _text(value: str) -> str:
    """Escape an iCalendar TEXT value."""
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def _fold(line: str) -> list[str]:
    """Split a content line at 75 octets, continuing with a space (RFC 5545 3.1)."""
    out, current = [], ""
    for ch in line:
        if len((current + ch).encode()) > 75:
            out.append(current)
            current = " "
        current += ch
    return [*out, current]


def to_ics(found: list[Item], now: datetime) -> str:
    """All-day events, one per item; importing again updates them (stable UIDs)."""
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//internship-agent//calendar//EN",
        "CALSCALE:GREGORIAN",
        "X-WR-CALNAME:Internships & opportunities",
    ]
    for i in found:
        uid = hashlib.sha1(f"{i.kind}|{i.key}".encode()).hexdigest()
        end = (i.end or i.day) + timedelta(days=1)  # DTEND is exclusive
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}@internship-agent",
            f"DTSTAMP:{stamp}",
            f"DTSTART;VALUE=DATE:{i.day:%Y%m%d}",
            f"DTEND;VALUE=DATE:{end:%Y%m%d}",
            f"SUMMARY:{_text(i.title)}",
            *([f"DESCRIPTION:{_text(i.detail)}"] if i.detail else []),
            *([f"URL:{i.url}"] if i.url else []),
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(part for line in lines for part in _fold(line)) + "\r\n"
