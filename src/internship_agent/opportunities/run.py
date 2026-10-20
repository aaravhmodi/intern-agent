"""Opportunity workflows: refresh the feeds, search for events, plan submissions."""

import json
import re
from collections import Counter
from collections.abc import Callable
from datetime import date, timedelta
from pathlib import Path

from openai import OpenAI
from pydantic import TypeAdapter

from internship_agent.config import Settings
from internship_agent.leads.schemas import Region
from internship_agent.notify import Push
from internship_agent.opportunities import feeds
from internship_agent.opportunities.ai import search_events, write_strategy
from internship_agent.opportunities.schemas import (
    Opportunity,
    OpportunityKind,
    OpportunityStatus,
    SubmissionStrategy,
)
from internship_agent.opportunities.store import OpportunityStore
from internship_agent.resume import load_resume_text
from internship_agent.sources.regions import regions_of
from internship_agent.sources.startups import page_names

PLANNED = {OpportunityStatus.INTERESTED, OpportunityStatus.REGISTERED, OpportunityStatus.SUBMITTED}
# Web search inlines markdown citations, "([site](https://...))", into its prose.
_CITATION = re.compile(r"\s*\(\[[^\]]*\]\([^)\s]*\)\)")


def without_citations(strategy: SubmissionStrategy) -> SubmissionStrategy:
    """Drop inline citations from the prose; each track keeps its page in source_url."""
    return SubmissionStrategy.model_validate_json(_CITATION.sub("", strategy.model_dump_json()))


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


def plan_submission(settings: Settings, key: str) -> Opportunity:
    """Write a submission strategy from the venue's live call for papers."""
    store = OpportunityStore(settings)
    venue = store.get(key)
    path = settings.candidate_context_path
    context = path.read_text(encoding="utf-8") if path.exists() else ""
    resume = load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")
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
    added: list[Opportunity], everything: list[Opportunity], today: date, click: str | None
) -> Push | None:
    """New finds by kind, and deadlines in the next week for anything you planned to do."""
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
    if not added and not due:
        return None
    counts = Counter(o.kind.value for o in added)
    lines = [f"New: {', '.join(f'{n} {k}' for k, n in counts.items())}"] if added else []
    lines += [f"Due {o.deadline:%b %d}: {o.title} ({o.deadline_label})" for o in due]
    return Push(
        title="Opportunity agent",
        message="\n".join(lines),
        click=click,
        tags=["calendar"],
        priority=4 if due else 3,
    )
