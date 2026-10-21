"""Job pipeline: what came back to both Gmail inboxes, matched to the leads it's about.

Reads the main and outreach inboxes read-only, keeps recruiting mail (ATS senders, people at
companies you applied to or emailed, bounces, application-stage wording), classifies each
email into a stage, and stores one event per email (sender, subject, stage, a short snippet,
never the full body) in the `pipeline` log. `board` turns leads + events into the columns
the dashboard shows.
"""

import re
from collections.abc import Callable
from datetime import UTC, date, datetime, timedelta
from email.header import decode_header, make_header
from email.message import Message
from email.utils import parseaddr, parsedate_to_datetime
from typing import Any, Literal
from urllib.parse import urlsplit

from pydantic import BaseModel

from internship_agent import db, notify
from internship_agent.applications.verification_mail import _message_text
from internship_agent.config import Settings
from internship_agent.leads.followups import company_domain
from internship_agent.leads.schemas import Lead, LeadStatus
from internship_agent.notify import Push
from internship_agent.tracking import Stage, classify_text

EventStage = Literal["applied", "reply", "assessment", "interview", "offer", "rejected", "bounced"]
# Applicant-tracking and assessment senders: their mail is about an application even when
# the sender name isn't the company's.
ATS = (
    "greenhouse.io",
    "greenhouse-mail.io",
    "lever.co",
    "ashbyhq.com",
    "myworkday.com",
    "workday.com",
    "smartrecruiters.com",
    "icims.com",
    "workablemail.com",
    "workable.com",
    "jobvite.com",
    "successfactors.com",
    "bamboohr.com",
    "rippling.com",
    "gem.com",
    "dover.com",
    "wellfound.com",
    "hackerrank.com",
    "codesignal.com",
    "codility.com",
    "hirevue.com",
    "teamtailor.com",
    "recruitee.com",
    "breezy.hr",
    "personio.de",
)
_BOUNCE = ("mailer-daemon", "postmaster")
_HINT = re.compile(
    r"\b(intern(ship)?s?|co-?op|winter 2027|application|applying|applied|interview|"
    r"assessment|offer|recruit(er|ing)|candidate|position|role)\b",
    re.I,
)
MAX_BODIES = 80  # full messages fetched per inbox per scan


class InboxEvent(BaseModel):
    message_id: str
    inbox: str  # the Gmail address it arrived at
    received_at: datetime
    sender: str
    sender_name: str
    subject: str
    stage: EventStage
    company: str
    lead_key: str | None
    snippet: str


def _header(message: Message, name: str) -> str:
    try:
        return " ".join(str(make_header(decode_header(str(message.get(name, ""))))).split())
    except Exception:  # a malformed header shouldn't stop the scan
        return " ".join(str(message.get(name, "")).split())


def _host(url: str | None) -> str:
    host = (urlsplit(url or "").hostname or "").lower()
    return host.removeprefix("www.")


def _is_ats(address: str) -> bool:
    domain = address.rpartition("@")[2].lower()
    return any(domain == d or domain.endswith("." + d) for d in ATS)


def _words(text: str) -> str:
    return " " + re.sub(r"[^a-z0-9]+", " ", text.lower()) + " "


def match(sender: str, sender_name: str, subject: str, body: str, leads: list[Lead]) -> Lead | None:
    """The lead an email is about: by the address emailed, then the company's own domain,
    then the company's name in the sender name or subject (for ATS mail). Leads you applied
    to or contacted win ties."""
    sender = sender.lower()
    domain = company_domain(sender)
    named = _words(f"{sender_name} {subject}")
    active = sorted(
        leads, key=lambda lead: lead.status not in (LeadStatus.APPLIED, LeadStatus.CONTACTED)
    )
    for lead in active:
        if sender in {(lead.sent_to or "").lower(), (lead.email or "").lower()} - {""}:
            return lead
    if domain and not _is_ats(sender):
        for lead in active:
            own = {
                company_domain(lead.sent_to or "") or "",
                company_domain(lead.email or "") or "",
                _host(lead.company_url),
            }
            if domain in own - {""}:
                return lead
    for lead in active:
        name = _words(lead.company).strip()
        if len(name) >= 4 and f" {name} " in named:
            return lead
    return None


