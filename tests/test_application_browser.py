from datetime import UTC, datetime
from pathlib import Path

import pytest

from internship_agent.applications.browser import (
    _EMAIL_VERIFICATION_TEXT,
    _SUCCESS_TEXT,
    _answer_for,
    _field_label,
    _fill_form,
    _numeric_answer,
    _online_checks,
    _post_submit_outcome,
    _posting_is_closed,
    _react_select_answer,
    _supported_url,
    _visible_captcha,
    apply_to_posting,
)
from internship_agent.leads.answers import AnswerBank
from internship_agent.leads.schemas import (
    ApplicationPrep,
    FormQuestion,
    Lead,
    LeadKind,
    PreparedAnswer,
)


def test_greenhouse_email_verification_is_not_submission_confirmation() -> None:
    text = (
        "A verification code was sent to the applicant. "
        "To submit your application, enter the 8-character code."
    )
    assert _EMAIL_VERIFICATION_TEXT.search(text)
    assert not _SUCCESS_TEXT.search(text)
    assert not _EMAIL_VERIFICATION_TEXT.search("Thank you for applying!")


@pytest.mark.parametrize(
    ("page_text", "expected"),
    [
        ("Thank you for applying to Acme!", "submitted"),
        ("Your application has been submitted.", "submitted"),
        ("We've received your application.", "submitted"),
        ("A verification code was sent to your email.", "uncertain"),
        ("Your form needs corrections: Missing entry for required field", "blocked"),
        ("Review your answers and click submit application.", "uncertain"),
    ],
)
def test_post_submit_outcomes_across_ats_pages(page_text: str, expected: str) -> None:
    assert _post_submit_outcome(page_text).status == expected


def test_post_submit_invalid_and_challenge_states() -> None:
    assert _post_submit_outcome("Please complete this field", invalid_fields=1).status == "blocked"
    assert _post_submit_outcome("Verify you are human", captcha_visible=True).detail.startswith(
        "CAPTCHA"
    )


def test_bachelor_degree_maps_to_greenhouse_degree_choice() -> None:
    answer = "Bachelor of Applied Science in Systems Design Engineering"
    assert _react_select_answer("Degree*", answer) == (
        "Bachelor",
        "Bachelor's Degree",
    )


class FakeField:
    def __init__(self, info: dict[str, object]) -> None:
        self.info = info
        self.filled = ""
        self.uploaded = ""
        self.checked = False

    def evaluate(self, _script: str) -> dict[str, object]:
        return self.info

    def is_visible(self) -> bool:
        return True

    def fill(self, value: str) -> None:
        self.filled = value

    def set_input_files(self, path: str) -> None:
        self.uploaded = path

    def check(self) -> None:
        self.checked = True

    def is_checked(self) -> bool:
        return self.checked


class FakeLocator:
    def __init__(self, fields: list[FakeField] | None = None) -> None:
        self.fields = fields or []

    def count(self) -> int:
        return len(self.fields)

    def nth(self, index: int) -> FakeField:
        return self.fields[index]


class FakeToggle:
    """An Ashby yes/no field entry: a label plus Yes/No buttons."""

    def __init__(self, label: str, required: bool = True) -> None:
        self.label, self.required, self.clicked = label, required, ""

    def count(self) -> int:
        return 1

    @property
    def first(self) -> "FakeToggle":
        return self

    def inner_text(self) -> str:
        return self.label

    def click(self) -> None:
        pass

    def locator(self, selector: str) -> "FakeToggle | FakeLocator":
        if selector.startswith("button[data-option="):
            self.clicked = selector.split("=")[1].rstrip("]")
        if selector == "label[class*=required]" and not self.required:
            return FakeLocator()
        return self


