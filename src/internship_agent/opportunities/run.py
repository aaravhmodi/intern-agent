"""Opportunity workflows: refresh the feeds, search for events, check them, plan submissions."""

import json
import re
from collections import Counter
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any

from openai import OpenAI
from pydantic import BaseModel, TypeAdapter

from internship_agent.config import Settings
from internship_agent.leads.schemas import Region
from internship_agent.leads.store import normalize_url
from internship_agent.notify import Push
from internship_agent.opportunities import apply, feeds
from internship_agent.opportunities.ai import (
    APPLY_INSTRUCTIONS,
    assess,
    next_step,
    search_events,
    write_strategy,
)
from internship_agent.opportunities.apply import Snapshot, describe
from internship_agent.opportunities.schemas import (
    BrowserStep,
    EventApplication,
    Opportunity,
    OpportunityAssessment,
    OpportunityKind,
    OpportunityStatus,
)
from internship_agent.opportunities.store import OpportunityStore
from internship_agent.resume import load_resume_text
from internship_agent.sources.regions import regions_of
from internship_agent.sources.startups import page_names
from internship_agent.workflows import answer_bank

PLANNED = {OpportunityStatus.INTERESTED, OpportunityStatus.REGISTERED, OpportunityStatus.SUBMITTED}
# Web search inlines markdown citations, "([site](https://...))", into its prose.
_CITATION = re.compile(r"\s*\(\[[^\]]*\]\([^)\s]*\)\)")


def without_citations[M: BaseModel](found: M) -> M:
    """Drop inline citations from the prose; the source pages are kept in their own fields."""
    return type(found).model_validate_json(_CITATION.sub("", found.model_dump_json()))


def upcoming(item: Opportunity, today: date) -> bool:
    last = item.ends_on or item.starts_on or item.deadline
    return last is None or last >= today


def next_date(item: Opportunity, today: date) -> date:
    """The deadline while it is still open, else the start: what to sort and act on."""
    if item.deadline and item.deadline >= today:
        return item.deadline
    return item.starts_on or date.max


def nearby(item: Opportunity, regions: set[Region], cities: list[str]) -> bool:
    """Online, a research venue (you submit from anywhere), or somewhere you can get to."""
    if item.online or item.kind is OpportunityKind.RESEARCH:
        return True
    place = item.location.lower()
    return bool(regions_of(item.location) & regions) or any(c.lower() in place for c in cities)


def keep(found: list[Opportunity], settings: Settings, today: date) -> list[Opportunity]:
    regions = {Region(r) for r in settings.search_regions}
    return [o for o in found if upcoming(o, today) and nearby(o, regions, settings.event_cities)]


def refresh(
    settings: Settings, today: date | None = None, log: Callable[[str], None] = lambda _: None
) -> list[Opportunity]:
    """Pull every feed and store new upcoming, nearby events. Returns what was added."""
    today = today or date.today()
    collectors: dict[str, Callable[[], list[Opportunity]]] = {
        "devpost": feeds.collect_devpost,
        "mlh": lambda: feeds.collect_mlh(today),
        "confs.tech": lambda: feeds.collect_confs_tech(today, settings.conference_topics),
        "ccfddl": lambda: feeds.collect_ccfddl(today, settings.research_areas),
    }
    found: list[Opportunity] = []
    for name, collect in collectors.items():
        try:  # one feed changing its format must not lose the others
            items = collect()
        except Exception as error:
            log(f"{name}: failed: {error}")
            continue
        log(f"{name}: {len(items)} listed")
        found += items
    added = OpportunityStore(settings).add_new(keep(found, settings, today))
    log(f"Added {len(added)} new opportunities")
    return added


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=settings.openai_api_key)


def find_events(settings: Settings, days: int = 60, count: int = 10) -> list[Opportunity]:
    """Web search for networking events; keep only dated ones whose page names them."""
    store, today = OpportunityStore(settings), date.today()
    end = today + timedelta(days=days)
    known = [o.title for o in store.load() if o.kind is OpportunityKind.NETWORKING]
    findings = search_events(
        _openai(settings),
        settings.openai_model,
        settings.event_cities,
        today,
        end,
        known[-60:],
        count,
    )
    found = [
        Opportunity(
            kind=OpportunityKind(f.kind),
            title=f.title,
            url=f.url,
            source="web search",
            starts_on=f.starts_on,
            location=f.location,
            details=f"{f.organizer}: {f.why}" if f.organizer else f.why,
        )
        for f in findings
        if today <= f.starts_on <= end
        and f.url.startswith(("https://", "http://"))
        # The page must name the event (first and last word of its title): no invented links.
        and page_names(f.url, f.title, f.title)
    ]
    return store.add_new(keep(found, settings, today))


