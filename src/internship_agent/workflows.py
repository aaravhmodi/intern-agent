"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import json
import re
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from typing import Any

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
    PreparedAnswer,
    QuestionKind,
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


def _record_openai_usage(settings: Settings, operation: str, model: str, usage: Any) -> None:
    """Store token counts only, so scheduled AI spending can be audited."""
    path = settings.data_dir / "openai-usage.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    details = getattr(usage, "input_tokens_details", None)
    cached = getattr(details, "cached_tokens", 0) or 0
    record = {
        "at": datetime.now(UTC).isoformat(),
        "operation": operation,
        "model": model,
        "input_tokens": usage.input_tokens,
        "cached_input_tokens": cached,
        "output_tokens": usage.output_tokens,
    }
    if model == "gpt-6-luna":
        long_context = usage.input_tokens > 272_000
        record["estimated_usd"] = round(
            (
                (usage.input_tokens - cached) * (0.20 if long_context else 0.10)
                + cached * (0.02 if long_context else 0.01)
                + usage.output_tokens * (0.75 if long_context else 0.50)
            )
            / 1_000_000,
            8,
        )
    with path.open("a", encoding="utf-8") as log:
        log.write(json.dumps(record) + "\n")


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
        result = assess_fit(
            client,
            settings.openai_model,
            resume,
            lead,
            prefs,
            usage_callback=lambda usage: _record_openai_usage(
                settings, "score", settings.openai_model, usage
            ),
        )
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


def _use_gmail_for_applications(settings: Settings, answers: list[PreparedAnswer]) -> None:
    """Use the inbox that can receive verification codes for applicant email fields."""
    if not settings.gmail_ready or not settings.gmail_address:
        return
    answer_bank(settings).remember("Email", settings.gmail_address)
    for item in answers:
        if normalize(item.question.label) in {"email", "email address", "e mail", "e mail address"}:
            item.answer = settings.gmail_address
            item.needs_user_input = False
            item.note = "Configured application inbox."


def _retryable_block(application: ApplicationPrep | None) -> bool:
    return bool(
        application
        and application.submission_status == "blocked"
        and "after submit" not in application.submission_detail.lower()
    )


def _incompatible_term(lead: Lead) -> bool:
    """Reject postings that explicitly require a term outside January-April 2027."""
    text = f"{lead.posting_title} {lead.posting_text}"
    return bool(
        re.search(
            # "4 - 8 month" offers a 4-month term, so only a standalone 8 months is too long.
            r"(?<!4 - )(?<!4-)\b(?:8|eight)[\s-]*month\b|\b8\s*[-\u2013]\s*12\s*month\b|"
            r"\b12[\s-]*week\b|\bjanuary\s*[-\u2013]\s*(?:june|august)\s*2027\b|"
            r"\bjanuary\s*2027\s*(?:through|to|[-\u2013])\s*june\s*2027\b|"
            r"\b(?:summer|fall|autumn)\s*2027\b|"
            r"\b(?:spring|summer|fall|autumn|winter)"
            r"(?:\s*[/\-]\s*(?:spring|summer|fall|autumn|winter))?\s*2026\b",
            text,
            re.I,
        )
    )


