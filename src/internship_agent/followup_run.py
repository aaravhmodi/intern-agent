"""Send the follow-ups that are due, after checking the mailbox for replies.

This is the one place email goes out without a click in the dashboard. It only writes to
people already emailed from the dashboard, only the fixed follow-up texts, and never to
someone who has written back or whose address bounced. If the mailbox can't be read,
nothing is sent.
"""

import time
from datetime import UTC, datetime, timedelta
from urllib.parse import urlsplit

from pydantic import BaseModel

from internship_agent import db, mailer, pipeline
from internship_agent.config import Settings
from internship_agent.leads.followups import (
    TEMPLATES,
    company_domain,
    followup_body,
    is_due,
    reply_subject,
)
from internship_agent.leads.schemas import Lead, LeadStatus, Note
from internship_agent.leads.store import LeadStore, PostgresLeadStore, open_lead_store
from internship_agent.mailbox import Mailbox

# Bounce notices arrive within minutes, or after a couple of days of retries at worst, so
# older emails aren't searched for one again: that search is most of a check's time.
BOUNCE_WINDOW = timedelta(days=7)
# A reply you haven't answered after this long gets one reminder push.
ANSWER_WITHIN = timedelta(days=2)


class FollowupSent(BaseModel):
    key: str
    company: str
    contact: str
    to: str
    # 1 for the first follow-up, 2 for the second.
    number: int
    subject: str
    body: str


class FollowupReport(BaseModel):
    # A dry run finds out who would get what and changes nothing.
    dry_run: bool
    sent: list[FollowupSent] = []
    # Wrote back since the last run, so they get no more follow-ups.
    replied: list[str] = []
    bounced: list[str] = []
    # Emailed at an address that belongs to another lead's company, so not followed up.
    wrong_address: list[str] = []
    # Emailed, no reply yet, and not due a follow-up today.
    waiting: int = 0
    # Got every follow-up and still hasn't replied.
    finished: int = 0
    # Due today but over the daily limit; they go out on the next run.
    held: int = 0
    error: str = ""
    # Wrote back and you haven't answered: reminded once per reply.
    unanswered: list[str] = []


def _logged_subject(settings: Settings, key: str) -> str | None:
    """The subject the first email went out with, from the send log."""
    subject = None
    for record in db.read_log(settings, "sent-log"):
        if record.get("key") == key and not record.get("followup"):
            subject = record.get("subject")
    return subject


def _site(lead: Lead) -> str:
    host = urlsplit(lead.company_url or "").hostname or ""
    return host.removeprefix("www.").lower()


def _misaddressed(leads: list[Lead]) -> set[str]:
    """Leads emailed at an address another lead's company owns.

    Two leads sharing one address means one email went to the wrong company (Keenable's
    was once sent to Veeda's contact address). The lead whose own site matches the
    address keeps its follow-ups; the others are not written to there again.
    """
    by_address: dict[str, list[Lead]] = {}
    for lead in leads:
        if lead.sent_at and lead.sent_to:
            by_address.setdefault(lead.sent_to, []).append(lead)
    wrong: set[str] = set()
    for address, sharing in by_address.items():
        domain = company_domain(address)
        owners = [lead for lead in sharing if domain and _site(lead).endswith(domain)]
        if len(sharing) > 1 and owners:
            wrong.update(lead.key for lead in sharing if lead not in owners)
    return wrong


def _name(lead: Lead) -> str:
    return f"{lead.contact_name or 'the team'} at {lead.company}"