class FakePage:
    def __init__(self, fields: list[FakeField], toggles: list[FakeToggle] | None = None) -> None:
        self.fields = fields
        self.toggles = toggles or []

    def locator(self, selector: str) -> FakeLocator:
        if selector.startswith("input:invalid"):
            return FakeLocator()
        if selector.startswith(".ashby-application-form-field-entry"):
            return FakeLocator(self.toggles)  # type: ignore[arg-type]
        if selector == "input[type=file]":
            return FakeLocator([f for f in self.fields if f.info.get("type") == "file"])
        return FakeLocator(self.fields)

    def get_by_role(self, _role: str) -> FakeLocator:
        return FakeLocator()

    def wait_for_function(self, _script: str, *, arg: str, timeout: int) -> None:
        assert arg == "resume.pdf" and timeout == 10000

    def wait_for_timeout(self, _milliseconds: int) -> None:
        pass


def posting(url: str) -> Lead:
    lead = Lead(
        kind=LeadKind.POSTING,
        company="Acme",
        source_url=url,
        posting_url=url,
        posting_title="Software Engineering Intern",
    )
    lead.application = ApplicationPrep(
        prepared_at=datetime.now(UTC),
        source="form",
        answers=[
            PreparedAnswer(
                question=FormQuestion(label="Why Acme?", required=True),
                answer="I like building useful software.",
            )
        ],
    )
    return lead


def test_supported_submission_hosts_are_explicit() -> None:
    assert _supported_url("https://boards.greenhouse.io/acme/jobs/123")
    assert _supported_url("https://jobs.ashbyhq.com/acme/123")
    assert _supported_url("https://jobs.lever.co/acme/123")
    assert not _supported_url("https://acme.wd5.myworkdayjobs.com/interns")
    assert not _supported_url("https://example.com/careers")
    assert not _supported_url("https://greenhouse.io.attacker.example/careers")
    assert not _supported_url("http://jobs.ashbyhq.com/acme/123")


def test_three_live_checks_before_submit() -> None:
    class LivePage:
        def __init__(self, url: str, unsafe_count: int = 0) -> None:
            self.url = url
            self.unsafe_count = unsafe_count

        def locator(self, _selector: str) -> FakeLocator:
            return FakeLocator([FakeField({}) for _ in range(self.unsafe_count)])

    lead = posting("https://jobs.ashbyhq.com/acme/123")
    live = LivePage(lead.posting_url or "")
    text = "Acme is hiring a Software Engineering Intern."
    assert _online_checks(live, lead, text) is None
    assert "approved HTTPS" in (_online_checks(LivePage("https://evil.example"), lead, text) or "")
    assert "job title" in (_online_checks(live, lead, "Unrelated opportunity") or "")
    assert "payment" in (_online_checks(LivePage(live.url, 1), lead, text) or "")
    wrong_term = "Software Engineering Intern (Fall/Winter 2026) at Acme"
    assert "term" in (_online_checks(live, lead, wrong_term) or "")


def test_hidden_recaptcha_support_nodes_do_not_block() -> None:
    class CaptchaElement:
        def __init__(self, visible: bool, css_class: str = "", src: str = "") -> None:
            self.visible = visible
            self.css_class = css_class
            self.src = src

        def is_visible(self) -> bool:
            return self.visible

        def get_attribute(self, name: str) -> str | None:
            return {"class": self.css_class, "src": self.src}.get(name)

    class CaptchaPage:
        def __init__(self, elements: list[CaptchaElement]) -> None:
            self.elements = elements

        def locator(self, _selector: str) -> FakeLocator:
            return FakeLocator(self.elements)

    support = CaptchaPage(
        [
            CaptchaElement(False),
            CaptchaElement(True, "grecaptcha-badge"),
            CaptchaElement(True, "grecaptcha-logo"),
            CaptchaElement(True, src="https://www.recaptcha.net/recaptcha/enterprise/anchor?k=abc"),
        ]
    )
    assert not _visible_captcha(support)
    assert _visible_captcha(CaptchaPage([CaptchaElement(True, "challenge")]))
    assert _visible_captcha(
        CaptchaPage(
            [
                CaptchaElement(
                    True, src="https://www.recaptcha.net/recaptcha/enterprise/bframe?k=abc"
                )
            ]
        )
    )


def test_answer_mapping_requires_unambiguous_question_match() -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    assert _answer_for("Why Acme?", lead) == "I like building useful software."
    assert _answer_for("How many years of experience?", lead) is None


