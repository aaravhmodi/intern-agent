import json
from datetime import date
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from internship_agent.leads.emails import guess_email
from internship_agent.leads.export import render_outreach
from internship_agent.leads.ranking import rank
from internship_agent.leads.schemas import (
    EmailStatus,
    FitAssessment,
    Lead,
    LeadKind,
    LeadStatus,
    OutreachDraft,
    Round,
    Verdict,
)
from internship_agent.leads.store import LeadStore, load_inbox, merge

TODAY = date(2026, 10, 4)


def lead(**overrides: Any) -> Lead:
    data: dict[str, Any] = {
        "contact_name": "Jane Doe",
        "company": "Acme AI",
        "announced_on": "2026-09-20",
        "source_url": "https://example.com/acme-raises",
    }
    return Lead.model_validate({**data, **overrides})


def posting(**overrides: Any) -> Lead:
    data: dict[str, Any] = {
        "kind": "posting",
        "company": "Bigco",
        "posting_title": "Software Engineering Intern, Winter 2027",
        "posting_url": "https://bigco.com/jobs/1",
        "source_url": "https://bigco.com/jobs/1",
    }
    return Lead.model_validate({**data, **overrides})


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
        Lead.model_validate({"contact_name": "A", "company": "B", "announced_on": "2026-09-01"})


def test_kind_specific_fields_required() -> None:
    with pytest.raises(ValidationError, match="announced_on"):
        lead(announced_on=None)
    with pytest.raises(ValidationError, match="posting_url"):
        posting(posting_url=None)


def test_email_needs_status_and_valid_format() -> None:
    with pytest.raises(ValidationError, match="email_status"):
        lead(email="jane@acme.ai")
    with pytest.raises(ValidationError, match="invalid email"):
        lead(email="jane-at-acme", email_status="pattern")
    assert lead(email=" Jane@Acme.AI ", email_status="pattern").email == "jane@acme.ai"


def test_fit_assessment_bounds() -> None:
    with pytest.raises(ValidationError):
        fit(101)


def test_key_is_stable_slug() -> None:
    assert lead(company="Acme AI, Inc.").key == "acme-ai-inc/jane-doe"
    assert posting().key == "bigco/software-engineering-intern-winter-2027"


def test_merge_keeps_existing_and_dedupes_incoming() -> None:
    contacted = lead(status=LeadStatus.CONTACTED)
    merged, added = merge([contacted], [lead(), lead(company="Beta"), lead(company="Beta")])

    assert added == 1
    assert [m.company for m in merged] == ["Acme AI", "Beta"]
    assert merged[0].status is LeadStatus.CONTACTED


def test_rank_orders_by_fit_then_round_and_drops_closed() -> None:
    leads = [
        lead(company="Seed", round=Round.SEED),
        lead(company="SeriesA", round=Round.SERIES_A),
        lead(company="HighFit", round=Round.SERIES_B, fit=fit(90)),
        lead(company="Old", announced_on="2026-01-01"),
        lead(company="Skipped", status=LeadStatus.SKIPPED),
        posting(company="OpenPosting", fit=fit(80)),
        posting(company="Expired", deadline="2026-09-30"),
    ]

    assert [x.company for x in rank(leads, TODAY, days=90)] == [
        "HighFit",
        "OpenPosting",
        "Seed",
        "SeriesA",
    ]


def test_store_round_trip_and_upsert(tmp_path: Path) -> None:
    store = LeadStore(tmp_path / "leads.json")
    store.save([lead(), posting()])

    updated = store.get("acme-ai/jane-doe")
    updated.fit = fit(70)
    store.upsert(updated)

    loaded = store.load()
    assert [x.kind for x in loaded] == [LeadKind.FOUNDER, LeadKind.POSTING]
    assert loaded[0].fit is not None and loaded[0].fit.score == 70


def test_load_inbox_validates(tmp_path: Path) -> None:
    path = tmp_path / "inbox.json"
    path.write_text(json.dumps([{"contact_name": "A", "company": "B"}]), encoding="utf-8")
    with pytest.raises(ValidationError):
        load_inbox(path)


@pytest.mark.parametrize(
    ("pattern", "expected"),
    [
        ("first", "jose@acme.ai"),
        ("first.last", "jose.garcia@acme.ai"),
        ("flast", "jgarcia@acme.ai"),
        ("firstlast", "josegarcia@acme.ai"),
        ("firstl", "joseg@acme.ai"),
    ],
)
def test_guess_email(pattern: str, expected: str) -> None:
    assert guess_email("José María García", "www.Acme.ai", pattern) == expected


def test_guess_email_rejects_bad_input() -> None:
    with pytest.raises(ValueError):
        guess_email("Cher", "acme.ai", "first.last")
    with pytest.raises(ValueError):
        guess_email("Jane Doe", "acme.ai", "nope")


def test_render_outreach_flags_unverified_emails_and_skips_undrafted() -> None:
    draft = OutreachDraft(x_dm="dm", email_subject="Winter 2027 intern", email_body="Hi Jane")
    text = render_outreach(
        [
            lead(email="jane@acme.ai", email_status=EmailStatus.PATTERN, draft=draft),
            lead(company="NoDraft"),
        ]
    )
    assert "UNVERIFIED" in text and "Winter 2027 intern" in text
    assert "NoDraft" not in text
