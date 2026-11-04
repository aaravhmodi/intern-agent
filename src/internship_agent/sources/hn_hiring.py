"""Intern roles from Hacker News' monthly "Ask HN: Who is hiring?" thread.

Ported from career-ops' providers/hackernews.mjs: the thread is found by the
`whoishiring` account's own tag (a free-text search can surface unrelated stories),
each top-level comment is one post, and its first line is the header, usually
"Company | Role | Location | URL".
"""

import html
import re
from datetime import datetime
from typing import Any
from urllib.parse import urlsplit

from pydantic import BaseModel

from internship_agent.leads.schemas import Lead, LeadKind, Region
from internship_agent.leads.store import normalize_url
from internship_agent.sources.http import get_json
from internship_agent.sources.regions import region_from_text, wanted_location
from internship_agent.sources.startup_jobs import is_intern_engineering

SEARCH_URL = (
    "https://hn.algolia.com/api/v1/search_by_date?tags=story,author_whoishiring&hitsPerPage=5"
)
_THREAD_TITLE = re.compile(r"ask\s+hn[:\s]+who\s+is\s+hiring", re.I)
_URL = re.compile(r"https?://[^\s<>\"')]+")
_JOBS_PATH = re.compile(r"/(?:careers?|jobs)(?:/|$)", re.I)
_ATS_HOSTS = (
    "greenhouse.io",
    "ashbyhq.com",
    "lever.co",
    "workable.com",
    "recruitee.com",
    "smartrecruiters.com",
    "bamboohr.com",
    "breezy.hr",
    "teamtailor.com",
    "jobvite.com",
    "rippling.com",
    "wellfound.com",
    "workatastartup.com",
)
_PLACEHOLDER = re.compile(r"^[\[<({]?\s*(?:company(?:\s+name)?|name)\s*[\]>)}]?$", re.I)


class HnPosting(BaseModel):
    title: str  # the whole header line
    company: str
    location: str
    url: str
    thread_url: str = ""
    posted_at: datetime | None = None


def item_url(item_id: str) -> str:
    return f"https://news.ycombinator.com/item?id={item_id}"


def latest_thread_id(search: dict[str, Any]) -> str | None:
    """The newest "Who is hiring?" story in an Algolia search_by_date response."""
    for hit in search.get("hits") or []:
        if isinstance(hit.get("objectID"), str) and _THREAD_TITLE.search(hit.get("title") or ""):
            return str(hit["objectID"])
    return None


def _urls(text: str) -> list[str]:
    found = []
    for url in _URL.findall(text):
        url = url.rstrip(".,;!?)")
        while url.endswith("]") and url.count("]") > url.count("["):
            url = url[:-1]
        found.append(url)
    return found


def _looks_like_job(url: str) -> bool:
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in _ATS_HOSTS) or bool(
        _JOBS_PATH.search(parts.path)
    )


def _company(field: str) -> str:
    name = re.sub(r"\(\s*\)|\[\s*\]", "", _URL.sub("", field))
    name = " ".join(name.split())
    return "" if _PLACEHOLDER.match(name) else name


def parse_comment(text: str, fallback_url: str = "") -> HnPosting | None:
    """One comment as a posting; the link is the header's, else a job link, else the comment."""
    plain = re.sub(r'<a\s[^>]*href="([^"]+)"[^>]*>.*?</a>', r"\1", text, flags=re.I | re.S)
    plain = re.sub(r"</?(?:p|br|div|li|h[1-6])\b[^>]*>", "\n", plain, flags=re.I)
    plain = html.unescape(re.sub(r"<[^>]+>", " ", plain))
    lines = [line.strip() for line in plain.splitlines() if line.strip()]
    if not lines:
        return None
    header = lines[0]
    parts = [p.strip() for p in header.split("|")]
    company = _company(parts[0]) if len(parts) >= 2 else ""
    location = _URL.sub("", parts[2]).strip() if len(parts) >= 3 else ""
    title = " ".join(_URL.sub("", header).split())
    if not title:
        return None
    url = next(iter(_urls(" ".join(parts[3:]))), "") or next(
        (u for u in _urls(plain) if _looks_like_job(u)), fallback_url
    )
    if not url:
        return None
    return HnPosting(title=title, company=company, location=location, url=url)


def parse_thread(item: dict[str, Any]) -> list[HnPosting]:
    thread_url = item_url(str(item.get("id", "")))
    postings: list[HnPosting] = []
    for child in item.get("children") or []:
        text = child.get("text") or ""
        if child.get("deleted") or child.get("dead") or not text.strip():
            continue
        comment_id = child.get("id")
        posting = parse_comment(text, item_url(str(comment_id)) if comment_id else thread_url)
        if posting is None or not posting.company:
            continue
        posting.thread_url = thread_url
        created = child.get("created_at")
        if isinstance(created, str):
            try:
                posting.posted_at = datetime.fromisoformat(created.replace("Z", "+00:00"))
            except ValueError:
                pass
        postings.append(posting)
    return postings


def fetch() -> list[HnPosting]:
    thread_id = latest_thread_id(get_json(SEARCH_URL))
    if thread_id is None:
        raise RuntimeError('no "Ask HN: Who is hiring?" thread found')
    return parse_thread(get_json(f"https://hn.algolia.com/api/v1/items/{thread_id}", timeout=60))


def matching(postings: list[HnPosting], regions: set[Region]) -> list[HnPosting]:
    """Engineering intern/co-op posts in a wanted region or remote."""
    return [
        p
        for p in postings
        if is_intern_engineering(p.title) and wanted_location(p.location, regions)
    ]


def to_lead(posting: HnPosting) -> Lead:
    return Lead(
        kind=LeadKind.POSTING,
        company=posting.company,
        posting_title=posting.title,
        posting_url=normalize_url(posting.url),
        source_url=posting.thread_url or posting.url,
        location=posting.location,
        region=region_from_text(posting.location),
        hiring_signals=["Posted in Hacker News' Who is hiring? thread"],
    )
