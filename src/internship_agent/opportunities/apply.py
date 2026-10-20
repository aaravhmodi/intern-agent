"""Apply or RSVP to an event in the saved browser, one page at a time.

The model reads each page (a numbered list of its fields and buttons) and says what to fill
and click; this module decides whether that is allowed. Hard rules, in code:

- three checks online before acting (AGENTS.md): the page is the event's own site or a known
  event platform, the landing page names the event, and nothing asks for payment;
- never a password, card or billing field; never a pay/buy/checkout click;
- stop at a CAPTCHA, a sign-in page, or a required question the candidate's material can't
  answer; leave newsletter and marketing boxes alone;
- personal details come from the answer bank, filled in here, never written by the model;
- "submitted" only when the page itself confirms it; otherwise "uncertain", never retried.
"""

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Protocol
from urllib.parse import urlsplit

from internship_agent.opportunities.schemas import (
    BrowserStep,
    EventApplication,
    Opportunity,
    StepAction,
)

MAX_STEPS = 12
# Event platforms an application may move through besides the event's own domain.
PLATFORMS = (
    "devpost.com",
    "mlh.io",
    "mlh.com",
    "lu.ma",
    "luma.com",
    "eventbrite.com",
    "eventbrite.ca",
    "typeform.com",
    "tally.so",
    "jotform.com",
    "airtable.com",
    "forms.gle",
    "hackerearth.com",
    "dorahacks.io",
    "ethglobal.com",
    "meetup.com",
)
_GOOGLE_FORMS = re.compile(r"^docs\.google\.com$")
_PAYMENT = re.compile(
    r"card ?number|credit ?card|debit|cvv|cvc|security code|expir|billing|payment|iban|"
    r"cc-(number|csc|exp)",
    re.I,
)
_PAY_CLICK = re.compile(
    r"\b(pay|buy|purchase|checkout|check out|place order|donate|subscribe|upgrade)\b|"
    r"[$€£]\s?[1-9]",
    re.I,
)
_OPTIONAL_BOX = re.compile(
    r"newsletter|marketing|promotion|special offers|subscribe|"
    r"updates from (our )?(sponsors|partners)",
    re.I,
)
# Signs that a sign-in worked: an account menu or a way out.
SIGNED_IN = re.compile(
    r"\b(sign out|log ?out|my account|account settings|my profile|your profile|my events|"
    r"your events|my tickets)\b",
    re.I,
)
_SIGN_IN_CONTROL = re.compile(r"^(sign ?in|log ?in|sign ?up|continue with \w+|send code)$", re.I)


def nothing_to_sign_in(snap: "Snapshot") -> bool:
    """After a sign-in, a page with no sign-in link or button and no field left to fill
    (Luma's "create a passkey?" prompt, say) means the session exists."""
    return not any(
        _SIGN_IN_CONTROL.match(e.label.strip())
        or (e.tag in ("input", "textarea") and e.type not in ("checkbox", "radio", "search"))
        for e in snap.elements
    )


# Bot checks (Cloudflare and the like) that show a page instead of the site.
HUMAN_CHECK = re.compile(
    r"verify (that )?you are (a )?human|verifying you are human|just a moment\.\.\.|"
    r"checking (if the site connection is secure|your browser)|performing security verification",
    re.I,
)
_CONFIRMED = re.compile(
    r"you('re| are) (now )?(registered|going|in\b|on the (wait ?list|list))|"
    r"registration (is )?(confirmed|complete|received|successful)|"
    r"thanks?( you)? for (registering|applying|signing up|your (application|registration|rsvp))|"
    r"application (was |has been )?(received|submitted)|"
    r"we('ve| have) received your (application|registration)|see you there|"
    r"request (sent|submitted|received)|pending (host )?approval|"
    r"you('ve| have) (joined|registered|applied)|joined (the |this )?hackathon|"
    r"on the wait ?list|rsvp (confirmed|received)",
    re.I,
)


@dataclass
class Element:
    index: int
    tag: str  # input, textarea, select, button, a, or an ARIA role
    type: str = ""
    label: str = ""
    required: bool = False
    value: str = ""
    options: list[str] = field(default_factory=list)
    autocomplete: str = ""


@dataclass
class Snapshot:
    url: str
    text: str
    elements: list[Element]
    captcha: bool = False


