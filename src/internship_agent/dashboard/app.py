from datetime import date
from importlib.resources import files
from typing import Any
from urllib.parse import quote

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from openai import OpenAI
from pydantic import BaseModel

from internship_agent.ai import draft_outreach
from internship_agent.config import get_settings
from internship_agent.leads.refill import DONE, open_postings
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus
from internship_agent.resume import load_resume_text
from internship_agent.workflows import find_more_postings, lead_store

app = FastAPI(title="Internship Agent", version="0.1.0")


class StatusUpdate(BaseModel):
    key: str
    status: LeadStatus


class KeyRequest(BaseModel):
    key: str


class FindMoreRequest(BaseModel):
    extra: int = 5


def _mailto(lead: Lead) -> str | None:
    if not lead.email or not lead.draft:
        return None
    subject = quote(lead.draft.email_subject)
    body = quote(lead.draft.email_body)
    return f"mailto:{lead.email}?subject={subject}&body={body}"


def _view(lead: Lead) -> dict[str, Any]:
    data = lead.model_dump(mode="json")
    data.update(key=lead.key, x_url=lead.x_url, mailto=_mailto(lead))
    return data


def _sort_key(lead: Lead) -> tuple[int, int, int]:
    done = 1 if lead.status in DONE else 0
    score = lead.fit.score if lead.fit else -1
    recency = (lead.announced_on or date.min).toordinal()
    return (done, -score, -recency)


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return files("internship_agent.dashboard").joinpath("index.html").read_text(encoding="utf-8")


@app.get("/api/leads")
def leads() -> dict[str, Any]:
    all_leads = lead_store(get_settings()).load()
    return {
        "leads": [_view(lead) for lead in sorted(all_leads, key=_sort_key)],
        "open_postings": len(open_postings(all_leads)),
        "applied": sum(1 for lead in all_leads if lead.status is LeadStatus.APPLIED),
        "founders": sum(1 for lead in all_leads if lead.kind is LeadKind.FOUNDER),
    }


@app.post("/api/status")
def set_status(update: StatusUpdate) -> dict[str, Any]:
    """Record a status. Marking a posting applied tops the open list back up."""
    settings = get_settings()
    store = lead_store(settings)
    try:
        lead = store.get(update.key)
    except KeyError as exc:
        raise HTTPException(404, "Lead not found") from exc
    lead.status = update.status
    store.upsert(lead)
    added: list[Lead] = []
    if update.status is LeadStatus.APPLIED and lead.kind is LeadKind.POSTING:
        added = find_more_postings(settings, settings.target_open_postings)
    return {"lead": _view(lead), "added": [_view(x) for x in added]}


@app.post("/api/find-more")
def find_more(request: FindMoreRequest) -> dict[str, Any]:
    settings = get_settings()
    current = len(open_postings(lead_store(settings).load()))
    added = find_more_postings(settings, current + request.extra)
    return {"added": [_view(x) for x in added]}


@app.post("/api/draft")
def draft(request: KeyRequest) -> dict[str, Any]:
    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(400, "OPENAI_API_KEY is not set")
    store = lead_store(settings)
    try:
        lead = store.get(request.key)
    except KeyError as exc:
        raise HTTPException(404, "Lead not found") from exc
    resume = load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")
    client = OpenAI(api_key=settings.openai_api_key)
    lead.draft = draft_outreach(client, settings.openai_model, resume, lead)
    if lead.status in (LeadStatus.NEW, LeadStatus.SCORED):
        lead.status = LeadStatus.DRAFTED
    store.upsert(lead)
    return {"lead": _view(lead)}
