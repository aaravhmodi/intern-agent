"""Learn which email format startups use from what bounced, and pick each founder's next guess.

Every format in emails.PATTERNS keeps a Beta estimate of how often it reaches someone,
built from past sends: a guess that bounced counts against its format, one with no bounce
a day later counts for it. Thompson sampling draws from each estimate and tries the best
draw, so the usual format is tried most while the others still get tested. A founder gets
one guess at a time, never a format that already bounced for them, and only at the domain
of their own company (never a made-up .ca or .com twin, which is somebody else's).
"""

import random
import re
from collections.abc import Iterator
from datetime import datetime, timedelta
from urllib.parse import urlsplit

from internship_agent.leads.emails import PATTERNS, guess_email
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, LeadStatus

# A send with no bounce after this long counts as delivered.
SETTLED = timedelta(days=1)
# How often each format is right at a small startup, as pseudo-sends out of 10.
# shortcut: guessed shares; real send outcomes outweigh them after a few dozen sends.
PRIOR = {
    "first": 5.5,
    "first.last": 2.5,
    "flast": 1.2,
    "firstlast": 0.5,
    "last": 0.3,
    "f.last": 0.3,
    "first_last": 0.2,
    "firstl": 0.2,
}
PRIOR_SENDS = 10
# Hosts that are not the company's own mail domain.
NOT_COMPANY = {
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com",
    "icloud.com",
    "linkedin.com",
    "x.com",
    "twitter.com",
    "github.com",
    "crunchbase.com",
    "ycombinator.com",
    "wellfound.com",
    "medium.com",
}
_RECRUITER = re.compile(r"recruit|talent|people partner|\bhr\b|human resources", re.I)
_ENGINEER = re.compile(r"engineer|developer|\bswe\b|programmer|technical staff", re.I)
_LEADER = re.compile(r"chief|\bcto\b|\bceo\b|found(?:er|ing)|\bvp\b|head|director", re.I)


def format_of(address: str, name: str) -> str | None:
    """Which format an address follows for this person, if any."""
    domain = address.rsplit("@", 1)[-1]
    for fmt in PATTERNS:
        try:
            if guess_email(name, domain, fmt) == address.lower():
                return fmt
        except ValueError:
            return None
    return None


def results(leads: list[Lead], now: datetime) -> Iterator[tuple[str, str, bool, bool]]:
    """(domain, format, delivered, settled) for every guess with a known result.

    A bounce comes back in minutes but a delivery only shows after a day: a send younger
    than that is yielded only if it bounced, and marked unsettled.
    """
    for lead in leads:
        if not lead.contact_name:
            continue
        for address in lead.bounced_emails:
            if fmt := format_of(address, lead.contact_name):
                yield address.rsplit("@", 1)[-1], fmt, False, True
        if not lead.sent_to or not lead.sent_at:
            continue
        settled = now - lead.sent_at >= SETTLED
        bounced = lead.followups_stopped == "bounced"
        if (settled or bounced) and (fmt := format_of(lead.sent_to, lead.contact_name)):
            yield lead.sent_to.rsplit("@", 1)[-1], fmt, not bounced, settled


def outcomes(leads: list[Lead], now: datetime) -> dict[str, list[int]]:
    """[delivered, bounced] per format, across every company.

    Only settled sends count: fresh bounces without the fresh deliveries beside them would
    make every format look worse than it is.
    """
    counts = {fmt: [0, 0] for fmt in PATTERNS}
    for _, fmt, delivered, settled in results(leads, now):
        if settled:
            counts[fmt][0 if delivered else 1] += 1
    return counts


def by_domain(leads: list[Lead], now: datetime) -> dict[str, dict[str, bool]]:
    """Per domain, each format tried there and whether it reached someone.

    A bounce counts at once: it already shows that format is wrong at that company.
    """
    known: dict[str, dict[str, bool]] = {}
    for domain, fmt, delivered, _ in results(leads, now):
        seen = known.setdefault(domain, {})
        seen[fmt] = seen.get(fmt, False) or delivered
    return known


def role_of(lead: Lead) -> str:
    """ "recruiter", "engineer" or "founder" (anyone else, e.g. a CEO or CTO), by title."""
    title = lead.contact_role or ""
    if _RECRUITER.search(title):
        return "recruiter"
    if _ENGINEER.search(title) and not _LEADER.search(title):
        return "engineer"
    return "founder"


def proven(at_domain: dict[str, bool] | None) -> bool:
    """Whether some format is known to reach people at this company."""
    return any((at_domain or {}).values())


def wants_email(lead: Lead) -> bool:
    """A founder never emailed, or whose last guess bounced and who has not replied."""
    if lead.kind is not LeadKind.FOUNDER or lead.status is LeadStatus.SKIPPED:
        return False
    if not lead.contact_name or lead.replied_at is not None:
        return False
    return lead.sent_at is None or lead.followups_stopped == "bounced"


def domain_of(lead: Lead) -> str | None:
    """The company's own mail domain: its known email's, else its website's."""
    hosts = [(lead.email or "").rsplit("@", 1)[-1], urlsplit(lead.company_url or "").hostname]
    for host in hosts:
        host = (host or "").lower().removeprefix("www.")
        if "." in host and host not in NOT_COMPANY:
            return host
    return None


def bounced_addresses(lead: Lead) -> list[str]:
    current = [lead.sent_to] if lead.followups_stopped == "bounced" and lead.sent_to else []
    return [*lead.bounced_emails, *current]


def next_guess(
    lead: Lead,
    domain: str,
    counts: dict[str, list[int]],
    rng: random.Random,
    at_domain: dict[str, bool] | None = None,
) -> str | None:
    """The address to try next for this person, or None once every format bounced.

    at_domain is what was learned at their company (by_domain): a format that reached
    someone there is used for everyone there, and one that bounced there is not tried.
    """
    bounced = bounced_addresses(lead)
    if lead.email_status is EmailStatus.PUBLISHED and lead.email and lead.email not in bounced:
        return lead.email
    name = lead.contact_name or ""
    tried = {format_of(address, name) for address in bounced}
    at_domain = at_domain or {}
    options = [f for f in PATTERNS if f not in tried and at_domain.get(f) is not False]
    options = [f for f in options if at_domain.get(f)] or options
    if not options:
        return None

    def draw(fmt: str) -> float:
        delivered, bounces = counts[fmt]
        prior = PRIOR.get(fmt, 0.2)
        return rng.betavariate(prior + delivered, PRIOR_SENDS - prior + bounces)

    try:
        return guess_email(name, domain, max(options, key=draw))
    except ValueError:  # no first and last name to build an address from
        return None


def point_at(lead: Lead, address: str) -> None:
    """Make the lead's email this guess, keeping a bounced earlier one so it is not retried."""
    if lead.followups_stopped == "bounced" and lead.sent_to:
        lead.bounced_emails.append(lead.sent_to)
        lead.sent_at = lead.sent_to = lead.sent_from = None
        lead.followups = []
        lead.followups_stopped = ""
    if address != lead.email or lead.email_status is not EmailStatus.PUBLISHED:
        fmt = format_of(address, lead.contact_name or "") or "unknown"
        lead.email = address
        lead.email_status = EmailStatus.PATTERN
        lead.email_source = f"Guessed {fmt}@ format, learned from bounces; unverified"
