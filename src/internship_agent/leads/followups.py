"""Follow-ups to outreach emails that got no reply: who is due one, and what it says.

A follow-up goes out when FOLLOWUP_DAYS have passed since the last email to someone and
nothing has come back. There are only as many as there are TEMPLATES, so nobody gets a
third. The wording is fixed text, not written by a model, because it is sent without
being reviewed first.
"""

from datetime import datetime, timedelta

from internship_agent.leads.schemas import Lead, LeadStatus

# What each follow-up says, in order: the same plain reminder each time, no apologising.
# {first} is their first name and {company} the company.
TEMPLATES = (
    """\
Hi {first},

Following up again on a Winter 2027 (Jan–Apr) software engineering internship at {company}.

Do you have 15 minutes to talk next week?

Aarav""",
) * 2

# Addresses at these domains say nothing about a company, so a reply from someone else
# there is not a reply from the company.
FREE_MAIL = frozenset(
    {
        "gmail.com",
        "googlemail.com",
        "outlook.com",
        "hotmail.com",
        "live.com",
        "yahoo.com",
        "icloud.com",
        "me.com",
        "proton.me",
        "protonmail.com",
        "aol.com",
        "hey.com",
    }
)


def last_contact(lead: Lead) -> datetime | None:
    """When this person was last emailed: the first email or the latest follow-up."""
    times = [t for t in (lead.sent_at, *lead.followups) if t is not None]
    return max(times) if times else None


def is_due(lead: Lead, now: datetime, wait_days: int) -> bool:
    """Whether a follow-up should go out now, before checking the inbox for a reply."""
    if not lead.sent_at or not lead.sent_to or lead.status is LeadStatus.SKIPPED:
        return False
    if lead.replied_at is not None or lead.followups_stopped:
        return False
    if len(lead.followups) >= len(TEMPLATES):
        return False
    contacted = last_contact(lead)
    return contacted is not None and now - contacted >= timedelta(days=wait_days)


def first_name(lead: Lead) -> str:
    name = lead.contact_name.split()
    return name[0] if name else "there"


def followup_body(lead: Lead) -> str:
    """The text of this lead's next follow-up."""
    template = TEMPLATES[len(lead.followups)]
    return template.format(first=first_name(lead), company=lead.company)


def reply_subject(original: str) -> str:
    subject = original.strip()
    return subject if subject.lower().startswith("re:") else f"Re: {subject}"


def company_domain(address: str) -> str | None:
    """The company's mail domain, or None when the address is at a free mail provider."""
    domain = address.rsplit("@", 1)[-1].strip().lower()
    return None if not domain or domain in FREE_MAIL else domain
