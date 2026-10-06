"""Fetch a posting's description text from public job-board APIs or the page itself."""

import html
import json
import re
import urllib.request
from typing import Any
from urllib.parse import urlsplit

MAX_CHARS = 6000


def _get(url: str, accept: str = "application/json") -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": accept})
    with urllib.request.urlopen(request, timeout=20) as response:
        body: bytes = response.read()
    return body


def _json(url: str) -> Any:
    return json.loads(_get(url))


def html_to_text(markup: str) -> str:
    markup = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", markup)
    text = re.sub(r"<[^>]+>", " ", markup)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _workday(url: str) -> str:
    parts = urlsplit(url)
    tenant = parts.netloc.split(".")[0]
    path = [p for p in parts.path.strip("/").split("/") if p]
    if path and re.fullmatch(r"[a-z]{2}-[A-Z]{2}", path[0]):
        path = path[1:]
    site, rest = path[0], "/".join(path[1:])
    data = _json(f"https://{parts.netloc}/wday/cxs/{tenant}/{site}/{rest}")
    return html_to_text(str(data.get("jobPostingInfo", {}).get("jobDescription", "")))


def _greenhouse(url: str) -> str:
    parts = urlsplit(url)
    match = re.search(r"/([^/]+)/jobs/(\d+)", parts.path) or re.search(r"gh_jid=(\d+)", parts.query)
    if match is None:
        raise ValueError("not a Greenhouse job URL")
    if match.lastindex == 2:
        board, job_id = match.group(1), match.group(2)
    else:
        board, job_id = parts.netloc.split(".")[-2], match.group(1)
    data = _json(f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{job_id}?content=true")
    return html_to_text(str(data.get("content", "")))


def _lever(url: str) -> str:
    _, company, job_id = urlsplit(url).path.split("/")[:3]
    data = _json(f"https://api.lever.co/v0/postings/{company}/{job_id}")
    lists = " ".join(f"{x.get('text', '')} {x.get('content', '')}" for x in data.get("lists", []))
    return html_to_text(f"{data.get('description', '')} {lists} {data.get('additional', '')}")


def _ashby(url: str) -> str:
    _, org, job_id = urlsplit(url).path.split("/")[:3]
    data = _json(f"https://api.ashbyhq.com/posting-api/job-board/{org}")
    for job in data.get("jobs", []):
        if job.get("id") == job_id:
            return str(job.get("descriptionPlain", ""))
    raise ValueError("Ashby job not found")


def fetch_posting_text(url: str) -> str:
    """Best-effort description text, truncated. Returns '' if nothing could be read."""
    host = urlsplit(url).netloc.lower()
    try:
        if "myworkdayjobs.com" in host:
            text = _workday(url)
        elif "greenhouse.io" in host or "gh_jid=" in url:
            text = _greenhouse(url)
        elif host == "jobs.lever.co":
            text = _lever(url)
        elif host == "jobs.ashbyhq.com":
            text = _ashby(url)
        else:
            text = html_to_text(_get(url, accept="text/html").decode("utf-8", "ignore"))
    except Exception:
        return ""
    return re.sub(r"\s+", " ", text).strip()[:MAX_CHARS]
