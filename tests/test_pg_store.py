import os
from pathlib import Path

import psycopg
import pytest

from internship_agent import db
from internship_agent.config import Settings
from internship_agent.leads.answers import AnswerBank
from internship_agent.leads.preferences import PreferenceStore
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus
from internship_agent.leads.store import PostgresLeadStore
from internship_agent.opportunities.schemas import Opportunity, OpportunityStatus
from internship_agent.opportunities.store import OpportunityStore

URL = os.environ.get("TEST_DATABASE_URL")
pytestmark = pytest.mark.skipif(not URL, reason="set TEST_DATABASE_URL to a Postgres database")


@pytest.fixture(autouse=True)
def test_tables(monkeypatch: pytest.MonkeyPatch) -> None:
    """Use test_intern_agent_* tables, emptied first, so real data is never touched."""
    monkeypatch.setattr(db, "PREFIX", "test_intern_agent_")
    assert URL
    with psycopg.connect(URL) as conn:
        for name in ("leads", "preferences", "answer_bank", "sent_log", "opportunities"):
            conn.execute(f"DROP TABLE IF EXISTS test_intern_agent_{name}")


def posting(n: int) -> Lead:
    url = f"https://x.com/jobs/{n}"
    return Lead(kind=LeadKind.POSTING, company=f"Co{n}", posting_url=url, source_url=url)


def test_a_stale_save_keeps_a_status_set_meanwhile() -> None:
    assert URL
    scrape, dashboard = PostgresLeadStore(URL), PostgresLeadStore(URL)
    scrape.save([posting(1), posting(2)])

    # The scrape loads every lead, then runs for minutes; you mark one applied meanwhile.
    leads = scrape.load()
    lead = dashboard.get(leads[0].key)
    lead.status = LeadStatus.APPLIED
    dashboard.upsert(lead)
    scrape.save([*leads, posting(3)])

    stored = dashboard.load()
    assert [lead.company for lead in stored] == ["Co1", "Co2", "Co3"]
    assert stored[0].status is LeadStatus.APPLIED
    with pytest.raises(KeyError):
        dashboard.get("missing")


def test_rules_answers_and_logs_live_in_tables(tmp_path: Path) -> None:
    assert URL
    settings = Settings(_env_file=None, data_dir=tmp_path, database_url=URL)
    prefs = PreferenceStore(tmp_path / "unused.json", db.table(settings, "preferences"))
    kept = prefs.add("Skip defense companies", "skip")
    prefs.add("Boost robotics", "boost")
    assert kept and prefs.remove(kept.id)
    assert [p.rule for p in prefs.load()] == ["Boost robotics"]

    bank = AnswerBank(tmp_path / "unused.json", db.table(settings, "answer_bank"))
    bank.remember("Are you legally authorized to work?", "Yes")
    bank.remember("Are you legally authorized to work?", "No")
    assert list(bank.load().values()) == ["No"]

    db.append(settings, "sent-log", {"key": "a", "subject": "Hi"})
    db.append(settings, "sent-log", {"key": "b", "subject": "Hey"})
    assert [r["key"] for r in db.read_log(settings, "sent-log")] == ["a", "b"]
    assert not list(tmp_path.iterdir())  # nothing went to files


def test_opportunities_live_in_a_table_and_keep_your_status(tmp_path: Path) -> None:
    assert URL
    store = OpportunityStore(Settings(_env_file=None, data_dir=tmp_path, database_url=URL))
    hack = Opportunity(kind="hackathon", title="Hack", url="https://hack.dev", source="test")
    talk = Opportunity(kind="conference", title="Conf", url="https://conf.dev", source="test")
    assert store.add_new([hack, talk]) == [hack, talk]
    item = store.get("https://hack.dev")
    item.status = OpportunityStatus.REGISTERED
    store.upsert(item)
    assert store.add_new([hack]) == []  # a refresh never undoes the status
    assert [(o.title, o.status) for o in store.load()] == [
        ("Hack", OpportunityStatus.REGISTERED),
        ("Conf", OpportunityStatus.NEW),
    ]
    assert not list(tmp_path.iterdir())