def classify(sender: str, subject: str, body: str, lead: Lead | None) -> EventStage | None:
    """The stage this email marks, or None if it isn't about your search."""
    if any(sender.lower().startswith(b) for b in _BOUNCE):
        return "bounced" if lead else None
    stage = classify_text(f"{subject}\n{body[:4000]}")
    relevant = lead is not None or _is_ats(sender) or _HINT.search(subject)
    if stage is not Stage.OTHER and relevant:
        return stage.value  # type: ignore[return-value]
    if lead is not None and lead.sent_at is not None and not _is_ats(sender):
        return "reply"  # someone at a company you emailed wrote back
    return None


def _bounced_lead(body: str, leads: list[Lead]) -> Lead | None:
    """A bounce notice quotes the address that failed."""
    text = body.lower()
    return next((lead for lead in leads if lead.sent_to and lead.sent_to.lower() in text), None)


# "Thank you for applying to Astranis!", "Your application to Vercel", "interest in Sony".
_APPLIED_TO = re.compile(
    r"\b(?:applying to|application to|application for|interest in|applied to)\s+(?:the\s+)?"
    r"([A-Z0-9][\w&.'\- ]{1,40}?)(?=\s*(?:[!.,:|(\-–]|$| for | position| role| team))"
)
# "Astranis: Thank You for Launching Your Application".
_NAME_FIRST = re.compile(
    r"^([A-Z0-9][\w&.' \-]{1,40}?):\s+(?:thank you|thanks|your application)", re.I
)


def display_company(event: InboxEvent) -> str:
    """The company a mail is from: its lead's name, else the one its subject names (ATS
    mail comes from greenhouse-mail.io, not the company), else what was stored."""
    if event.lead_key is None and (
        named := _APPLIED_TO.search(event.subject) or _NAME_FIRST.match(event.subject)
    ):
        return named.group(1).strip()
    return event.company


def to_event(inbox: str, message: Message, leads: list[Lead]) -> InboxEvent | None:
    sender_name, sender = parseaddr(_header(message, "From"))
    sender = sender.lower()
    subject = _header(message, "Subject")
    body = _message_text(message)
    is_bounce = any(sender.startswith(b) for b in _BOUNCE)
    lead = (
        _bounced_lead(body, leads)
        if is_bounce
        else match(sender, sender_name, subject, body, leads)
    )
    stage = classify(sender, subject, body, lead)
    if stage is None:
        return None
    try:
        received = parsedate_to_datetime(_header(message, "Date")).astimezone(UTC)
    except (TypeError, ValueError):
        received = datetime.now(UTC)
    return InboxEvent(
        message_id=_header(message, "Message-ID") or f"{sender}|{subject}|{received.isoformat()}",
        inbox=inbox,
        received_at=received,
        sender=sender,
        sender_name=sender_name,
        subject=subject[:200],
        stage=stage,
        company=lead.company if lead else (sender_name or sender.rpartition("@")[2]),
        lead_key=lead.key if lead else None,
        snippet=body[:240],
    )


def worth_reading(headers: Message, leads: list[Lead], known: set[str]) -> bool:
    """From headers alone: new, and from a recruiting sender, a contact, a bounce or about
    applications. Only these are downloaded in full."""
    if _header(headers, "Message-ID") in known:
        return False
    name, sender = parseaddr(_header(headers, "From"))
    sender = sender.lower()
    if (
        _is_ats(sender)
        or any(sender.startswith(b) for b in _BOUNCE)
        or _HINT.search(_header(headers, "Subject"))
    ):
        return True
    domain = company_domain(sender)
    addresses = {lead.sent_to.lower() for lead in leads if lead.sent_to}
    domains = {d for a in addresses if (d := company_domain(a))}
    return sender in addresses or domain in domains


def events(settings: Settings) -> list[InboxEvent]:
    return [InboxEvent.model_validate(r) for r in db.read_log(settings, "pipeline")]


def inboxes(settings: Settings) -> list[tuple[str, str]]:
    """(address, app password) of the main Gmail and, if set up, the outreach Gmail."""
    found = []
    if settings.gmail_ready:
        found.append(settings.gmail_account(None))
    if settings.outreach_ready:
        found.append(settings.gmail_account("outreach"))
    return found


