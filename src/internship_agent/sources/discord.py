"""SWE intern roles posted in Discord job channels, read from the server's own signed-in browser.

The `browser` service in compose.yaml is a Chromium you sign in to through noVNC
(http://<TAILSCALE_IP>:6081/vnc.html), the same way the study agent signs in to LEARN. Leave any
channel of the server open there. The scrape opens the server's intern channels in a tab of its
own and reads the job cards its bot posts: company, title, location, and a job.northern.dev link
that redirects to the real application page.
"""

import re
import urllib.request
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from typing import Any

from internship_agent.leads.schemas import Lead, LeadKind
from internship_agent.sources.regions import region_from_text
from internship_agent.sources.simplify import is_software_role

# Sidebar channels worth reading; the rest of the server is chat.
CHANNELS = re.compile(r"intern-swe|interns-and-new-grad", re.I)
JOB_LINK = "https://job.northern.dev/"
_CHANNEL_LINKS = """els => els.map(e => [e.getAttribute('aria-label') || '', e.href])"""
_MESSAGES = """els => els.map(e => ({
  id: e.id,
  at: e.querySelector('time[datetime]')?.getAttribute('datetime') || '',
  text: e.innerText,
  links: [...e.querySelectorAll('a[href]')].map(a => [a.href, a.innerText.trim()]),
}))"""
# Scroll the message list to the top so Discord loads the posts before these.
_SCROLL_UP = """() => {
  let box = document.querySelector('ol[data-list-id=chat-messages]');
  while (box && !(box.scrollHeight > box.clientHeight
      && /auto|scroll/.test(getComputedStyle(box).overflowY))) box = box.parentElement;
  if (box) box.scrollTop = 0;
}"""
MAX_SCROLLS = 80  # per channel, so a channel with years of history can't run forever


def parse(message: dict[str, Any]) -> dict[str, str] | None:
    """Company, title, location and link from one bot job card; None for anything else."""
    # The card links both the company (its author line) and the title to the job.
    named = {t: h for h, t in message["links"] if h.startswith(JOB_LINK) and t}
    if not named:
        return None
    *company, title = list(named)[:2]
    lines = [line.strip() for line in message["text"].splitlines()]
    if not company:
        at = lines.index(title) if title in lines else 0
        company = [line for line in lines[:at] if line and line != ","][-1:]
    after = lines[lines.index("Location") + 1] if "Location" in lines[:-1] else ""
    return {
        "company": company[0] if company else "",
        "title": title,
        "location": after,
        "url": named[title],
    }


def application_url(link: str) -> str:
    """Where the job.northern.dev link redirects (the real posting), without tracking."""
    request = urllib.request.Request(link, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return str(response.geturl()).split("?utm_source")[0]
    except Exception:  # the redirect is a nicety; the Discord link still works
        return link


def cards(cdp_url: str, days: int) -> list[dict[str, str]]:
    """Job cards from every intern channel, scrolling back until posts are `days` old."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(cdp_url)
        pages = [p for c in browser.contexts for p in c.pages if "/channels/" in p.url]
        if not pages:
            raise RuntimeError("No Discord channel open: sign in and open one at :6081/vnc.html")
        channels = [
            href
            for label, href in pages[0].eval_on_selector_all(
                "a[href*='/channels/'][data-list-item-id^=channels]", _CHANNEL_LINKS
            )
            if CHANNELS.search(label)
        ]
        page = pages[0].context.new_page()  # its own tab: the one you left open stays put
        cutoff = (datetime.now(UTC) - timedelta(days=days)).isoformat()
        seen: dict[str, dict[str, Any]] = {}
        try:
            for href in channels:
                page.goto(href, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_selector("li[id^=chat-messages-]", timeout=30000)
                page.wait_for_timeout(2500)
                for _ in range(MAX_SCROLLS):
                    # Discord drops messages that scroll out of view, so keep each as it loads.
                    loaded = page.eval_on_selector_all("li[id^=chat-messages-]", _MESSAGES)
                    before = len(seen)
                    seen.update({m["id"]: m for m in loaded})
                    oldest = min((m["at"] for m in loaded if m["at"]), default="")
                    if len(seen) == before or (oldest and oldest < cutoff):
                        break  # the channel's start, or far enough back
                    page.evaluate(_SCROLL_UP)
                    page.wait_for_timeout(1500)
        finally:
            page.close()
    return [card for m in seen.values() if (card := parse(m))]


def postings(
    cdp_url: str | None, log: Callable[[str], None] = lambda _: None, days: int = 6
) -> list[Lead]:
    """SWE intern/co-op leads posted in the last `days` days; nothing without a browser."""
    if not cdp_url:
        return []
    found = {c["url"]: c for c in cards(cdp_url, days) if is_software_role(c["title"])}
    leads = [
        Lead(
            kind=LeadKind.POSTING,
            company=c["company"] or "Unknown",
            posting_title=c["title"],
            posting_url=application_url(link),
            source_url=link,
            location=c["location"],
            region=region_from_text(c["location"]),
            hiring_signals=["Posted in the northern.dev Discord job channels"],
        )
        for link, c in found.items()
    ]
    log(f"{len(leads)} SWE intern role(s) from the Discord job channels")
    return leads
