"""Orchestration that combines deterministic steps with OpenAI calls."""

from openai import OpenAI

from internship_agent.ai import assess_fit
from internship_agent.config import Settings
from internship_agent.leads.refill import refill
from internship_agent.leads.schemas import Lead, LeadStatus
from internship_agent.leads.store import LeadStore
from internship_agent.resume import load_resume_text
from internship_agent.sources import simplify


def lead_store(settings: Settings) -> LeadStore:
    return LeadStore(settings.data_dir / "leads.json")


def find_more_postings(settings: Settings, target_open: int) -> list[Lead]:
    """Top up open postings from the public SimplifyJobs list and score the new ones."""
    store = lead_store(settings)
    candidates = [simplify.to_lead(p) for p in simplify.matching(simplify.parse(simplify.fetch()))]
    leads, added = refill(store.load(), candidates, target_open)
    store.save(leads)
    if added and settings.openai_api_key:
        client = OpenAI(api_key=settings.openai_api_key)
        resume = load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")
        for lead in added:
            lead.fit = assess_fit(client, settings.openai_model, resume, lead)
            lead.status = LeadStatus.SCORED
            store.upsert(lead)
    return added
