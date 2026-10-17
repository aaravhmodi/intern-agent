import json
from datetime import UTC, datetime
from types import SimpleNamespace

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads.answers import AnswerBank
from internship_agent.leads.schemas import (
    ApplicationPrep,
    FitAssessment,
    FormQuestion,
    Lead,
    PreparedAnswer,
)


def test_campaign_stops_after_target_confirmed_submissions(monkeypatch) -> None:
    leads = [
        Lead(
            kind="posting",
            company=f"Company {i}",
            posting_title="Software Intern",
            posting_url=f"https://jobs.ashbyhq.com/company{i}/intern",
            source_url=f"https://jobs.ashbyhq.com/company{i}/intern",
            fit=FitAssessment(
                score=90 - i, verdict="strong", reasons=[], concerns=[], talking_points=[]
            ),
        )
        for i in range(3)
    ]

    class Store:
        def load(self) -> list[Lead]:
            return leads

        def save(self, _: list[Lead]) -> None:
            pass

    submitted: list[str] = []

    def prepare(_: Settings, key: str) -> Lead:
        lead = next(item for item in leads if item.key == key)
        lead.application = ApplicationPrep(prepared_at=datetime.now(UTC), source="form", answers=[])
        return lead

    def submit(_: Settings, key: str) -> Lead:
        lead = next(item for item in leads if item.key == key)
        assert lead.application is not None
        lead.application.submission_status = "submitted"
        submitted.append(key)
        return lead

    monkeypatch.setattr(workflows, "lead_store", lambda _: Store())
    monkeypatch.setattr(workflows.simplify, "fetch", lambda: "")
    monkeypatch.setattr(workflows.simplify, "parse", lambda _: [])
    monkeypatch.setattr(workflows.simplify, "matching", lambda _, regions: [])
    monkeypatch.setattr(workflows, "refill", lambda existing, candidates, target: (existing, []))
    monkeypatch.setattr(workflows, "score", lambda settings, postings: [])
    monkeypatch.setattr(workflows, "prepare_application", prepare)
    monkeypatch.setattr(workflows, "submit_application", submit)

    report = workflows.daily(
        Settings(_env_file=None, auto_submit_applications=True), target_submissions=2
    )
    assert report.submitted == report.attempted == len(submitted) == 2
    assert len(report.prepared) == 2


def test_scrape_stores_every_matching_non_workday_posting(monkeypatch) -> None:
    candidates = [
        Lead(
            kind="posting",
            company=f"Company {i}",
            posting_title="Software Intern",
            posting_url=f"https://jobs.ashbyhq.com/company{i}/intern",
            source_url=f"https://jobs.ashbyhq.com/company{i}/intern",
        )
        for i in range(3)
    ]
    candidates.append(
        Lead(
            kind="posting",
            company="Workday Company",
            posting_title="Software Intern",
            posting_url="https://example.myworkdayjobs.com/intern",
            source_url="https://example.myworkdayjobs.com/intern",
        )
    )

    class Store:
        items: list[Lead] = []

        def load(self) -> list[Lead]:
            return self.items

        def save(self, items: list[Lead]) -> None:
            self.items = items

    store = Store()
    monkeypatch.setattr(workflows, "lead_store", lambda _: store)
    monkeypatch.setattr(workflows.simplify, "fetch", lambda: "")
    monkeypatch.setattr(workflows.simplify, "parse", lambda _: [])
    monkeypatch.setattr(workflows.simplify, "matching", lambda _, regions: candidates)
    monkeypatch.setattr(workflows.simplify, "to_lead", lambda candidate: candidate)

    new = workflows.scrape_jobs(Settings(_env_file=None))
    assert len(new) == len(store.items) == 3


def test_pre_submit_block_can_be_retried_but_uncertain_cannot() -> None:
    blocked = ApplicationPrep(
        prepared_at=datetime.now(UTC),
        source="form",
        answers=[],
        submission_status="blocked",
        submission_detail="CAPTCHA detected; manual completion required",
    )
    uncertain = blocked.model_copy(
        update={
            "submission_status": "uncertain",
            "submission_detail": "CAPTCHA appeared after submit; verify manually",
        }
    )
    assert workflows._retryable_block(blocked)
    assert not workflows._retryable_block(uncertain)


def test_incompatible_eight_month_term_is_rejected() -> None:
    lead = Lead(
        kind="posting",
        company="Bree",
        source_url="https://jobs.ashbyhq.com/bree/test",
        posting_url="https://jobs.ashbyhq.com/bree/test",
        posting_title="Software Engineer Co-op",
        posting_text="This is an 8-month co-op term. (January - August 2027)",
    )
    assert workflows._incompatible_term(lead)
    assert workflows._incompatible_term(
        lead.model_copy(update={"posting_title": "Intern (Fall/Winter 2026)", "posting_text": ""})
    )
    assert workflows._incompatible_term(
        lead.model_copy(update={"posting_text": "8 - 12 month work-term beginning January 2027"})
    )
    assert workflows._incompatible_term(
        lead.model_copy(update={"posting_text": "Cycle: January - June 2027"})
    )
    assert workflows._incompatible_term(
        lead.model_copy(update={"posting_text": "12-week internship starting January 2027"})
    )
    assert not workflows._incompatible_term(
        lead.model_copy(update={"posting_text": "A 16-week internship (JAN - APRIL)."})
    )