def _candidate(settings: Settings) -> tuple[str, str]:
    """The resume and the candidate context the AI matches events against."""
    path = settings.candidate_context_path
    context = path.read_text(encoding="utf-8") if path.exists() else ""
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt"), context


def checked(
    client: OpenAI, settings: Settings, resume: str, context: str, event: Opportunity
) -> OpportunityAssessment:
    """Assess one event from its own pages; travel support counts only if a page confirms it."""
    found = without_citations(
        assess(client, settings.openai_model, resume, context, event, date.today())
    )
    found.fit_score = max(0, min(100, found.fit_score))
    # The cited page must load and name the event (its title's first word, passed twice).
    first_word = event.title.split()[0]
    if found.travel in ("covered", "partial") and not page_names(
        found.travel_source_url, first_word, first_word
    ):
        found.travel = "unknown"
        found.travel_details = f"Not confirmed on the event's pages: {found.travel_details}"
    return found


# Which unchecked events to check first. Student hackathons are where travel is paid (MLH
# reimbursements, buses); research venues last, since their strategy covers them.
_CHECK_ORDER = {
    OpportunityKind.HACKATHON: 0,
    OpportunityKind.NETWORKING: 1,
    OpportunityKind.CONFERENCE: 2,
    OpportunityKind.RESEARCH: 3,
}


def worth_checking(
    items: list[Opportunity], today: date, limit: int, cities: list[str]
) -> list[Opportunity]:
    """Unchecked upcoming events by kind, then in Canada or your cities before elsewhere,
    in person before online, soonest first."""
    todo = [
        o
        for o in items
        if o.assessment is None and o.status is not OpportunityStatus.SKIPPED and upcoming(o, today)
    ]
    todo.sort(
        key=lambda o: (
            _CHECK_ORDER[o.kind],
            not nearby(o, {Region.CANADA}, cities) or o.online,
            o.online,
            next_date(o, today),
        )
    )
    return todo[:limit]


def check_events(
    settings: Settings,
    keys: list[str] | None = None,
    limit: int = 5,
    log: Callable[[str], None] = lambda _: None,
) -> list[Opportunity]:
    """Assess the given events, or the `limit` most worth checking. Returns those assessed."""
    store, client = OpportunityStore(settings), _openai(settings)
    items = store.load()
    todo = (
        [o for o in items if o.key in _keys(keys)]
        if keys
        else worth_checking(items, date.today(), limit, settings.event_cities)
    )
    resume, context = _candidate(settings)

    def one(event: Opportunity) -> OpportunityAssessment | None:
        try:
            return checked(client, settings, resume, context, event)
        except Exception as error:  # the others are still worth checking
            log(f"{event.title}: check failed: {error}")
            return None

    # Each check is a web search; two at a time stays under the tokens-per-minute limit.
    done = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(one, event): event for event in todo}
        # Each is saved as soon as it finishes, so a restart mid-run (a deploy) keeps the
        # checks already paid for; saving happens on this thread only, never two at once.
        for future in as_completed(futures):
            if (result := future.result()) is not None:
                event = futures[future]
                event.assessment = result
                store.upsert(event)
                done.append(event)
    return done


APPLIABLE = {OpportunityKind.HACKATHON, OpportunityKind.NETWORKING}


def _keys(urls: list[str]) -> set[str]:
    """Event URLs as typed (a trailing slash, tracking parameters) in their stored key form."""
    return {normalize_url(u) for u in urls}


def to_apply(items: list[Opportunity], today: date) -> list[Opportunity]:
    """Hackathons and events you marked Interested, never tried, still open and not started."""
    return [
        o
        for o in items
        if o.kind in APPLIABLE
        and o.status is OpportunityStatus.INTERESTED
        and o.application is None
        and (o.starts_on is None or o.starts_on >= today)
        and not (o.assessment and o.assessment.apply_by and o.assessment.apply_by < today)
    ]


def proof_path(settings: Settings, key: str) -> Path:
    """Screenshot of an event's confirmation page."""
    name = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")[:120]
    return settings.application_browser_dir / "event-confirmations" / f"{name}.png"