class Page(Protocol):
    """The browser, as the agent sees it. The real one is Playwright (opportunities.browser)."""

    def open(self, url: str) -> None: ...

    def snapshot(self) -> Snapshot: ...

    def act(self, action: StepAction, value: str, resume: Path) -> None: ...

    def screenshot(self, path: Path) -> None: ...


StepFn = Callable[[Snapshot, list[str]], BrowserStep]


def _host(url: str) -> str:
    return (urlsplit(url).hostname or "").lower()


def _site(host: str) -> str:
    """The registrable part of a host, roughly: calhacks.io for www.calhacks.io."""
    return ".".join(host.split(".")[-2:])


def allowed(url: str, event_url: str) -> bool:
    """On the event's own site, a known event platform, or a Google Form."""
    host = _host(url)
    if urlsplit(url).scheme != "https" or not host:
        return False
    if _site(host) == _site(_host(event_url)) or _GOOGLE_FORMS.match(host):
        return True
    return any(host == p or host.endswith("." + p) for p in PLATFORMS)


_COMMON = {"the", "and", "for", "with", "annual"}


def names_event(text: str, event: Opportunity) -> bool:
    """The page mentions the event: its title's first distinctive word."""
    words = [
        w for w in re.findall(r"[a-z0-9]+", event.title.lower()) if len(w) > 2 and w not in _COMMON
    ]
    return not words or words[0] in text.lower()


def describe(snapshot: Snapshot) -> str:
    """The page as the model reads it: the numbered elements, then the visible text."""
    lines = []
    for e in snapshot.elements:
        bits = [f"[{e.index}] {e.tag}"]
        if e.type:
            bits.append(f"type={e.type}")
        if e.required:
            bits.append("required")
        bits.append(repr(e.label[:120]))
        if e.value:
            bits.append(f"value={e.value[:60]!r}")
        if e.options:
            bits.append("options=" + " | ".join(o[:40] for o in e.options[:25]))
        lines.append(" ".join(bits))
    return (
        f"URL: {snapshot.url}\nELEMENTS:\n" + "\n".join(lines) + f"\nTEXT:\n{snapshot.text[:4000]}"
    )


def _refusal(action: StepAction, element: Element | None) -> str | None:
    """Why an action must not run, or None. A refusal stops the whole application."""
    if element is None:
        return f"the page has no element {action.element}"
    about = f"{element.label} {element.type} {element.autocomplete}"
    if element.type == "password":
        return "a password field (sign in yourself first)"
    if action.kind in ("fill", "select") and _PAYMENT.search(about):
        return f"a payment field ({element.label[:40]})"
    if action.kind == "click" and _PAY_CLICK.search(element.label):
        return f"a payment button ({element.label[:40]})"
    return None


def resolve(value: str, bank: dict[str, str]) -> str | None:
    """A literal value, or a saved answer for "@bank:<question>" (None if there is none)."""
    if not value.startswith("@bank:"):
        return value
    wanted = value.removeprefix("@bank:").strip().lower()
    return next((a for q, a in bank.items() if q.strip().lower() == wanted and a.strip()), None)


