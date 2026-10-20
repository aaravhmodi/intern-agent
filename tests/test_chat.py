import json
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest
from fastapi.testclient import TestClient

from internship_agent import chat
from internship_agent.config import Settings
from internship_agent.dashboard import app as dashboard
from internship_agent.opportunities.schemas import Opportunity
from internship_agent.opportunities.store import OpportunityStore

REPOS = [
    {
        "name": "rag-packing",
        "html_url": "https://github.com/me/rag-packing",
        "fork": False,
        "language": "Python",
        "pushed_at": "2026-07-05T00:00:00Z",
        "default_branch": "main",
        "description": "Budget-constrained multi-hop RAG packing experiments",
    },
    {"name": "someone-else", "html_url": "https://github.com/me/x", "fork": True},
]


def _settings(tmp_path: Path) -> Settings:
    context = tmp_path / "context.md"
    context.write_text("Founding engineer at Enerzen.", encoding="utf-8")
    return Settings(
        _env_file=None,
        data_dir=tmp_path,
        database_url=None,
        candidate_context_path=context,
        github_user="me",
        website_url="https://me.dev",
        website_pages=["/experience"],
    )


def fake_get(url: str) -> str:
    if url.startswith("https://api.github.com/"):
        return json.dumps(REPOS)
    if url.endswith("README.md"):
        return "# RAG packing\nPacks passages under a token budget."
    if url == "https://me.dev/experience":
        return "<html><script>x()</script><h1>experience</h1><p>Upside Robotics intern</p></html>"
    raise OSError("unreachable")


def test_profile_has_context_resume_website_and_github(tmp_path: Path) -> None:
    text = chat.build_profile(_settings(tmp_path), "RESUME TEXT", get=fake_get)
    assert "Founding engineer at Enerzen." in text and "RESUME TEXT" in text
    assert "experience Upside Robotics intern" in text and "x()" not in text
    assert "- rag-packing (https://github.com/me/rag-packing; Python; pushed 2026-07-05)" in text
    assert "Packs passages under a token budget." in text
    assert "someone-else" not in text  # forks are left out


def test_a_source_that_fails_is_noted_not_fatal(tmp_path: Path) -> None:
    def broken(url: str) -> str:
        raise OSError("offline")

    text = chat.build_profile(_settings(tmp_path), "R", get=broken)
    assert "(could not load: offline)" in text and "Founding engineer" in text


def test_search_opportunities_finds_by_keyword(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    OpportunityStore(settings).add_new(
        [
            Opportunity(
                kind="conference",
                title="PyCon US",
                url="https://pycon.org",
                source="t",
                starts_on=date(2027, 5, 1),
                topics=["python"],
            ),
            Opportunity(kind="hackathon", title="Hack Western", url="https://hw.dev", source="t"),
        ]
    )
    found = json.loads(chat.search_opportunities(settings, "python conference"))
    assert [o["title"] for o in found] == ["PyCon US"]
    assert chat.search_opportunities(settings, "quantum") == "No stored opportunity matches."


def test_read_repo_returns_the_readme_or_says_it_is_missing(tmp_path: Path) -> None:
    settings = _settings(tmp_path)
    assert "token budget" in chat.read_repo(settings, "RAG-Packing", get=fake_get)
    assert chat.read_repo(settings, "nope", get=fake_get) == "No public repository named 'nope'."


class FakeResponses:
    """First asks for a tool, then answers using what the tool returned."""

    def __init__(self) -> None:
        self.inputs: list[list[Any]] = []

    def create(self, **kw: Any) -> SimpleNamespace:
        self.inputs.append(list(kw["input"]))
        if len(self.inputs) == 1:
            call = SimpleNamespace(
                type="function_call",
                name="search_opportunities",
                arguments='{"query": "pycon"}',
                call_id="c1",
            )
            return SimpleNamespace(output=[call], output_text="", usage=None)
        tool_output = kw["input"][-1]["output"]
        return SimpleNamespace(output=[], output_text=f"Found: {tool_output}", usage=None)


def test_answer_runs_tools_and_grounds_the_system_prompt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    settings = _settings(tmp_path)
    OpportunityStore(settings).add_new(
        [Opportunity(kind="conference", title="PyCon US", url="https://pycon.org", source="t")]
    )
    monkeypatch.setattr(chat, "profile", lambda s, r: "PROFILE TEXT")
    responses = FakeResponses()
    client = SimpleNamespace(responses=responses)
    reply = chat.answer(
        settings,
        client,  # type: ignore[arg-type]
        [chat.ChatMessage(role="user", content="Talks at PyCon?")],
        "https://pycon.org",
        "R",
    )
    assert reply.startswith("Found: [") and "PyCon US" in reply
    system = responses.inputs[0][0]["content"]
    assert "PROFILE TEXT" in system and '"title":"PyCon US"' in system  # the selected item


def test_profile_is_cached_for_a_day(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls = []
    monkeypatch.setattr(chat, "build_profile", lambda s, r: calls.append(1) or "P")
    settings = _settings(tmp_path)
    assert chat.profile(settings, "R") == chat.profile(settings, "R") == "P"
    assert len(calls) == 1


def test_chat_endpoint_needs_a_question(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("DATABASE_URL", "")
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    client = TestClient(dashboard.app)
    assert client.post("/api/chat", json={"messages": []}).status_code == 400
    monkeypatch.setattr(dashboard, "resume_text", lambda s: "R")
    monkeypatch.setattr(dashboard.chat, "answer", lambda *a, **k: "Hi")
    ok = client.post("/api/chat", json={"messages": [{"role": "user", "content": "hello"}]})
    assert ok.json() == {"reply": "Hi"}
