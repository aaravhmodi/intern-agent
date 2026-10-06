"""Rules learned from the user's notes, stored locally and applied deterministically."""

import re
import uuid
from datetime import UTC, datetime
from pathlib import Path

from pydantic import TypeAdapter

from internship_agent.leads.schemas import (
    Lead,
    LeadStatus,
    Note,
    Preference,
    PreferenceEffect,
)

_PREFS = TypeAdapter(list[Preference])


def _normalize(rule: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", rule.lower()).strip()


class PreferenceStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[Preference]:
        if not self.path.exists():
            return []
        return _PREFS.validate_json(self.path.read_bytes())

    def save(self, prefs: list[Preference]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_bytes(_PREFS.dump_json(prefs, indent=2))

    def add(self, rule: str, effect: PreferenceEffect, source_note: str = "") -> Preference | None:
        """Add a rule unless an equivalent one exists. Returns the new rule, or None."""
        prefs = self.load()
        if any(_normalize(p.rule) == _normalize(rule) for p in prefs):
            return None
        pref = Preference(
            id=uuid.uuid4().hex[:8],
            rule=rule.strip(),
            effect=effect,
            created_at=datetime.now(UTC),
            source_note=source_note[:500],
        )
        self.save([*prefs, pref])
        return pref

    def remove(self, pref_id: str) -> bool:
        prefs = self.load()
        kept = [p for p in prefs if p.id != pref_id]
        self.save(kept)
        return len(kept) != len(prefs)


def apply_violations(lead: Lead, prefs: list[Preference], violated_ids: list[str]) -> bool:
    """Skip a lead that breaks a 'skip' rule, recording why. Returns True if skipped.

    Leads you already applied to or contacted are never changed.
    """
    if lead.status in (LeadStatus.APPLIED, LeadStatus.CONTACTED, LeadStatus.SKIPPED):
        return False
    by_id = {p.id: p for p in prefs}
    broken = [by_id[i] for i in violated_ids if i in by_id]
    skip_rules = [p for p in broken if p.effect is PreferenceEffect.SKIP]
    if not skip_rules:
        return False
    lead.status = LeadStatus.SKIPPED
    reasons = "; ".join(p.rule for p in skip_rules)
    lead.notes.append(Note(at=datetime.now(UTC), text=f"Auto-skipped by your rule: {reasons}"))
    return True
