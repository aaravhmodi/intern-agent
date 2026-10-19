"""Recent US startup raises from SEC Form D filings: free and official, no key or account.

A company must file a Form D within 15 days of first selling shares, often before any
announcement. The filing names the people running it but not its website or email.
The SEC asks automated clients to name themselves with a contact address and to make
no more than 10 requests a second.
"""

import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import date
from urllib.parse import urlsplit

from internship_agent.ai import CompanySite
from internship_agent.leads.emails import guess_email
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, Region, Segment
from internship_agent.sources.startups import page_text

ARCHIVES = "https://www.sec.gov/Archives/"
TECH = {"Computers", "Other Technology", "Telecommunications"}
# Roughly pre-seed to Series B: smaller is friends and family, larger is a late-stage company.
MIN_USD, MAX_USD = 250_000, 50_000_000
EARLY_BELOW_USD = 5_000_000
_SUFFIX = re.compile(r",?\s+(inc|incorporated|llc|corp|corporation|co|ltd|pbc)\.?$", re.I)


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


def founder_email(
    name: str, domain: str, published: str | None, source: str | None
) -> tuple[str | None, EmailStatus, str]:
    """A published address only if it is theirs and the cited page shows it; else a guess."""
    local = (published or "").split("@")[0].lower()
    theirs = any(len(part) > 1 and part.lower() in local for part in name.split())
    if published and source and theirs and published.lower() in page_text(source).lower():
        return published.lower(), EmailStatus.PUBLISHED, source
    try:
        # shortcut: first@ is the most common format at small startups; a verifier
        # (e.g. Hunter's free tier) would pick the right one.
        guess = guess_email(name, domain, "first")
    except ValueError:
        return None, EmailStatus.NONE, ""
    return guess, EmailStatus.PATTERN, "Guessed first@ format; check before sending"


def to_lead(filing: Filing, site: CompanySite) -> Lead:
    assert site.company_url
    domain = urlsplit(site.company_url).netloc.lower().removeprefix("www.")
    email, status, source = founder_email(
        filing.contact_name, domain, site.email, site.email_source
    )
    return Lead(
        kind=LeadKind.FOUNDER,
        company=filing.company,
        company_url=site.company_url,
        what_they_build=site.what_they_build,
        location=filing.location,
        source_url=filing.url,
        contact_name=filing.contact_name,
        contact_role=filing.contact_role,
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
