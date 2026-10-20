"""This project's tables in the shared `projects` Postgres database.

Every table is intern_agent_<name>(id, key, data jsonb): id keeps the order rows were
added in, key (optional, unique) names a row, data is the record. Other projects in the
same database use their own prefix. Without DATABASE_URL everything stays in data/.
"""

import json
from typing import Any

import psycopg

from internship_agent.config import Settings

PREFIX = "intern_agent_"


class Table:
    def __init__(self, url: str, name: str) -> None:
        self.url, self.name = url, PREFIX + name

    def _connect(self) -> psycopg.Connection[tuple[Any, ...]]:
        conn = psycopg.connect(self.url)
        conn.execute(
            f"CREATE TABLE IF NOT EXISTS {self.name} "
            "(id bigserial PRIMARY KEY, key text UNIQUE, data jsonb NOT NULL)"
        )
        return conn

    def rows(self, key: str | None = None) -> list[tuple[str | None, str]]:
        """(key, data as JSON text) of every row in order, or of the row with this key."""
        sql = f"SELECT key, data::text FROM {self.name}"
        with self._connect() as conn:
            if key is None:
                return conn.execute(sql + " ORDER BY id").fetchall()
            return conn.execute(sql + " WHERE key = %s", (key,)).fetchall()

    def put(self, rows: list[tuple[str | None, str]], *, replace_all: bool = False) -> None:
        """Add rows; one whose key exists updates that row. replace_all drops the rest."""
        with self._connect() as conn, conn.cursor() as cur:  # one transaction
            if replace_all:
                cur.execute(f"DELETE FROM {self.name}")
            cur.executemany(
                f"INSERT INTO {self.name} (key, data) VALUES (%s, %s) "
                "ON CONFLICT (key) DO UPDATE SET data = excluded.data",
                rows,
            )


def table(settings: Settings, name: str) -> Table | None:
    return Table(settings.database_url, name) if settings.database_url else None


def append(settings: Settings, log: str, record: dict[str, Any]) -> None:
    """Add a record to a log such as "sent-log": a table row, or a line in data/<log>.jsonl."""
    line = json.dumps(record)
    if db := table(settings, log.replace("-", "_")):
        db.put([(None, line)])
        return
    path = settings.data_dir / f"{log}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def read_log(settings: Settings, log: str) -> list[dict[str, Any]]:
    if db := table(settings, log.replace("-", "_")):
        return [json.loads(data) for _, data in db.rows()]
    path = settings.data_dir / f"{log}.jsonl"
    records = []
    for line in path.read_text(encoding="utf-8").splitlines() if path.exists() else []:
        try:
            records.append(json.loads(line))
        except ValueError:  # a line cut short by a crash
            continue
    return records
