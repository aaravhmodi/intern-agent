from datetime import UTC, datetime

from internship_agent.leads.schemas import (
    ApplicationPrep,
    FitAssessment,
    FormQuestion,
    Lead,
    PreparedAnswer,
    QuestionKind,
)
from internship_agent.notify import MESSAGE_BYTES, posting_push, summary_push, written_answers


def answer(label: str, text: str = "", **kw: object) -> PreparedAnswer:
    return PreparedAnswer(question=FormQuestion(label=label), answer=text, **kw)  # type: ignore[arg-type]


def lead(answers: list[PreparedAnswer], score: int = 85) -> Lead:
    return Lead(
        kind="posting",  # type: ignore[arg-type]
        company="Acme",
        posting_title="SWE Intern",
        posting_url="https://jobs.ashbyhq.com/acme/1",
        source_url="https://jobs.ashbyhq.com/acme/1",
        location="New York, NY",
        fit=FitAssessment(
            score=score, verdict="strong", reasons=[], concerns=[], talking_points=[]
        ),
        application=ApplicationPrep(prepared_at=datetime.now(UTC), source="form", answers=answers),
    )


def test_only_ai_written_job_answers_are_sent() -> None:
    answers = [
        answer("Why do you want to work at Acme?", "Because of the robots."),
        answer("Are you authorized to work in the US?", "", needs_user_input=True),
        answer("LinkedIn profile", "linkedin.com/in/aarav", note="From your saved answers."),
        PreparedAnswer(question=FormQuestion(label="Resume", kind=QuestionKind.FILE)),
    ]
    picked = written_answers(lead(answers))
    assert [a.question.label for a in picked] == ["Why do you want to work at Acme?"]


def test_posting_push_shows_answers_and_what_is_left() -> None:
    push = posting_push(
        lead(
            [
                answer("Describe a project you're proud of", "The Upside dashboard."),
                answer("Do you need visa sponsorship?", "", needs_user_input=True),
            ]
        )
    )
    assert push.title == "Acme: SWE Intern (85)"
    assert push.click == "https://jobs.ashbyhq.com/acme/1"
    assert "A: The Upside dashboard." in push.message
    assert "You fill in (1): Do you need visa sponsorship?" in push.message
    assert push.priority == 4


def test_long_answers_stay_under_ntfy_limit() -> None:
    answers = [answer(f"Question {i}?", "word " * 2000) for i in range(8)]
    push = posting_push(lead(answers, score=70))
    assert len(push.message.encode("utf-8")) <= MESSAGE_BYTES
    assert push.message.count("Q: ") == 8
    assert push.priority == 3


def test_summary_lists_top_scores() -> None:
    a, b = lead([], score=70), lead([], score=90)
    b.company = "Beta"
    push = summary_push([a, b], [a, b], "http://100.76.57.23:8765")
    assert "Top: Beta 90, Acme 70" in push.message
    assert push.click == "http://100.76.57.23:8765"
