"""The saved, signed-in browser (Playwright) behind the event application agent."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from internship_agent.applications.browser import _visible_captcha
from internship_agent.opportunities.apply import HUMAN_CHECK, Element, Snapshot
from internship_agent.opportunities.schemas import StepAction

# Numbers every visible field and button so the model can name them.
_SNAPSHOT_JS = """() => {
  const sel = "input:not([type=hidden]), textarea, select, button, a[href], [role=button], " +
    "[role=checkbox], [role=radio], [role=combobox], [role=option], [contenteditable=true]";
  const seen = [];
  for (const el of document.querySelectorAll(sel)) {
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height || getComputedStyle(el).visibility === "hidden") continue;
    if (seen.length >= 150) break;
    const i = seen.length;
    el.setAttribute("data-agent-i", String(i));
    const labels = el.labels ? Array.from(el.labels).map(l => l.innerText).join(" ") : "";
    const near = el.closest("label, fieldset, [role=group]");
    const label = (el.getAttribute("aria-label") || labels || el.placeholder ||
      (["INPUT", "SELECT", "TEXTAREA"].includes(el.tagName) ? "" : el.innerText) ||
      (near ? near.innerText : "") || el.name || el.id || "").trim().replace(/\\s+/g, " ");
    seen.push({
      index: i,
      tag: el.getAttribute("role") || el.tagName.toLowerCase(),
      type: el.type && el.tagName !== "BUTTON" ? String(el.type) : "",
      label: label.slice(0, 200),
      required: !!(el.required || el.getAttribute("aria-required") === "true"),
      value: el.type === "checkbox" || el.type === "radio" ? (el.checked ? "checked" : "")
        : (el.value || "").slice(0, 80),
      options: el.tagName === "SELECT" ? Array.from(el.options).map(o => o.text.trim()) : [],
      autocomplete: el.getAttribute("autocomplete") || "",
    });
  }
  return seen;
}"""


# A ticked Turnstile / reCAPTCHA / hCaptcha box stays on the page; its token says it's solved.
_SOLVED_JS = """() => Array.from(document.querySelectorAll(
  "input[name='cf-turnstile-response'], textarea[name='g-recaptcha-response'], " +
  "textarea[name='h-captcha-response']")).some(el => (el.value || "").length > 20)"""


class PlaywrightPage:
    def __init__(self, context: Any) -> None:
        self.context = context
        self.page = context.pages[0] if context.pages else context.new_page()

    def _latest(self) -> None:
        """Follow a link that opened in a new tab."""
        pages = [p for p in self.context.pages if not p.is_closed()]
        if pages:
            self.page = pages[-1]

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded", timeout=45000)
        self.page.wait_for_timeout(1500)

    def snapshot(self) -> Snapshot:
        # A redirect while the page is being read (Eventbrite does this) destroys the
        # JavaScript context; wait for the new page and read it again.
        for attempt in range(4):
            self._latest()
            try:
                self.page.wait_for_load_state("domcontentloaded", timeout=15000)
                elements = [Element(**e) for e in self.page.evaluate(_SNAPSHOT_JS)]
                text = self.page.locator("body").inner_text(timeout=8000)
                captcha = _visible_captcha(self.page) and not self.page.evaluate(_SOLVED_JS)
                return Snapshot(self.page.url, text, elements, captcha)
            except Exception as error:
                if attempt == 3 or "context was destroyed" not in str(error):
                    raise
                self.page.wait_for_timeout(1500)
        raise AssertionError("unreachable")

    def wait_for_human(self, timeout_seconds: int = 240) -> bool:
        """Someone is at the screen: wait for them to clear the check. True once it's gone."""
        for _ in range(timeout_seconds // 2):
            self.page.wait_for_timeout(2000)
            snap = self.snapshot()
            if not snap.captcha and not HUMAN_CHECK.search(snap.text[:1500]):
                return True
        return False

    def sessions(self) -> dict[str, Any]:
        """Cookies of every site signed in to, in Playwright's portable form."""
        state: dict[str, Any] = self.context.storage_state()
        return state

    def act(self, action: StepAction, value: str, resume: Path) -> None:
        target = self.page.locator(f'[data-agent-i="{action.element}"]').first
        if action.kind == "fill":
            target.fill(value)
        elif action.kind == "select":
            try:
                target.select_option(label=value)
            except Exception:
                target.select_option(value=value)
        elif action.kind in ("check", "uncheck"):
            want = action.kind == "check"
            if target.get_attribute("role") in ("checkbox", "radio"):
                if (target.get_attribute("aria-checked") == "true") != want:
                    target.click()
            else:
                target.set_checked(want)
        elif action.kind == "upload_resume":
            target.set_input_files(str(resume))
        else:
            try:
                target.click(timeout=10000)
            except Exception as error:
                # A CAPTCHA overlay (Eventbrite's hCaptcha) covers the button: let the next
                # snapshot find the challenge and wait for the person, instead of crashing.
                if "Timeout" not in type(error).__name__:
                    raise
            try:
                self.page.wait_for_load_state("domcontentloaded", timeout=10000)
            except Exception:
                pass
        self.page.wait_for_timeout(700)

    def screenshot(self, path: Path) -> None:
        self.page.screenshot(path=str(path), full_page=True)


@contextmanager
def saved_browser(browser_dir: Path, headless: bool = True) -> Iterator[PlaywrightPage]:
    """The persistent application profile (sign-ins come from `opportunities sign-in`)."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            str(browser_dir), headless=headless, accept_downloads=False
        )
        try:
            yield PlaywrightPage(context)
        finally:
            context.close()


def import_sessions(browser_dir: Path, cookies: list[dict[str, Any]]) -> int:
    """Add sign-in cookies (exported elsewhere) to the saved profile. Returns how many."""
    with saved_browser(browser_dir) as page:
        page.context.add_cookies(cookies)
    return len(cookies)
