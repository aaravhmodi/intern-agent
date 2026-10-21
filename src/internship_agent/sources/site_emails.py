"""Email addresses a startup publishes on its own website: a person's, or one for jobs.

Only addresses printed on the site count, never guesses, so they don't bounce the way a
guessed jobs@ would. Pages that don't load are skipped.
"""

import re
from urllib.parse import urlsplit

from internship_agent.sources.form_d import _fetch
from internship_agent.sources.startups import _fold

PAGES = ("", "careers", "jobs", "contact", "about", "team", "about-us", "company")
# Shared inboxes worth writing to about an internship, best first.
GENERIC = (
    "careers",
    "jobs",
    "talent",
    "recruiting",
    "hiring",
    "people",
    "founders",
    "team",
    "hello",
    "contact",
    "info",
)
# Inboxes that go to the wrong people for this, or nobody.
_SKIP = re.compile(
    r"support|help|sales|press|media|pr$|legal|privacy|abuse|security|billing|invoice|"
    r"no-?reply|donotreply|unsubscribe|partner|marketing|example|test|admin|webmaster",
    re.I,
)


def published(company_url: str, domain: str) -> dict[str, str]:
    """Every address at the company's domain on its main pages, with the page it was on."""
    host = urlsplit(company_url).hostname or domain
    root = f"https://{host}"
    found: dict[str, str] = {}
    for path in PAGES:
        url, page = _fetch(f"{root}/{path}")
        for address in re.findall(rf"[\w.+-]+@(?:[\w-]+\.)*{re.escape(domain)}\b", page, re.I):
            found.setdefault(address.lower().rstrip("."), url)
    return found


def personal(addresses: dict[str, str], name: str) -> tuple[str, str] | None:
    """An address with the person's first or last name in it, and the page showing it."""
    parts = [part for part in _fold(name).split() if len(part) > 2]  # "al" is in "sales"
    for address, url in addresses.items():
        local = address.split("@")[0]
        if any(part in local for part in parts) and not _SKIP.search(local):
            return address, url
    return None


def generic(addresses: dict[str, str]) -> tuple[str, str] | None:
    """The best shared inbox to ask about an internship, and the page showing it."""
    ranked = [
        (GENERIC.index(local), address, url)
        for address, url in addresses.items()
        if (local := address.split("@")[0]) in GENERIC
    ]
    if not ranked:
        return None
    _, address, url = min(ranked)
    return address, url
