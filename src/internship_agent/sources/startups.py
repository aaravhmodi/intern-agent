"""Turn web-search findings into founder leads, keeping only verifiable, recent ones."""

import html
import unicodedata
import urllib.error
import urllib.request
from collections.abc import Callable
from datetime import date, timedelta

from pydantic import ValidationError

from internship_agent.ai import StartupFinding
from internship_agent.leads.schemas import Lead, LeadKind, Region, Segment
from internship_agent.leads.segments import ROUND_SEGMENT, parse_round
from internship_agent.sources.regions import region_from_text


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()


def mentions(page: str, finding: StartupFinding) -> bool:
    """The page names the company and the founder's last name."""
    folded = _fold(page)
    company = _fold(finding.company.split()[0])
    last_name = _fold(finding.founder_name.split()[-1])
    return company in folded and last_name in folded


def source_confirms(finding: StartupFinding) -> bool:
    """True if the cited article loads and names the company and founder.

    Guards against invented URLs and misattributed founders. Pages that refuse scripts
    (paywalls, bot protection) prove the page exists but cannot be read, so they pass.
    """
    url = finding.source_url
    if not url.startswith(("https://", "http://")):
        return False
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            body: bytes = response.read()
    except urllib.error.HTTPError as exc:
        return exc.code in (401, 403, 429)
    except Exception:
        return False
    return mentions(html.unescape(body.decode("utf-8", "ignore")), finding)


def to_leads(
    findings: list[StartupFinding],
    today: date,
    max_age_days: int,
    stages: list[Segment],
    confirm: Callable[[StartupFinding], bool] = source_confirms,
    region: Region | None = None,
) -> list[Lead]:
    leads: list[Lead] = []
    for f in findings:
        if not (today - timedelta(days=max_age_days) <= f.announced_on <= today):
            continue
        round_ = parse_round(f.round)
        segment = ROUND_SEGMENT.get(round_)
        if segment not in stages or not f.founder_name.strip():
            continue
        if not confirm(f):
            continue
        data = {
            "kind": LeadKind.FOUNDER,
            "company": f.company,
            "company_url": f.company_url,
            "contact_name": f.founder_name,
            "contact_role": f.founder_role,
            "round": round_,
            "amount_usd": f.amount_usd,
            "announced_on": f.announced_on,
            "source_url": f.source_url,
            "what_they_build": f.what_they_build,
            "location": f.location,
            "segment": segment,
            "region": region_from_text(f.location) or region,
            "hiring_signals": [f"Announcement post: {f.social_url}"] if f.social_url else [],
        }
        try:
            lead = Lead.model_validate({**data, "x_handle": f.x_handle})
        except ValidationError:
            lead = Lead.model_validate(data)  # drop an unusable X handle, keep the lead
        leads.append(lead)
    return leads
