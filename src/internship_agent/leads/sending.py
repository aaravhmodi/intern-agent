"""Deterministic safety checks before an email is sent."""

from internship_agent.leads.schemas import EmailStatus, Lead


class SendBlocked(ValueError):
    pass


def check_send(lead: Lead, to: str, confirm_unverified: bool, resend: bool) -> None:
    """Raise SendBlocked unless this send is safe to perform."""
    if lead.sent_at is not None and not resend:
        raise SendBlocked(f"Already emailed {lead.sent_to} on {lead.sent_at:%Y-%m-%d}")
    to = to.strip().lower()
    guessed = lead.email_status is EmailStatus.PATTERN and to == (lead.email or "")
    if guessed and not confirm_unverified:
        raise SendBlocked("This address is a guess. Confirm you verified it before sending.")