def run(
    page: Page,
    event: Opportunity,
    bank: dict[str, str],
    next_step: StepFn,
    resume: Path,
    proof: Path,
    *,
    dry_run: bool = False,
    max_steps: int = MAX_STEPS,
    confirmed: re.Pattern[str] | None = None,
    wait_for_human: Callable[[], bool] | None = None,
    inbox: Callable[[str], str | None] | None = None,
) -> EventApplication:
    """Work through the event's pages until it confirms (or a rule stops it).

    `confirmed` is the page text that counts as done (an application or RSVP by default).
    With `wait_for_human` (someone is at the screen) a CAPTCHA waits for them instead of
    stopping. `inbox("code")` / `inbox("link")` read the sign-in code or link just emailed.
    """
    done_text = confirmed or _CONFIRMED
    history: list[str] = []

    def done(status: str, detail: str, *, shot: bool = False) -> EventApplication:
        saved = False
        if shot:
            try:
                proof.parent.mkdir(parents=True, exist_ok=True)
                page.screenshot(proof)
                saved = True
            except Exception:  # a failed screenshot must never lead to a second attempt
                pass
        return EventApplication(
            status=status,
            detail=detail,
            at=datetime.now(UTC),
            steps=history,
            proof=saved and status == "submitted",
        )

    page.open(event.url)
    acted = False
    for step_number in range(max_steps):
        snap = page.snapshot()
        if not allowed(snap.url, event.url):
            return done("blocked", f"Left the event's sites for {_host(snap.url)}", shot=acted)
        if snap.captcha or HUMAN_CHECK.search(snap.text[:1500]):
            if wait_for_human is not None and wait_for_human():
                history.append("  you cleared a 'verify you're human' check")
                continue
            return done(
                "needs_you",
                "A CAPTCHA or 'verify you're human' check appeared; finish this one yourself",
                shot=acted,
            )
        if step_number == 0 and not names_event(snap.text, event):
            return done("blocked", "The event page doesn't name the event")
        if any(e.type == "password" for e in snap.elements):
            return done(
                "needs_you",
                f"{_site(_host(snap.url))} asks for a password; sign in there yourself "
                "(internship-agent opportunities sign-in)",
            )
        if any(
            _PAYMENT.search(f"{e.label} {e.autocomplete}")
            for e in snap.elements
            if e.tag in ("input", "select")
        ):
            return done("blocked", "The form asks for payment details", shot=acted)
        if acted and done_text.search(snap.text):
            return done("submitted", _quote(snap.text, done_text), shot=True)

        step = next_step(snap, history)
        history.append(f"Page {step_number + 1}: {step.page}")
        if step.outcome == "submitted":
            if done_text.search(snap.text):
                return done("submitted", _quote(snap.text, done_text), shot=True)
            if done_text is SIGNED_IN and acted and nothing_to_sign_in(snap):
                return done(
                    "submitted", "Signed in: no sign-in form or link left on the page", shot=True
                )
            return done(
                "uncertain",
                "The agent thought it was done, but the page doesn't "
                "confirm it; check the event page and your email",
                shot=True,
            )
        if step.outcome in ("needs_you", "blocked"):
            return done(step.outcome, step.reason, shot=acted)
        if dry_run:
            planned = "; ".join(f"{a.kind} [{a.element}]" for a in step.actions)
            return done("ready", f"Dry run: would {planned or 'do nothing'} on the first page")

        elements = {e.index: e for e in snap.elements}
        for action in step.actions:
            if action.kind == "email_link":
                link = inbox("link") if inbox else None
                if not link or not allowed(link, event.url):
                    return done("needs_you", "No sign-in link arrived by email", shot=acted)
                page.open(link)
                acted = True
                history.append("  opened the sign-in link from your email")
                continue
            element = elements.get(action.element)
            if reason := _refusal(action, element):
                return done("blocked", f"Stopped before {reason}", shot=acted)
            assert element is not None
            if action.kind == "check" and _OPTIONAL_BOX.search(element.label):
                history.append(f"  left unticked: {element.label[:60]}")
                continue
            if action.value == "@inbox_code":
                code = inbox("code") if inbox else None
                if not code:
                    return done("needs_you", "No sign-in code arrived by email", shot=acted)
                page.act(action, code, resume)
                acted = True
                history.append(f"  {action.kind} {element.label[:60]!r} = (emailed code)")
                continue
            value = resolve(action.value, bank)
            if value is None:
                return done(
                    "needs_you",
                    f"No saved answer for {action.value.removeprefix('@bank:')!r}"
                    f" ({element.label[:60]}); add it, then apply again",
                    shot=acted,
                )
            page.act(action, value, resume)
            acted = True
            shown = "(saved answer)" if action.value.startswith("@bank:") else value[:60]
            history.append(
                f"  {action.kind} {element.label[:60]!r}" + (f" = {shown}" if value else "")
            )
        if not step.actions:
            return done("needs_you", f"Nothing to do on this page: {step.reason}", shot=acted)
    return done("uncertain", "Ran out of steps before the event confirmed anything", shot=acted)


def _quote(text: str, pattern: re.Pattern[str] = _CONFIRMED) -> str:
    """The page's own confirmation line, as proof."""
    match = pattern.search(text)
    if match is None:
        return "Confirmed"
    start = text.rfind("\n", 0, match.start()) + 1
    end = text.find("\n", match.end())
    line = " ".join(text[start : end if end != -1 else len(text)].split())
    return f'Confirmed: "{line[:200]}"'