def test_saving_answers_preserves_uncertain_submission(monkeypatch, tmp_path) -> None:
    lead = Lead(
        kind="posting",
        company="Example",
        source_url="https://jobs.ashbyhq.com/example/test",
        posting_url="https://jobs.ashbyhq.com/example/test",
        application=ApplicationPrep(
            prepared_at=datetime.now(UTC),
            source="form",
            answers=[],
            submission_status="uncertain",
            submission_detail="Submit was clicked but no confirmation was detected",
        ),
    )

    class Store:
        def get(self, _key: str) -> Lead:
            return lead

        def upsert(self, _lead: Lead) -> None:
            pass

    monkeypatch.setattr(workflows, "lead_store", lambda _settings: Store())
    monkeypatch.setattr(workflows, "answer_bank", lambda _settings: AnswerBank(tmp_path / "bank"))
    saved = workflows.save_answers(Settings(_env_file=None), lead.key, {})
    assert saved.application is not None
    assert saved.application.submission_status == "uncertain"
    assert "no confirmation" in saved.application.submission_detail


def test_refresh_uses_saved_answer_without_regenerating_cover_letter(monkeypatch, tmp_path) -> None:
    lead = Lead(
        kind="posting",
        company="Example",
        source_url="https://jobs.ashbyhq.com/example/test",
        posting_url="https://jobs.ashbyhq.com/example/test",
        application=ApplicationPrep(
            prepared_at=datetime.now(UTC),
            source="form",
            cover_letter="Tailored letter",
            answers=[
                PreparedAnswer(question=FormQuestion(label="Can you relocate?", required=True))
            ],
            submission_status="blocked",
            submission_detail="Required answers need your input",
        ),
    )

    class Store:
        def get(self, _key: str) -> Lead:
            return lead

        def upsert(self, _lead: Lead) -> None:
            pass

    bank = AnswerBank(tmp_path / "bank.json")
    bank.remember("Can you relocate?", "Yes")
    monkeypatch.setattr(workflows, "lead_store", lambda _settings: Store())
    monkeypatch.setattr(workflows, "answer_bank", lambda _settings: bank)
    refreshed = workflows.refresh_saved_application(Settings(_env_file=None), lead.key)
    assert refreshed.application is not None
    assert refreshed.application.answers[0].answer == "Yes"
    assert refreshed.application.cover_letter == "Tailored letter"
    assert refreshed.application.submission_status == "pending"


def test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(monkeypatch) -> None:
    leads = [
        Lead(
            kind="posting",
            company=f"Company {i}",
            source_url=f"https://jobs.ashbyhq.com/company{i}/intern",
            posting_url=f"https://jobs.ashbyhq.com/company{i}/intern",
            posting_title="Software Intern",
            fit=(
                FitAssessment(
                    score=80, verdict="strong", reasons=[], concerns=[], talking_points=[]
                )
                if i < 2
                else None
            ),
        )
        for i in range(3)
    ]
    leads.append(
        Lead(
            kind="posting",
            company="Cached",
            source_url="https://jobs.ashbyhq.com/cached/intern",
            posting_url="https://jobs.ashbyhq.com/cached/intern",
            posting_title="Software Intern",
            fit=FitAssessment(
                score=75, verdict="strong", reasons=[], concerns=[], talking_points=[]
            ),
            application=ApplicationPrep(
                prepared_at=datetime.now(UTC),
                source="common",
                cover_letter="Saved letter",
                answers=[],
            ),
        )
    )

    class Store:
        def load(self) -> list[Lead]:
            return leads

    scored: list[str] = []
    prepared: list[str] = []

    def score_new(_settings: Settings, candidates: list[Lead]) -> list[Lead]:
        scored.extend(lead.key for lead in candidates)
        for lead in candidates:
            lead.fit = FitAssessment(
                score=70, verdict="possible", reasons=[], concerns=[], talking_points=[]
            )
        return []

    def prepare(_settings: Settings, key: str) -> Lead:
        prepared.append(key)
        return next(lead for lead in leads if lead.key == key)

    monkeypatch.setattr(workflows, "scrape_jobs", lambda _settings, _log: [])
    monkeypatch.setattr(workflows, "lead_store", lambda _settings: Store())
    monkeypatch.setattr(workflows, "score", score_new)
    monkeypatch.setattr(workflows, "prepare_application", prepare)
    monkeypatch.setattr(
        workflows,
        "refresh_saved_application",
        lambda _settings, key: next(lead for lead in leads if lead.key == key),
    )
    report = workflows.daily(Settings(_env_file=None, auto_submit_applications=False))
    assert scored == [leads[2].key]
    assert len(prepared) == 3
    assert len(report.prepared) == 4


def test_usage_log_contains_counts_without_prompt_content(tmp_path) -> None:
    settings = Settings(_env_file=None, data_dir=tmp_path)
    usage = SimpleNamespace(
        input_tokens=100,
        output_tokens=20,
        input_tokens_details=SimpleNamespace(cached_tokens=30),
    )
    workflows._record_openai_usage(settings, "score", "gpt-6-luna", usage)
    record = json.loads((tmp_path / "openai-usage.jsonl").read_text())
    assert record["input_tokens"] == 100
    assert record["cached_input_tokens"] == 30
    assert record["output_tokens"] == 20
    assert record["estimated_usd"] == 0.0000173
    assert set(record) == {
        "at",
        "operation",
        "model",
        "input_tokens",
        "cached_input_tokens",
        "output_tokens",
        "estimated_usd",
    }
