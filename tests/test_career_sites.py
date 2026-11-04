from internship_agent.leads.schemas import LeadKind, Region
from internship_agent.sources import big_companies, gallery

AMAZON_PAGE = {
    "jobs": [
        {
            "title": "Software Development Engineer Intern",
            "job_path": "/en/jobs/1/sde-intern",
            "location": "US, WA, Seattle",
        },
        {
            "title": "Software Development Engineer Intern",
            "job_path": "/en/jobs/2/sde-intern",
            "location": "MX, Zapopan",
        },
        {"title": "Senior Manager, Retail", "job_path": "/en/jobs/3/mgr", "location": "US, WA"},
    ]
}
MICROSOFT_PAGE = {
    "data": {
        "positions": [
            {
                "name": "Software Engineer Intern",
                "positionUrl": "/careers/job/9",
                "standardizedLocations": ["Redmond, WA, US"],
            },
            {
                "name": "Sales Director",
                "positionUrl": "/careers/job/10",
                "standardizedLocations": ["Redmond, WA, US"],
            },
        ]
    }
}


def test_amazon_and_microsoft_keep_only_intern_engineering_roles() -> None:
    amazon = big_companies.amazon_roles([AMAZON_PAGE])
    assert [r.url for r in amazon][0] == "https://www.amazon.jobs/en/jobs/1/sde-intern"
    assert len(amazon) == 2  # the Sales/Manager title is dropped, region is filtered later
    microsoft = big_companies.microsoft_roles([MICROSOFT_PAGE])
    assert [r.title for r in microsoft] == ["Software Engineer Intern"]
    assert microsoft[0].url == "https://apply.careers.microsoft.com/careers/job/9"


def test_postings_are_filtered_to_the_search_regions(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.setattr(big_companies, "GREENHOUSE", {})
    monkeypatch.setattr(
        big_companies, "_get", lambda url: AMAZON_PAGE if "amazon" in url else MICROSOFT_PAGE
    )
    leads = big_companies.postings({Region.USA})
    assert {lead.company for lead in leads} == {"Amazon", "Microsoft"}
    assert all(lead.kind is LeadKind.POSTING and lead.region is Region.USA for lead in leads)
    assert not any("Zapopan" in lead.location for lead in leads)


def test_gallery_boards_are_found_once_each() -> None:
    html = (
        '<a href="https://jobs.ashbyhq.com/ElevenLabs/750a8325-7ce1-45ea-b0b1-61dab78a456e">x</a>'
        '<a href="https://jobs.ashbyhq.com/elevenlabs/c4e0d704-c7eb-4d6d-b71b-23bfd86fe463">y</a>'
        '<a href="https://job-boards.greenhouse.io/grafanalabs/jobs/6231343004">z</a>'
        '<a href="https://example.com/not-a-board">n</a>'
    )
    assert gallery.boards(html) == [("ashby", "elevenlabs"), ("greenhouse", "grafanalabs")]


def test_an_ashby_job_is_gone_once_its_board_stops_listing_it(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    live = "84dfad5c-d790-4c4a-9411-40b676b1abbb"
    monkeypatch.setattr(big_companies, "_get", lambda url: {"jobs": [{"id": live}]})
    base = "https://jobs.ashbyhq.com/veeda-ai/"
    assert not big_companies.posting_is_gone(base + live)
    assert big_companies.posting_is_gone(base + "00000000-0000-0000-0000-000000000000")


def test_github_lists_read_both_table_styles() -> None:
    from internship_agent.sources import github_lists

    badge = "[![Apply](https://img.shields.io/badge/-Apply-blue)]"
    canadian = (
        "| Company | Role | Location | Apply | Date Posted |\n|---|---|---|:-:|---|\n"
        f"| HeyGen | SWE Intern (W27) | Toronto, ON | {badge}(https://gh.test/1) | Oct 1 |\n"
        f"| ↳ | ML Intern | Toronto, ON | {badge}(https://gh.test/2) | Oct 1 |\n"
        "| RBC | Analyst Intern | Toronto, ON | Closed🔒 | Oct 1 |\n"
    )
    speedy = (
        "| Company | Position | Location | Salary | Posting | Age |\n|---|---|---|---|---|---|\n"
        '| <a href="https://twitch.tv"><strong>Twitch</strong></a> | SWE Intern | SF, CA | $61/hr '
        '| <a href="https://gh.test/3"><img src="https://i.imgur.com/x.png"/></a> | 0d |\n'
    )
    leads = github_lists.parse(canadian, "https://raw.githubusercontent.com/a/b/main/README.md")
    leads += github_lists.parse(speedy, "https://raw.githubusercontent.com/a/b/main/README.md")
    assert [(lead.company, lead.posting_url) for lead in leads] == [
        ("HeyGen", "https://gh.test/1"),
        ("HeyGen", "https://gh.test/2"),
        ("Twitch", "https://gh.test/3"),
    ]


def test_discord_source_is_off_without_a_browser() -> None:
    from internship_agent.sources import discord

    assert discord.postings(None) == []


def test_discord_job_cards_are_parsed_and_chat_is_ignored() -> None:
    from internship_agent.sources import discord

    link = "https://job.northern.dev/veeda-ai-internship-software-engineering-2bb85092"
    card = {
        "text": "Nordique\nVERIFIED APP\nVeeda AI\n,\nInternship - Software Engineering\nLevel\n"
        "Internship\nLocation\nToronto, ON\nSponsorship\nUnknown",
        "links": [[link, "Internship - Software Engineering"], [link, ""]],
    }
    assert discord.parse(card) == {
        "company": "Veeda AI",
        "title": "Internship - Software Engineering",
        "location": "Toronto, ON",
        "url": link,
    }
    assert discord.parse({"text": "anyone hear back from google?", "links": []}) is None
