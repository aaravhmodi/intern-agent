"""Opportunity workflows: refresh the feeds, search for events, check them, plan submissions."""

import json
import re
from collections import Counter
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path

from openai import OpenAI
from pydantic import BaseModel, TypeAdapter

from internship_agent.config import Settings
from internship_agent.leads.schemas import Region
from internship_agent.notify import Push
from internship_agent.opportunities import feeds
from internship_agent.opportunities.ai import assess, search_events, write_strategy
from internship_agent.opportunities.schemas import (
    Opportunity,
    OpportunityAssessment,
    OpportunityKind,
    OpportunityStatus,
)
from internship_agent.opportunities.store import OpportunityStore
from internship_agent.resume import load_resume_text
from internship_agent.sources.regions import regions_of
from internship_agent.sources.startups import page_names

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


def worth_checking(items: list[Opportunity], today: date, limit: int) -> list[Opportunity]:
    """Unchecked upcoming events: in person before online (travel matters there), research
    venues last (their strategy covers them), soonest first."""
    todo = [
        o
        for o in items
        if o.assessment is None and o.status is not OpportunityStatus.SKIPPED and upcoming(o, today)
    ]
    todo.sort(key=lambda o: (o.kind is OpportunityKind.RESEARCH, o.online, next_date(o, today)))
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
        [o for o in items if o.key in set(keys)]
        if keys
        else worth_checking(items, date.today(), limit)
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
