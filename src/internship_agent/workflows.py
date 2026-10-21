"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import os
import random
import re
import time
from collections import Counter
from collections.abc import Callable, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from typing import Any
from zoneinfo import ZoneInfo

from openai import OpenAI

from internship_agent import db, mailer, notify
from internship_agent.ai import (
    STATUS_FROM_NOTE,
    TEAM_CONTACTS,
    assess_fit,
    interpret_note,
    prepare_answers,
    prepare_cover_letter,
    search_people,
    search_startups,
)
from internship_agent.config import Settings
from internship_agent.leads import patterns
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
    EmailStatus,
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
from internship_agent.leads.store import LeadStore, PostgresLeadStore, merge, open_lead_store
from internship_agent.resume import load_resume_text
from internship_agent.sources import form_d, simplify, site_emails, startups
from internship_agent.sources.application_form import fetch_questions
from internship_agent.sources.people import to_people
from internship_agent.sources.posting_text import fetch_posting_text
from internship_agent.sources.startup_jobs import find_intern_roles
from internship_agent.x_search import post_confirms, search_x_raises

BUSY_FOR = timedelta(hours=3)  # a marker older than this is from a job that died


@contextmanager
def busy(settings: Settings) -> Iterator[None]:
    """Mark a long job (sending email, a search) as running: a deploy waits until it ends."""
    marker = settings.data_dir / "busy" / str(os.getpid())
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.touch()
    try:
        yield
    finally:
        marker.unlink(missing_ok=True)


def is_busy(settings: Settings) -> bool:
    folder = settings.data_dir / "busy"
    cutoff = datetime.now(UTC).timestamp() - BUSY_FOR.total_seconds()
    return folder.exists() and any(m.stat().st_mtime > cutoff for m in folder.iterdir())


def lead_store(settings: Settings) -> LeadStore | PostgresLeadStore:
    return open_lead_store(settings.data_dir, settings.database_url)


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=settings.openai_api_key)


def _record_openai_usage(settings: Settings, operation: str, model: str, usage: Any) -> None:
    """Store token counts only, so scheduled AI spending can be audited."""
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
    db.append(settings, "openai-usage", record)


def resume_text(settings: Settings) -> str:
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")


def preference_store(settings: Settings) -> PreferenceStore:
    path = settings.data_dir / "preferences.json"
    return PreferenceStore(path, db.table(settings, "preferences"))


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
    record = {"at": datetime.now(UTC).isoformat(), "region": region.value, **usage}
    db.append(settings, "xai-usage", record)


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


def find_form_d_startups(
    settings: Settings,
    days: int = 3,
    log: Callable[[str], None] = lambda _: None,
    *,
    min_usd: int = 0,
) -> list[Lead]:
    """US tech startups that filed a Form D in the last few days, with a site and an email.

    Finding the website and email is free (likely domains are tried directly); only the
    usual fit score of each new lead uses OpenAI. min_usd skips smaller raises.
    """
    if not settings.gmail_address:
        raise ValueError("Set GMAIL_ADDRESS: the SEC asks for a contact address")
    store = lead_store(settings)
    known = {form_d.company_name(lead.company).lower() for lead in store.load()}
    new: list[Lead] = []
    for back in range(1, days + 1):
        day = date.today() - timedelta(days=back)
        filings = [
            f for f in form_d.filings(day, settings.gmail_address) if f.amount_usd >= min_usd
        ]
        log(f"{day}: {len(filings)} tech Form D filing(s)")
        found: list[Lead] = []
        for filing in filings:
            if filing.company.lower() in known:
                continue
            known.add(filing.company.lower())
            site = form_d.find_site(filing)
            if not site:
                log(f"{filing.company}: no website that names them")
                continue
            try:
                found.append(form_d.to_lead(filing, site))
            except ValueError as error:  # one odd site must not lose the whole run
                log(f"{filing.company}: skipped ({error})")
        # Saved day by day, so a long backfill keeps what it found if it stops partway.
        existing = store.load()
        leads, added = merge(existing, found)
        roles = [p for f in leads[len(existing) :] for p in startup_postings(f)]
        leads, _ = merge(leads, roles)
        store.save(leads)
        new += leads[len(existing) :]
        if found:
            log(f"+{added} startups, +{len(roles)} open roles")
    score(settings, new)
    return new