def prepare_application(settings: Settings, key: str) -> Lead:
    """Prepare application materials without changing a prior submission outcome."""
    store = lead_store(settings)
    lead = store.get(key)
    prior_application = lead.application
    if lead.kind is LeadKind.POSTING and lead.posting_url and not lead.posting_text:
        lead.posting_text = fetch_posting_text(lead.posting_url)
    questions = fetch_questions(lead.posting_url) if lead.posting_url else []
    source = "form" if questions else "common"
    if not questions:
        questions = common_questions(lead.company)
    prepared = prefill(questions, answer_bank(settings))
    _use_gmail_for_applications(settings, prepared)
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
                usage_callback=lambda usage: _record_openai_usage(
                    settings, "answers", settings.openai_writing_model, usage
                ),
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
        client,
        settings.openai_writing_model,
        resume_text(settings),
        context,
        lead,
        usage_callback=lambda usage: _record_openai_usage(
            settings, "cover_letter", settings.openai_writing_model, usage
        ),
    )
    lead.application = ApplicationPrep(
        prepared_at=datetime.now(UTC),
        source=source,
        cover_letter=cover_letter,
        answers=prepared,
        submission_status=(
            prior_application.submission_status
            if prior_application
            and prior_application.submission_status
            in {"blocked", "failed", "uncertain", "skipped", "submitted"}
            and not _retryable_block(prior_application)
            else "pending"
        ),
        submission_detail=(
            prior_application.submission_detail
            if prior_application and not _retryable_block(prior_application)
            else ""
        ),
        submitted_at=prior_application.submitted_at if prior_application else None,
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
    if lead.application.submission_status not in {"uncertain", "submitted"}:
        lead.application.submission_status = "pending"
        lead.application.submission_detail = ""
    store.upsert(lead)
    return lead


def refresh_saved_application(settings: Settings, key: str) -> Lead:
    """Reuse prepared materials and fill blank answers from the verified answer bank."""
    store = lead_store(settings)
    lead = store.get(key)
    if lead.application is None:
        raise ValueError("Prepare application answers first")
    if lead.application.submission_status in {"submitted", "uncertain"}:
        return lead
    bank = answer_bank(settings)
    for item in lead.application.answers:
        if item.answer.strip():
            continue
        saved = bank.lookup(item.question)
        if saved is not None:
            item.answer = saved
            item.needs_user_input = False
            item.note = "From your saved answers."
    if _retryable_block(lead.application):
        lead.application.submission_status = "pending"
        lead.application.submission_detail = ""
    store.upsert(lead)
    return lead


def submit_application(
    settings: Settings, key: str, *, dry_run: bool = False, headless: bool = True
) -> Lead:
    """Submit one prepared application through a persistent, user-authenticated browser."""
    from internship_agent.applications.browser import apply_to_posting

    if not settings.auto_submit_applications and not dry_run:
        raise ValueError("Automatic application submission is disabled")
    store = lead_store(settings)
    lead = store.get(key)
    if lead.application is None:
        raise ValueError("Prepare application answers first")
    if lead.application.submission_status == "submitted":
        return lead
    if lead.application.submission_status == "uncertain":
        lead.application.submission_detail = (
            "A prior submit attempt may have reached the employer; verify on the application "
            "site before trying again."
        )
        store.upsert(lead)
        return lead
    _use_gmail_for_applications(settings, lead.application.answers)
    if _incompatible_term(lead):
        lead.application.submission_status = "skipped"
        lead.application.submission_detail = "Posting requires a term outside January-April 2027"
        store.upsert(lead)
        return lead
    transcript_questions = [
        answer.question.label
        for answer in lead.application.answers
        if answer.question.required and "transcript" in answer.question.label.lower()
    ]
    if transcript_questions:
        lead.application.submission_status = "skipped"
        lead.application.submission_detail = (
            "Automatic application skipped because a transcript is required"
        )
        store.upsert(lead)
        return lead
    unanswered = [
        answer.question.label
        for answer in lead.application.answers
        if answer.question.required
        and answer.question.kind is not QuestionKind.FILE
        and not answer.answer.strip()
    ]
    if unanswered:
        lead.application.submission_status = "blocked"
        lead.application.submission_detail = (
            f"Required answers need your input: {', '.join(unanswered[:5])}"
        )
        store.upsert(lead)
        return lead

    from internship_agent.applications.verification_mail import wait_for_greenhouse_code

    result = apply_to_posting(
        lead,
        settings.resume_path,
        settings.application_browser_dir,
        bank=answer_bank(settings),
        verification_code_provider=(
            lambda started: (
                wait_for_greenhouse_code(
                    settings.gmail_address or "",
                    settings.gmail_app_password.get_secret_value(),
                    started,
                company=lead.company,
                )
                if settings.gmail_ready and settings.gmail_app_password
                else None
            )
        ),
        dry_run=dry_run,
        headless=headless,
    )
    lead.application.submission_status = result.status
    lead.application.submission_detail = result.detail
    if result.status == "submitted":
        lead.application.submitted_at = datetime.now(UTC)
        lead.status = LeadStatus.APPLIED
    store.upsert(lead)
    return lead


@dataclass
class DailyReport:
    new: list[Lead]
    skipped: list[Lead]
    prepared: list[Lead]
    pushed: int
    submitted: int = 0
    application_blocked: int = 0
    attempted: int = 0
    estimated_ai_usd: float = 0.0


def _run_ai_cost(settings: Settings, started: datetime) -> float:
    """Add token-based Luna estimates for calls recorded during this run."""
    path = settings.data_dir / "openai-usage.jsonl"
    if not path.exists():
        return 0.0
    total = 0.0
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
            if datetime.fromisoformat(record["at"]) >= started:
                total += float(record.get("estimated_usd", 0))
        except (ValueError, KeyError, TypeError):
            continue
    return total


def scrape_jobs(settings: Settings, log: Callable[[str], None] = lambda _: None) -> list[Lead]:
    """Save every matching posting from the configured startup boards and Simplify feed."""
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
    return new


def daily(
    settings: Settings,
    log: Callable[[str], None] = lambda _: None,
    *,
    target_submissions: int | None = None,
    lowest_first: bool = False,
) -> DailyReport:
    """Find postings, prepare eligible applications, optionally submit, and report by ntfy."""
    if target_submissions is not None and target_submissions < 1:
        raise ValueError("target_submissions must be positive")
    started = datetime.now(UTC)
    new = scrape_jobs(settings, log)
    store = lead_store(settings)
    leads = store.load()
    unscored = [
        lead
        for lead in open_postings(leads)
        if lead.fit is None and not _incompatible_term(lead) and not is_workday(lead)
    ]
    if settings.auto_submit_applications:
        from internship_agent.applications.browser import _supported_url

        unscored = [
            lead for lead in unscored if lead.posting_url and _supported_url(lead.posting_url)
        ]
    log(f"Scoring {len(unscored)} new eligible posting(s)")
    skipped = score(settings, unscored)
    skipped_keys = {lead.key for lead in skipped}
    eligible = [
        lead
        for lead in open_postings(store.load())
        if lead.fit is not None and lead.key not in skipped_keys and not _incompatible_term(lead)
    ]
    if settings.auto_submit_applications:
        from internship_agent.applications.browser import _supported_url

        eligible = [
            lead for lead in eligible if lead.posting_url and _supported_url(lead.posting_url)
        ]
    eligible.sort(key=lambda lead: lead.fit.score if lead.fit else 0, reverse=not lowest_first)
    prepared: list[Lead] = []
    submitted = 0
    application_blocked = 0
    attempted = 0
    for lead in eligible:
        if target_submissions is not None and submitted >= target_submissions:
            break
        # A prior uncertain submit may have reached the employer. Never repeat it blindly.
        if lead.application and lead.application.submission_status == "uncertain":
            application_blocked += 1
            continue
        if lead.application and lead.application.submission_status == "skipped":
            application_blocked += 1
            continue
        try:
            if lead.application and lead.application.cover_letter:
                lead = refresh_saved_application(settings, lead.key)
            else:
                lead = prepare_application(settings, lead.key)
            prepared.append(lead)
        except Exception as error:
            log(f"{lead.key}: could not prepare answers ({type(error).__name__})")
            application_blocked += 1
            continue
        if not settings.auto_submit_applications:
            continue
        if lead.application and lead.application.submission_status != "pending":
            application_blocked += 1
            continue
        try:
            attempted += 1
            lead = submit_application(settings, lead.key)
            prepared[-1] = lead
        except Exception as error:
            log(f"{lead.key}: application submission failed ({type(error).__name__})")
            application_blocked += 1
            continue
        if lead.application and lead.application.submission_status == "submitted":
            submitted += 1
        elif lead.application and lead.application.submission_status != "ready":
            application_blocked += 1

    estimated_ai_usd = _run_ai_cost(settings, started)
    log(f"Estimated OpenAI cost this run: ${estimated_ai_usd:.4f}")
    pushed = 0
    if settings.ntfy_topic:
        pushes = [
            notify.summary_push(
                new,
                prepared,
                settings.dashboard_url,
                submitted,
                application_blocked,
                attempted=attempted,
                target=target_submissions,
                estimated_ai_usd=estimated_ai_usd,
            )
        ]
        if target_submissions is None:
            pushes += [notify.posting_push(lead) for lead in prepared]
        for push in pushes:
            try:
                notify.send(settings.ntfy_server, settings.ntfy_topic, push)
                pushed += 1
            except Exception as error:
                log(f"push failed: {error}")
    return DailyReport(
        new=new,
        skipped=skipped,
        prepared=prepared,
        pushed=pushed,
        submitted=submitted,
        application_blocked=application_blocked,
        attempted=attempted,
        estimated_ai_usd=estimated_ai_usd,
    )
