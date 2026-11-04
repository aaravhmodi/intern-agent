from typing import Any

import pytest

from internship_agent.config import Settings
from internship_agent.leads.schemas import LeadKind, Region
from internship_agent.sources import hn_hiring, speedrun, startup_jobs
from internship_agent.sources.regions import wanted_location

REGIONS = {Region.CANADA, Region.USA}


def test_workable_recruitee_smartrecruiters_payloads() -> None:
    workable = startup_jobs.parse_workable(
        {
            "jobs": [
                {"title": "Software Engineer Intern", "url": "https://apply.workable.com/acme/j/1",
                 "city": "Toronto", "country": "Canada"},
                {"title": "Remote Co-op", "shortlink": "https://apply.workable.com/j/2",
                 "telecommuting": True},
                {"title": "No link"},
            ]
        }
    )  # fmt: skip
    assert [(r.location, r.board) for r in workable] == [
        ("Toronto, Canada", "workable"),
        ("Remote", "workable"),
    ]

    recruitee = startup_jobs.parse_recruitee(
        {"offers": [{"title": "ML Intern", "careers_url": "https://jobs.acme.com/o/ml",
                     "city": "Berlin", "country": "Germany", "remote": True}]}
    )  # fmt: skip
    assert recruitee[0].location == "Berlin, Germany, Remote"
    assert recruitee[0].url == "https://jobs.acme.com/o/ml"

    sr = startup_jobs.parse_smartrecruiters(
        {"content": [{"name": "Backend Intern", "id": "744000",
                      "location": {"city": "Austin", "region": "TX", "country": "us"}}]},
        "acme",
    )  # fmt: skip
    assert sr[0].url == "https://jobs.smartrecruiters.com/acme/744000"
    assert sr[0].location == "Austin, TX, us"


