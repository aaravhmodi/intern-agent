import json
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from pydantic import TypeAdapter

from internship_agent.leads.schemas import Lead

_LEADS = TypeAdapter(list[Lead])
_TRACKING_PARAMS = {"ref", "src", "source", "gh_src", "embed"}


class LeadStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[Lead]:
        if not self.path.exists():
            return []
        return _LEADS.validate_json(self.path.read_bytes())

    def save(self, leads: list[Lead]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_bytes(_LEADS.dump_json(leads, indent=2))
        tmp.replace(self.path)

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


def normalize_url(url: str) -> str:
    """Canonical form of a posting URL so the same job from two sources dedupes."""
    parts = urlsplit(url.strip())
    query = [
        (k, v)
        for k, v in parse_qsl(parts.query)
        if not k.startswith("utm_") and k not in _TRACKING_PARAMS
    ]
    path = parts.path.rstrip("/")
    for suffix in ("/application", "/apply"):
        path = path.removesuffix(suffix)
    return urlunsplit(("https", parts.netloc.lower(), path, urlencode(query), ""))


def _identity(lead: Lead) -> set[str]:
    ids = {lead.key}
    if lead.posting_url:
        ids.add(normalize_url(lead.posting_url))
    return ids


def merge(existing: list[Lead], incoming: list[Lead]) -> tuple[list[Lead], int]:
    """Add new leads; never overwrite one already stored (it may be scored or contacted).

    A lead is a duplicate if its key or its normalized posting URL is already known.
    """
    known: set[str] = set().union(*(_identity(lead) for lead in existing)) if existing else set()
    added: list[Lead] = []
    for lead in incoming:
        ids = _identity(lead)
        if ids & known:
            continue
        known |= ids
        added.append(lead)
    return [*existing, *added], len(added)


def load_inbox(path: Path) -> list[Lead]:
    return _LEADS.validate_python(json.loads(path.read_text(encoding="utf-8")))
