"""Look for open intern/co-op roles on a startup's public job board (Ashby, Greenhouse, Lever)."""

import json
import re
import urllib.request
from typing import Any
from urllib.parse import urlsplit

from pydantic import BaseModel

_INTERN = re.compile(r"\b(intern|interns|internship|co-?op|student)\b", re.I)
_ENGINEERING = re.compile(
    r"\b(software|engineer\w*|developer|data|machine learning|ml|ai|platform|backend|"
    r"front-?end|full[- ]?stack|infrastructure|research|robotics)\b",
    re.I,
)


class OpenRole(BaseModel):
    title: str
    url: str
    location: str
    board: str


def _json(url: str) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read())


def board_slugs(company: str, company_url: str | None) -> list[str]:
    """Likely job-board slugs: the website's name, then the company name."""
    slugs: list[str] = []
    if company_url:
        host = urlsplit(company_url if "//" in company_url else f"https://{company_url}").netloc
        stem = host.lower().removeprefix("www.").split(".")[0]
        if stem:
            slugs.append(stem)
    name = re.sub(r"\b(inc|ltd|labs?|ai|technologies|corp)\b\.?", "", company.lower())
    for slug in (re.sub(r"[^a-z0-9]", "", name), re.sub(r"[^a-z0-9]+", "-", name).strip("-")):
        if len(slug) >= 3 and slug not in slugs:
            slugs.append(slug)
    return slugs


def _ashby(slug: str) -> list[OpenRole]:
    data = _json(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
    return [
        OpenRole(title=j["title"], url=j["jobUrl"], location=j.get("location", ""), board="ashby")
        for j in data.get("jobs", [])
        if j.get("isListed", True)
    ]


def _greenhouse(slug: str) -> list[OpenRole]:
    data = _json(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    return [
        OpenRole(
            title=j["title"],
            url=j["absolute_url"],
            location=(j.get("location") or {}).get("name", ""),
            board="greenhouse",
        )
        for j in data.get("jobs", [])
    ]


def _lever(slug: str) -> list[OpenRole]:
    data = _json(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    return [
        OpenRole(
            title=j["text"],
            url=j["hostedUrl"],
            location=(j.get("categories") or {}).get("location", ""),
            board="lever",
        )
        for j in data
    ]


def intern_roles(roles: list[OpenRole]) -> list[OpenRole]:
    return [r for r in roles if _INTERN.search(r.title) and _ENGINEERING.search(r.title)]


def find_intern_roles(company: str, company_url: str | None) -> list[OpenRole]:
    """Open intern/co-op roles from the first public job board found for the company."""
    for slug in board_slugs(company, company_url):
        for fetch in (_ashby, _greenhouse, _lever):
            try:
                roles = fetch(slug)
            except Exception:
                continue
            if roles:
                return intern_roles(roles)
    return []
