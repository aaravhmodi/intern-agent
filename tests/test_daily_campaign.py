from datetime import UTC, datetime

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads.schemas import ApplicationPrep, FitAssessment, Lead


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

    report = workflows.daily(Settings(_env_file=None), target_submissions=2)
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
