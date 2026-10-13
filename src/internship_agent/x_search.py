"""Find startups by their own posts on X announcing a raise, using Grok's X search.

A seed round is often announced by the founder on X days before, or instead of, any news
article. This searches X itself and keeps the post as the source. Reading only: nothing is
ever posted, followed, liked or messaged.

Grok is given X search and nothing else. Offered web search as well, it answered from news
sites and returned no posts at all.
"""

import html
import json
import re
import urllib.request
import warnings
from datetime import date, timedelta
from typing import Any

from openai import OpenAI

from internship_agent.ai import StartupFinding, StartupFindings
from internship_agent.leads.schemas import Region, Segment

X_REGIONS: dict[Region, str] = {
    Region.CANADA: "Canada",
    Region.USA: "the United States",
    Region.EUROPE: "Europe (the UK, Germany, France, the Netherlands, the Nordics and elsewhere)",
}

X_RAISE_INSTRUCTIONS = """\
Use X search to find posts on X (x.com) in which a startup's founder, or the company's own
account, announces that the company has raised a funding round. The post must be dated from
{start} to {end}; the company must be based in {region}; the round must be {stages}. Prefer
software and AI companies that could use a software-engineering intern.
Search the way founders write, for example: "we raised", "we've raised", "excited to announce
our seed round", "closed our pre-seed", "announcing our $", "thrilled to share we raised",
"backed by". Run four to six different searches, no more. Ignore posts by news outlets,
newsletters and investors that only report someone else's raise.
For each company report only what the post or the poster's profile states: company; the
founder's name and title (the poster, or the founder a company post names; an empty name if
none is given, never the company's name); round; amount in USD if stated; announced_on (the
date of the post); social_url and source_url (both the URL of that post, in the form
https://x.com/<handle>/status/<id>); x_handle (the poster's handle, without @); the company
website if shown; one factual sentence on what they build; and location. Skip a company if you
cannot give the URL of the post itself. Exclude these already-known companies: {exclude}."""

_POST_URL = re.compile(r"^https?://(?:www\.)?(?:x|twitter)\.com/[^/]+/status/(\d+)")


_EMBED = "https://publish.twitter.com/oembed"
_RAISE_WORDS = re.compile(
    r"rais(ed|e|ing)|seed|funding|fundraise|series [a-d]|round|backed by", re.IGNORECASE
)


def post_id(url: str | None) -> str | None:
    """The id of the X post a URL points to, or None when it is not a post."""
    match = _POST_URL.match(url or "")
    return match.group(1) if match else None


def post_text(url: str) -> str | None:
    """What an X post says, from X's public embed lookup; None when there is no such post.

    The lookup needs no key and costs nothing, so every post Grok reports is read this way
    before it becomes a lead.
    """
    found = post_id(url)
    if found is None:
        return None
    handle = (url or "").split("/")[3]
    lookup = f"{_EMBED}?omit_script=1&url=https://twitter.com/{handle}/status/{found}"
    try:
        with urllib.request.urlopen(lookup, timeout=15) as response:
            page = json.loads(response.read())
    except (OSError, ValueError):
        return None
    text = html.unescape(re.sub(r"<[^>]+>", " ", str(page.get("html", ""))))
    return " ".join(text.split())


def post_confirms(finding: StartupFinding) -> bool:
    """True when the post exists and is about raising money, not a link Grok made up."""
    text = post_text(finding.social_url or finding.source_url)
    return text is not None and _RAISE_WORDS.search(text) is not None


def _tool_usage(response: Any) -> dict[str, int]:
    usage = getattr(response, "usage", None)
    details = getattr(usage, "server_side_tool_usage_details", None)
    if details is None:
        extra = getattr(usage, "model_extra", None) or {}
        details = extra.get("server_side_tool_usage_details") or {}
    read = (
        details.get
        if isinstance(details, dict)
        else lambda key, default=0: getattr(details, key, default)
    )
    return {
        "input_tokens": int(getattr(usage, "input_tokens", 0) or 0),
        "output_tokens": int(getattr(usage, "output_tokens", 0) or 0),
        # X search is billed per post and profile fetched, on top of tokens.
        "x_posts_fetched": int(read("x_posts_fetched", 0) or 0),
        "x_users_fetched": int(read("x_users_fetched", 0) or 0),
    }


def search_x_raises(
    client: OpenAI,
    model: str,
    start: date,
    end: date,
    stages: list[Segment],
    region: Region,
    exclude: list[str],
    count: int,
) -> tuple[list[StartupFinding], dict[str, int]]:
    """One X search for raise announcements in a region: the findings and what it used."""
    stage_text = ", ".join(
        "pre-seed or seed" if s is Segment.EARLY else "Series A to D" for s in stages
    )
    # to_date is exclusive, so the day after `end` includes today's posts.
    tools: list[dict[str, Any]] = [
        {"type": "x_search", "from_date": str(start), "to_date": str(end + timedelta(days=1))}
    ]
    with warnings.catch_warnings():
        # The OpenAI SDK warns when serializing tools it doesn't know (Grok's x_search).
        warnings.simplefilter("ignore")
        response = client.responses.parse(
            model=model,
            tools=tools,  # type: ignore[arg-type]
            input=[
                {
                    "role": "system",
                    "content": X_RAISE_INSTRUCTIONS.format(
                        start=start,
                        end=end,
                        region=X_REGIONS[region],
                        stages=stage_text,
                        exclude=", ".join(exclude) or "none",
                    ),
                },
                {"role": "user", "content": f"Find up to {count} startups."},
            ],
            text_format=StartupFindings,
        )
    usage = _tool_usage(response)
    if response.output_parsed is None:
        return [], usage
    parsed = StartupFindings.model_validate(response.output_parsed.model_dump())
    return parsed.startups, usage
