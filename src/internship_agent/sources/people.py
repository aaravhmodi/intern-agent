"""Turn web-search findings into people to connect with, keeping only sourced ones."""

import re
from collections.abc import Callable
from urllib.parse import urlsplit

from internship_agent.ai import PersonFinding
from internship_agent.leads.schemas import Person
from internship_agent.sources.startups import page_names

_PROFILE = re.compile(r"^https://(?:[a-z]{2,3}\.)?linkedin\.com/in/[^/?#\s]+/?$")


def _on_linkedin(url: str) -> bool:
    parts = urlsplit(url)
    host = parts.hostname or ""
    return parts.scheme == "https" and (host == "linkedin.com" or host.endswith(".linkedin.com"))


def source_names(company: str, finding: PersonFinding) -> bool:
    """True if the cited page names the company and the person.

    LinkedIn refuses scripts and is never fetched here, so a LinkedIn source passes unread:
    you see the profile yourself before sending anything.
    """
    return _on_linkedin(finding.source_url) or page_names(finding.source_url, company, finding.name)


def to_people(
    company: str,
    findings: list[PersonFinding],
    skip: str = "",
    confirm: Callable[[str, PersonFinding], bool] = source_names,
) -> list[Person]:
    """Distinct, sourced people with a full name, leaving out the lead's main contact."""
    seen = {skip.casefold()}
    people: list[Person] = []
    for f in findings:
        name = " ".join(f.name.split())
        if len(name.split()) < 2 or name.casefold() in seen or not confirm(company, f):
            continue
        seen.add(name.casefold())
        profile = f.linkedin_url if f.linkedin_url and _PROFILE.match(f.linkedin_url) else None
        people.append(
            Person(name=name, role=f.role.strip(), linkedin_url=profile, source_url=f.source_url)
        )
    return people
