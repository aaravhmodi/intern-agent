"""2nd and 3rd degree LinkedIn connections at a company, read from the server's signed-in browser.

Sign in to LinkedIn in the same `browser` service the Discord scrape uses (noVNC at
http://<TAILSCALE_IP>:6081/vnc.html). The lookup runs LinkedIn's own people search, filtered to
your 2nd and 3rd+ degree network, in a tab of its own and only reads the first page of results:
it never clicks Connect, Message or Follow. LinkedIn watches for automated browsing, so lookups
are spaced out and capped per run (see `find_network` in workflows).
"""

import json
import re
from typing import Any
from urllib.parse import urlencode, urlsplit

from pydantic import ValidationError

from internship_agent.leads.contacts import company_key
from internship_agent.leads.schemas import NetworkPerson

SEARCH = "https://www.linkedin.com/search/results/people/"
# LinkedIn's network filter: F is 1st degree, S 2nd, O 3rd and beyond.
NETWORK = ["S", "O"]
_DEGREE = re.compile(r"\b(2nd|3rd\+?)\b")
_MUTUAL = re.compile(r"mutual connection", re.I)
# Lines in a result card that are buttons or screen-reader labels, not facts about the person.
_NOISE = re.compile(
    r"^(?:view .+ profile|connect|message|follow|pending|•.*|\d(?:st|nd|rd)\+? degree connection"
    r"|status is \w+)$",
    re.I,
)
# Every result card on the page: its text and the first profile link in it.
_CARDS = """els => els.map(e => ({
  text: e.innerText,
  href: [...e.querySelectorAll('a[href*="/in/"]')].map(a => a.href)[0] || '',
}))"""


class SignInRequired(RuntimeError):
    """The browser is not signed in to LinkedIn."""


def search_url(company: str) -> str:
    """LinkedIn people search for the company, limited to your 2nd and 3rd+ degree network."""
    query = {"keywords": company, "network": json.dumps(NETWORK, separators=(",", ":"))}
    return f"{SEARCH}?{urlencode(query)}&origin=FACETED_SEARCH"


def _mentions(text: str, company: str) -> bool:
    """Whether `text` names the company as a whole word ('Acme' in 'Engineer at Acme Inc')."""
    key = company_key(company)
    return bool(key) and re.search(rf"\b{re.escape(key)}\b", company_key(text)) is not None


def parse_card(card: dict[str, Any], company: str) -> NetworkPerson | None:
    """One search result as a person who works at `company`; None for anything else.

    LinkedIn matches the keywords anywhere in a profile, so a result counts only when its
    headline or "Current:" line names the company. Hidden "LinkedIn Member" results have no
    name or profile to reach them by and are dropped.
    """
    lines = [line.strip() for line in str(card.get("text", "")).splitlines() if line.strip()]
    degree = next((m.group(1) for line in lines if (m := _DEGREE.search(line))), None)
    if not lines or degree is None or lines[0].lower().startswith("linkedin member"):
        return None
    facts = [line for line in lines[1:] if not _NOISE.match(line) and not _DEGREE.fullmatch(line)]
    mutual = next((line for line in facts if _MUTUAL.search(line)), "")
    about = [line for line in facts if line != mutual]
    current = next((line for line in about if line.lower().startswith("current:")), "")
    headline = about[0] if about else ""
    if not (_mentions(headline, company) or _mentions(current, company)):
        return None
    try:
        return NetworkPerson(
            name=re.split(r"\s+•", lines[0])[0],
            profile_url=str(card.get("href", "")),
            degree=2 if degree == "2nd" else 3,
            headline=current.removeprefix("Current:").strip() or headline,
            mutual=mutual,
        )
    except ValidationError:
        return None


def people_from_cards(cards: list[dict[str, Any]], company: str) -> list[NetworkPerson]:
    """Distinct people at the company, 2nd degree first (they have someone to introduce you)."""
    found: dict[str, NetworkPerson] = {}
    for card in cards:
        person = parse_card(card, company)
        if person and person.profile_url not in found:
            found[person.profile_url] = person
    return sorted(found.values(), key=lambda p: p.degree)


def _signed_out(url: str) -> bool:
    path = urlsplit(url).path
    return any(part in path for part in ("/login", "/authwall", "/checkpoint", "/uas/"))


def cards(cdp_url: str, company: str) -> list[dict[str, Any]]:
    """The first page of results for the company's network search, read without clicking."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(cdp_url)
        if not browser.contexts:
            raise RuntimeError("The browser has no window open")
        page = browser.contexts[0].new_page()  # its own tab: whatever you left open stays put
        try:
            page.goto(search_url(company), wait_until="domcontentloaded", timeout=45000)
            if _signed_out(page.url):
                raise SignInRequired("Sign in to LinkedIn in the server browser (:6081/vnc.html)")
            try:
                page.wait_for_selector("main a[href*='/in/']", timeout=20000)
            except Exception:  # no results renders no profile links at all
                return []
            page.wait_for_timeout(1500)  # the rest of the page's cards
            result: list[dict[str, Any]] = page.eval_on_selector_all("main li", _CARDS)
            return [c for c in result if c["href"]]
        finally:
            page.close()


def connections(cdp_url: str, company: str) -> list[NetworkPerson]:
    """Your 2nd and 3rd+ degree connections who work at `company`, from LinkedIn search."""
    return people_from_cards(cards(cdp_url, company), company)
