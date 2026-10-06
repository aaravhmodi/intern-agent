"""Parse the SimplifyJobs / Pitt CSC off-season internship list (public GitHub Markdown)."""

import re
import urllib.request
from html.parser import HTMLParser

from pydantic import BaseModel

from internship_agent.leads.schemas import Lead, LeadKind, Region
from internship_agent.leads.store import normalize_url
from internship_agent.sources.regions import region_from_text, regions_of

OFF_SEASON_URL = (
    "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/README-Off-Season.md"
)
# Simplify role markers: advanced degree required, US citizenship required.
EXCLUDED_MARKERS = ("🎓", "🇺🇸")
_MARKERS = re.compile(r"[🌀-🫿🇦-🇿☀-➿]+")
SWE_SECTIONS = ("Software Engineering", "Data Science, AI & Machine Learning")
DEFAULT_LOCATIONS = (
    "Toronto",
    "Waterloo",
    "Kitchener",
    "Ottawa",
    "Montreal",
    "Vancouver",
    "Mississauga",
    "Oakville",
    "Markham",
    "Canada",
    "Remote",
)


class Posting(BaseModel):
    section: str
    company: str
    role: str
    location: str
    terms: str
    url: str
    closed: bool
    age: str

    @property
    def age_days(self) -> int:
        """'3d' -> 3, '1mo' -> 30; unknown formats sort last."""
        match = re.fullmatch(r"(\d+)(d|mo)", self.age.strip())
        if not match:
            return 10_000
        n = int(match.group(1))
        return n if match.group(2) == "d" else n * 30


class _TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[tuple[str, list[str]]]] = []
        self._row: list[tuple[str, list[str]]] | None = None
        self._cell: str | None = None
        self._links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if tag == "tr":
            self._row = []
        elif tag == "td":
            self._cell, self._links = "", []
        elif self._cell is not None and tag == "a":
            self._links.append(attr.get("href") or "")
        elif self._cell is not None and tag == "img":
            self._cell += attr.get("alt") or ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "td" and self._row is not None and self._cell is not None:
            self._row.append((self._cell.strip(), self._links))
            self._cell = None
        elif tag == "tr" and self._row:
            self.rows.append(self._row)
            self._row = None

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell += data


def parse(markdown: str) -> list[Posting]:
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^## (.+)$", markdown, re.M)]
    postings: list[Posting] = []
    for table in re.finditer(r"<table>.*?</table>", markdown, re.S):
        section = next((h for pos, h in reversed(headings) if pos < table.start()), "")
        parser = _TableParser()
        parser.feed(table.group(0))
        company = ""
        for row in parser.rows:
            if len(row) < 6:
                continue
            name = row[0][0]
            company = company if name.startswith("↳") else name.replace("🔥", "").strip()
            links = [link for link in row[4][1] if "simplify.jobs" not in link]
            postings.append(
                Posting(
                    section=section,
                    company=company,
                    role=row[1][0],
                    location=row[2][0],
                    terms=row[3][0],
                    url=links[0] if links else "",
                    closed="🔒" in row[4][0] or not links,
                    age=row[5][0],
                )
            )
    return postings


def matching(
    postings: list[Posting],
    term: str = "Winter 2027",
    locations: tuple[str, ...] = DEFAULT_LOCATIONS,
    regions: set[Region] | None = None,
) -> list[Posting]:
    """Open postings for the term, in SWE/AI sections and preferred places, newest first.

    A posting matches if its location names one of `locations` or falls in one of `regions`.
    """
    found = [
        p
        for p in postings
        if term in p.terms
        and not p.closed
        and any(s in p.section for s in SWE_SECTIONS)
        and (
            any(loc in p.location for loc in locations)
            or bool(regions and regions_of(p.location) & regions)
        )
        and not any(marker in p.role for marker in EXCLUDED_MARKERS)
    ]
    return sorted(found, key=lambda p: p.age_days)


def to_lead(posting: Posting) -> Lead:
    return Lead(
        kind=LeadKind.POSTING,
        company=posting.company,
        posting_title=_MARKERS.sub("", posting.role).strip(),
        posting_url=normalize_url(posting.url),
        source_url=OFF_SEASON_URL,
        location=posting.location,
        region=region_from_text(posting.location),
    )


def fetch(url: str = OFF_SEASON_URL) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "internship-agent"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body: bytes = response.read()
    return body.decode("utf-8")
