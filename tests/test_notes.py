from pathlib import Path
from typing import Any

import pytest

from internship_agent import workflows
from internship_agent.ai import NoteResult, PreferenceDraft, format_preferences
from internship_agent.config import Settings
from internship_agent.leads.preferences import PreferenceStore, apply_violations
from internship_agent.leads.schemas import Lead, LeadStatus, PreferenceEffect
from internship_agent.leads.store import LeadStore
from internship_agent.sources.posting_text import html_to_text


def posting(**overrides: Any) -> Lead:
    data: dict[str, Any] = {
        "kind": "posting",
        "company": "Acme",
        "posting_title": "SWE Intern",
        "posting_url": "https://acme.com/jobs/1",
        "source_url": "https://acme.com/jobs/1",
    }
    return Lead.model_validate({**data, **overrides})


def test_preference_store_dedupes_and_removes(tmp_path: Path) -> None:
    store = PreferenceStore(tmp_path / "prefs.json")
    first = store.add("Skip roles that require French", PreferenceEffect.SKIP, "needs French")
    assert first is not None
    assert store.add("skip roles that require french!", PreferenceEffect.SKIP) is None
    assert [p.rule for p in store.load()] == ["Skip roles that require French"]
    assert store.remove(first.id) and store.load() == []
    assert not store.remove("missing")


def test_apply_violations_skips_only_for_skip_rules(tmp_path: Path) -> None:
    store = PreferenceStore(tmp_path / "prefs.json")
    french = store.add("Skip roles that require French", PreferenceEffect.SKIP)
    banks = store.add("Prefer fewer banks", PreferenceEffect.DOWNRANK)
    assert french and banks
    prefs = store.load()

    lead = posting()
    assert not apply_violations(lead, prefs, [banks.id, "unknown"])
    assert lead.status is LeadStatus.NEW

    assert apply_violations(lead, prefs, [french.id])
    assert lead.status is LeadStatus.SKIPPED
    assert "require French" in lead.notes[-1].text


def test_apply_violations_never_touches_applied_leads(tmp_path: Path) -> None:
    store = PreferenceStore(tmp_path / "prefs.json")
    french = store.add("Skip roles that require French", PreferenceEffect.SKIP)
    assert french
    lead = posting(status=LeadStatus.APPLIED)
    assert not apply_violations(lead, store.load(), [french.id])
    assert lead.status is LeadStatus.APPLIED and lead.notes == []


def test_format_preferences() -> None:
    assert format_preferences([]) == "none yet"


def test_html_to_text_drops_scripts_and_tags() -> None:
    page = "<style>x{}</style><p>French&nbsp;required</p><script>alert(1)</script>"
    assert html_to_text(page) == "French required"


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    return Settings(data_dir=tmp_path, openai_api_key="test", _env_file=None)  # type: ignore[call-arg]


def test_handle_note_saves_note_status_and_learns(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    LeadStore(settings.data_dir / "leads.json").save([posting()])
    result = NoteResult(
        lead_note="Posting requires fluent French.",
        status_change="skipped",
        new_preferences=[PreferenceDraft(rule="Skip roles that require French", effect="skip")],
        reply="Saved and skipped.",
    )
    monkeypatch.setattr(workflows, "interpret_note", lambda *a: result)

    outcome = workflows.handle_note(
        settings, "this job needs french, not applying", "acme/swe-intern"
    )

    lead = LeadStore(settings.data_dir / "leads.json").get("acme/swe-intern")
    assert lead.status is LeadStatus.SKIPPED
    assert lead.notes[-1].text == "Posting requires fluent French."
    assert outcome.status_changed == "skipped"
    assert [p.rule for p in outcome.learned] == ["Skip roles that require French"]

    # The same rule is not learned twice.
    again = workflows.handle_note(settings, "same thing", "acme/swe-intern")
    assert again.learned == [] and again.status_changed is None


def test_general_note_without_lead_only_learns(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    result = NoteResult(
        lead_note=None,
        status_change="skipped",
        new_preferences=[PreferenceDraft(rule="Prefer early-stage AI startups", effect="boost")],
        reply="Noted.",
    )
    monkeypatch.setattr(workflows, "interpret_note", lambda *a: result)
    outcome = workflows.handle_note(settings, "I like early AI startups", None)
    assert outcome.lead is None and outcome.status_changed is None
    assert PreferenceStore(settings.data_dir / "preferences.json").load()[0].effect == "boost"
