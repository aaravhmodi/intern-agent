from datetime import date

import pytest

from internship_agent.leads.schemas import LeadKind, Round, Segment
from internship_agent.sources import funding_news as fn

TODAY = date(2026, 11, 4)

RSS = """<?xml version="1.0"?><rss><channel>
<item><title><![CDATA[Acme raises $12.5M Series A to build robot arms]]></title>
<link>https://techcrunch.com/2026/11/02/acme/</link>
<pubDate>Mon, 02 Nov 2026 14:00:00 +0000</pubDate>
<description>&lt;p&gt;Toronto-based Acme...&lt;/p&gt;</description></item>
<item><title>Evil raises $5M</title><link>https://evil.example/x</link>
<pubDate>Mon, 02 Nov 2026 14:00:00 +0000</pubDate></item>
<item><title>BigCo acquires Tiny for $40M</title><link>https://techcrunch.com/a</link>
<pubDate>Mon, 02 Nov 2026 14:00:00 +0000</pubDate></item>
</channel></rss>"""


@pytest.mark.parametrize(
    ("title", "company"),
    [
        ("Acme raises $12.5M Series A to build robot arms", "Acme"),
        ("AI startup Beta Labs lands $3 million seed round", "Beta Labs"),
        ("Toronto-based startup Gamma secures $8M", "Gamma"),
        ("Delta, a startup building chips, raises $20M", "Delta"),
        ("Epsilon announces $4M seed funding", "Epsilon"),
        ("Zeta emerges from stealth with $6M", "Zeta"),
        ("Sequoia-backed Eta raises $15M - TechCrunch", "Eta"),
        ("Ask HN: How do I raise a seed round?", ""),
        ("Why startup valuations are a bubble", ""),
    ],
)
def test_company_from_title(title: str, company: str) -> None:
    assert fn.company_from_title(title) == company


@pytest.mark.parametrize(
    ("text", "usd"),
    [("raises $12.5M", 12_500_000), ("$3 million seed", 3_000_000), ("$1.2B", 1_200_000_000),
     ("$750k", 750_000), ("no money", None)],
)  # fmt: skip
def test_amount_usd(text: str, usd: int | None) -> None:
    assert fn.amount_usd(text) == usd


def test_parse_rss_keeps_only_the_feeds_own_links() -> None:
    items = fn.parse_rss(RSS, "techcrunch")
    assert [i.title for i in items] == [
        "Acme raises $12.5M Series A to build robot arms",
        "BigCo acquires Tiny for $40M",
    ]
    assert items[0].published_on == date(2026, 11, 2)
    assert items[0].text == "Toronto-based Acme..."


@pytest.mark.parametrize(
    "title",
    [
        "BigCo acquires Tiny for $40M",
        "Acme raises $40M Series A, then cuts 30% of staff",
        "Acme lays off 100 after raising $10M",
        "Foo Ventures raises $200M fund",
        "Acme wins $1M grant",
    ],
)
def test_non_startup_raises_are_excluded(title: str) -> None:
    item = fn.NewsItem(source="techcrunch", title=title, url="https://techcrunch.com/x",
                       published_on=TODAY)  # fmt: skip
    assert not fn.is_funding_news(item)


def test_build_candidates_groups_filters_and_sorts() -> None:
    def item(title: str, on: date, source: str = "techcrunch") -> fn.NewsItem:
        return fn.NewsItem(source=source, title=title, url="https://techcrunch.com/x",
                           published_on=on)  # fmt: skip

    items = [
        item("Acme raises $12M Series A", date(2026, 11, 1)),
        item("Acme raises $12M Series A", date(2026, 11, 1), "hacker_news"),
        item("Newer lands $2M seed", date(2026, 11, 3)),
        item("Old raises $5M", date(2026, 8, 1)),  # too old
        item("Mega raises $900M", date(2026, 11, 2)),  # too big
        item("Late raises $90M Series F", date(2026, 11, 2)),  # too late-stage
        fn.NewsItem(source="techcrunch", title="Undated raises $1M", url="https://techcrunch.com/u",
                    published_on=None),
    ]  # fmt: skip
    found = fn.build_candidates(items, TODAY, max_age_days=30)
    assert [c.company for c in found] == ["Newer", "Acme"]
    acme = found[1]
    assert acme.sources == ["techcrunch", "hacker_news"]
    assert acme.round is Round.SERIES_A and acme.amount_usd == 12_000_000

    lead = fn.to_lead(found[0])
    assert lead.kind is LeadKind.FOUNDER
    assert lead.contact_name == ""
    assert lead.segment is Segment.EARLY
    assert lead.announced_on == date(2026, 11, 3)


def test_parse_hn() -> None:
    data = {"hits": [{"objectID": "123", "title": "Acme raises $3M seed",
                      "created_at": "2026-11-01T10:00:00.000Z"},
                     {"objectID": "bad", "title": "x"}]}  # fmt: skip
    items = fn.parse_hn(data)
    assert len(items) == 1
    assert items[0].url == "https://news.ycombinator.com/item?id=123"
    assert items[0].published_on == date(2026, 11, 1)


def test_fetch_items_survives_failing_feeds(monkeypatch: pytest.MonkeyPatch) -> None:
    def text(url: str, timeout: float = 15) -> str:
        if "siliconangle" in url:
            raise OSError("blocked")
        return RSS

    monkeypatch.setattr(fn, "get_text", text)
    monkeypatch.setattr(fn, "get_json", lambda url, timeout=15: {"hits": []})
    logs: list[str] = []
    items = fn.fetch_items(TODAY, 30, logs.append)
    assert items and any("blocked" in line for line in logs)