def sent_note(settings: Settings, to: str, sender: str | None, at: datetime) -> Note:
    """'Emailed jane@acme.ai from you@gmail.com on Oct 20 at 8:03 PM.' (local time)"""
    local = at.astimezone(ZoneInfo(settings.timezone))
    when = f"{local:%b} {local.day} at {local.hour % 12 or 12}:{local:%M} {local:%p}"
    return Note(
        at=at, text=f"Emailed {to}" + (f" from {sender}" if sender else "") + f" on {when}."
    )


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
    # New outreach goes from the outreach Gmail when one is set up, keeping bounces off
    # the main account.
    sender, password = settings.gmail_account("outreach")
    message = mailer.build_message(
        sender,
        to.strip(),
        subject,
        body,
        settings.resume_path if attach_resume else None,
    )
    mailer.send(message, sender, password)
    lead.sent_at = datetime.now(UTC)
    lead.sent_to = to.strip().lower()
    lead.sent_from = sender.lower() if sender != settings.gmail_address else None
    lead.status = LeadStatus.CONTACTED
    lead.notes.append(sent_note(settings, lead.sent_to, sender, lead.sent_at))
    store.upsert(lead)
    record = {
        "at": lead.sent_at.isoformat(),
        "key": key,
        "to": lead.sent_to,
        "from": sender.lower(),
        "subject": subject,
    }
    db.append(settings, "sent-log", record)
    return lead


_PITCH = """I'm a third-year Systems Design Engineering student at the University of \
Waterloo with 3 internships completed at CIBC and Upside Robotics ($7.5M USD seed). A few \
results:

- Upside Robotics: software engineer on backend systems, working 60+ hour weeks across \
multiple roles. Built the FastAPI backend and operations dashboard 35+ employees and \
executives use (metric retrieval from weeks to minutes), an ETL pipeline that cut warehouse \
load times by 80%, and cut robot-telemetry latency by 50%.
- CIBC: built a React-Django dashboard for 25+ projects and integrated ML anomaly detection \
that cut debugging time by 40%."""
_SIGN_OFF = "\n\nPortfolio: aaravmodi.ca\nAarav"
# The email Aarav approved on October 19, which Jeff Dunkel answered; everyone gets it,
# CEO, recruiter or engineer. {first} and {company} are filled in.
OUTREACH_SUBJECT = "15 min chat? Waterloo SWE intern, Winter 2027"
OUTREACH_BODY = (
    "Hi {first},\n\n" + _PITCH + "\n\nCould we do a 15-minute call so I can learn more about "
    "{company} and any opportunities for a Winter 2027 (Jan-Apr) internship?" + _SIGN_OFF
)
# Starts the note left on a CEO's lead once their company was searched for a team.
TEAM_SEARCHED = "Searched for a recruiter and a senior engineer"


