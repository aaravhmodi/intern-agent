from datetime import UTC, datetime
from pathlib import Path

from internship_agent.applications.browser import (
    _answer_for,
    _field_label,
    _fill_form,
    _numeric_answer,
    _supported_url,
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


class FakeField:
    def __init__(self, info: dict[str, object]) -> None:
        self.info = info
        self.filled = ""
        self.uploaded = ""

    def evaluate(self, _script: str) -> dict[str, object]:
        return self.info

    def is_visible(self) -> bool:
        return True

    def fill(self, value: str) -> None:
        self.filled = value

    def set_input_files(self, path: str) -> None:
        self.uploaded = path


class FakeLocator:
    def __init__(self, fields: list[FakeField] | None = None) -> None:
        self.fields = fields or []

    def count(self) -> int:
        return len(self.fields)

    def nth(self, index: int) -> FakeField:
        return self.fields[index]


class FakePage:
    def __init__(self, fields: list[FakeField]) -> None:
        self.fields = fields

    def locator(self, selector: str) -> FakeLocator:
        if selector.startswith("input:invalid"):
            return FakeLocator()
        return FakeLocator(self.fields)

    def get_by_role(self, _role: str) -> FakeLocator:
        return FakeLocator()


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


def test_answer_mapping_requires_unambiguous_question_match() -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    assert _answer_for("Why Acme?", lead) == "I like building useful software."
    assert _answer_for("How many years of experience?", lead) is None


def test_answer_mapping_uses_saved_answer_for_live_form_fields(tmp_path: Path) -> None:
    lead = posting("https://jobs.ashbyhq.com/acme/123")
    bank = AnswerBank(tmp_path / "answer-bank.json")
    bank.remember("School*", "University of Waterloo")
    assert _answer_for("School*", lead, bank) == "University of Waterloo"


def test_field_label_does_not_expose_generated_lever_field_ids() -> None:
    assert _field_label(
        {"name": "cards[abc-123][field0]", "associatedLabel": "Which year of studies?"}
    ) == "Which year of studies?"
    assert _field_label({"name": "cards[abc-123][field0]"}) == ""


def test_numeric_input_format_uses_saved_salary_and_study_values() -> None:
    assert _numeric_answer("CAD 30 per hour or higher", "Desired Salary") == "30"
    assert _numeric_answer("Third year", "Year of study") == "3"
    assert _numeric_answer("around thirty", "Desired Salary") is None


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
