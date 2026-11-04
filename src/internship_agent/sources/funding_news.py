"""Recently funded startups from public funding news (RSS feeds and Hacker News).

Ported from career-ops' company-funded.mjs. No AI: the company, amount and round come
from the headline, and acquisitions, layoffs, IPOs, VC funds and grants are dropped.
Each company becomes a founder lead with no contact yet; the usual people and email
lookups fill that in.
"""

import html
import re
from collections.abc import Callable
from datetime import UTC, date, datetime, timedelta
from email.utils import parsedate_to_datetime
from urllib.parse import urlencode, urlsplit

from pydantic import BaseModel

from internship_agent.leads.schemas import Lead, LeadKind, Round
from internship_agent.leads.segments import ROUND_SEGMENT, parse_round
from internship_agent.sources.http import get_json, get_text
from internship_agent.sources.regions import region_from_text

RSS_FEEDS = {
    "techcrunch": (
        "https://techcrunch.com/category/startups/feed/",
        "https://techcrunch.com/tag/funding/feed/",
    ),
    "prnewswire": ("https://www.prnewswire.com/rss/venture-capital-list.rss",),
    "siliconangle": ("https://siliconangle.com/feed/",),
}
SOURCE_HOSTS = {
    "techcrunch": "techcrunch.com",
    "prnewswire": "prnewswire.com",
    "siliconangle": "siliconangle.com",
    "hacker_news": "news.ycombinator.com",
}
SOURCE_RANK = {"techcrunch": 70, "prnewswire": 65, "siliconangle": 45, "hacker_news": 35}
HN_QUERIES = (
    "AI startup raises funding",
    "Series A AI startup",
    "developer tools startup funding",
    "infrastructure startup raises funding",
    "agentic AI raises seed",
)

_VERB = r"(?:raises?|raised|lands|landed|secures?|secured|closes?|closed|nabs?|nabbed|bags?|bagged)"
_MONEY = r"\$[\d.,]+\s*(?:billion|million|bn|[bkm])?"
_TITLE_PATTERNS = [
    re.compile(rf"^(.+?)\s+{_VERB}\s+(?:an?\s+|over\s+|more\s+than\s+|up\s+to\s+)?{_MONEY}", re.I),
    re.compile(
        rf"^(.+?)\s+{_VERB}\s+(?:an?\s+)?(?:\w+\s+){{0,4}}"
        r"(?:funding|round|series\s+[a-h]|seed|pre-seed|investment|financing)\b",
        re.I,
    ),
    re.compile(
        rf"^(.+?)\s+announce[sd]?\s+(?:{_MONEY}\s+)?(?:\w+\s+){{0,4}}"
        r"(?:funding|round|series\s+[a-h]|seed|pre-seed|financing)\b",
        re.I,
    ),
    re.compile(
        rf"^(.+?)\s+(?:gets|got|receives?|received)\s+(?:{_MONEY}\s+)?(?:in\s+)?"
        r"(?:funding|investment|financing)\b",
        re.I,
    ),
    re.compile(r"^(.+?)\s+emerges? from stealth\b", re.I),
]
_FUNDING = re.compile(
    r"\b(funding|funded|raises?|raised|series\s+[a-h]|seed\s+round|pre-seed|venture\s+round|"
    r"investment|financing|lands?|landed|secures?|secured|closes?|closed|emerges?\s+from\s+stealth)\b",
    re.I,
)
_EXCLUDED = [
    re.compile(
        r"(?<!\w)(acquires?|acquired|acquisition|merger|spac|ipo|bankruptcy|layoffs?|earnings|"
        r"quarterly results)(?!\w)",
        re.I,
    ),
    re.compile(
        r"(?<!\w)(cuts?|axes|slashes|eliminates|sheds)\s+\d[\d,.]*\s*(?:%\s*)?(?:of\s+)?"
        r"(?:its\s+|the\s+|their\s+)?(jobs|roles|positions|staff|employees|workers|workforce|"
        r"headcount)(?!\w)",
        re.I,
    ),
    re.compile(r"\b(lays?\s+off|laid\s+off|job\s+cuts|workforce\s+reductions?)\b", re.I),
    re.compile(r"\b(public offering|private placement|offering of common stock)\b", re.I),
    re.compile(rf"\braises?\s+{_MONEY}\s+fund\b", re.I),
    re.compile(r"\b(venture fund|vc fund|investment fund|new fund|fund (?:ii|iii|iv|v))\b", re.I),
    re.compile(r"\b(grants?|scholarships?|awards?|donations?|donates?)\b", re.I),
    re.compile(r"\b(how to raise|guide to fundraising|startup valuations|bubble)\b", re.I),
]
_GENERIC = {
    "ai", "startup", "startups", "company", "companies", "founder", "founders", "developer",
    "developers", "techcrunch", "pr newswire",
}  # fmt: skip
_SECTOR = (
    r"(?:ai|genai|agentic|coding|developer tools|developer|data|security|fintech|software|"
    r"robotics|defense|healthcare|biotech|open-source|enterprise|infrastructure|crypto|climate)"
)


