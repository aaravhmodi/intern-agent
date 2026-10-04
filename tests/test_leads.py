import json
from datetime import date
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from internship_agent.leads.ranking import rank
from internship_agent.leads.schemas import (
    FitAssessment,
    FounderLead,
    LeadStatus,
    Round,
    Verdict,
)
from internship_agent.leads.store import LeadStore, load_inbox, merge


def lead(**overrides: Any) -> FounderLead:
    data: dict[str, Any] = {
        "founder_name": "Jane Doe",
        "company": "Acme AI",
        "announced_on": "2026-09-20",
        "source_url": "https://example.com/acme-raises",
    }
    return FounderLead.model_validate({**data, **overrides})


def fit(score: int) -> FitAssessment:
    return FitAssessment(
        score=score, verdict=Verdict.POSSIBLE, reasons=[], concerns=[], talking_points=[]
    )


def test_x_handle_is_normalized() -> None:
    assert lead(x_handle="@janedoe").x_handle == "janedoe"
    assert lead(x_handle="https://x.com/janedoe/").x_handle == "janedoe"
    assert lead(x_handle="").x_handle is None
    assert lead(x_handle="janedoe").x_url == "https://x.com/janedoe"


def test_invalid_x_handle_rejected() -> None:
    with pytest.raises(ValidationError):
        lead(x_handle="not a handle!")


def test_source_url_required() -> None:
    with pytest.raises(ValidationError):
        FounderLead.model_validate(
            {"founder_name": "A", "company": "B", "announced_on": "2026-09-01"}
        )


def test_fit_assessment_bounds() -> None:
    with pytest.raises(ValidationError):
        fit(101)


def test_key_is_stable_slug() -> None:
    assert lead(company="Acme AI, Inc.").key == "acme-ai-inc/jane-doe"


def test_merge_keeps_existing_and_dedupes_incoming() -> None:
    scored = lead(status=LeadStatus.CONTACTED)
    merged, added = merge([scored], [lead(), lead(company="Beta"), lead(company="Beta")])

    assert added == 1
    assert [m.company for m in merged] == ["Acme AI", "Beta"]
    assert merged[0].status is LeadStatus.CONTACTED


def test_rank_orders_by_fit_then_round_and_drops_old_or_skipped() -> None:
    today = date(2026, 10, 4)
    leads = [
        lead(company="Seed", round=Round.SEED),
        lead(company="SeriesA", round=Round.SERIES_A),
        lead(company="HighFit", round=Round.SERIES_B, fit=fit(90)),
        lead(company="Old", announced_on="2026-01-01"),
        lead(company="Skipped", status=LeadStatus.SKIPPED),
    ]

    assert [x.company for x in rank(leads, today, days=90)] == ["HighFit", "Seed", "SeriesA"]


def test_store_round_trip_and_upsert(tmp_path: Path) -> None:
    store = LeadStore(tmp_path / "leads.json")
    store.save([lead(), lead(company="Beta")])

    updated = store.get("acme-ai/jane-doe")
    updated.fit = fit(70)
    store.upsert(updated)

    loaded = store.load()
    assert [x.company for x in loaded] == ["Acme AI", "Beta"]
    assert loaded[0].fit is not None and loaded[0].fit.score == 70


def test_load_inbox_validates(tmp_path: Path) -> None:
    path = tmp_path / "inbox.json"
    path.write_text(json.dumps([{"founder_name": "A", "company": "B"}]), encoding="utf-8")
    with pytest.raises(ValidationError):
        load_inbox(path)
