from collections.abc import Awaitable, Callable
from datetime import date
from importlib.resources import files
from typing import Any
from urllib.parse import urlsplit

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, JSONResponse
from openai import OpenAI
from pydantic import BaseModel

from internship_agent.ai import draft_outreach
from internship_agent.config import get_settings
from internship_agent.leads.refill import DONE, open_postings
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus, Segment
from internship_agent.leads.segments import effective_segment
from internship_agent.leads.sending import SendBlocked
from internship_agent.mailer import MailError
from internship_agent.workflows import (
    find_more_postings,
    find_startups,
    handle_note,
    lead_store,
    preference_store,
    prepare_application,
    rescore_open,
    resume_text,
    save_answers,
    send_email,
)

app = FastAPI(title="Internship Agent", version="0.2.0")

_LOCAL_HOSTS = {"127.0.0.1", "localhost", "testserver"}


@app.middleware("http")
async def local_only(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Block DNS rebinding and cross-site requests: this server can send email."""
    host = (request.headers.get("host") or "").rsplit(":", 1)[0]
    if host not in _LOCAL_HOSTS:
        return JSONResponse({"detail": "Forbidden host"}, status_code=403)
    origin = request.headers.get("origin")
    if request.method != "GET" and origin is not None:
        origin_host = urlsplit(origin).hostname or ""
        if origin_host not in _LOCAL_HOSTS:
            return JSONResponse({"detail": "Cross-site request blocked"}, status_code=403)
    return await call_next(request)


class StatusUpdate(BaseModel):
    key: str
    status: LeadStatus


class KeyRequest(BaseModel):
    key: str


class FindMoreRequest(BaseModel):
    extra: int = 5


class FindStartupsRequest(BaseModel):
    stages: list[Segment] = [Segment.EARLY, Segment.MID]
    count: int = 5


class NoteRequest(BaseModel):
    message: str
    key: str | None = None


class AnswerEdit(BaseModel):
    index: int
    answer: str


class SaveAnswersRequest(BaseModel):
    key: str
    answers: list[AnswerEdit]


class PreferenceDelete(BaseModel):
    id: str


class SendRequest(BaseModel):
    key: str
    to: str
    subject: str
    body: str
    attach_resume: bool = True
    confirm_unverified: bool = False
    resend: bool = False


def _view(lead: Lead) -> dict[str, Any]:
    data = lead.model_dump(mode="json")
    segment = effective_segment(lead)
    data.update(key=lead.key, x_url=lead.x_url, segment=segment.value if segment else None)
    return data


def _sort_key(lead: Lead) -> tuple[int, int, int]:
    done = 1 if lead.status in DONE else 0
    score = lead.fit.score if lead.fit else -1
    recency = (lead.announced_on or date.min).toordinal()
    return (done, -score, -recency)


def _get(key: str) -> Lead:
    try:
        return lead_store(get_settings()).get(key)
    except KeyError as exc:
        raise HTTPException(404, "Lead not found") from exc


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return files("internship_agent.dashboard").joinpath("index.html").read_text(encoding="utf-8")


@app.get("/api/leads")
def leads() -> dict[str, Any]:
    settings = get_settings()
    all_leads = lead_store(settings).load()
    return {
        "leads": [_view(lead) for lead in sorted(all_leads, key=_sort_key)],
        "open_postings": len(open_postings(all_leads)),
        "sender": settings.gmail_address if settings.gmail_ready else None,
        "preferences": [p.model_dump(mode="json") for p in preference_store(settings).load()],
    }


@app.post("/api/status")
def set_status(update: StatusUpdate) -> dict[str, Any]:
    """Record a status. Marking a posting applied tops the open list back up."""
    settings = get_settings()
    lead = _get(update.key)
    lead.status = update.status
    lead_store(settings).upsert(lead)
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


@app.post("/api/find-startups")
def find_more_startups(request: FindStartupsRequest) -> dict[str, Any]:
    try:
        added = find_startups(get_settings(), request.stages, request.count)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"added": [_view(x) for x in added]}


@app.post("/api/draft")
def draft(request: KeyRequest) -> dict[str, Any]:
    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(400, "OPENAI_API_KEY is not set")
    lead = _get(request.key)
    client = OpenAI(api_key=settings.openai_api_key)
    lead.draft = draft_outreach(client, settings.openai_model, resume_text(settings), lead)
    if lead.status in (LeadStatus.NEW, LeadStatus.SCORED):
        lead.status = LeadStatus.DRAFTED
    lead_store(settings).upsert(lead)
    return {"lead": _view(lead)}


@app.post("/api/send")
def send(request: SendRequest) -> dict[str, Any]:
    """Send exactly one email. Only reachable from an explicit click in the dashboard."""
    _get(request.key)
    try:
        lead = send_email(
            get_settings(),
            request.key,
            request.to,
            request.subject,
            request.body,
            request.attach_resume,
            request.confirm_unverified,
            request.resend,
        )
    except (SendBlocked, MailError) as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}


@app.post("/api/note")
def note(request: NoteRequest) -> dict[str, Any]:
    """Interpret a note with AI: save it on the lead, update status, learn preferences."""
    message = request.message.strip()
    if not message:
        raise HTTPException(400, "Write a note first")
    if request.key:
        _get(request.key)
    try:
        result = handle_note(get_settings(), message[:2000], request.key)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {
        "reply": result.reply,
        "status_changed": result.status_changed,
        "learned": [p.model_dump(mode="json") for p in result.learned],
        "lead": _view(result.lead) if result.lead else None,
    }


@app.post("/api/preferences/delete")
def delete_preference(request: PreferenceDelete) -> dict[str, Any]:
    if not preference_store(get_settings()).remove(request.id):
        raise HTTPException(404, "Preference not found")
    return {"ok": True}


@app.post("/api/rescore")
def rescore() -> dict[str, Any]:
    """Re-score all to-do leads against the current preferences (uses OpenAI)."""
    try:
        checked, skipped = rescore_open(get_settings())
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"checked": checked, "skipped": [_view(x) for x in skipped]}


@app.post("/api/application/prepare")
def prepare(request: KeyRequest) -> dict[str, Any]:
    """Read the posting's application questions and prepare answers (nothing is submitted)."""
    _get(request.key)
    try:
        lead = prepare_application(get_settings(), request.key)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}


@app.post("/api/application/save")
def save(request: SaveAnswersRequest) -> dict[str, Any]:
    _get(request.key)
    edits = {e.index: e.answer[:5000] for e in request.answers}
    try:
        lead = save_answers(get_settings(), request.key, edits)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}
