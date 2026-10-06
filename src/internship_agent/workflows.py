"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import json
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta

from openai import OpenAI

from internship_agent import mailer
from internship_agent.ai import (
    STATUS_FROM_NOTE,
    assess_fit,
    interpret_note,
    prepare_answers,
    search_startups,
)
from internship_agent.config import Settings
from internship_agent.leads.answers import (
    AnswerBank,
    common_questions,
    normalize,
    prefill,
    validate,
)
from internship_agent.leads.preferences import PreferenceStore, apply_violations
from internship_agent.leads.refill import DONE, refill
from internship_agent.leads.schemas import (
    ApplicationPrep,
    Lead,
    LeadKind,
    LeadStatus,
    Note,
    Preference,
    Region,
    Segment,
)
from internship_agent.leads.sending import check_send
from internship_agent.leads.store import LeadStore, merge
from internship_agent.resume import load_resume_text
from internship_agent.sources import simplify, startups
from internship_agent.sources.application_form import fetch_questions
from internship_agent.sources.posting_text import fetch_posting_text
from internship_agent.sources.startup_jobs import find_intern_roles


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
    regions = {Region(r) for r in settings.search_regions}
    postings = simplify.matching(simplify.parse(simplify.fetch()), regions=regions)
    candidates = [simplify.to_lead(p) for p in postings]
    leads, added = refill(store.load(), candidates, target_open)
    store.save(leads)
    score(settings, added)
    return added


CHANNELS = ("news", "x", "linkedin")
XAI_BASE_URL = "https://api.x.ai/v1"


def _log_xai(settings: Settings, region: Region, usage: dict[str, int]) -> None:
    """Record each Grok call's token usage so spending on the xAI credit is visible."""
    log = settings.data_dir / "xai-usage.jsonl"
    log.parent.mkdir(parents=True, exist_ok=True)
    record = {"at": datetime.now(UTC).isoformat(), "region": region.value, **usage}
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def startup_postings(founder: Lead) -> list[Lead]:
    """Open intern/co-op roles on a startup's public job board, as posting leads."""
    leads: list[Lead] = []
    for role in find_intern_roles(founder.company, founder.company_url):
        leads.append(
            Lead(
                kind=LeadKind.POSTING,
                company=founder.company,
                company_url=founder.company_url,
                posting_title=role.title,
                posting_url=role.url,
                source_url=role.url,
                location=role.location,
                what_they_build=founder.what_they_build,
                segment=founder.segment,
                region=founder.region,
                contact_name=founder.contact_name,
                contact_role=founder.contact_role,
                x_handle=founder.x_handle,
                hiring_signals=[f"Open role on their {role.board} job board; raised recently"],
            )
        )
    return leads


def find_startups(
    settings: Settings,
    stages: list[Segment],
    count: int = 5,
    max_age_days: int = 60,
    regions: list[Region] | None = None,
    channels: tuple[str, ...] = CHANNELS,
    progress: Callable[[str], None] | None = None,
) -> list[Lead]:
    """Search every region x channel for recent raises, verify, check their job boards, score.

    Each pass excludes companies already known, so later passes surface new ones.
    """
    store = lead_store(settings)
    client = _openai(settings)
    xai = (
        OpenAI(api_key=settings.xai_api_key, base_url=XAI_BASE_URL)
        if settings.xai_api_key
        else None
    )
    xai_calls = 0
    today = date.today()
    start = today - timedelta(days=max_age_days)
    before = len(store.load())
    for region in regions or [Region(r) for r in settings.search_regions]:
        for channel in channels:
            existing = store.load()
            use_grok = (
                channel == "x" and xai is not None and xai_calls < settings.xai_max_calls_per_run
            )
            if use_grok:
                assert xai is not None
                xai_calls += 1
                tools = [
                    {"type": "x_search", "from_date": str(start), "to_date": str(today)},
                    {"type": "web_search"},
                ]
                pass_client, pass_model = xai, settings.xai_model
            else:
                tools, pass_client, pass_model = None, client, settings.openai_model
            findings, usage = search_startups(
                pass_client,
                pass_model,
                start,
                today,
                stages,
                region,
                channel,
                sorted({lead.company for lead in existing}),
                count,
                tools=tools,
            )
            if use_grok:
                _log_xai(settings, region, usage)
            found = startups.to_leads(findings, today, max_age_days, stages, region=region)
            leads, added = merge(existing, found)
            new_founders = leads[len(existing) :]
            roles = [p for f in new_founders for p in startup_postings(f)]
            leads, _ = merge(leads, roles)
            store.save(leads)
            if progress:
                progress(f"{region.value}/{channel}: +{added} startups, +{len(roles)} open roles")
    new = store.load()[before:]
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


def answer_bank(settings: Settings) -> AnswerBank:
    return AnswerBank(settings.data_dir / "answer-bank.json")


def prepare_application(settings: Settings, key: str) -> Lead:
    """Read the posting's application questions and prepare answers. Never submits anything."""
    store = lead_store(settings)
    lead = store.get(key)
    if lead.kind is LeadKind.POSTING and lead.posting_url and not lead.posting_text:
        lead.posting_text = fetch_posting_text(lead.posting_url)
    questions = fetch_questions(lead.posting_url) if lead.posting_url else []
    source = "form" if questions else "common"
    if not questions:
        questions = common_questions(lead.company)
    prepared = prefill(questions, answer_bank(settings))
    todo = [(i, p) for i, p in enumerate(prepared) if p.note == "ai"]
    if todo:
        listing = [
            (
                i,
                f"{p.question.label} (type: {p.question.kind.value}"
                + (f"; options: {' | '.join(p.question.options)}" if p.question.options else "")
                + ")",
            )
            for i, p in todo
        ]
        drafts = {
            d.index: d
            for d in prepare_answers(
                _openai(settings),
                settings.openai_writing_model,
                resume_text(settings),
                lead,
                listing,
            )
        }
        for i, item in todo:
            draft = drafts.get(i)
            cleaned = validate(item.question, draft.answer) if draft else None
            if draft is None or draft.needs_user_input or cleaned is None:
                item.answer, item.needs_user_input = "", True
                item.note = draft.note if draft and draft.note else "Fill this in yourself."
            else:
                item.answer, item.needs_user_input, item.note = cleaned, False, draft.note
    lead.application = ApplicationPrep(
        prepared_at=datetime.now(UTC), source=source, answers=prepared
    )
    store.upsert(lead)
    return lead


def save_answers(settings: Settings, key: str, edits: dict[int, str]) -> Lead:
    """Save edited answers. Personal answers the user fills in are remembered for next time."""
    store, bank = lead_store(settings), answer_bank(settings)
    lead = store.get(key)
    if lead.application is None:
        raise ValueError("Prepare answers first")
    for index, text in edits.items():
        if not 0 <= index < len(lead.application.answers):
            continue
        item = lead.application.answers[index]
        was_personal = item.needs_user_input or item.note == "From your saved answers."
        item.answer = text.strip()
        if item.answer:
            company_specific = normalize(lead.company) in normalize(item.question.label)
            reusable = "Optional; your choice." not in item.note and not company_specific
            if was_personal and reusable:
                bank.remember(item.question.label, item.answer)
            item.needs_user_input = False
    store.upsert(lead)
    return lead
