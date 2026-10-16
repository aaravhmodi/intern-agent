"""Deterministic safety checks before an email is sent."""

import re

from internship_agent.leads.schemas import EmailStatus, Lead


class SendBlocked(ValueError):
    pass


_IMMIGRATION_TERMS = re.compile(
    r"\bvisa\b|\bj[\s-]?1\b|\bsponsor(?:ship)?\b|\bimmigration\b|"
    r"\bwork authori[sz]ation\b|\bwork permit\b|\bgreen card\b",
    re.IGNORECASE,
)


def check_send(lead: Lead, to: str, confirm_unverified: bool, resend: bool) -> None:
    """Raise SendBlocked unless this send is safe to perform."""
    if lead.sent_at is not None and not resend:
        raise SendBlocked(f"Already emailed {lead.sent_to} on {lead.sent_at:%Y-%m-%d}")
    to = to.strip().lower()
    guessed = lead.email_status is EmailStatus.PATTERN and to == (lead.email or "")
    if guessed and not confirm_unverified:
        raise SendBlocked("This address is a guess. Confirm you verified it before sending.")


def check_outreach_text(subject: str, body: str) -> None:
    """Prevent visa or work-authorization details from appearing in lead email."""
    if _IMMIGRATION_TERMS.search(f"{subject}\n{body}"):
        raise SendBlocked("Lead emails must not mention visa, sponsorship, or work authorization.")
