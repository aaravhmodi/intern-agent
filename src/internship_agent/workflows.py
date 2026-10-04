"""Orchestration that combines deterministic steps with OpenAI calls and email."""

import json
from datetime import UTC, date, datetime, timedelta

from openai import OpenAI

from internship_agent import mailer
from internship_agent.ai import assess_fit, search_startups
from internship_agent.config import Settings
from internship_agent.leads.refill import refill
from internship_agent.leads.schemas import Lead, LeadStatus, Segment
from internship_agent.leads.sending import check_send
from internship_agent.leads.store import LeadStore, merge
from internship_agent.resume import load_resume_text
from internship_agent.sources import simplify, startups


def lead_store(settings: Settings) -> LeadStore:
    return LeadStore(settings.data_dir / "leads.json")


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=settings.openai_api_key)


def resume_text(settings: Settings) -> str:
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")


def score(settings: Settings, leads: list[Lead]) -> None:
    """Score leads in place and store them; keeps a researched segment if one is set."""
    if not leads or not settings.openai_api_key:
        return
    client, resume, store = _openai(settings), resume_text(settings), lead_store(settings)
    for lead in leads:
        result = assess_fit(client, settings.openai_model, resume, lead)
        lead.fit = result.fit
        lead.segment = lead.segment or result.company_segment
        if lead.status is LeadStatus.NEW:
            lead.status = LeadStatus.SCORED
        store.upsert(lead)


def find_more_postings(settings: Settings, target_open: int) -> list[Lead]:
    """Top up open postings from the public SimplifyJobs list and score the new ones."""
    store = lead_store(settings)
    candidates = [simplify.to_lead(p) for p in simplify.matching(simplify.parse(simplify.fetch()))]
    leads, added = refill(store.load(), candidates, target_open)
    store.save(leads)
    score(settings, added)
    return added


def find_startups(
    settings: Settings, stages: list[Segment], count: int = 5, max_age_days: int = 60
) -> list[Lead]:
    """Web-search recent funding rounds, keep verifiable ones, store and score them."""
    store = lead_store(settings)
    existing = store.load()
    today = date.today()
    findings = search_startups(
        _openai(settings),
        settings.openai_model,
        today - timedelta(days=max_age_days),
        today,
        stages,
        sorted({lead.company for lead in existing}),
        count,
    )
    leads, _ = merge(existing, startups.to_leads(findings, today, max_age_days, stages))
    store.save(leads)
    new = leads[len(existing) :]
    score(settings, new)
    return new


def send_email(
    settings: Settings,
    key: str,
    to: str,
    subject: str,
    body: str,
    attach_resume: bool,
    confirm_unverified: bool,
    resend: bool = False,
) -> Lead:
    """Send one email for a lead after the safety checks, then record it."""
    if not settings.gmail_ready or not settings.gmail_address or not settings.gmail_app_password:
        raise mailer.MailError("Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env to send email.")
    store = lead_store(settings)
    lead = store.get(key)
    check_send(lead, to, confirm_unverified, resend)
    message = mailer.build_message(
        settings.gmail_address,
        to.strip(),
        subject,
        body,
        settings.resume_path if attach_resume else None,
    )
    mailer.send(message, settings.gmail_address, settings.gmail_app_password.get_secret_value())
    lead.sent_at = datetime.now(UTC)
    lead.sent_to = to.strip().lower()
    lead.status = LeadStatus.CONTACTED
    store.upsert(lead)
    log = settings.data_dir / "sent-log.jsonl"
    with log.open("a", encoding="utf-8") as f:
        at = lead.sent_at.isoformat()
        record = {"at": at, "key": key, "to": lead.sent_to, "subject": subject}
        f.write(json.dumps(record) + "\n")
    return lead