def test_answer_mapping_uses_saved_answer_for_live_form_fields(tmp_path: Path) -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    bank = AnswerBank(tmp_path / "answer-bank.json")
    bank.remember("School*", "University of Waterloo")
    assert _answer_for("School*", lead, bank) == "University of Waterloo"


def test_short_country_label_does_not_match_work_authorization_answer(tmp_path: Path) -> None:
    lead = posting("https://boards.greenhouse.io/acme/jobs/123")
    assert lead.application is not None
    lead.application.answers.append(
        PreparedAnswer(
            question=FormQuestion(label="Are you authorized to work in this country?"),
            answer="Yes",
        )
    )
    bank = AnswerBank(tmp_path / "answer-bank.json")
    bank.remember("Country*", "Canada")
    assert _answer_for("Country*", lead, bank) == "Canada"


def test_field_label_does_not_expose_generated_lever_field_ids() -> None:
    assert (
        _field_label(
            {"name": "cards[abc-123][field0]", "associatedLabel": "Which year of studies?"}
        )
        == "Which year of studies?"
    )
    assert _field_label({"name": "cards[abc-123][field0]"}) == ""
    assert (
        _field_label(
            {"label": "Third", "associatedLabel": "Which year of studies are you currently in?"}
        )
        == "Which year of studies are you currently in?"
    )


def test_fill_form_selects_saved_year_from_lever_radio_group(tmp_path: Path) -> None:
    lead = posting("https://jobs.lever.co/acme/123")
    assert lead.application is not None
    lead.application.answers.append(
        PreparedAnswer(
            question=FormQuestion(
                label="Which year of studies are you currently in?", required=True
            ),
            answer="Third year",
        )
    )
    first = FakeField(
        {
            "tag": "input",
            "type": "radio",
            "label": "First",
            "associatedLabel": "Which year of studies are you currently in?",
            "required": True,
            "name": "year",
            "value": "First",
            "placeholder": "",
        }
    )
    third = FakeField({**first.info, "label": "Third", "value": "Third"})
    assert _fill_form(FakePage([first, third]), lead, tmp_path / "resume.pdf") is None
    assert not first.checked
    assert third.checked


def test_fill_form_uses_lever_question_above_textarea(tmp_path: Path) -> None:
    lead = posting("https://jobs.lever.co/acme/123")
    assert lead.application is not None
    lead.application.answers.append(
        PreparedAnswer(
            question=FormQuestion(label="What school are you attending?", required=True),
            answer="University of Waterloo",
        )
    )
    school = FakeField(
        {
            "tag": "textarea",
            "type": "textarea",
            "label": "",
            "associatedLabel": "What school are you attending?",
            "required": True,
            "name": "cards[abc][field0]",
            "value": "",
            "placeholder": "",
        }
    )
    assert _fill_form(FakePage([school]), lead, tmp_path / "resume.pdf") is None
    assert school.filled == "University of Waterloo"


def test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(tmp_path: Path) -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    assert lead.application is not None
    lead.application.answers.append(
        PreparedAnswer(
            question=FormQuestion(label="Are you legally eligible to work in Canada?"),
            answer="Yes, I am a Canadian citizen",
        )
    )
    known = FakeToggle("Are you legally eligible to work in Canada?")
    assert _fill_form(FakePage([], [known]), lead, tmp_path / "resume.pdf") == (
        "No application fields found on the page"
    )
    assert known.clicked == "yes"
    unknown = FakeToggle("Do you have a driver's licence?")
    assert "driver" in (_fill_form(FakePage([], [unknown]), lead, tmp_path / "r.pdf") or "")
    optional = FakeToggle("Do you have a driver's licence?", required=False)
    assert _fill_form(FakePage([], [optional]), lead, tmp_path / "r.pdf") is not None
    assert optional.clicked == ""


