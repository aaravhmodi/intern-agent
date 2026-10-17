"""Browser-based application form filling and submission for supported job sites."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from internship_agent.leads.answers import AnswerBank
from internship_agent.leads.refill import is_workday
from internship_agent.leads.schemas import FormQuestion, Lead

_FIELD_SELECTOR = "input:not([type=hidden]), textarea, select"
_CAPTCHA_SELECTOR = (
    "iframe[src*='captcha' i], [class*='captcha' i], [id*='captcha' i], "
    "[name*='captcha' i], [class*='turnstile' i], [id*='turnstile' i]"
)


def _visible_captcha(page: Any) -> bool:
    """Ignore passive reCAPTCHA widgets; stop for an actual visible challenge."""
    matches = page.locator(_CAPTCHA_SELECTOR)
    for index in range(matches.count()):
        item = matches.nth(index)
        if not item.is_visible():
            continue
        css = (item.get_attribute("class") or "").lower()
        src = (item.get_attribute("src") or "").lower()
        if any(name in css for name in ("grecaptcha-badge", "grecaptcha-logo")):
            continue
        if "recaptcha" in src and "/anchor" in src:
            continue
        return True
    return False


_SUCCESS_TEXT = re.compile(
    r"thank you for (applying|your application)|application (was |has been )?received|"
    r"application (was |has been )?submitted|we('ve| have) received your application|"
    r"successfully submitted",
    re.I,
)
_CLOSED_TEXT = re.compile(
    r"there are no current openings|job (?:is )?no longer available|"
    r"position (?:has been|is) filled|no longer accepting applications|posting is closed",
    re.I,
)
_APPLY_BUTTON = re.compile(r"^(apply( now)?|apply for this (job|role)|start application)$", re.I)
_SUBMIT_BUTTON = re.compile(r"^(submit( application)?|send application|apply( now)?)$", re.I)


@dataclass(frozen=True)
class SubmissionResult:
    status: str
    detail: str


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def _field_label(info: dict[str, Any]) -> str:
    """Prefer visible/accessibility labels over ATS-generated field identifiers."""
    for key in ("associatedLabel", "ariaLabel", "label"):
        value = str(info.get(key, "")).strip()
        if value:
            return value
    name = str(info.get("name", "")).strip()
    if re.fullmatch(r"cards\[[^]]+\]\[field\d+\]", name):
        return ""
    return name or str(info.get("placeholder", "")).strip()


def _numeric_answer(answer: str, label: str) -> str | None:
    """Format an explicitly saved value for a numeric HTML input without guessing units."""
    match = re.search(r"(?<![a-z0-9])\d+(?:\.\d+)?", answer.lower())
    if match:
        return match.group(0)
    if re.search(r"year|study|grade", label, re.I):
        ordinal = re.search(r"\b(first|second|third|fourth|fifth)\b", answer, re.I)
        if ordinal:
            values = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
            return str(values[ordinal.group(1).lower()])
    return None


def _posting_is_closed(text: str) -> bool:
    return bool(_CLOSED_TEXT.search(text))


def _save_submission_diagnostic(page: Any, browser_dir: Path, lead: Lead) -> None:
    """Keep a private screenshot of an uncertain post-submit state for review."""
    try:
        directory = browser_dir / "diagnostics"
        directory.mkdir(parents=True, exist_ok=True)
        name = _normalize(lead.key).replace(" ", "-")
        page.screenshot(path=str(directory / f"{name}.png"), full_page=True)
    except Exception:
        # A diagnostic failure must not cause a second submission attempt.
        pass


def _supported_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.scheme != "https":
        return False
    host = parsed.netloc.lower()
    return any(
        host == domain or host.endswith(f".{domain}")
        for domain in ("greenhouse.io", "ashbyhq.com", "lever.co")
    )


def _online_checks(page: Any, lead: Lead, body_text: str) -> str | None:
    """Check the live destination, role, and form before any submission click."""
    if not _supported_url(page.url):
        return "Live page left the approved HTTPS application site"
    title_words = set(_normalize(lead.posting_title).split())
    visible_words = set(_normalize(body_text).split())
    minimum = min(len(title_words), max(2, len(title_words) // 2))
    if title_words and len(title_words & visible_words) < minimum:
        return "Live page does not match the saved job title"
    unsafe_fields = page.locator(
        "input[type=password], input[autocomplete='cc-number'], "
        "input[autocomplete='cc-csc'], input[name*='credit_card' i], "
        "input[name*='payment' i]"
    )
    if unsafe_fields.count():
        return "Live form requests payment or credentials"
    return None


def _answer_for(label: str, lead: Lead, bank: AnswerBank | None = None) -> str | None:
    assert lead.application is not None
    wanted = _normalize(label)
    if not wanted:
        return None
    answers = [
        (_normalize(item.question.label), item.answer)
        for item in lead.application.answers
        if item.answer.strip()
    ]
    exact = next((answer for question, answer in answers if question == wanted), None)
    if exact is not None:
        return exact
    matches = [
        answer
        for question, answer in answers
        if question and (question in wanted or wanted in question)
    ]
    if len(set(matches)) == 1:
        return matches[0]
    if bank is not None:
        return bank.lookup(FormQuestion(label=label))
    return None


def _fill_form(
    page: Any, lead: Lead, resume_path: Path, bank: AnswerBank | None = None
) -> str | None:
    """Fill fields only when they have an unambiguous saved answer; return a block reason."""
    fields = page.locator(_FIELD_SELECTOR)
    count = fields.count()
    for index in range(count):
        field = fields.nth(index)
        info = field.evaluate(
            "el => ({tag: el.tagName.toLowerCase(), type: (el.type || '').toLowerCase(), "
            "label: (el.labels ? Array.from(el.labels).map(x => x.innerText).join(' ') : ''), "
            "ariaLabel: el.getAttribute('aria-label') || '', "
            "associatedLabel: (() => { const ids = (el.getAttribute('aria-labelledby') || '')"
            ".split(/\\s+/).filter(Boolean); const explicit = ids.map(id => "
            "document.getElementById(id)?.innerText || '').filter(Boolean).join(' '); "
            "if (explicit) return explicit; const group = el.closest("
            "'.application-question, .form-group, .form-field') || el.parentElement; "
            "const label = group?.querySelector('.application-label, legend, label') || "
            "el.closest('.application-field')?.parentElement?.querySelector("
            "'.application-label, legend, label'); "
            "return label?.innerText || ''; })(), "
            "required: el.required || el.getAttribute('aria-required') === 'true', "
            "ariaHidden: el.getAttribute('aria-hidden') === 'true', "
            "value: el.value || '', name: el.name || '', placeholder: el.placeholder || '', "
            "role: el.getAttribute('role') || ''})"
        )
        if info.get("ariaHidden"):
            # Greenhouse uses hidden required inputs as validity proxies for React selects.
            continue
        if not field.is_visible() and info["type"] != "file":
            continue
        if info.get("role") == "combobox":
            # React selects have required proxy inputs; fill them in the combobox pass.
            continue
        label = _field_label(info)
        if info["type"] == "file":
            if re.search(r"resume|cv upload", label, re.I) and resume_path.is_file():
                field.set_input_files(str(resume_path))
            elif info["required"]:
                return "Required file upload is not supported for this field"
            continue
        if info["type"] == "radio":
            answer = _answer_for(label, lead, bank)
            option = str(info.get("label", "")).strip()
            if (
                answer
                and option
                and (
                    _normalize(answer) == _normalize(option)
                    or _normalize(answer).startswith(_normalize(option) + " ")
                )
            ):
                field.check()
            continue
        if info["type"] == "checkbox":
            answer = _answer_for(label, lead, bank)
            option = _normalize(str(info.get("label") or info.get("value") or ""))
            wanted = _normalize(answer) if answer else ""
            if (
                answer
                and option
                and (
                    option == wanted
                    or option in wanted.split(" and ")
                    or option in wanted
                    and option not in {"on", "yes", "no"}
                )
            ):
                field.check()
            elif (
                answer
                and wanted in {"yes", "true", "i agree"}
                and (option in {"", "on"} or "agree" in option or "consent" in option)
            ):
                field.check()
            elif not answer and info["required"] and not field.is_checked():
                return f"Required consent/selection needs review: {label or 'unlabeled field'}"
            continue
        if info["type"] in {"submit", "button", "reset"}:
            continue
        if re.search(r"cover.?letter", label, re.I) and lead.application.cover_letter:
            field.fill(lead.application.cover_letter)
            continue
        answer = _answer_for(label, lead, bank)
        if answer:
            if info["tag"] == "select":
                options = field.locator("option").all_text_contents()
                option = next((o for o in options if _normalize(o) == _normalize(answer)), None)
                if option is None:
                    option = next((o for o in options if _normalize(answer) in _normalize(o)), None)
                if option:
                    field.select_option(label=option)
                    continue
            else:
                if info["type"] == "number":
                    answer = _numeric_answer(answer, label)
                    if answer is None:
                        if info["required"]:
                            return f"Required numeric field needs a verified number: {label}"
                        continue
                field.fill(answer)
                continue
        if info["required"] and not info["value"].strip():
            return f"Required field needs a verified answer: {label or 'unlabeled field'}"

    comboboxes = page.get_by_role("combobox")
    for index in range(comboboxes.count()):
        combo = comboboxes.nth(index)
        info = combo.evaluate(
            "el => ({tag: el.tagName.toLowerCase(), required: "
            "el.getAttribute('aria-required') === 'true', labelledBy: "
            "(el.getAttribute('aria-labelledby') || '').split(/\\s+/).filter(Boolean), "
            "value: el.value || ''})"
        )
        if info["tag"] == "select":
            continue
        label = combo.evaluate(
            "(el, ids) => ids.map(id => document.getElementById(id)?.innerText || '')"
            ".filter(Boolean).join(' ')",
            info["labelledBy"],
        )
        answer = _answer_for(label, lead, bank)
        if not answer:
            if info["required"] and not info["value"].strip():
                return f"Required selection needs a verified answer: {label or 'unlabeled field'}"
            continue
        combo.click()
        combo.fill(answer)
        page.wait_for_timeout(500)
        options = page.get_by_role("option")
        target = None
        for option_index in range(options.count()):
            option = options.nth(option_index)
            option_text = option.inner_text().strip()
            if _normalize(option_text) == _normalize(answer):
                target = option
                break
        if target is None:
            for option_index in range(options.count()):
                option = options.nth(option_index)
                option_text = _normalize(option.inner_text())
                if option_text and (
                    option_text in _normalize(answer) or _normalize(answer) in option_text
                ):
                    target = option
                    break
        if target is not None:
            target.click()
        elif info["required"]:
            return f"Could not match saved answer to required selection: {label}"

    if count == 0:
        return "No application fields found on the page"
    invalid_required = page.locator("input:invalid, textarea:invalid, select:invalid").count()
    if invalid_required:
        return f"{invalid_required} required form field(s) remain incomplete"
    return None


def apply_to_posting(
    lead: Lead,
    resume_path: Path,
    browser_dir: Path,
    *,
    bank: AnswerBank | None = None,
    dry_run: bool = False,
    headless: bool = True,
) -> SubmissionResult:
    """Fill a supported ATS form and submit after all visible required fields are satisfied."""
    from playwright.sync_api import Error as PlaywrightError
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
    from playwright.sync_api import sync_playwright

    if is_workday(lead):
        return SubmissionResult("skipped", "Workday applications are excluded")
    url = lead.posting_url or ""
    if not _supported_url(url):
        return SubmissionResult("skipped", "No submission adapter for this job site")
    if lead.application is None:
        return SubmissionResult("blocked", "Prepare application answers first")
    if not resume_path.is_file():
        return SubmissionResult("blocked", "Configured resume PDF was not found")

    try:
        with sync_playwright() as playwright:
            context = playwright.chromium.launch_persistent_context(
                str(browser_dir), headless=headless, accept_downloads=False
            )
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(1200)
            body_text = page.locator("body").inner_text(timeout=5000)
            if _posting_is_closed(body_text):
                return SubmissionResult("skipped", "Posting is closed or no longer available")
            if reason := _online_checks(page, lead, body_text):
                return SubmissionResult("blocked", reason)
            if _visible_captcha(page):
                return SubmissionResult("blocked", "CAPTCHA detected; manual completion required")

            if page.locator(_FIELD_SELECTOR).count() == 0:
                try:
                    page.wait_for_function(
                        "() => document.querySelectorAll('input:not([type=hidden]), "
                        "textarea, select').length > 0 || "
                        "Array.from(document.querySelectorAll('button, a')).some(el => "
                        "/^apply( for this (job|role)| now)?$/i.test(el.innerText.trim()))",
                        timeout=5000,
                    )
                except PlaywrightTimeoutError:
                    pass
                apply_button = page.get_by_role("link", name=_APPLY_BUTTON)
                if apply_button.count() == 0:
                    apply_button = page.get_by_role("button", name=_APPLY_BUTTON)
                if apply_button.count():
                    apply_button.first.click()
                    try:
                        page.wait_for_function(
                            "() => document.querySelectorAll('input:not([type=hidden]), "
                            "textarea, select').length > 0",
                            timeout=10000,
                        )
                    except PlaywrightTimeoutError:
                        pass

            if reason := _online_checks(page, lead, page.locator("body").inner_text(timeout=5000)):
                return SubmissionResult("blocked", reason)

            required_transcript = any(
                answer.question.required and "transcript" in answer.question.label.lower()
                for answer in lead.application.answers
            )
            if not required_transcript:
                required_transcript = page.locator("input[type=file][required]").evaluate_all(
                    "els => els.some(el => { const label = el.labels ? "
                    "Array.from(el.labels).map(x => x.innerText).join(' ') : ''; "
                    "return /transcript/i.test(label + ' ' + (el.name || '') + ' ' + "
                    "(el.getAttribute('aria-label') || '')); })"
                )
            if required_transcript:
                return SubmissionResult(
                    "skipped", "Automatic application skipped because a transcript is required"
                )

            reason = _fill_form(page, lead, resume_path, bank)
            if reason:
                return SubmissionResult("blocked", reason)
            if dry_run:
                return SubmissionResult("ready", "Form filled; dry run did not submit")
            if _visible_captcha(page):
                return SubmissionResult("blocked", "CAPTCHA detected; manual completion required")

            submit = page.get_by_role("button", name=_SUBMIT_BUTTON)
            if submit.count() == 0:
                submit = page.locator("input[type=submit]")
            if submit.count() == 0:
                return SubmissionResult("blocked", "Could not identify the final submit button")
            submit.last.click()
            page.wait_for_timeout(1800)
            body = page.locator("body").inner_text(timeout=5000)
            if _SUCCESS_TEXT.search(body):
                return SubmissionResult("submitted", "Application confirmation detected")
            invalid = page.locator("input:invalid, textarea:invalid, select:invalid").count()
            if invalid:
                return SubmissionResult(
                    "blocked", f"Form reported {invalid} invalid field(s) after submit"
                )
            _save_submission_diagnostic(page, browser_dir, lead)
            if _visible_captcha(page):
                return SubmissionResult(
                    "uncertain", "CAPTCHA appeared after submit; verify manually"
                )
            return SubmissionResult(
                "uncertain", "Submit was clicked but no application confirmation was detected"
            )
    except PlaywrightError as exc:
        # Browser exception messages can contain URLs and form values; keep logs generic.
        return SubmissionResult("failed", f"Browser automation failed ({type(exc).__name__})")


def open_login_browser(browser_dir: Path) -> None:
    """Open the persistent browser for one-time manual sign-in to job sites."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as playwright:
        context = playwright.chromium.launch_persistent_context(
            str(browser_dir), headless=False, accept_downloads=False
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://jobs.ashbyhq.com", wait_until="domcontentloaded")
        input("Sign in to the job sites you use, then press Enter here to close the browser... ")
        context.close()
