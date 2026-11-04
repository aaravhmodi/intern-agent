"""Everyone you already know of at a company, and a vCard export of them.

Ideas from career-ops' contacts.mjs / contact-lookup.mjs: check for a saved (warm)
contact at a company before searching for a cold one, and export the phonebook as
vCard 3.0 with stable UIDs so re-importing updates contacts instead of duplicating them.
"""

import hashlib
import re
from enum import StrEnum

from pydantic import BaseModel

from internship_agent.leads.schemas import Lead

_LEGAL_SUFFIX = re.compile(r"\b(inc|llc|ltd|limited|corp|corporation|co|gmbh|sa|plc)\.?$")


class ContactType(StrEnum):
    FOUNDER = "founder"
    RECRUITER = "recruiter"
    HIRING_MANAGER = "hiring-manager"
    ENGINEER = "engineer"
    OTHER = "other"


class Contact(BaseModel):
    name: str
    company: str
    role: str = ""
    type: ContactType = ContactType.OTHER
    email: str | None = None
    linkedin_url: str | None = None
    x_handle: str | None = None
    lead_keys: list[str] = []


def company_key(name: str) -> str:
    """'Acme, Inc.' and 'acme' are the same company; 'Acme Robotics' is not."""
    key = re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
    return _LEGAL_SUFFIX.sub("", key).strip()


def contact_type(role: str) -> ContactType:
    role = role.lower()
    if re.search(r"recruit|talent|people (?:ops|partner)|\bhr\b|university relations", role):
        return ContactType.RECRUITER
    if re.search(r"founder|\bceo\b|\bcto\b|\bcoo\b|chief", role):
        return ContactType.FOUNDER
    if re.search(r"manager|head of|director|\blead\b|\bvp\b|vice president", role):
        return ContactType.HIRING_MANAGER
    if re.search(r"engineer|developer|scientist|researcher", role):
        return ContactType.ENGINEER
    return ContactType.OTHER


def contacts_from_leads(leads: list[Lead]) -> list[Contact]:
    """Each named person across all leads once, with whatever channels any lead has."""
    found: dict[tuple[str, str], Contact] = {}

    def add(lead: Lead, name: str, role: str, **channels: str | None) -> None:
        name = " ".join(name.split())
        if not name:
            return
        key = (company_key(lead.company), name.casefold())
        contact = found.get(key)
        if contact is None:
            contact = found[key] = Contact(
                name=name, company=lead.company, role=role, type=contact_type(role)
            )
        if not contact.role and role:
            contact.role, contact.type = role, contact_type(role)
        for field, value in channels.items():
            if value and not getattr(contact, field):
                setattr(contact, field, value)
        if lead.key not in contact.lead_keys:
            contact.lead_keys.append(lead.key)

    for lead in leads:
        add(
            lead,
            lead.contact_name,
            lead.contact_role,
            email=lead.email,
            linkedin_url=lead.linkedin_url,
            x_handle=lead.x_handle,
        )
        for person in lead.people:
            add(lead, person.name, person.role, linkedin_url=person.linkedin_url)
    return list(found.values())


def contacts_at(leads: list[Lead], company: str) -> list[Contact]:
    key = company_key(company)
    return [c for c in contacts_from_leads(leads) if company_key(c.company) == key]


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("\n", "\\n").replace(",", "\\,").replace(";", "\\;")


def _fold(line: str) -> str:
    """Fold at 75 octets without splitting a UTF-8 character (RFC 2425)."""
    out: list[str] = []
    current, size, limit = "", 0, 75
    for char in line:
        width = len(char.encode("utf-8"))
        if size + width > limit:
            out.append(current)
            current, size, limit = " ", 1, 75
        current += char
        size += width
    out.append(current)
    return "\r\n".join(out)


def uid(contact: Contact) -> str:
    digest = hashlib.sha1(
        f"{company_key(contact.company)}\n{contact.name.casefold()}".encode()
    ).hexdigest()
    return f"internship-agent-{digest[:16]}"


def to_vcard(contacts: list[Contact]) -> str:
    cards: list[str] = []
    for c in contacts:
        *given, family = c.name.split()
        lines = [
            "BEGIN:VCARD",
            "VERSION:3.0",
            f"UID:{uid(c)}",
            f"FN:{_escape(c.name)}",
            f"N:{_escape(family)};{_escape(' '.join(given))};;;",
            f"ORG:{_escape(c.company)}",
        ]
        if c.role:
            lines.append(f"TITLE:{_escape(c.role)}")
        if c.email:
            lines.append(f"EMAIL;TYPE=INTERNET:{c.email}")
        if c.linkedin_url:
            lines.append(f"URL:{c.linkedin_url}")
        if c.x_handle:
            lines.append(f"X-SOCIALPROFILE;TYPE=twitter:https://x.com/{c.x_handle}")
        lines.append(f"NOTE:{_escape(c.type.value)}")
        lines.append("END:VCARD")
        cards.append("\r\n".join(_fold(line) for line in lines))
    return "".join(card + "\r\n" for card in cards)