def sync(
    settings: Settings,
    leads: list[Lead],
    days: int = 45,
    open_mailbox: Callable[[str, str], Any] | None = None,
) -> list[InboxEvent]:
    """Scan both inboxes for new pipeline emails and store them. Returns the new events."""
    from internship_agent.mailbox import GmailMailbox

    connect = open_mailbox or GmailMailbox
    known = {e.message_id for e in events(settings)}
    since = datetime.now(UTC) - timedelta(days=days)
    added: list[InboxEvent] = []
    for address, password in inboxes(settings):
        with connect(address, password) as box:
            candidates = [
                (number, headers)
                for number, headers in box.inbox_headers(since)
                if worth_reading(headers, leads, known)
            ]
            for number, _ in candidates[-MAX_BODIES:]:  # newest last; keep the latest
                message = box.message(number)
                if message is None or (event := to_event(address, message, leads)) is None:
                    continue
                if event.message_id in known:
                    continue
                known.add(event.message_id)
                db.append(settings, "pipeline", event.model_dump(mode="json"))
                added.append(event)
    return added


# Replies aren't here: n8n (main inbox) and `followups --check-only` (outreach) push those.
_NOTABLE = {
    "assessment": "Assessment",
    "interview": "Interview",
    "offer": "Offer",
}


def push_for(new: list[InboxEvent], click: str | None) -> Push | None:
    """A phone push for what needs you: assessments, interviews, offers."""
    lines = [
        f"{_NOTABLE[e.stage]}: {e.company}: {e.subject[:80]}" for e in new if e.stage in _NOTABLE
    ]
    if not lines:
        return None
    return Push(
        title="Job pipeline", message="\n".join(lines), click=click, priority=4, tags=["briefcase"]
    )


def scan(settings: Settings, push: bool = True) -> list[InboxEvent]:
    """Sync both inboxes against the stored leads; push what needs you. The very first scan
    backfills quietly instead of pushing weeks of old mail."""
    from internship_agent.leads.store import open_lead_store

    first = not events(settings)
    leads = open_lead_store(settings.data_dir, settings.database_url).load()
    added = sync(settings, leads, settings.pipeline_days)
    if (
        push
        and not first
        and settings.ntfy_topic
        and (message := push_for(added, settings.dashboard_url))
    ):
        notify.send(settings.ntfy_server, settings.ntfy_topic, message)
    return added


COLUMNS = ("waiting", "reply", "assessment", "interview", "offer", "rejected", "bounced")


def board(leads: list[Lead], found: list[InboxEvent]) -> list[dict[str, Any]]:
    """One card per company in your pipeline, in the column of its latest email.

    Applied-to and emailed leads with nothing back yet are "waiting". A confirmation
    ("applied") doesn't move a card: it's still waiting on a person.
    """
    by_lead: dict[str, list[InboxEvent]] = {}
    unmatched: dict[str, list[InboxEvent]] = {}
    for e in sorted(found, key=lambda e: e.received_at):
        (
            by_lead.setdefault(e.lead_key, [])
            if e.lead_key
            else unmatched.setdefault(display_company(e), [])
        ).append(e)
    cards = []
    for lead in leads:
        mail = by_lead.get(lead.key, [])
        if (
            not mail
            and lead.status not in (LeadStatus.APPLIED, LeadStatus.CONTACTED)
            and not lead.sent_at
        ):
            continue
        cards.append(_card(lead.company, lead.key, lead.posting_title, lead.status.value, mail))
    for company, mail in unmatched.items():
        cards.append(_card(company, None, "", "", mail))
    return sorted(cards, key=lambda c: c["last"] or "", reverse=True)


def _card(
    company: str, key: str | None, title: str, status: str, mail: list[InboxEvent]
) -> dict[str, Any]:
    moved = [e for e in mail if e.stage != "applied"]
    column = moved[-1].stage if moved else "waiting"
    return {
        "company": company,
        "key": key,
        "title": title,
        "status": status,
        "column": column,
        "last": mail[-1].received_at.isoformat() if mail else None,
        "emails": [e.model_dump(mode="json") for e in reversed(mail)],
    }