def add_team_contacts(
    settings: Settings,
    min_usd: int = 15_000_000,
    limit: int | None = None,
    log: Callable[[str], None] = lambda _: None,
) -> list[Lead]:
    """At each big startup, find a recruiter and a senior engineer to email besides the CEO.

    Each becomes a lead of its own, so it is emailed, followed up and tracked like the CEO.
    One web search per company, never repeated: the CEO's lead gets a note saying so.
    """
    store = lead_store(settings)
    leads = store.load()
    staffed = Counter(lead.company for lead in leads if lead.kind is LeadKind.FOUNDER)
    big = [
        lead
        for lead in leads
        if lead.kind is LeadKind.FOUNDER
        and lead.status is not LeadStatus.SKIPPED
        and (lead.amount_usd or 0) >= min_usd
        and staffed[lead.company] == 1
        and patterns.role_of(lead) == "founder"
        and not any(note.text.startswith(TEAM_SEARCHED) for note in lead.notes)
    ]
    client = _openai(settings)
    added: list[Lead] = []
    for lead in big[:limit]:
        try:
            found = search_people(
                client, settings.openai_model, lead, None, count=2, who=TEAM_CONTACTS
            )
        except Exception as error:  # one failed search must not stop the rest
            log(f"{lead.company}: search failed ({type(error).__name__})")
            continue
        people = to_people(lead.company, found, skip=lead.contact_name or "")
        now = datetime.now(UTC)
        for person in people:
            added.append(
                Lead(
                    kind=LeadKind.FOUNDER,
                    company=lead.company,
                    company_url=lead.company_url,
                    what_they_build=lead.what_they_build,
                    location=lead.location,
                    source_url=person.source_url or lead.source_url,
                    contact_name=person.name,
                    contact_role=person.role,
                    linkedin_url=person.linkedin_url,
                    amount_usd=lead.amount_usd,
                    announced_on=lead.announced_on,
                    segment=lead.segment,
                    region=lead.region,
                    hiring_signals=lead.hiring_signals,
                    fit=lead.fit,
                    status=LeadStatus.SCORED if lead.fit else LeadStatus.NEW,
                    notes=[
                        Note(at=now, text=f"{person.role} at {lead.company}; emailed with the CEO.")
                    ],
                )
            )
        # Saved company by company, so a run cut short keeps who it found.
        existing = store.load()
        merged, _ = merge(existing, added[-len(people) :] if people else [])
        store.save(merged)
        names = ", ".join(f"{p.name} ({p.role})" for p in people) or "nobody confirmed"
        lead.notes.append(Note(at=now, text=f"{TEAM_SEARCHED}: {names}."))
        store.upsert(lead)
        log(f"{lead.company}: {names}")
    return added


def find_site_emails(
    settings: Settings, log: Callable[[str], None] = lambda _: None
) -> tuple[int, int]:
    """Look for addresses each startup publishes on its own site; no guessing, no AI.

    A person's own address replaces their guess. The company's best shared inbox
    (careers@, jobs@, hello@...) is kept as the fallback once guesses bounce.
    Returns (people given a published address, companies with a shared inbox).
    """
    store = lead_store(settings)
    by_domain: dict[str, list[Lead]] = {}
    for lead in store.load():
        if lead.kind is LeadKind.FOUNDER and lead.status is not LeadStatus.SKIPPED:
            if lead.company_url and (domain := patterns.domain_of(lead)):
                by_domain.setdefault(domain, []).append(lead)

    def scan(domain: str) -> dict[str, str]:
        return site_emails.published(by_domain[domain][0].company_url or "", domain)

    people = companies = 0
    with ThreadPoolExecutor(max_workers=8) as pool:
        for domain, found in zip(by_domain, pool.map(scan, by_domain), strict=True):
            shared = site_emails.generic(found)
            companies += shared is not None
            for stale in by_domain[domain]:
                lead = store.get(stale.key)  # fresh: the inbox check may have changed it
                mine = site_emails.personal(found, lead.contact_name or "")
                own = mine and lead.email_status is not EmailStatus.PUBLISHED
                if own and mine and mine[0] not in patterns.bounced_addresses(lead):
                    lead.email, lead.email_status, lead.email_source = (
                        mine[0],
                        EmailStatus.PUBLISHED,
                        mine[1],
                    )
                    people += 1
                elif not (shared and lead.company_email != shared[0]):
                    continue
                if shared:
                    lead.company_email = shared[0]
                    text = f"{shared[0]} is published on {shared[1]}."
                    lead.notes.append(Note(at=datetime.now(UTC), text=text))
                store.upsert(lead)
            log(f"{by_domain[domain][0].company}: {', '.join(found) or 'none published'}")
    return people, companies


