import os

import psycopg
import pytest

from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus
from internship_agent.leads.store import PostgresLeadStore

URL = os.environ.get("TEST_DATABASE_URL")
pytestmark = pytest.mark.skipif(not URL, reason="set TEST_DATABASE_URL to a throwaway database")


def posting(n: int) -> Lead:
    url = f"https://x.com/jobs/{n}"
    return Lead(kind=LeadKind.POSTING, company=f"Co{n}", posting_url=url, source_url=url)


def test_a_stale_save_keeps_a_status_set_meanwhile() -> None:
    assert URL
    with psycopg.connect(URL) as conn:
        conn.execute("DROP TABLE IF EXISTS leads")
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
