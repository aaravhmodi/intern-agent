from pydantic import TypeAdapter

from internship_agent import db
from internship_agent.config import Settings
from internship_agent.opportunities.schemas import Opportunity

_ALL = TypeAdapter(list[Opportunity])


class OpportunityStore:
    """Table intern_agent_opportunities when DATABASE_URL is set; else data/opportunities.json."""

    def __init__(self, settings: Settings) -> None:
        self.table = db.table(settings, "opportunities")
        self.path = settings.data_dir / "opportunities.json"

    def load(self) -> list[Opportunity]:
        if self.table:
            return [Opportunity.model_validate_json(data) for _, data in self.table.rows()]
        return _ALL.validate_json(self.path.read_bytes()) if self.path.exists() else []

    def get(self, key: str) -> Opportunity:
        for item in self.load():
            if item.key == key:
                return item
        raise KeyError(key)

    def _save(self, changed: list[Opportunity], everything: list[Opportunity]) -> None:
        if self.table:
            self.table.put([(o.key, o.model_dump_json()) for o in changed])
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_bytes(_ALL.dump_json(everything, indent=2))
        tmp.replace(self.path)

    def upsert(self, updated: Opportunity) -> None:
        items = self.load()
        for i, item in enumerate(items):
            if item.key == updated.key:
                items[i] = updated
                break
        else:
            items.append(updated)
        self._save([updated], items)

    def add_new(self, found: list[Opportunity]) -> list[Opportunity]:
        """Store events not seen before; never overwrite one (it may have a status or plan)."""
        items = self.load()
        known: set[str] = set().union(*(o.identity for o in items)) if items else set()
        added = []
        for item in found:
            if item.identity & known:
                continue
            known |= item.identity
            added.append(item)
        if added:
            self._save(added, [*items, *added])
        return added