def test_find_intern_roles_falls_through_to_new_boards(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_json(url: str) -> Any:
        if "workable" in url:
            return {"jobs": [{"title": "Software Engineering Intern",
                              "url": "https://apply.workable.com/acme/j/1"}]}  # fmt: skip
        raise OSError("404")

    monkeypatch.setattr(startup_jobs, "_json", fake_json)
    roles = startup_jobs.find_intern_roles("Acme", "https://acme.com")
    assert [r.board for r in roles] == ["workable"]


def test_hn_thread_is_found_by_title() -> None:
    search = {
        "hits": [
            {"objectID": "1", "title": "Ask HN: Who wants to be hired? (November 2026)"},
            {"objectID": "2", "title": "Ask HN: Who is hiring? (November 2026)"},
        ]
    }
    assert hn_hiring.latest_thread_id(search) == "2"
    assert hn_hiring.latest_thread_id({"hits": []}) is None


def test_hn_comment_header_and_link() -> None:
    text = (
        "Acme Robotics | Software Engineering Intern (Winter 2027) | Toronto, ON | "
        '<a href="https://jobs.ashbyhq.com/acme/123">https://jobs.ashbyhq.com/acme/123</a>'
        "<p>We build robots &amp; more. Blog: https://acme.com/blog</p>"
    )
    posting = hn_hiring.parse_comment(text, "https://news.ycombinator.com/item?id=9")
    assert posting is not None
    assert posting.company == "Acme Robotics"
    assert posting.location == "Toronto, ON"
    assert posting.url == "https://jobs.ashbyhq.com/acme/123"


def test_hn_comment_prefers_job_links_then_permalink() -> None:
    body = "Beta | Backend Intern | Remote<p>Home https://beta.io and https://beta.io/careers/42."
    posting = hn_hiring.parse_comment(body, "https://news.ycombinator.com/item?id=9")
    assert posting is not None and posting.url == "https://beta.io/careers/42"

    bare = hn_hiring.parse_comment(
        "Gamma | ML Intern | NYC", "https://news.ycombinator.com/item?id=9"
    )
    assert bare is not None and bare.url == "https://news.ycombinator.com/item?id=9"
    assert hn_hiring.parse_comment("", "x") is None
    assert hn_hiring.parse_comment("Name | Intern | Remote", "x").company == ""  # type: ignore[union-attr]


def test_hn_thread_matching_and_leads() -> None:
    item = {
        "id": 100,
        "children": [
            {"id": 1, "text": "Acme | Software Engineer Intern | Waterloo, ON",
             "created_at": "2026-11-02T15:00:00.000Z"},
            {"id": 2, "text": "Big Co | Senior Software Engineer | Toronto, ON"},
            {"id": 3, "text": "Euro | Software Intern | Lisbon, Portugal"},
            {"id": 4, "deleted": True, "text": "x"},
        ],
    }  # fmt: skip
    postings = hn_hiring.parse_thread(item)
    assert [p.company for p in postings] == ["Acme", "Big Co", "Euro"]
    kept = hn_hiring.matching(postings, REGIONS)
    assert [p.company for p in kept] == ["Acme"]
    lead = hn_hiring.to_lead(kept[0])
    assert lead.kind is LeadKind.POSTING
    assert lead.posting_url == "https://news.ycombinator.com/item?id=1"
    assert lead.source_url == "https://news.ycombinator.com/item?id=100"
    assert lead.region is Region.CANADA


def test_speedrun_page_is_host_locked_and_filtered() -> None:
    page = {
        "jobs": [
            {"title": "Software Engineer Intern", "company": "Rocket",
             "url": "https://speedrun-talent-network.com/jobs/1", "location": "San Francisco, CA",
             "published_at": "2026-10-30T00:00:00Z"},
            {"title": "ML Intern", "company": "Evil", "url": "https://evil.example/jobs/2",
             "location": "Remote"},
            {"title": "Account Executive", "company": "Sales Co",
             "url": "https://speedrun-talent-network.com/jobs/3", "remote": True},
        ],
        "total_pages": 1,
    }  # fmt: skip
    jobs = speedrun.parse_page(page)
    assert [j.company for j in jobs] == ["Rocket", "Sales Co"]
    assert jobs[1].location == "Remote"
    kept = speedrun.matching(jobs, REGIONS)
    assert [j.company for j in kept] == ["Rocket"]
    assert speedrun.to_lead(kept[0]).region is Region.USA


def test_speedrun_fetch_stops_at_total_pages(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    def fake(url: str, timeout: float = 15) -> Any:
        calls.append(url)
        return {"jobs": [{"title": "Intern", "company": "A",
                          "url": f"https://speedrun-talent-network.com/jobs/{len(calls)}"}],
                "total_pages": 2}  # fmt: skip

    monkeypatch.setattr(speedrun, "get_json", fake)
    assert len(speedrun.fetch(max_pages=5)) == 2
    assert len(calls) == 2


def test_wanted_location() -> None:
    assert wanted_location("Toronto, ON", {Region.CANADA})
    assert wanted_location("Remote (US)", {Region.CANADA})
    assert not wanted_location("Bangalore, India", {Region.CANADA, Region.USA})


def test_feed_postings_survives_a_broken_feed(monkeypatch: pytest.MonkeyPatch) -> None:
    from internship_agent import workflows

    def broken() -> list[hn_hiring.HnPosting]:
        raise OSError("down")

    monkeypatch.setattr(hn_hiring, "fetch", broken)
    monkeypatch.setattr(
        speedrun,
        "fetch",
        lambda: [speedrun.SpeedrunJob(title="Software Intern", company="Rocket",
                                      location="Toronto, ON",
                                      url="https://speedrun-talent-network.com/jobs/1")],
    )  # fmt: skip
    logs: list[str] = []
    leads = workflows.feed_postings(Settings(_env_file=None), REGIONS, logs.append)  # type: ignore[call-arg]
    assert [lead.company for lead in leads] == ["Rocket"]
    assert any("down" in line for line in logs)