class NewsItem(BaseModel):
    source: str
    title: str
    url: str
    published_on: date | None
    text: str = ""


class FundingCandidate(BaseModel):
    company: str
    amount_usd: int | None
    round: Round
    announced_on: date
    title: str
    url: str
    sources: list[str]
    score: int


def _plain(text: str) -> str:
    text = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", text, flags=re.S)
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", html.unescape(text))).split())


def _tag(block: str, *names: str) -> str:
    for name in names:
        match = re.search(rf"<{name}\b[^>]*>(.*?)</{name}>", block, re.S | re.I)
        if match:
            return _plain(match.group(1))
    return ""


def _date(value: str) -> date | None:
    if not value:
        return None
    try:
        return parsedate_to_datetime(value).date()
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def trusted_url(url: str, source: str) -> str:
    """The link if it is https on the feed's own site, else empty."""
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    want = SOURCE_HOSTS.get(source, "")
    ok = parts.scheme == "https" and bool(want) and (host == want or host.endswith("." + want))
    return url if ok else ""


def parse_rss(xml: str, source: str) -> list[NewsItem]:
    items: list[NewsItem] = []
    for block in re.findall(r"<(?:item|entry)\b[^>]*>(.*?)</(?:item|entry)>", xml, re.S | re.I):
        title = _tag(block, "title")
        link = _tag(block, "link")
        if not link:
            href = re.search(r"<link\b[^>]*href=\"([^\"]+)\"", block, re.I)
            link = href.group(1) if href else ""
        url = trusted_url(link.strip(), source)
        if not title or not url:
            continue
        items.append(
            NewsItem(
                source=source,
                title=title,
                url=url,
                published_on=_date(_tag(block, "pubDate", "published", "updated", "dc:date")),
                text=_tag(block, "description", "summary"),
            )
        )
    return items


def parse_hn(data: dict[str, object]) -> list[NewsItem]:
    items: list[NewsItem] = []
    hits = data.get("hits")
    for hit in hits if isinstance(hits, list) else []:
        title = _plain(str(hit.get("title") or ""))
        object_id = str(hit.get("objectID") or "")
        if not title or not object_id.isdigit():
            continue
        created = str(hit.get("created_at") or "")
        items.append(
            NewsItem(
                source="hacker_news",
                title=title,
                url=f"https://news.ycombinator.com/item?id={object_id}",
                published_on=_date(created),
            )
        )
    return items


def is_funding_news(item: NewsItem) -> bool:
    text = f"{item.title} {item.text}"
    return bool(_FUNDING.search(text)) and not any(p.search(text) for p in _EXCLUDED)


def _clean_company(raw: str) -> str:
    s = re.sub(r"\s+[|–—-]\s+(TechCrunch|PR Newswire|SiliconANGLE).*$", "", raw, flags=re.I)
    s = re.sub(r"^(?:Show|Ask|Launch) HN:\s*", "", s, flags=re.I).strip(" \"'`")
    s = re.sub(r"['’]s$", "", s)
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s)
    s = re.sub(r"\s*,.*$", "", s)
    s = re.sub(r"^.*?\bstartup\s+(?=\S)", "", s, flags=re.I)  # "Toronto-based startup Acme"
    s = re.sub(r"^[A-Z][\w&.-]+-backed\s+", "", s)
    s = re.sub(rf"^(?:the\s+)?(?:{_SECTOR}\s+)+(?:startup|company|platform)?\s*", "", s, flags=re.I)
    s = re.sub(r"^(?:startup|company|platform)\s+", "", s, flags=re.I)
    s = re.sub(r"\s+(?:reportedly|in talks to)$", "", s, flags=re.I)
    s = " ".join(s.split())
    if not 2 <= len(s) <= 60 or s.lower() in _GENERIC or not re.search(r"[A-Za-z0-9]", s):
        return ""
    if re.search(r"\b(valuation|bubble|fears|earnings|fund)\b", s, re.I):
        return ""
    if len(s.split()) > 5:  # a sentence fragment, not a name
        return ""
    return s


