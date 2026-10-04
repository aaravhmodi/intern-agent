import json
from pathlib import Path

from pydantic import TypeAdapter

from internship_agent.leads.schemas import FounderLead

_LEADS = TypeAdapter(list[FounderLead])


class LeadStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[FounderLead]:
        if not self.path.exists():
            return []
        return _LEADS.validate_json(self.path.read_bytes())

    def save(self, leads: list[FounderLead]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_bytes(_LEADS.dump_json(leads, indent=2))

    def get(self, key: str) -> FounderLead:
        for lead in self.load():
            if lead.key == key:
                return lead
        raise KeyError(key)

    def upsert(self, updated: FounderLead) -> None:
        leads = self.load()
        for i, lead in enumerate(leads):
            if lead.key == updated.key:
                leads[i] = updated
                break
        else:
            leads.append(updated)
        self.save(leads)


def merge(
    existing: list[FounderLead], incoming: list[FounderLead]
) -> tuple[list[FounderLead], int]:
    """Add new leads; never overwrite one already stored (it may be scored or contacted)."""
    known = {lead.key for lead in existing}
    added = {lead.key: lead for lead in incoming if lead.key not in known}
    return [*existing, *added.values()], len(added)


def load_inbox(path: Path) -> list[FounderLead]:
    return _LEADS.validate_python(json.loads(path.read_text(encoding="utf-8")))
