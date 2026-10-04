from types import SimpleNamespace
from typing import Any, cast

import pytest
from openai import OpenAI

from internship_agent.ai import assess_fit
from internship_agent.leads.schemas import FitAssessment, FitResult, Lead, Segment, Verdict


class FakeResponses:
    def __init__(self, parsed: Any) -> None:
        self.parsed = parsed
        self.kwargs: dict[str, Any] = {}

    def parse(self, **kwargs: Any) -> Any:
        self.kwargs = kwargs
        return SimpleNamespace(output_parsed=self.parsed)


def fake_client(parsed: Any) -> tuple[OpenAI, FakeResponses]:
    responses = FakeResponses(parsed)
    return cast(OpenAI, SimpleNamespace(responses=responses)), responses


LEAD = Lead.model_validate(
    {
        "contact_name": "Jane",
        "company": "Acme",
        "announced_on": "2026-09-20",
        "source_url": "https://example.com",
    }
)


def test_assess_fit_sends_resume_and_lead_and_validates() -> None:
    expected = FitResult(
        fit=FitAssessment(
            score=80, verdict=Verdict.STRONG, reasons=["r"], concerns=[], talking_points=["t"]
        ),
        company_segment=Segment.MID,
    )
    client, responses = fake_client(expected)

    result = assess_fit(client, "test-model", "Python, FastAPI", LEAD)

    assert result == expected
    assert responses.kwargs["model"] == "test-model"
    assert responses.kwargs["text_format"] is FitResult
    user_message = responses.kwargs["input"][1]["content"]
    assert "Python, FastAPI" in user_message and "Acme" in user_message


def test_assess_fit_raises_when_model_returns_nothing() -> None:
    client, _ = fake_client(None)
    with pytest.raises(ValueError):
        assess_fit(client, "m", "resume", LEAD)
