"""Recent US startup raises from SEC Form D filings: free and official, no key or account.

A company must file a Form D within 15 days of first selling shares, often before any
announcement. The filing names the people running it but not its website or email.
The SEC asks automated clients to name themselves with a contact address and to make
no more than 10 requests a second.
"""

import html
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date
from urllib.parse import urlsplit

from internship_agent.leads.emails import guess_email
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, Region, Segment
from internship_agent.sources.startups import _fold

ARCHIVES = "https://www.sec.gov/Archives/"
TECH = {"Computers", "Other Technology", "Telecommunications"}
# Roughly pre-seed to Series B: smaller is friends and family, larger is a late-stage company.
MIN_USD, MAX_USD = 250_000, 50_000_000
EARLY_BELOW_USD = 5_000_000
_LEGAL = r"(inc|incorporated|llc|corp|corporation|co|ltd|pbc)"
_SUFFIX = re.compile(rf",?\s+{_LEGAL}\.?$", re.I)
TLDS = ("com", "ai", "io", "co", "app", "bot", "tech", "dev", "xyz")
PREFIXES = ("", "get", "try", "use")
ABOUT_PATHS = ("about", "team", "about-us", "company")


@dataclass
class Filing:
    company: str
    location: str
    amount_usd: int
    first_sale: str
    filed_on: date
    url: str  # the filing's folder on sec.gov
    contact_name: str
    contact_role: str
    people: list[str] = field(default_factory=list)
    officers: list[str] = field(default_factory=list)  # the contact first


def index_url(day: date) -> str:
    quarter = (day.month - 1) // 3 + 1
    return f"{ARCHIVES}edgar/daily-index/{day.year}/QTR{quarter}/form.{day:%Y%m%d}.idx"


def form_d_paths(index: str) -> list[str]:
    """Paths of new Form D filings in a daily form index; amendments are "D/A"."""
    return [line.split()[-1] for line in index.splitlines() if line.startswith("D ")]


def company_name(name: str) -> str:
    return _SUFFIX.sub("", name.strip())


def _person(name: str) -> str:
    return name.title() if name.isupper() else name


def parse_filing(xml: str, url: str, filed_on: date) -> Filing | None:
    """A young tech company's raise of a startup-sized amount, or None for anything else."""
    root = ET.fromstring(xml)

    def text(path: str) -> str:
        return (root.findtext(path) or "").strip()

    offering = "offeringData/"
    if text(offering + "industryGroup/industryGroupType") not in TECH:
        return None
    if text(offering + "typeOfFiling/newOrAmendment/isAmendment") == "true":
        return None
    if text("primaryIssuer/yearOfInc/withinFiveYears") != "true":
        return None
    sales = offering + "offeringSalesAmounts/"
    amounts = [text(sales + "totalAmountSold"), text(sales + "totalOfferingAmount")]
    amount = max((int(a) for a in amounts if a.isdigit()), default=0)
    if not MIN_USD <= amount <= MAX_USD:
        return None
    officers: list[str] = []
    people: list[str] = []
    for info in root.iterfind("relatedPersonsList/relatedPersonInfo"):
        first = (info.findtext("relatedPersonName/firstName") or "").strip()
        last = (info.findtext("relatedPersonName/lastName") or "").strip()
        name = _person(f"{first} {last}".strip())
        roles = [r.text for r in info.iterfind("relatedPersonRelationshipList/relationship")]
        people.append(name)
        if "Executive Officer" in roles and first and last:
            officers.append(name)
    if not officers:
        return None
    signer = _person(text(offering + "signatureBlock/signature/nameOfSigner"))
    contact = signer if signer in officers else officers[0]
    role = text(offering + "signatureBlock/signature/signatureTitle") if contact == signer else ""
    city = text("primaryIssuer/issuerAddress/city").title()
    state = text("primaryIssuer/issuerAddress/stateOrCountry")
    return Filing(
        company=company_name(text("primaryIssuer/entityName")),
        location=", ".join(p for p in (city, state) if p),
        amount_usd=amount,
        first_sale=text(offering + "typeOfFiling/dateOfFirstSale/value"),
        filed_on=filed_on,
        url=url,
        contact_name=contact,
        contact_role=role or "Executive Officer",
        people=people,
        officers=[contact, *(o for o in officers if o != contact)],
    )


