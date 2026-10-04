from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from internship_agent.dashboard import app as dashboard
from internship_agent.leads.schemas import EmailStatus, Lead, LeadStatus, OutreachDraft
from internship_agent.leads.store import LeadStore


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("OPENAI_API_KEY", "")
    LeadStore(tmp_path / "leads.json").save(
        [
            Lead.model_validate(
                {
                    "kind": "posting",
                    "company": "Acme",
                    "posting_title": "SWE Intern",
                    "posting_url": "https://acme.com/jobs/1",
                    "source_url": "https://acme.com/jobs/1",
                    "contact_name": "Jane Doe",
                    "email": "jane@acme.com",
                    "email_status": EmailStatus.PATTERN,
                    "draft": OutreachDraft(
                        x_dm="dm", email_subject="Winter 2027 & you", email_body="Hi Jane"
                    ),
                }
            )
        ]
    )
    return TestClient(dashboard.app)


def test_index_serves_html(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Internship Agent" in response.text


def test_leads_includes_key_and_encoded_mailto(client: TestClient) -> None:
    data = client.get("/api/leads").json()
    lead = data["leads"][0]
    assert lead["key"] == "acme/jane-doe"
    assert lead["mailto"] == "mailto:jane@acme.com?subject=Winter%202027%20%26%20you&body=Hi%20Jane"
    assert data["open_postings"] == 1


def test_marking_applied_triggers_refill(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[int] = []

    def fake_find_more(settings: object, target_open: int) -> list[Lead]:
        calls.append(target_open)
        return []

    monkeypatch.setattr(dashboard, "find_more_postings", fake_find_more)
    response = client.post("/api/status", json={"key": "acme/jane-doe", "status": "applied"})

    assert response.status_code == 200
    assert response.json()["lead"]["status"] == LeadStatus.APPLIED
    assert calls == [15]
    assert client.get("/api/leads").json()["applied"] == 1


def test_skipping_does_not_refill(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(dashboard, "find_more_postings", lambda *a: pytest.fail("refilled"))
    response = client.post("/api/status", json={"key": "acme/jane-doe", "status": "skipped"})
    assert response.status_code == 200


def test_unknown_lead_404(client: TestClient) -> None:
    assert client.post("/api/status", json={"key": "nope", "status": "applied"}).status_code == 404