HEARD = {"reply", "assessment", "interview", "offer"}  # a person, not a robot, wrote back
_SOURCES = {"pattern": "Guessed address", "published": "Published address"}


def _pct(part: int, whole: int) -> int:
    return round(100 * part / whole) if whole else 0


def insights(
    leads: list[Lead], found: list[InboxEvent], outreach: str | None, today: date
) -> dict[str, Any]:
    """The numbers behind the board, and what they say: outreach and application funnels,
    where emails bounce, inbound mail by day, and takeaways computed from them."""
    seen: dict[str, set[str]] = {}
    first_heard: dict[str, datetime] = {}
    for e in sorted(found, key=lambda e: e.received_at):
        if e.lead_key:
            seen.setdefault(e.lead_key, set()).add(e.stage)
            if e.stage in HEARD:
                first_heard.setdefault(e.lead_key, e.received_at)

    def got(lead: Lead) -> set[str]:
        return seen.get(lead.key, set())

    emailed = [lead for lead in leads if lead.sent_at]
    bounced = [lead for lead in emailed if "bounced" in got(lead)]
    heard = [lead for lead in emailed if got(lead) & HEARD]
    delivered = len(emailed) - len(bounced)
    applied = [
        lead
        for lead in leads
        if lead.status is LeadStatus.APPLIED
        or (lead.application is not None and lead.application.submission_status == "submitted")
    ]
    confirmed = [lead for lead in leads if "applied" in got(lead)]
    # Companies (by name, as shown) with at least one email at each stage.
    by_stage = {
        s: {display_company(e) for e in found if e.stage == s} for s in HEARD | {"rejected"}
    }

    def split(rows: dict[str, list[Lead]]) -> list[dict[str, Any]]:
        return [
            {
                "label": label,
                "sent": len(group),
                "bounced": sum("bounced" in got(lead) for lead in group),
                "heard": sum(bool(got(lead) & HEARD) for lead in group),
            }
            for label, group in rows.items()
            if group
        ]

    def grouped(name: Callable[[Lead], str]) -> dict[str, list[Lead]]:
        rows: dict[str, list[Lead]] = {}
        for lead in emailed:
            rows.setdefault(name(lead), []).append(lead)
        return rows

    outreach_box = (outreach or "").lower()
    sources = split(grouped(lambda lead: _SOURCES.get(lead.email_status.value, "Other address")))
    inboxes_ = split(
        grouped(
            lambda lead: (
                "Outreach Gmail"
                if (lead.sent_from or "").lower() in ("outreach", outreach_box) and lead.sent_from
                else "Main Gmail"
            )
        )
    )
    segments = split(
        grouped(
            lambda lead: {"early": "Early-stage", "mid": "Mid-stage", "big": "Big company"}.get(
                lead.segment.value if lead.segment else "", "Unclassified"
            )
        )
    )

    start = today - timedelta(days=20)
    daily = []
    for offset in range(21):
        day = start + timedelta(days=offset)
        inbound = [e for e in found if e.received_at.astimezone(UTC).date() == day]
        daily.append(
            {
                "day": day.isoformat(),
                "sent": sum(
                    lead.sent_at.astimezone(UTC).date() == day for lead in emailed if lead.sent_at
                ),
                "confirmation": sum(e.stage == "applied" for e in inbound),
                "bounced": sum(e.stage == "bounced" for e in inbound),
                "heard": sum(e.stage in HEARD for e in inbound),
                "rejected": sum(e.stage == "rejected" for e in inbound),
            }
        )

    lags = sorted(
        (first_heard[lead.key] - lead.sent_at).days
        for lead in heard
        if lead.sent_at and lead.key in first_heard and first_heard[lead.key] > lead.sent_at
    )
    notes = _takeaways(sources, segments, emailed, heard, delivered, leads, got, by_stage, today)
    return {
        "tiles": [
            {"label": "Emailed", "value": len(emailed), "sub": f"{len(bounced)} bounced"},
            {
                "label": "Delivered",
                "value": f"{_pct(delivered, len(emailed))}%",
                "sub": f"{delivered} of {len(emailed)}",
            },
            {
                "label": "Replies",
                "value": len(heard),
                "sub": f"{_pct(len(heard), delivered)}% of delivered",
            },
            {
                "label": "Applied",
                "value": len(applied),
                "sub": f"{len(confirmed)} confirmed by email",
            },
            {
                "label": "Interviews",
                "value": len(by_stage["interview"]),
                "sub": f"{len(by_stage['offer'])} offers",
            },
            {"label": "Rejections", "value": len(by_stage["rejected"]), "sub": "by email"},
        ],
        "funnels": {
            "outreach": [
                ["Emailed", len(emailed)],
                ["Delivered", delivered],
                ["Replied", len(heard)],
                ["Interview", sum("interview" in got(lead) for lead in emailed)],
            ],
            "applications": [
                ["Applied", len(applied)],
                ["Confirmed by email", len(confirmed)],
                ["Heard back", sum(bool(got(lead) & HEARD) for lead in applied)],
                ["Interview", sum("interview" in got(lead) for lead in applied)],
            ],
        },
        "sources": sources,
        "inboxes": inboxes_,
        "segments": segments,
        "daily": daily,
        "median_reply_days": lags[len(lags) // 2] if lags else None,
        "notes": notes,
    }


def _takeaways(
    sources: list[dict[str, Any]],
    segments: list[dict[str, Any]],
    emailed: list[Lead],
    heard: list[Lead],
    delivered: int,
    leads: list[Lead],
    got: Callable[[Lead], set[str]],
    by_stage: dict[str, set[str]],
    today: date,
) -> list[dict[str, str]]:
    """Plain-language takeaways, each computed from the numbers above (no model involved)."""
    notes = []
    by_label = {row["label"]: row for row in sources}
    guessed = by_label.get("Guessed address")
    if guessed and guessed["sent"] >= 10 and _pct(guessed["bounced"], guessed["sent"]) >= 20:
        notes.append(
            {
                "tone": "warn",
                "text": (
                    f"{_pct(guessed['bounced'], guessed['sent'])}% of emails to guessed "
                    f"addresses bounced ({guessed['bounced']} of {guessed['sent']}). Bounces "
                    "count against your Gmail's sender reputation, so send to a guessed "
                    "address only once its format is proven at that company."
                ),
            }
        )
    if delivered:
        rate = _pct(len(heard), delivered)
        text = f"{len(heard)} of {delivered} delivered emails got a reply from a person ({rate}%)."
        compare = [r for r in segments if r["sent"] - r["bounced"] >= 15]
        if len(compare) >= 2:
            text += (
                " By stage: "
                + ", ".join(
                    f"{r['label'].lower()} {_pct(r['heard'], r['sent'] - r['bounced'])}%"
                    for r in compare
                )
                + "."
            )
        notes.append({"tone": "info", "text": text})
    went_through = [
        lead.company
        for lead in leads
        if lead.application is not None
        and lead.application.submission_status in ("uncertain", "failed", "blocked", "pending")
        and got(lead) & {"applied", "rejected", "interview", "assessment"}
    ]
    if went_through:
        notes.append(
            {
                "tone": "ok",
                "text": (
                    f"{len(went_through)} application(s) recorded as not confirmed did reach "
                    f"the employer, who emailed back: {', '.join(sorted(went_through))}."
                ),
            }
        )
    if by_stage["interview"] or by_stage["offer"]:
        notes.append(
            {
                "tone": "ok",
                "text": (
                    "Needs you: "
                    + ", ".join(sorted(by_stage["offer"] | by_stage["interview"]))
                    + ". Open the card to see the email."
                ),
            }
        )
    cold = [
        lead
        for lead in emailed
        if lead.sent_at
        and lead.sent_at.astimezone(UTC).date() <= today - timedelta(days=14)
        and not got(lead) & (HEARD | {"bounced"})
        and len(lead.followups) >= 2
    ]
    if cold:
        notes.append(
            {
                "tone": "info",
                "text": (
                    f"{len(cold)} people emailed over two weeks ago have had both follow-ups "
                    "and no reply. A LinkedIn note is the remaining channel; otherwise let "
                    "them go."
                ),
            }
        )
    return notes