def _get(url: str, contact: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": f"internship-agent {contact}"})
    with urllib.request.urlopen(request, timeout=30) as response:
        body: bytes = response.read()
    time.sleep(0.15)  # stays under the SEC's 10 requests a second
    return body.decode("utf-8", "ignore")


def filings(day: date, contact: str) -> list[Filing]:
    """The wanted Form D filings made on one day; none on weekends and holidays."""
    try:
        index = _get(index_url(day), contact)
    except urllib.error.HTTPError as error:
        if error.code in (403, 404):  # no index for that day
            return []
        raise
    found: list[Filing] = []
    for path in form_d_paths(index):
        url = ARCHIVES + path.removesuffix(".txt").replace("-", "") + "/"
        try:
            filing = parse_filing(_get(url + "primary_doc.xml", contact), url, day)
        except Exception:  # one unreadable filing should not stop the day
            continue
        if filing:
            found.append(filing)
    return found


@dataclass
class Site:
    url: str
    what_they_build: str
    pages: dict[str, str]  # url -> html of the pages read


def candidate_domains(company: str) -> list[str]:
    """Likely domains, most likely first: knowablelabs.com ... getknowable.ai ..."""
    words = re.findall(r"[a-z0-9]+", _fold(company))
    bases = dict.fromkeys(["".join(words), words[0]])
    return [f"{p}{b}.{t}" for b in bases for p in PREFIXES for t in TLDS]


def _fetch(url: str) -> tuple[str, str]:
    """The final URL after redirects and the page, or ("", "") if it doesn't load."""
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            body: bytes = response.read()
            return response.geturl(), html.unescape(body.decode("utf-8", "ignore"))
    except Exception:
        return "", ""


def _has_name(text: str, person: str) -> bool:
    parts = _fold(person).split()
    return len(parts) > 1 and all(re.search(rf"\b{re.escape(p)}\b", text) for p in parts)


def _description(page: str) -> str:
    for tag in re.findall(r"<meta[^>]+>", page, re.I):
        if re.search(r"""(name|property)=["'](og:)?description["']""", tag, re.I):
            content = re.search(r"""content=["']([^"']*)""", tag, re.I)
            if content and content.group(1).strip():
                return content.group(1).strip()[:300]
    title = re.search(r"<title[^>]*>(.*?)</title>", page, re.I | re.S)
    return title.group(1).strip()[:300] if title else ""


def _check(domain: str, filing: Filing) -> tuple[int, Site] | None:
    """2 if the site names someone on the filing, 1 if its legal name; None if neither."""
    final, home = _fetch(f"https://{domain}/")
    if not home or _fold(filing.company.split()[0]) not in _fold(home):
        return None
    host = urlsplit(final).hostname or domain
    # A redirect to a host that isn't theirs (e.g. x.azurestaticapps.net) keeps the domain
    # they registered, which is the one their email uses.
    if re.findall(r"[a-z0-9]+", _fold(filing.company))[0] not in host:
        host = domain
    root = f"https://{host}"
    pages = {final: home}
    for path in ABOUT_PATHS:
        url, page = _fetch(f"{root}/{path}")
        if page:
            pages[url] = page
    text = _fold(" ".join(pages.values()))
    if any(_has_name(text, person) for person in filing.people):
        rank = 2
    elif re.search(rf"\b{re.escape(_fold(filing.company))},?\s+{_LEGAL}\b", text):
        rank = 1
    else:
        return None
    return rank, Site(root + "/", _description(home), pages)


def find_site(filing: Filing) -> Site | None:
    """The company's own website, found by trying likely domains; no search engine or AI.

    Many companies share a name, so a site only counts if it names someone on the filing
    or shows the company's legal name ("Motaris Inc"). Sites that name nobody are missed.
    """
    with ThreadPoolExecutor(max_workers=16) as pool:
        checks = pool.map(lambda domain: _check(domain, filing), candidate_domains(filing.company))
        hits = [hit for hit in checks if hit]
    hits.sort(key=lambda hit: -hit[0])  # stable: equal ranks keep the likelier domain first
    return hits[0][1] if hits else None


def founder_email(
    name: str, domain: str, pages: dict[str, str]
) -> tuple[str | None, EmailStatus, str]:
    """Their own address if their site shows it; otherwise a guess."""
    for url, page in pages.items():
        for address in re.findall(rf"[\w.+-]+@{re.escape(domain)}", page, re.I):
            local = address.split("@")[0].lower()
            if any(len(part) > 1 and part in local for part in _fold(name).split()):
                return address.lower(), EmailStatus.PUBLISHED, url
    try:
        # shortcut: first@ is the most common format at small startups; a verifier
        # (e.g. Hunter's free tier) would pick the right one.
        guess = guess_email(name, domain, "first")
    except ValueError:
        return None, EmailStatus.NONE, ""
    return guess, EmailStatus.PATTERN, "Guessed first@ format; check before sending"


def to_lead(filing: Filing, site: Site, officer: str | None = None) -> Lead:
    """A lead for the filing's contact, or for another of its executive officers."""
    name = officer or filing.contact_name
    domain = (urlsplit(site.url).hostname or "").removeprefix("www.")
    email, status, source = founder_email(name, domain, site.pages)
    return Lead(
        kind=LeadKind.FOUNDER,
        company=filing.company,
        company_url=site.url,
        what_they_build=site.what_they_build,
        location=filing.location,
        source_url=filing.url,
        contact_name=name,
        contact_role=filing.contact_role if name == filing.contact_name else "Executive Officer",
        email=email,
        email_status=status,
        email_source=source,
        amount_usd=filing.amount_usd,
        announced_on=filing.filed_on,
        segment=Segment.EARLY if filing.amount_usd < EARLY_BELOW_USD else Segment.MID,
        region=Region.USA,
        hiring_signals=[
            f"SEC Form D: raised ${filing.amount_usd:,}, first sale {filing.first_sale}"
        ],
    )
