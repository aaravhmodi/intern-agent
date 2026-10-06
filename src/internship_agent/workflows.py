"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import json
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta

from openai import OpenAI

from internship_agent import mailer
from internship_agent.ai import STATUS_FROM_NOTE, assess_fit, interpret_note, search_startups
from internship_agent.config import Settings
from internship_agent.leads.preferences import PreferenceStore, apply_violations
from internship_agent.leads.refill import DONE, refill
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus, Note, Preference, Segment
from internship_agent.leads.sending import check_send
from internship_agent.leads.store import LeadStore, merge
from internship_agent.resume import load_resume_text
from internship_agent.sources import simplify, startups
from internship_agent.sources.posting_text import fetch_posting_text


def lead_store(settings: Settings) -> LeadStore:
    return LeadStore(settings.data_dir / "leads.json")


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=settings.openai_api_key)


def resume_text(settings: Settings) -> str:
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")


def preference_store(settings: Settings) -> PreferenceStore:
    return PreferenceStore(settings.data_dir / "preferences.json")


def score(settings: Settings, leads: list[Lead]) -> list[Lead]:
    """Score leads in place and store them, applying learned preferences.

    Fetches each posting's description first so rules like "requires French" can be
    checked. Returns the leads that were auto-skipped by a 'skip' rule.
    """
    if not leads or not settings.openai_api_key:
        return []
    client, resume, store = _openai(settings), resume_text(settings), lead_store(settings)
    prefs = preference_store(settings).load()
    skipped: list[Lead] = []
    for lead in leads:
        if lead.kind is LeadKind.POSTING and lead.posting_url and not lead.posting_text:
            lead.posting_text = fetch_posting_text(lead.posting_url)
        result = assess_fit(client, settings.openai_model, resume, lead, prefs)
        lead.fit = result.fit
        lead.segment = lead.segment or result.company_segment
        if lead.status is LeadStatus.NEW:
            lead.status = LeadStatus.SCORED
        if apply_violations(lead, prefs, result.violated_preference_ids):
            skipped.append(lead)
        store.upsert(lead)
    return skipped


def rescore_open(settings: Settings) -> tuple[int, list[Lead]]:
    """Re-score every lead still in to-do against the current preferences."""
    todo = [lead for lead in lead_store(settings).load() if lead.status not in DONE]
    return len(todo), score(settings, todo)


@dataclass
class NoteOutcome:
    reply: str
    learned: list[Preference]
    status_changed: str | None
    lead: Lead | None


def handle_note(settings: Settings, message: str, key: str | None) -> NoteOutcome:
    """Interpret a note: save it on the lead, update status, and learn new preferences."""
    store, prefs_store = lead_store(settings), preference_store(settings)
    lead = store.get(key) if key else None
    result = interpret_note(
        _openai(settings), settings.openai_model, message, lead, prefs_store.load()
    )
    learned: list[Preference] = []
    for draft in result.new_preferences:
        pref = prefs_store.add(draft.rule, draft.effect, source_note=message)
        if pref is not None:
            learned.append(pref)
    status_changed = None
    if lead is not None:
        lead.notes.append(Note(at=datetime.now(UTC), text=result.lead_note or message))
        new_status = STATUS_FROM_NOTE.get(result.status_change)
        if new_status is not None and lead.status is not new_status:
            lead.status = new_status
            status_changed = new_status.value
        store.upsert(lead)
    return NoteOutcome(result.reply, learned, status_changed, lead)


def find_more_postings(settings: Settings, target_open: int) -> list[Lead]:
    """Top up open postings from the public SimplifyJobs list and score the new ones."""
    store = lead_store(settings)
    candidates = [simplify.to_lead(p) for p in simplify.matching(simplify.parse(simplify.fetch()))]
    leads, added = refill(store.load(), candidates, target_open)
    store.save(leads)
    score(settings, added)
    return added


def find_startups(
    settings: Settings, stages: list[Segment], count: int = 5, max_age_days: int = 60
) -> list[Lead]:
    """Web-search recent funding rounds, keep verifiable ones, store and score them."""
    store = lead_store(settings)
    existing = store.load()
    today = date.today()
    findings = search_startups(
        _openai(settings),
        settings.openai_model,
        today - timedelta(days=max_age_days),
        today,
        stages,
        sorted({lead.company for lead in existing}),
        count,
    )
    leads, _ = merge(existing, startups.to_leads(findings, today, max_age_days, stages))
    store.save(leads)
    new = leads[len(existing) :]
    score(settings, new)
    return new


def send_email(
    settings: Settings,
    key: str,
    to: str,
    subject: str,
    body: str,
    attach_resume: bool,
    confirm_unverified: bool,
    resend: bool = False,
) -> Lead:
    """Send one email for a lead after the safety checks, then record it."""
    if not settings.gmail_ready or not settings.gmail_address or not settings.gmail_app_password:
        raise mailer.MailError("Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env to send email.")
    store = lead_store(settings)
    lead = store.get(key)
    check_send(lead, to, confirm_unverified, resend)
    message = mailer.build_message(
        settings.gmail_address,
        to.strip(),
        subject,
        body,
        settings.resume_path if attach_resume else None,
    )
    mailer.send(message, settings.gmail_address, settings.gmail_app_password.get_secret_value())
    lead.sent_at = datetime.now(UTC)
    lead.sent_to = to.strip().lower()
    lead.status = LeadStatus.CONTACTED
    store.upsert(lead)
    log = settings.data_dir / "sent-log.jsonl"
    with log.open("a", encoding="utf-8") as f:
        at = lead.sent_at.isoformat()
        record = {"at": at, "key": key, "to": lead.sent_to, "subject": subject}
        f.write(json.dumps(record) + "\n")
    return lead