def guess_and_send(
    settings: Settings,
    limit: int,
    *,
    send: bool = False,
    retries: bool = False,
    log: Callable[[str], None] = lambda _: None,
    pause_seconds: float = 20,
) -> list[tuple[Lead, str]]:
    """Email people never emailed, at the address format most likely to work.

    With `retries`, someone whose guess bounced (found by the inbox check) is also picked,
    with the next most likely format, up to three guesses each. A company gets one guess a
    day until one reaches someone there; then its format is known and its recruiter and
    engineer, who wait until then, are emailed with it. Dry run unless `send`.
    """
    store = lead_store(settings)
    leads = store.load()
    now = datetime.now(UTC)
    counts = patterns.outcomes(leads, now)
    known = patterns.by_domain(leads, now)
    log("Delivered/bounced so far: " + ", ".join(f"{f} {d}/{b}" for f, (d, b) in counts.items()))
    rng = random.Random(date.today().toordinal())  # same picks for a dry run and its send
    wanted = sorted(
        (lead for lead in leads if patterns.wants_email(lead, retries)),
        key=lambda lead: lead.fit.score if lead.fit else 0,
        reverse=True,
    )
    picked: list[tuple[Lead, str]] = []
    domains: set[str] = set()
    # A shared inbox (careers@...) is written to once, however many people point at it.
    emailed = {lead.sent_to for lead in leads if lead.sent_to}
    for lead in wanted:
        if len(picked) == limit:
            break
        domain = patterns.domain_of(lead)
        if not domain:
            continue
        at_domain = known.get(domain)
        proven = patterns.proven(at_domain)
        if patterns.role_of(lead) != "founder" and not proven:
            continue  # waits until the CEO's email shows the company's format
        if domain in domains and not proven:
            continue  # one unproven guess per company a day
        address = patterns.next_guess(lead, domain, counts, rng, at_domain)
        if address and address not in emailed:
            domains.add(domain)
            emailed.add(address)
            picked.append((lead, address))
    for lead, address in picked:
        role = patterns.role_of(lead)
        bounced = patterns.bounced_addresses(lead)
        retry = f" (retry; bounced: {', '.join(bounced)})" if bounced else ""
        log(f"{lead.company} [{role}] {lead.contact_name}: {address}{retry}")
        if not send:
            continue
        patterns.point_at(lead, address)
        store.upsert(lead)
        shared = address == lead.company_email
        first = f"{lead.company} team" if shared else (lead.contact_name or "there").split()[0]
        try:
            send_email(
                settings,
                lead.key,
                address,
                OUTREACH_SUBJECT,
                OUTREACH_BODY.format(first=first, company=lead.company),
                attach_resume=True,
                confirm_unverified=True,  # every address here is a guess, by design
                resend=True,
            )
        except Exception as error:  # one refused send must not stop the batch
            log(f"{lead.company}: not sent ({type(error).__name__}: {error})")
            continue
        time.sleep(pause_seconds)  # spread the batch out so Gmail doesn't flag it
    return picked


