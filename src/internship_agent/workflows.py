"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import json
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta

from openai import OpenAI

from internship_agent import mailer, notify
from internship_agent.ai import (
    STATUS_FROM_NOTE,
    assess_fit,
    interpret_note,
    prepare_answers,
    prepare_cover_letter,
    search_people,
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
from internship_agent.leads.refill import DONE, is_workday, open_postings, refill
from internship_agent.leads.schemas import (
    ApplicationPrep,
    Lead,
    LeadKind,
    LeadStatus,
    Note,
    Person,
    Preference,
    Region,
    Segment,
)
from internship_agent.leads.segments import effective_segment
from internship_agent.leads.sending import check_outreach_text, check_send
from internship_agent.leads.store import LeadStore, merge
from internship_agent.resume import load_resume_text
from internship_agent.sources import simplify, startups
from internship_agent.sources.application_form import fetch_questions
from internship_agent.sources.people import to_people
from internship_agent.sources.posting_text import fetch_posting_text
from internship_agent.sources.startup_jobs import find_intern_roles
from internship_agent.x_search import post_confirms, search_x_raises


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
                people=founder.people,
                hiring_signals=[f"Open role on their {role.board} job board; raised recently"],
            )
        )
    return leads


def find_people(settings: Settings, key: str) -> Lead:
    """Look up more people at the lead's company to connect with on LinkedIn, and store them.

    A search that confirms nobody keeps the people already stored.
    """
    store = lead_store(settings)
    lead = store.get(key)
    found = search_people(_openai(settings), settings.openai_model, lead, effective_segment(lead))
    lead.people = to_people(lead.company, found, skip=lead.contact_name) or lead.people
    store.upsert(lead)
    return lead


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
            known = sorted({lead.company for lead in existing})
            use_grok = (
                channel == "x" and xai is not None and xai_calls < settings.xai_max_calls_per_run
            )
            if use_grok:
                # Founders' own posts on X announcing a raise, kept only when the post
                # exists and says so. Without an xAI key the X channel is a web
                # search for the same thing, which finds far less.
                assert xai is not None
                xai_calls += 1
                findings, usage = search_x_raises(
                    xai, settings.xai_model, start, today, stages, region, known, count
                )
                _log_xai(settings, region, usage)
                found = startups.to_leads(
                    findings,
                    today,
                    max_age_days,
                    stages,
                    confirm=post_confirms,
                    region=region,
                    require_founder=False,
                )
            else:
                findings, _ = search_startups(
                    client,
                    settings.openai_model,
                    start,
                    today,
                    stages,
                    region,
                    channel,
                    known,
                    count,
                )
                found = startups.to_leads(findings, today, max_age_days, stages, region=region)
            leads, added = merge(existing, found)
            new_founders = leads[len(existing) :]
            roles = [p for f in new_founders for p in startup_postings(f)]
            leads, _ = merge(leads, roles)
            store.save(leads)
            if progress:
                progress(f"{region.value}/{channel}: +{added} startups, +{len(roles)} open roles")
    new = store.load()[before:]

    def people_at(founder: Lead) -> list[Person]:
        try:
            found = search_people(
                client, settings.openai_model, founder, effective_segment(founder)
            )
            return to_people(founder.company, found, skip=founder.contact_name)
        except Exception as error:  # the startup is still worth keeping without them
            if progress:
                progress(f"{founder.company}: no people found: {error}")
            return []

    # Each lookup is a web search of up to two minutes, so they run side by side; more than
    # two at once runs into the OpenAI tokens-per-minute limit.
    founders = [lead for lead in new if lead.kind is LeadKind.FOUNDER]
    with ThreadPoolExecutor(max_workers=2) as pool:
        people = dict(
            zip((f.company for f in founders), pool.map(people_at, founders), strict=True)
        )
    for lead in new:
        lead.people = people.get(lead.company, [])
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
    check_outreach_text(subject, body)
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
    context = (
        settings.candidate_context_path.read_text(encoding="utf-8")
        if settings.candidate_context_path.exists()
        else ""
    )
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
                context,
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
    client = _openai(settings)
    cover_letter = prepare_cover_letter(
        client, settings.openai_writing_model, resume_text(settings), context, lead
    )
    lead.application = ApplicationPrep(
        prepared_at=datetime.now(UTC),
        source=source,
        cover_letter=cover_letter,
        answers=prepared,
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


@dataclass
class DailyReport:
    new: list[Lead]
    skipped: list[Lead]
    prepared: list[Lead]
    pushed: int
    submitted: int = 0


def daily(settings: Settings, log: Callable[[str], None] = lambda _: None) -> DailyReport:
    """Find postings, prepare open non-Workday applications, and report by ntfy.

    Submission remains a manual action; this workflow only drafts application materials.
    """
    store = lead_store(settings)
    leads = store.load()
    founders = [lead for lead in leads if lead.kind is LeadKind.FOUNDER and lead.status not in DONE]
    candidates: list[Lead] = []
    for founder in founders:
        try:
            candidates.extend(startup_postings(founder))
        except Exception as error:  # one broken job board must not stop the run
            log(f"{founder.company}: {error}")
    log(f"{len(candidates)} startup job-board role(s) across {len(founders)} startup(s)")
    regions = {Region(r) for r in settings.search_regions}
    simplify_postings = simplify.matching(simplify.parse(simplify.fetch()), regions=regions)
    candidates.extend(simplify.to_lead(p) for p in simplify_postings)

    candidates = [lead for lead in candidates if not is_workday(lead)]
    # Store every eligible job surfaced today; the daily preparation pass covers the whole
    # open database rather than stopping at the old small "top N" cap.
    target = len(open_postings(leads)) + len(candidates)
    leads, new = refill(leads, candidates, target)
    store.save(leads)
    log(f"{len(new)} new posting(s)")
    skipped = score(settings, open_postings(leads))
    skipped_keys = {lead.key for lead in skipped}
    eligible = [
        lead
        for lead in open_postings(store.load())
        if lead.fit is not None and lead.key not in skipped_keys
    ]
    eligible.sort(key=lambda lead: -(lead.fit.score if lead.fit else 0))
    prepared: list[Lead] = []
    for lead in eligible:
        try:
            prepared.append(prepare_application(settings, lead.key))
        except Exception as error:
            log(f"{lead.key}: could not prepare answers: {error}")

    pushed = 0
    if settings.ntfy_topic:
        pushes = [notify.summary_push(new, prepared, settings.dashboard_url)]
        pushes += [notify.posting_push(lead) for lead in prepared]
        for push in pushes:
            try:
                notify.send(settings.ntfy_server, settings.ntfy_topic, push)
                pushed += 1
            except Exception as error:
                log(f"push failed: {error}")
    return DailyReport(new=new, skipped=skipped, prepared=prepared, pushed=pushed, submitted=0)
