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


def test_health_says_busy_while_a_long_job_runs(client: TestClient, tmp_path: Path) -> None:
    from internship_agent.config import get_settings
    from internship_agent.workflows import busy

    assert client.get("/health").json() == {"busy": False}
    with busy(get_settings()):
        assert client.get("/health").json() == {"busy": True}
    assert client.get("/health").json() == {"busy": False}


def test_index_serves_html(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "Winter 2027 Search" in response.text
    assert 'href="/dashboard.css"' in response.text
    css = client.get("/dashboard.css")
    assert css.status_code == 200
    assert css.headers["content-type"].startswith("text/css")
    assert "color-scheme: dark" in css.text


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


def test_finding_people_needs_an_openai_key(client: TestClient) -> None:
    response = client.post("/api/people", json={"key": "acme/jane-doe"})
    assert response.status_code == 400 and "OPENAI_API_KEY" in response.json()["detail"]


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


def test_retry_reopens_only_uncertain_applications(client: TestClient, tmp_path: Path) -> None:
    from datetime import UTC, datetime

    from internship_agent.leads.schemas import ApplicationPrep

    store = LeadStore(tmp_path / "leads.json")
    lead = store.load()[0]
    lead.application = ApplicationPrep(prepared_at=datetime.now(UTC), source="form", answers=[])
    assert client.post("/api/application/retry", json={"key": lead.key}).status_code == 400
    lead.application.submission_status = "uncertain"
    store.upsert(lead)
    response = client.post("/api/application/retry", json={"key": lead.key})
    assert response.json()["lead"]["application"]["submission_status"] == "pending"


def test_auto_apply_prepares_then_submits(
    client: TestClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[tuple[str, bool]] = []
    store = LeadStore(tmp_path / "leads.json")
    lead = store.load()[0]

    def prepare(_s: object, key: str, *, accept_posting_term: bool = False) -> None:
        calls.append(("prepare", accept_posting_term))

    def submit(_s: object, key: str, *, accept_posting_term: bool = False) -> Lead:
        calls.append(("submit", accept_posting_term))
        return lead

    monkeypatch.setattr(dashboard, "prepare_application", prepare)
    monkeypatch.setattr(dashboard, "submit_application", submit)
    assert client.post("/api/application/auto", json={"key": lead.key}).status_code == 200
    # A job you picked by hand is never blocked by the January-April filter.
    assert calls == [("prepare", False), ("submit", True)]

    # Outside January-April: answers are re-prepared to the posting's own term.
    calls.clear()
    lead.posting_text = "This is an 8-month co-op term (January - August 2027)."
    store.upsert(lead)
    assert client.post("/api/application/auto", json={"key": lead.key}).status_code == 200
    assert calls == [("prepare", True), ("submit", True)]


def test_confirmation_screenshot_is_served_as_proof(
    client: TestClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from internship_agent.applications.browser import screenshot_path

    monkeypatch.setenv("APPLICATION_BROWSER_DIR", str(tmp_path / "application-browser"))
    lead = LeadStore(tmp_path / "leads.json").load()[0]
    url = "/api/application/proof"
    assert client.get(url, params={"key": lead.key}).status_code == 404
    assert client.get("/api/leads").json()["leads"][0]["has_proof"] is False
    path = screenshot_path(tmp_path / "application-browser", lead, "confirmations")
    path.parent.mkdir(parents=True)
    path.write_bytes(b"\x89PNG fake")
    response = client.get(url, params={"key": lead.key})
    assert response.status_code == 200 and response.headers["content-type"] == "image/png"
    assert client.get("/api/leads").json()["leads"][0]["has_proof"] is True


def test_favicon_is_served_for_every_path_browsers_ask_for(client: TestClient) -> None:
    for path, kind in (
        ("/favicon.svg", "image/svg+xml"),
        ("/favicon.ico", "image/png"),
        ("/apple-touch-icon.png", "image/png"),
    ):
        response = client.get(path)
        assert response.status_code == 200 and response.headers["content-type"] == kind
        assert response.content
    assert client.get("/favicon.svg").text.startswith("<svg")
    page = client.get("/").text
    assert 'rel="icon"' in page and 'rel="apple-touch-icon"' in page