def run_followups(
    settings: Settings,
    mailbox: Mailbox,
    *,
    now: datetime | None = None,
    dry_run: bool = False,
    pause_seconds: float = 0,
    outreach_mailbox: Mailbox | None = None,
    send_due: bool = True,
) -> FollowupReport:
    """Stop follow-ups for anyone who replied, then send the ones that are due.

    Leads first emailed from the outreach Gmail are checked in, and followed up from,
    that account (outreach_mailbox); the rest use the main one.
    """
    if not settings.gmail_address or not settings.gmail_app_password:
        raise mailer.MailError("Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env to send email.")
    moment = now or datetime.now(UTC)
    store = open_lead_store(settings.data_dir, settings.database_url)
    report = FollowupReport(dry_run=dry_run)
    leads = store.load()
    misaddressed = _misaddressed(leads)
    # Bounces the dashboard's inbox scan already found, at any age, beyond the mailbox search.
    scanned: dict[str, list[datetime]] = {}
    for event in pipeline.events(settings):
        if event.stage == "bounced" and event.lead_key:
            scanned.setdefault(event.lead_key, []).append(event.received_at)
    for lead in leads:
        if not lead.sent_at or not lead.sent_to or lead.status is LeadStatus.SKIPPED:
            continue
        if lead.replied_at is not None or lead.followups_stopped:
            continue
        if lead.key in misaddressed:
            report.wrong_address.append(f"{_name(lead)} (sent to {lead.sent_to})")
            if not dry_run:
                lead.followups_stopped = "wrong address"
                lead.notes.append(
                    Note(
                        at=moment,
                        text=f"The email went to {lead.sent_to}, another company's address; "
                        "no follow-ups. Email them at their own address.",
                    )
                )
                store.upsert(lead)
            continue
        # Everyone still waiting is checked, due or not, so a reply always ends it.
        box = outreach_mailbox if lead.sent_from and outreach_mailbox else mailbox
        heard = box.heard_from(lead.sent_to, lead.sent_at)
        if heard is not None:
            report.replied.append(_name(lead))
            if not dry_run:
                lead.replied_at = heard
                lead.notes.append(
                    Note(
                        at=moment, text=f"They wrote back on {heard:%B} {heard.day}; no follow-ups."
                    )
                )
                store.upsert(lead)
            continue
        # Only a bounce since the address last emailed counts: earlier guesses bounce by design.
        since = lead.sent_at - timedelta(minutes=5)
        if (
            lead.sent_to in lead.bounced_emails
            or any(at >= since for at in scanned.get(lead.key, []))
            or (moment - lead.sent_at < BOUNCE_WINDOW and box.bounced(lead.sent_to, lead.sent_at))
        ):
            report.bounced.append(_name(lead))
            if not dry_run:
                lead.followups_stopped = "bounced"
                lead.notes.append(
                    Note(at=moment, text=f"The email to {lead.sent_to} bounced; no follow-ups.")
                )
                store.upsert(lead)
            continue
        if not send_due:  # only recording replies and bounces this time
            continue
        if len(lead.followups) >= len(TEMPLATES):
            report.finished += 1
            continue
        if not is_due(lead, moment, settings.followup_days):
            report.waiting += 1
            continue
        if len(report.sent) >= settings.followup_daily_limit:
            report.held += 1
            continue

        first = box.first_email(lead.sent_to, lead.sent_at)
        original = (
            (first.subject if first else None)
            or _logged_subject(settings, lead.key)
            or (
                lead.draft.email_subject
                if lead.draft
                else f"Winter 2027 internship at {lead.company}"
            )
        )
        number = len(lead.followups) + 1
        sending = FollowupSent(
            key=lead.key,
            company=lead.company,
            contact=lead.contact_name,
            to=lead.sent_to,
            number=number,
            subject=reply_subject(original),
            body=followup_body(lead),
        )
        if not dry_run:
            sender, password = settings.gmail_account(lead.sent_from)
            message = mailer.build_message(
                sender,
                sending.to,
                sending.subject,
                sending.body,
                in_reply_to=first.message_id if first else None,
                references=first.references if first else None,
            )
            try:
                mailer.send(message, sender, password)
            except mailer.RecipientRefused:
                # This address will never take mail: stop its follow-ups, go on with the rest.
                report.bounced.append(_name(lead))
                lead.followups_stopped = "bounced"
                lead.notes.append(
                    Note(at=moment, text=f"Gmail refused {lead.sent_to}; no follow-ups.")
                )
                store.upsert(lead)
                continue
            except mailer.MailError as exc:
                # Gmail is refusing: stop rather than try everyone else.
                report.error = str(exc)
                break
            # Recorded straight away, so a later failure can't send this one twice.
            lead.followups.append(moment)
            lead.notes.append(
                Note(
                    at=moment,
                    text=f"Automatic follow-up {number} of {len(TEMPLATES)} sent to {sending.to}.",
                )
            )
            store.upsert(lead)
            record = {
                "at": moment.isoformat(),
                "key": lead.key,
                "to": sending.to,
                "subject": sending.subject,
                "followup": number,
            }
            db.append(settings, "sent-log", record)
            if pause_seconds:
                time.sleep(pause_seconds)
        report.sent.append(sending)
    _remind_unanswered(settings, store, mailbox, outreach_mailbox, moment, dry_run, report)
    return report


def _remind_unanswered(
    settings: Settings,
    store: LeadStore | PostgresLeadStore,
    mailbox: Mailbox,
    outreach_mailbox: Mailbox | None,
    moment: datetime,
    dry_run: bool,
    report: FollowupReport,
) -> None:
    """List people whose latest reply you never answered, once per reply."""
    latest: dict[str, pipeline.InboxEvent] = {}
    for event in pipeline.events(settings):
        if event.stage in pipeline.HEARD and event.lead_key:
            seen = latest.get(event.lead_key)
            if seen is None or event.received_at > seen.received_at:
                latest[event.lead_key] = event
    outreach = (settings.outreach_gmail_address or "").lower()
    for lead in store.load():
        event = latest.get(lead.key)
        if event is None or moment - event.received_at < ANSWER_WITHIN:
            continue
        if lead.reminded_reply_at and lead.reminded_reply_at >= event.received_at:
            continue
        box = outreach_mailbox if outreach_mailbox and event.inbox.lower() == outreach else mailbox
        if box.wrote_to(event.sender, event.received_at):
            continue
        report.unanswered.append(f"{event.sender_name or event.sender} at {lead.company}")
        if not dry_run:
            lead.reminded_reply_at = event.received_at
            store.upsert(lead)
