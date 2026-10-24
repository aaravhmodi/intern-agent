"""Intern roles linked in a Discord jobs channel, read from the server's own signed-in browser.

The `browser` service in compose.yaml is a Chromium you sign in to through noVNC
(http://<TAILSCALE_IP>:6081/vnc.html), the same way the study agent signs in to LEARN. Leave the
jobs channel open there; the scrape reads its links over the debugging port. The channel's links
to Greenhouse, Ashby and Lever boards are read like startups.gallery's.
"""

from collections.abc import Callable

from internship_agent.leads.schemas import Lead
from internship_agent.sources import gallery
from internship_agent.sources.startup_jobs import intern_roles


def channel_links(cdp_url: str) -> str:
    """Every link in the open Discord channel's loaded messages, as one string."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(cdp_url)
        pages = [p for c in browser.contexts for p in c.pages if "/channels/" in p.url]
        if not pages:
            raise RuntimeError("No Discord channel open: sign in and open it at :6081/vnc.html")
        page = pages[0]
        page.reload(wait_until="domcontentloaded", timeout=45000)  # pick up new posts
        try:
            page.wait_for_selector("[id^=chat-messages]", timeout=30000)
        except Exception as error:
            raise RuntimeError("Discord needs sign-in again at :6081/vnc.html") from error
        page.wait_for_timeout(2000)
        links: list[str] = page.eval_on_selector_all(
            "[id^=chat-messages] a[href]", "els => els.map(e => e.href)"
        )
    return "\n".join(links)


def postings(cdp_url: str | None, log: Callable[[str], None] = lambda _: None) -> list[Lead]:
    """Intern/co-op leads from the job boards linked in the channel; nothing without a browser."""
    if not cdp_url:
        return []
    found = gallery.boards(channel_links(cdp_url))
    leads: list[Lead] = []
    for kind, slug in found:
        try:
            for role in intern_roles(gallery._READERS[kind](slug)):
                lead = gallery.to_lead(slug, role)
                lead.hiring_signals = ["Posted in the Discord jobs channel"]
                leads.append(lead)
        except Exception as error:  # one broken board must not stop the rest
            log(f"discord {slug}: {error}")
    log(f"{len(leads)} role(s) from {len(found)} board(s) linked on Discord")
    return leads
