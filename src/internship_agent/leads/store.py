import json
from pathlib import Path

from pydantic import TypeAdapter

from internship_agent.leads.schemas import Lead

_LEADS = TypeAdapter(list[Lead])


class LeadStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[Lead]:
        if not self.path.exists():
            return []
        return _LEADS.validate_json(self.path.read_bytes())

    def save(self, leads: list[Lead]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_bytes(_LEADS.dump_json(leads, indent=2))

    def get(self, key: str) -> Lead:
        for lead in self.load():
            if lead.key == key:
                return lead
        raise KeyError(key)

    def upsert(self, updated: Lead) -> None:
        leads = self.load()
        for i, lead in enumerate(leads):
            if lead.key == updated.key:
                leads[i] = updated
                break
        else:
            leads.append(updated)
        self.save(leads)


def merge(existing: list[Lead], incoming: list[Lead]) -> tuple[list[Lead], int]:
    """Add new leads; never overwrite one already stored (it may be scored or contacted)."""
    known = {lead.key for lead in existing}
    added = {lead.key: lead for lead in incoming if lead.key not in known}
    return [*existing, *added.values()], len(added)


def load_inbox(path: Path) -> list[Lead]:
    return _LEADS.validate_python(json.loads(path.read_text(encoding="utf-8")))