def company_from_title(title: str) -> str:
    if re.match(r"^(ask hn|tell hn|who is hiring|launch hn)\b", title, re.I):
        return ""
    for pattern in _TITLE_PATTERNS:
        match = pattern.search(title)
        if match:
            return _clean_company(match.group(1))
    return ""


def amount_usd(text: str) -> int | None:
    """'$12.5M' or '$3 million' in the text, in dollars."""
    match = re.search(r"\$([\d,]+(?:\.\d+)?)\s*(billion|million|bn|[bkm])?\b", text, re.I)
    if not match:
        return None
    value = float(match.group(1).replace(",", ""))
    unit = (match.group(2) or "").lower()
    scale = {"billion": 1e9, "bn": 1e9, "b": 1e9, "million": 1e6, "m": 1e6, "k": 1e3}
    return int(value * scale.get(unit, 1))


def build_candidates(
    items: list[NewsItem], today: date, max_age_days: int = 30, max_usd: int = 250_000_000
) -> list[FundingCandidate]:
    """One candidate per company, newest first; mega-rounds and late stages are dropped."""
    by_company: dict[str, FundingCandidate] = {}
    for item in items:
        if not item.published_on or not (
            today - timedelta(days=max_age_days) <= item.published_on <= today
        ):
            continue
        if not is_funding_news(item):
            continue
        company = company_from_title(item.title)
        if not company:
            continue
        text = f"{item.title} {item.text}"
        amount = amount_usd(item.title) or amount_usd(text)
        round_ = parse_round(text)
        if amount is not None and amount > max_usd:
            continue
        if re.search(r"series\s*[e-h]\b", text, re.I):
            continue
        key = re.sub(r"[^a-z0-9]+", " ", company.lower()).strip()
        bonus = (10 if amount else 0) + (8 if round_ is not Round.OTHER else 0)
        found = by_company.get(key)
        if found is None:
            by_company[key] = FundingCandidate(
                company=company,
                amount_usd=amount,
                round=round_,
                announced_on=item.published_on,
                title=item.title,
                url=item.url,
                sources=[item.source],
                score=SOURCE_RANK.get(item.source, 5) + bonus,
            )
            continue
        found.amount_usd = found.amount_usd or amount
        found.round = found.round if found.round is not Round.OTHER else round_
        if item.source not in found.sources:
            found.sources.append(item.source)
            found.score += SOURCE_RANK.get(item.source, 5) + bonus
    return sorted(by_company.values(), key=lambda c: (c.announced_on, c.score), reverse=True)


def fetch_items(
    today: date, max_age_days: int = 30, log: Callable[[str], None] = lambda _: None
) -> list[NewsItem]:
    """Every news item from the feeds; one feed failing does not stop the others."""
    items: list[NewsItem] = []
    for source, urls in RSS_FEEDS.items():
        for url in urls:
            try:
                items.extend(parse_rss(get_text(url), source))
            except Exception as error:
                log(f"{url}: {error}")
    since = int(
        datetime.combine(today - timedelta(days=max_age_days), datetime.min.time(), UTC).timestamp()
    )
    for query in HN_QUERIES:
        params = urlencode(
            {
                "query": query,
                "tags": "story",
                "hitsPerPage": 50,
                "numericFilters": f"created_at_i>{since}",
            }
        )
        try:
            items.extend(parse_hn(get_json(f"https://hn.algolia.com/api/v1/search?{params}")))
        except Exception as error:
            log(f"HN '{query}': {error}")
    return items


def to_lead(candidate: FundingCandidate) -> Lead:
    return Lead(
        kind=LeadKind.FOUNDER,
        company=candidate.company,
        round=candidate.round,
        amount_usd=candidate.amount_usd,
        announced_on=candidate.announced_on,
        source_url=candidate.url,
        segment=ROUND_SEGMENT.get(candidate.round),
        region=region_from_text(candidate.title),
        hiring_signals=[f"Funding news: {candidate.title}"],
    )
