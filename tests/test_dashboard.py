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
    monkeypatch.setenv("GMAIL_ADDRESS", "")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "")
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
    assert "Winter 2027 Search" in response.text


def test_leads_includes_key_and_segment(client: TestClient) -> None:
    data = client.get("/api/leads").json()
    lead = data["leads"][0]
    assert lead["key"] == "acme/jane-doe"
    assert lead["segment"] is None
    assert data["open_postings"] == 1
    assert data["sender"] is None


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
    statuses = [x["status"] for x in client.get("/api/leads").json()["leads"]]
    assert statuses == ["applied"]


def test_skipping_does_not_refill(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(dashboard, "find_more_postings", lambda *a: pytest.fail("refilled"))
    response = client.post("/api/status", json={"key": "acme/jane-doe", "status": "skipped"})
    assert response.status_code == 200


def test_unknown_lead_404(client: TestClient) -> None:
    assert client.post("/api/status", json={"key": "nope", "status": "applied"}).status_code == 404


def test_cross_site_post_is_blocked(client: TestClient) -> None:
    response = client.post(
        "/api/status",
        json={"key": "acme/jane-doe", "status": "applied"},
        headers={"Origin": "https://evil.example"},
    )
    assert response.status_code == 403


def test_foreign_host_is_blocked(client: TestClient) -> None:
    assert client.get("/api/leads", headers={"Host": "attacker.example"}).status_code == 403


def test_send_refused_when_gmail_not_configured(client: TestClient) -> None:
    response = client.post(
        "/api/send",
        json={"key": "acme/jane-doe", "to": "jane@acme.com", "subject": "Hi", "body": "Hello"},
    )
    assert response.status_code == 400
    assert "GMAIL" in response.json()["detail"]


def test_send_guess_requires_confirmation_then_records(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    from internship_agent import mailer

    monkeypatch.setenv("GMAIL_ADDRESS", "me@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "app-password")
    sent: list[str] = []
    monkeypatch.setattr(mailer, "send", lambda message, sender, pw: sent.append(message["To"]))
    body = {
        "key": "acme/jane-doe",
        "to": "jane@acme.com",
        "subject": "Hi",
        "body": "Hello",
        "attach_resume": False,
    }

    blocked = client.post("/api/send", json=body)
    assert blocked.status_code == 400 and "guess" in blocked.json()["detail"]
    assert sent == []

    ok = client.post("/api/send", json={**body, "confirm_unverified": True})
    assert ok.status_code == 200
    assert ok.json()["lead"]["status"] == "contacted"
    assert sent == ["jane@acme.com"]

    again = client.post("/api/send", json={**body, "confirm_unverified": True})
    assert again.status_code == 400 and "Already emailed" in again.json()["detail"]
    assert sent == ["jane@acme.com"]
