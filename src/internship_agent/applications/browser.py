"""Browser-based application form filling and submission for supported job sites."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from internship_agent.leads.refill import is_workday
from internship_agent.leads.schemas import Lead

_FIELD_SELECTOR = "input:not([type=hidden]), textarea, select"
_CAPTCHA_SELECTOR = (
    "iframe[src*='captcha' i], [class*='captcha' i], [id*='captcha' i], "
    "[name*='captcha' i], [class*='turnstile' i], [id*='turnstile' i]"
)
_SUCCESS_TEXT = re.compile(
    r"thank you for (applying|your application)|application (was |has been )?received|"
    r"we('ve| have) received your application|successfully submitted",
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


def _supported_url(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return any(
        host == domain or host.endswith(f".{domain}")
        for domain in ("greenhouse.io", "ashbyhq.com", "lever.co")
    )


def _answer_for(label: str, lead: Lead) -> str | None:
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
    return matches[0] if len(set(matches)) == 1 else None


def _fill_form(page: Any, lead: Lead, resume_path: Path) -> str | None:
    """Fill fields only when they have an unambiguous saved answer; return a block reason."""
    fields = page.locator(_FIELD_SELECTOR)
    count = fields.count()
    for index in range(count):
        field = fields.nth(index)
        info = field.evaluate(
            "el => ({tag: el.tagName.toLowerCase(), type: (el.type || '').toLowerCase(), "
            "label: (el.labels ? Array.from(el.labels).map(x => x.innerText).join(' ') : ''), "
            "required: el.required || el.getAttribute('aria-required') === 'true', "
            "value: el.value || '', name: el.name || '', placeholder: el.placeholder || ''})"
        )
        if not field.is_visible() and info["type"] != "file":
            continue
        label = " ".join(
            part for part in (info["label"], info["name"], info["placeholder"]) if part
        )
        if info["type"] == "file":
            if re.search(r"resume|cv upload", label, re.I) and resume_path.is_file():
                field.set_input_files(str(resume_path))
            elif info["required"]:
                return "Required file upload is not supported for this field"
            continue
        if info["type"] in {"checkbox", "radio"}:
            if info["required"] and not field.is_checked():
                return f"Required consent/selection needs review: {label or 'unlabeled field'}"
            continue
        if info["type"] in {"submit", "button", "reset"}:
            continue
        if re.search(r"cover.?letter", label, re.I) and lead.application.cover_letter:
            field.fill(lead.application.cover_letter)
            continue
        answer = _answer_for(label, lead)
        if answer:
            if info["tag"] == "select":
                options = field.locator("option").all_text_contents()
                option = next((o for o in options if _normalize(o) == _normalize(answer)), None)
                if option is None:
                    option = next(
                        (o for o in options if _normalize(answer) in _normalize(o)), None
                    )
                if option:
                    field.select_option(label=option)
                    continue
            else:
                field.fill(answer)
                continue
        if info["required"] and not info["value"].strip():
            return f"Required field needs a verified answer: {label or 'unlabeled field'}"

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
    dry_run: bool = False,
    headless: bool = True,
) -> SubmissionResult:
    """Fill a supported ATS form and submit after all visible required fields are satisfied."""
    from playwright.sync_api import Error as PlaywrightError
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
            if page.locator(_CAPTCHA_SELECTOR).count():
                return SubmissionResult("blocked", "CAPTCHA detected; manual completion required")

            if page.locator(_FIELD_SELECTOR).count() == 0:
                apply_button = page.get_by_role("link", name=_APPLY_BUTTON)
                if apply_button.count() == 0:
                    apply_button = page.get_by_role("button", name=_APPLY_BUTTON)
                if apply_button.count():
                    apply_button.first.click()
                    page.wait_for_load_state("domcontentloaded", timeout=20000)
                    page.wait_for_timeout(800)

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

            reason = _fill_form(page, lead, resume_path)
            if reason:
                return SubmissionResult("blocked", reason)
            if dry_run:
                return SubmissionResult("ready", "Form filled; dry run did not submit")
            if page.locator(_CAPTCHA_SELECTOR).count():
                return SubmissionResult("blocked", "CAPTCHA detected; manual completion required")

            submit = page.get_by_role("button", name=_SUBMIT_BUTTON)
            if submit.count() == 0:
                submit = page.get_by_role("input", name=_SUBMIT_BUTTON)
            if submit.count() == 0:
                return SubmissionResult("blocked", "Could not identify the final submit button")
            submit.last.click()
            page.wait_for_timeout(1800)
            if page.locator(_CAPTCHA_SELECTOR).count():
                return SubmissionResult("blocked", "CAPTCHA appeared after submit; verify manually")
            body = page.locator("body").inner_text(timeout=5000)
            if _SUCCESS_TEXT.search(body):
                return SubmissionResult("submitted", "Application confirmation detected")
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
