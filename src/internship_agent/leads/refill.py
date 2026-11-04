"""Keep a target number of open postings: once you apply, new ones take their place."""

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, date, datetime

from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus, Note
from internship_agent.leads.store import merge, normalize_url

DONE = {LeadStatus.APPLIED, LeadStatus.CONTACTED, LeadStatus.SKIPPED}


def is_workday(lead: Lead) -> bool:
    """Workday-hosted application forms are intentionally left for manual handling."""
    url = (lead.posting_url or "").lower()
    return "myworkdayjobs.com" in url or "workday.com" in url


def open_postings(leads: list[Lead]) -> list[Lead]:
    return [
        lead
        for lead in leads
        if lead.kind is LeadKind.POSTING and lead.status not in DONE and not is_workday(lead)
    ]


def refill(
    leads: list[Lead], candidates: list[Lead], target_open: int
) -> tuple[list[Lead], list[Lead]]:
    """Add candidates (in order) until there are `target_open` open postings.

    Candidates already present (same key or posting URL), including ones you applied to or
    skipped, are never re-added. Returns (all leads, newly added leads).
    """
    candidates = [candidate for candidate in candidates if not is_workday(candidate)]
    # A posting saved before its source's date was read gets it when a source lists it again.
    posted = {
        normalize_url(c.posting_url): c.posted_on
        for c in candidates
        if c.posting_url and c.posted_on
    }
    for lead in leads:
        if lead.posting_url and not lead.posted_on:
            lead.posted_on = posted.get(normalize_url(lead.posting_url))
    needed = target_open - len(open_postings(leads))
    if needed <= 0:
        return leads, []
    added: list[Lead] = []
    for candidate in candidates:
        if len(added) == needed:
            break
        merged, count = merge([*leads, *added], [candidate])
        if count:
            added.append(merged[-1])
    for lead in added:  # no date from the source: the day it was found is the closest known
        lead.posted_on = lead.posted_on or date.today()
    return [*leads, *added], added


def expire_postings(leads: list[Lead], today: date) -> list[Lead]:
    """Skip open postings past their deadline, with a note. Skipped, not deleted, so the next
    scrape does not find and add them again."""
    expired = [
        lead
        for lead in open_postings(leads)
        if lead.deadline is not None and lead.deadline < today and lead.sent_at is None
    ]
    for lead in expired:
        lead.status = LeadStatus.SKIPPED
        lead.notes.append(
            Note(at=datetime.now(UTC), text=f"Expired: the deadline was {lead.deadline:%b %d, %Y}.")
        )
    return expired


def drop_unavailable(leads: list[Lead]) -> list[Lead]:
    """Skip open postings whose application came back skipped (closed, wrong term) or blocked
    (CAPTCHA, form errors), with the reason as a note. A missing resume is a setup problem, not
    the posting's, so it stays."""
    dropped = [
        lead
        for lead in open_postings(leads)
        if lead.application
        and lead.application.submission_status in ("skipped", "blocked")
        and "resume" not in lead.application.submission_detail.lower()
    ]
    for lead in dropped:
        assert lead.application
        lead.status = LeadStatus.SKIPPED
        lead.notes.append(
            Note(at=datetime.now(UTC), text=f"Removed: {lead.application.submission_detail}")
        )
    return dropped


def expire_closed(leads: list[Lead], is_gone: Callable[[str], bool]) -> list[Lead]:
    """Skip every open posting whose page says the role is gone, with a note. Skipped, not
    deleted, so the next scrape does not add it again."""
    checked = [lead for lead in open_postings(leads) if lead.posting_url]
    with ThreadPoolExecutor(8) as pool:  # one page fetch each; a few hundred a night
        gone = list(pool.map(lambda lead: is_gone(lead.posting_url or ""), checked))
    closed = [lead for lead, is_closed in zip(checked, gone, strict=True) if is_closed]
    for lead in closed:
        lead.status = LeadStatus.SKIPPED
        lead.notes.append(Note(at=datetime.now(UTC), text="Closed: the posting is no longer live."))
    return closed
