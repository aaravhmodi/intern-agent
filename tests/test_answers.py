# ruff: noqa: E501
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pytest

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads.answers import AnswerBank, category, prefill, validate
from internship_agent.leads.schemas import (
    ApplicationPrep,
    FormQuestion,
    Lead,
    PreparedAnswer,
    QuestionKind,
)
from internship_agent.leads.store import LeadStore
from internship_agent.sources.application_form import (
    ashby_questions,
    greenhouse_questions,
    lever_questions,
)


def q(
    label: str, kind: QuestionKind = QuestionKind.TEXT, options: list[str] | None = None
) -> FormQuestion:
    return FormQuestion(label=label, kind=kind, options=options or [])


def test_greenhouse_parser() -> None:
    data: dict[str, Any] = {
        "questions": [
            {
                "label": "Resume/CV",
                "required": True,
                "fields": [{"type": "input_file"}, {"type": "textarea"}],
            },
            {
                "label": "How long?",
                "required": True,
                "fields": [
                    {
                        "type": "multi_value_multi_select",
                        "values": [{"label": "4 months"}, {"label": "8 months"}],
                    }
                ],
            },
        ]
    }
    parsed = greenhouse_questions(data)
    assert parsed[0].kind is QuestionKind.FILE
    assert parsed[1].kind is QuestionKind.MULTI_SELECT and parsed[1].options == [
        "4 months",
        "8 months",
    ]


def test_ashby_parser() -> None:
    data = {
        "data": {
            "jobPosting": {
                "applicationForm": {
                    "sections": [
                        {
                            "fieldEntries": [
                                {
                                    "isRequired": True,
                                    "field": {"title": "Why us?", "type": "LongText"},
                                },
                                {
                                    "isRequired": False,
                                    "field": {"title": "Winter?", "type": "Boolean"},
                                },
                            ]
                        }
                    ]
                }
            }
        }
    }
    parsed = ashby_questions(data)
    assert [(x.label, x.kind, x.required) for x in parsed] == [
        ("Why us?", QuestionKind.LONG_TEXT, True),
        ("Winter?", QuestionKind.YES_NO, False),
    ]


def test_lever_parser_reads_required_marker() -> None:
    page = (
        '<div class="application-label">Resume/CV <span>✱</span></div>'
        '<div class="application-label full-width">Current company</div>'
    )
    parsed = lever_questions(page)
    assert [(x.label, x.required, x.kind) for x in parsed] == [
        ("Resume/CV", True, QuestionKind.FILE),
        ("Current company", False, QuestionKind.TEXT),
    ]


@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("Are you legally authorized to work in Canada?", "personal"),
        ("What are your hourly compensation expectations?", "personal"),
        ("How did you hear about Zip?", "personal"),
        ("Do you self-identify as a racialized person?", "demographic"),
        ("Gender Identity:", "demographic"),
        ("Why are you interested in working at Harvey?", "ai"),
        ("What is your expected graduation date?", "ai"),
    ],
)
def test_category(label: str, expected: str) -> None:
    assert category(q(label)) == expected


def test_validate_by_kind() -> None:
    single = q("Pick", QuestionKind.SINGLE_SELECT, ["Software Development", "Finance"])
    assert validate(single, "software development") == "Software Development"
    assert validate(single, "Marketing") is None
    multi = q("Pick", QuestionKind.MULTI_SELECT, ["4 months", "8 months"])
    assert validate(multi, "4 months; 8 months") == "4 months; 8 months"
    assert validate(multi, "4 months; 2 years") is None
    assert validate(q("Ok?", QuestionKind.YES_NO), "yes, I am") == "Yes"
    assert validate(q("Name"), "  ") is None


def test_prefill_uses_bank_and_flags_personal(tmp_path: Path) -> None:
    bank = AnswerBank(tmp_path / "bank.json")
    bank.remember("Are you legally authorized to work in Canada?", "Yes")
    questions = [
        q("Resume", QuestionKind.FILE),
        q("Are you legally authorised to work in Canada?", QuestionKind.YES_NO),
        q("Will you require sponsorship?"),
        q("Veteran status"),
        q("Why us?", QuestionKind.LONG_TEXT),
    ]
    prepared = prefill(questions, bank)
    assert prepared[0].note.startswith("Upload")
    assert prepared[1].answer == "Yes" and not prepared[1].needs_user_input
    assert prepared[2].needs_user_input and prepared[2].note == "Only you can answer this."
    assert prepared[3].note.startswith("Optional")
    assert prepared[4].note == "ai"


def test_save_answers_remembers_personal_but_not_company_specific(tmp_path: Path) -> None:
    settings = Settings(data_dir=tmp_path, _env_file=None)  # type: ignore[call-arg]
    lead = Lead.model_validate(
        {
            "kind": "posting",
            "company": "Geotab",
            "posting_title": "Intern",
            "posting_url": "https://g.com/1",
            "source_url": "https://g.com/1",
        }
    )
    lead.application = ApplicationPrep(
        prepared_at=datetime.now(UTC),
        source="form",
        answers=[
            PreparedAnswer(
                question=q("Are you legally authorized to work?"), needs_user_input=True
            ),
            PreparedAnswer(
                question=q("Were you previously employed with Geotab?"), needs_user_input=True
            ),
            PreparedAnswer(
                question=q("Gender"), needs_user_input=True, note="Optional; your choice."
            ),
            PreparedAnswer(question=q("Why us?"), answer="Because.", note="AI"),
        ],
    )
    LeadStore(tmp_path / "leads.json").save([lead])

    saved = workflows.save_answers(
        settings, lead.key, {0: "Yes", 1: "No", 2: "Prefer not to say", 3: "Edited.", 9: "ignored"}
    )

    assert saved.application is not None
    assert [a.answer for a in saved.application.answers] == [
        "Yes",
        "No",
        "Prefer not to say",
        "Edited.",
    ]
    assert not any(a.needs_user_input for a in saved.application.answers)
    assert AnswerBank(tmp_path / "answer-bank.json").load() == {
        "are you legally authorized to work": "Yes"
    }