def test_fill_form_selects_only_four_month_availability(tmp_path: Path) -> None:
    lead = posting("https://jobs.lever.co/acme/123")
    assert lead.application is not None
    lead.application.answers.append(
        PreparedAnswer(
            question=FormQuestion(label="Please indicate your availability", required=True),
            answer="January 2027 through April 2027 (4 months)",
        )
    )
    fields = [
        FakeField(
            {
                "tag": "input",
                "type": "checkbox",
                "label": option,
                "associatedLabel": "Please indicate your availability",
                "required": True,
                "name": "availability",
                "value": option,
                "placeholder": "",
            }
        )
        for option in ("4 months", "8 months")
    ]
    assert _fill_form(FakePage(fields), lead, tmp_path / "resume.pdf") is None
    assert fields[0].checked
    assert not fields[1].checked


def test_fill_form_defers_react_select_input_to_combobox_pass(tmp_path: Path) -> None:
    lead = posting("https://job-boards.greenhouse.io/acme/jobs/123")
    proxy = FakeField(
        {
            "tag": "input",
            "type": "text",
            "role": "combobox",
            "associatedLabel": "Discipline*",
            "required": True,
            "name": "",
            "value": "",
            "placeholder": "",
        }
    )
    assert _fill_form(FakePage([proxy]), lead, tmp_path / "resume.pdf") is None


def test_greenhouse_resume_upload_uses_input_id_when_label_says_attach(tmp_path: Path) -> None:
    lead = posting("https://job-boards.greenhouse.io/acme/jobs/123")
    resume = tmp_path / "resume.pdf"
    resume.write_bytes(b"fixture")
    upload = FakeField(
        {
            "tag": "input",
            "type": "file",
            "label": "Attach",
            "id": "resume",
            "name": "",
            "required": False,
            "value": "",
            "placeholder": "",
        }
    )
    assert _fill_form(FakePage([upload]), lead, resume) is None
    assert upload.uploaded == str(resume)


def test_numeric_input_format_uses_saved_salary_and_study_values() -> None:
    assert _numeric_answer("CAD 30 per hour or higher", "Desired Salary") == "30"
    assert _numeric_answer("Third year", "Year of study") == "3"
    assert _numeric_answer("around thirty", "Desired Salary") is None


def test_closed_posting_text_is_detected() -> None:
    assert _posting_is_closed("There are no current openings.")
    assert not _posting_is_closed("Apply for this Job")


def test_submission_confirmation_text_variants() -> None:
    assert _SUCCESS_TEXT.search("Your application has been submitted")
    assert _SUCCESS_TEXT.search("Thank you for applying")


def test_fill_form_uses_prepared_answers_and_uploads_resume(tmp_path: Path) -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    resume = tmp_path / "resume.pdf"
    resume.write_bytes(b"fixture")
    why = FakeField(
        {
            "tag": "textarea",
            "type": "textarea",
            "label": "Why Acme?",
            "required": True,
            "value": "",
            "name": "why",
            "placeholder": "",
        }
    )
    cv = FakeField(
        {
            "tag": "input",
            "type": "file",
            "label": "Resume/CV",
            "required": True,
            "value": "",
            "name": "resume",
            "placeholder": "",
        }
    )
    assert _fill_form(FakePage([why, cv]), lead, resume) is None
    assert why.filled == "I like building useful software."
    assert cv.uploaded == str(resume)


def test_fill_form_blocks_unanswered_required_questions(tmp_path: Path) -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    field = FakeField(
        {
            "tag": "input",
            "type": "text",
            "label": "What is your salary expectation?",
            "required": True,
            "value": "",
            "name": "salary",
            "placeholder": "",
        }
    )
    reason = _fill_form(FakePage([field]), lead, tmp_path / "resume.pdf")
    assert reason and "Required field" in reason


def test_workday_is_skipped_without_opening_a_browser(tmp_path: Path) -> None:
    result = apply_to_posting(
        posting("https://acme.wd5.myworkdayjobs.com/interns"),
        tmp_path / "resume.pdf",
        tmp_path / "browser",
    )
    assert result.status == "skipped"
    assert "Workday" in result.detail


def test_confirmation_quote_keeps_the_employers_line() -> None:
    from internship_agent.applications.browser import _confirmation_quote

    body = "Acme Careers\nThank you for applying to Acme! We'll be in touch.\nBack to jobs"
    assert _confirmation_quote(body) == "Thank you for applying to Acme! We'll be in touch."
    assert _confirmation_quote("Security code required") == ""