def inbox_send(
    settings: Settings,
    limit: int,
    *,
    send: bool = False,
    log: Callable[[str], None] = lambda _: None,
    pause_seconds: float = 20,
) -> list[Lead]:
    """Email the shared inbox each startup publishes, hiring ones (careers@) first.

    Each inbox becomes a lead of its own (the company's "team"), so its send, follow-ups
    and bounce are tracked without touching the CEO's own email. An inbox is written to
    once, and never at a company where someone already replied. Dry run unless `send`.
    """
    store = lead_store(settings)
    leads = store.load()
    emailed = {lead.sent_to for lead in leads if lead.sent_to}
    done = {lead.company for lead in leads if lead.replied_at or lead.status is LeadStatus.SKIPPED}
    best: dict[str, Lead] = {}
    for lead in leads:
        address = lead.company_email
        if lead.kind is not LeadKind.FOUNDER or not address or address in emailed:
            continue
        if lead.company not in done:
            best.setdefault(lead.company, lead)
    ranked = sorted(
        best.values(),
        key=lambda lead: (
            site_emails.GENERIC.index((lead.company_email or "").split("@")[0]),
            -(lead.fit.score if lead.fit else 0),
        ),
    )
    picked: list[Lead] = []
    for source in ranked[:limit]:
        inbox = Lead(
            kind=LeadKind.FOUNDER,
            company=source.company,
            company_url=source.company_url,
            what_they_build=source.what_they_build,
            location=source.location,
            source_url=source.source_url,
            contact_role="Company inbox",
            email=source.company_email,
            email_status=EmailStatus.PUBLISHED,
            email_source="Published on the company's own site",
            company_email=source.company_email,
            amount_usd=source.amount_usd,
            announced_on=source.announced_on,
            segment=source.segment,
            region=source.region,
            hiring_signals=source.hiring_signals,
            fit=source.fit,
            status=LeadStatus.SCORED if source.fit else LeadStatus.NEW,
        )
        assert inbox.email
        log(f"{inbox.company}: {inbox.email}")
        picked.append(inbox)
        if not send:
            continue
        store.upsert(inbox)
        try:
            send_email(
                settings,
                inbox.key,
                inbox.email,
                OUTREACH_SUBJECT,
                OUTREACH_BODY.format(first=f"{inbox.company} team", company=inbox.company),
                attach_resume=True,
                confirm_unverified=False,  # published on their site, not a guess
            )
        except Exception as error:  # one refused send must not stop the batch
            log(f"{inbox.company}: not sent ({type(error).__name__}: {error})")
            continue
        time.sleep(pause_seconds)  # spread the batch out so Gmail doesn't flag it
    return picked


def answer_bank(settings: Settings) -> AnswerBank:
    return AnswerBank(settings.data_dir / "answer-bank.json", db.table(settings, "answer_bank"))


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


# Questions a posting's own term answers (availability, duration, dates), not the answer bank.
_TERM_QUESTION = re.compile(
    r"availab|\bterm\b|duration|how long|\bmonths?\b|start date|end date|internship period",
    re.I,
)
_ACCEPT_TERM_NOTE = (
    "FOR THIS APPLICATION ONLY: the candidate has chosen to apply on this posting's own term "
    "and dates. Answer availability, duration and start/end-date questions to match the "
    "posting, and do not mention a four-month or January-April limit. This overrides any "
    "term or date preference stated above."
)


def prepare_application(settings: Settings, key: str, *, accept_posting_term: bool = False) -> Lead:
    """Prepare application materials without changing a prior submission outcome.

    accept_posting_term: you chose a posting outside January-April, so term questions and the
    cover letter follow the posting's dates instead of the saved four-month answers.
    """
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
    if accept_posting_term:
        context += f"\n\n{_ACCEPT_TERM_NOTE}"
        for index, item in enumerate(prepared):
            label = item.question.label
            if (
                item.note == "From your saved answers."
                and _TERM_QUESTION.search(label)
                and "interview" not in label.lower()
            ):
                prepared[index] = PreparedAnswer(
                    question=item.question, needs_user_input=True, note="ai"
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
    settings: Settings,
    key: str,
    *,
    dry_run: bool = False,
    headless: bool = True,
    accept_posting_term: bool = False,
) -> Lead:
    """Submit one prepared application through a persistent, user-authenticated browser.

    accept_posting_term skips the January-April check; only a job you picked by hand sets it.
    """
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
    if not accept_posting_term and _incompatible_term(lead):
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
        check_term=not accept_posting_term,
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
    total = 0.0
    for record in db.read_log(settings, "openai-usage"):
        try:
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
    skip_strong: bool = False,
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
    if skip_strong:
        eligible = [lead for lead in eligible if lead.fit and lead.fit.verdict != "strong"]
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