def apply_events(
    settings: Settings,
    keys: list[str] | None = None,
    *,
    dry_run: bool = False,
    log: Callable[[str], None] = lambda _: None,
    page_factory: Callable[[], Any] | None = None,
) -> list[Opportunity]:
    """Apply or RSVP in the saved browser: the given events, or every one due to_apply.

    Each result is saved as soon as it is known; an uncertain or failed attempt is never
    retried on its own (the dashboard can reopen it).
    """
    store = OpportunityStore(settings)
    items = store.load()
    todo = (
        [o for o in items if o.key in _keys(keys) and o.kind in APPLIABLE]
        if keys
        else to_apply(items, date.today())
    )
    if not todo:
        return []
    client = _openai(settings)
    resume, context = _candidate(settings)
    bank = answer_bank(settings).load()
    done = []
    from internship_agent.opportunities.browser import saved_browser

    open_page = page_factory or (lambda: saved_browser(settings.application_browser_dir))
    with open_page() as page:
        for event in todo:
            instructions = APPLY_INSTRUCTIONS.format(
                event=event.model_dump_json(
                    include={"kind", "title", "url", "starts_on", "ends_on", "location", "online"}
                ),
                bank="\n".join(f"- {q}" for q in sorted(bank)),
                context=context,
                resume=resume,
            )

            def step(
                snapshot: Snapshot, history: list[str], text: str = instructions
            ) -> BrowserStep:
                return next_step(client, settings.openai_model, text, describe(snapshot), history)

            try:
                result = apply.run(
                    page,
                    event,
                    bank,
                    step,
                    settings.resume_path,
                    proof_path(settings, event.key),
                    dry_run=dry_run,
                )
            except Exception as error:  # browser messages can hold form values: keep it generic
                log(f"{event.title}: failed ({type(error).__name__})")
                result = EventApplication(
                    status="failed",
                    detail=f"Browser automation failed ({type(error).__name__})",
                    at=datetime.now(UTC),
                )
            if dry_run:
                log(f"{event.title}: {result.detail}")
                continue
            event.application = result
            if result.status == "submitted":
                event.status = OpportunityStatus.SUBMITTED
            store.upsert(event)
            log(f"{event.title}: {result.status}: {result.detail}")
            done.append(event)
    return done


def plan_submission(settings: Settings, key: str) -> Opportunity:
    """Write a submission strategy from the venue's live call for papers."""
    store = OpportunityStore(settings)
    venue = store.get(key)
    resume, context = _candidate(settings)
    strategy = without_citations(
        write_strategy(
            _openai(settings), settings.openai_model, resume, context, venue, date.today()
        )
    )
    # A track is kept only if its cited page loads and names the venue.
    strategy.tracks = [
        t for t in strategy.tracks if page_names(t.source_url, venue.title, venue.title)
    ]
    venue.strategy = strategy
    store.upsert(venue)
    return venue


def import_inbox(settings: Settings, path: Path) -> list[Opportunity]:
    """Add events found by hand or by the /find-opportunities command."""
    found = TypeAdapter(list[Opportunity]).validate_python(
        json.loads(path.read_text(encoding="utf-8"))
    )
    return OpportunityStore(settings).add_new(keep(found, settings, date.today()))


def applied_push(tried: list[Opportunity], click: str | None) -> Push:
    """What the morning's event applications did: applied, and what needs you."""
    lines = []
    for o in tried:
        a = o.application
        if a is None:
            continue
        mark = (
            "✓ Applied"
            if a.status == "submitted"
            else "Needs you"
            if a.status == "needs_you"
            else "Not applied"
        )
        lines.append(
            f"{mark}: {o.title}" + ("" if a.status == "submitted" else f" ({a.detail[:90]})")
        )
    return Push(
        title="Event applications",
        message="\n".join(lines) or "Nothing tried",
        click=click,
        tags=["ticket"],
    )


def summary_push(
    added: list[Opportunity],
    everything: list[Opportunity],
    today: date,
    click: str | None,
    assessed: list[Opportunity] | None = None,
) -> Push | None:
    """New finds by kind, newly found trips with travel paid, and deadlines in the next week
    for anything you planned to do."""
    trips = [
        f"{'Travel paid' if a.travel == 'covered' else 'Travel help'}: {o.title}"
        f" ({o.starts_on or 'date?'}, {a.location or o.location})"
        for o in assessed or []
        if (a := o.assessment) and a.travel in ("covered", "partial")
    ]
    due = sorted(
        (
            o
            for o in everything
            if o.status in PLANNED
            and o.deadline
            and today <= o.deadline <= today + timedelta(days=7)
        ),
        key=lambda o: o.deadline or today,
    )
    if not added and not due and not trips:
        return None
    counts = Counter(o.kind.value for o in added)
    lines = [f"New: {', '.join(f'{n} {k}' for k, n in counts.items())}"] if added else []
    lines += trips
    lines += [f"Due {o.deadline:%b %d}: {o.title} ({o.deadline_label})" for o in due]
    return Push(
        title="Opportunity agent",
        message="\n".join(lines),
        click=click,
        tags=["calendar"],
        priority=4 if due else 3,
    )
