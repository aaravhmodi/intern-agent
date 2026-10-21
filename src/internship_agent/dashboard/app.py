import threading
import time
from collections.abc import Awaitable, Callable
from contextlib import nullcontext
from datetime import UTC, date, datetime
from importlib.resources import files
from typing import Any
from urllib.parse import urlsplit

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from openai import OpenAI
from pydantic import BaseModel

from internship_agent import agenda, chat, pipeline
from internship_agent.ai import draft_outreach
from internship_agent.applications.browser import screenshot_path
from internship_agent.config import get_settings
from internship_agent.followup_run import run_followups
from internship_agent.leads.refill import DONE, open_postings
from internship_agent.leads.schemas import Lead, LeadKind, LeadStatus, Region, Segment
from internship_agent.leads.segments import effective_segment
from internship_agent.leads.sending import SendBlocked
from internship_agent.mailbox import GmailMailbox, MailboxError
from internship_agent.mailer import MailError
from internship_agent.opportunities import run as opportunity_run
from internship_agent.opportunities.schemas import Opportunity, OpportunityStatus
from internship_agent.opportunities.store import OpportunityStore
from internship_agent.workflows import (
    _incompatible_term,
    _record_openai_usage,
    find_more_postings,
    find_people,
    find_startups,
    handle_note,
    lead_store,
    preference_store,
    prepare_application,
    refresh_saved_application,
    rescore_open,
    resume_text,
    save_answers,
    send_email,
    submit_application,
)
from internship_agent.workflows import (
    daily as run_daily,
)

app = FastAPI(title="Internship Agent", version="0.2.0")

_LOCAL_HOSTS = {"127.0.0.1", "localhost", "testserver"}
_ALLOWED_HOSTS = _LOCAL_HOSTS | set(get_settings().dashboard_allowed_hosts)


@app.middleware("http")
async def local_only(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Block DNS rebinding and cross-site requests: this server can send email."""
    host = (request.headers.get("host") or "").rsplit(":", 1)[0]
    if host not in _ALLOWED_HOSTS:
        return JSONResponse({"detail": "Forbidden host"}, status_code=403)
    origin = request.headers.get("origin")
    if request.method != "GET" and origin is not None:
        origin_host = urlsplit(origin).hostname or ""
        if origin_host not in _ALLOWED_HOSTS:
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
    regions: list[Region] | None = None
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


class SubmitApplicationRequest(BaseModel):
    key: str
    dry_run: bool = False


class PreferenceDelete(BaseModel):
    id: str


class FollowupsRequest(BaseModel):
    # Find out who would get what without sending anything.
    dry_run: bool = True


@app.post("/api/daily/run")
def daily_run() -> dict[str, Any]:
    """Run the scheduled, read-only discovery and application-material preparation."""
    try:
        report = run_daily(get_settings())
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {
        "new": len(report.new),
        "skipped": len(report.skipped),
        "prepared": len(report.prepared),
        "submitted": report.submitted,
        "pushes": report.pushed,
    }


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
    proof = screenshot_path(get_settings().application_browser_dir, lead, "confirmations")
    data.update(
        key=lead.key,
        x_url=lead.x_url,
        segment=segment.value if segment else None,
        has_proof=proof.is_file(),
    )
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


@app.get("/dashboard.css")
def dashboard_css() -> Response:
    stylesheet = files("internship_agent.dashboard").joinpath("dashboard.css")
    return Response(stylesheet.read_text(encoding="utf-8"), media_type="text/css")


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
        added = find_startups(
            get_settings(), request.stages, request.count, regions=request.regions
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"added": [_view(x) for x in added]}


@app.post("/api/people")
def people(request: KeyRequest) -> dict[str, Any]:
    """Look up more people at the company to connect with on LinkedIn (uses OpenAI)."""
    _get(request.key)
    try:
        lead = find_people(get_settings(), request.key)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}


@app.post("/api/draft")
def draft(request: KeyRequest) -> dict[str, Any]:
    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(400, "OPENAI_API_KEY is not set")
    lead = _get(request.key)
    client = OpenAI(api_key=settings.openai_api_key)
    lead.draft = draft_outreach(client, settings.openai_writing_model, resume_text(settings), lead)
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


@app.post("/api/followups/run")
def followups(request: FollowupsRequest) -> dict[str, Any]:
    """Follow up on emails with no reply. Sends only when FOLLOWUPS_ENABLED is on.

    Called on a schedule, so unlike /api/send no click is involved: it writes only to
    people already emailed from here, only the fixed follow-up texts, at most twice each,
    and never after a reply or a bounce.
    """
    settings = get_settings()
    if not settings.gmail_address or not settings.gmail_app_password:
        raise HTTPException(400, "Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env first.")
    dry_run = request.dry_run or not settings.followups_enabled
    password = settings.gmail_app_password.get_secret_value()
    try:
        with (
            GmailMailbox(settings.gmail_address, password) as mailbox,
            (
                GmailMailbox(*settings.gmail_account("outreach"))
                if settings.outreach_ready
                else nullcontext()
            ) as outreach,
        ):
            report = run_followups(
                settings,
                mailbox,
                dry_run=dry_run,
                pause_seconds=0 if dry_run else 2,
                outreach_mailbox=outreach,
            )
    except (MailboxError, MailError) as exc:
        raise HTTPException(503, str(exc)) from exc
    return {"enabled": settings.followups_enabled, **report.model_dump(mode="json")}


class ChatRequest(BaseModel):
    messages: list[chat.ChatMessage]
    key: str | None = None  # the lead or opportunity open in the dashboard


@app.post("/api/chat")
def ask(request: ChatRequest) -> dict[str, Any]:
    """Answer from your profile, GitHub, the agent's data and the web (uses OpenAI)."""
    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(400, "OPENAI_API_KEY is not set")
    if not request.messages or request.messages[-1].role != "user":
        raise HTTPException(400, "Ask a question first")
    reply = chat.answer(
        settings,
        OpenAI(api_key=settings.openai_api_key),
        request.messages,
        request.key,
        resume_text(settings),
        usage=lambda u: _record_openai_usage(settings, "chat", settings.chat_model, u),
    )
    return {"reply": reply}


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


@app.get("/api/application/proof")
def application_proof(key: str) -> FileResponse:
    """Screenshot of the employer's confirmation page, taken right after submitting."""
    path = screenshot_path(get_settings().application_browser_dir, _get(key), "confirmations")
    if not path.is_file():
        raise HTTPException(404, "No confirmation screenshot for this application")
    return FileResponse(path, media_type="image/png")


@app.post("/api/application/auto")
def auto_apply(request: KeyRequest) -> dict[str, Any]:
    """One click: prepare (or refresh) answers like the daily run, then submit.

    You picked this job, so it applies even outside January-April; for such a posting the
    answers and cover letter are re-prepared to match the posting's own term and dates.
    """
    settings = get_settings()
    lead = _get(request.key)
    try:
        if _incompatible_term(lead):
            prepare_application(settings, request.key, accept_posting_term=True)
        elif lead.application and lead.application.cover_letter:
            refresh_saved_application(settings, request.key)
        else:
            prepare_application(settings, request.key)
        lead = submit_application(settings, request.key, accept_posting_term=True)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}


@app.post("/api/application/retry")
def allow_retry(request: KeyRequest) -> dict[str, Any]:
    """You checked an uncertain attempt never reached the employer: allow one more submit."""
    settings = get_settings()
    lead = _get(request.key)
    if lead.application is None or lead.application.submission_status != "uncertain":
        raise HTTPException(400, "Only an uncertain application can be reopened")
    lead.application.submission_status = "pending"
    lead.application.submission_detail = ""
    lead_store(settings).upsert(lead)
    return {"lead": _view(lead)}


def _opportunity(key: str) -> Opportunity:
    try:
        return OpportunityStore(get_settings()).get(key)
    except KeyError as exc:
        raise HTTPException(404, "Opportunity not found") from exc


def _opportunity_view(item: Opportunity) -> dict[str, Any]:
    return {**item.model_dump(mode="json"), "key": item.key}


class OpportunityStatusUpdate(BaseModel):
    key: str
    status: OpportunityStatus


class CheckRequest(BaseModel):
    key: str | None = None  # one event; otherwise the `limit` most worth checking
    limit: int = 5


@app.post("/api/opportunities/check")
def check_opportunities(request: CheckRequest) -> dict[str, Any]:
    """Read events' own pages: location, in person or online, travel paid, effort, fit.

    Hackathons that now clear the auto-pick bar are marked Interested right away.
    """
    settings = get_settings()
    if request.key:
        _opportunity(request.key)
    try:
        done = opportunity_run.check_events(
            settings, [request.key] if request.key else None, min(request.limit, 10)
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    picked = opportunity_run.auto_pick(settings)
    return {
        "checked": [_opportunity_view(o) for o in done],
        "picked": [_opportunity_view(o) for o in picked],
    }


def _calendar_items() -> list[agenda.Item]:
    settings = get_settings()
    return agenda.items(
        lead_store(settings).load(),
        OpportunityStore(settings).load(),
        settings.followup_days,
        date.today(),
    )


# Job pipeline: both Gmail inboxes, read in the background and on demand.
_pipeline_lock = threading.Lock()
_pipeline_state: dict[str, Any] = {"at": None, "error": None}


def _scan_inboxes() -> int:
    """One scan at a time; remembers when it last ran and how it went (never the mail)."""
    with _pipeline_lock:
        try:
            added = pipeline.scan(get_settings())
        except Exception as exc:  # IMAP or network trouble: report the kind, not the words
            _pipeline_state.update(error=type(exc).__name__)
            raise
        _pipeline_state.update(at=datetime.now(UTC).isoformat(), error=None)
        return len(added)


def _scan_forever(minutes: int) -> None:
    while True:
        try:
            _scan_inboxes()
        except Exception:
            pass  # recorded in _pipeline_state; try again next round
        time.sleep(minutes * 60)


@app.on_event("startup")
def _start_inbox_scans() -> None:
    settings = get_settings()
    if settings.pipeline_sync_minutes > 0 and pipeline.inboxes(settings):
        threading.Thread(
            target=_scan_forever, args=(settings.pipeline_sync_minutes,), daemon=True
        ).start()


@app.get("/api/pipeline")
def job_pipeline() -> dict[str, Any]:
    """Every company you applied to or emailed, in the column of its latest email."""
    settings = get_settings()
    return {
        "cards": pipeline.board(lead_store(settings).load(), pipeline.events(settings)),
        "inboxes": [address for address, _ in pipeline.inboxes(settings)],
        "last_scan": _pipeline_state["at"],
        "error": _pipeline_state["error"],
    }


@app.post("/api/pipeline/scan")
def scan_inboxes() -> dict[str, Any]:
    """Read both inboxes now (read-only)."""
    if not pipeline.inboxes(get_settings()):
        raise HTTPException(400, "Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD to read your inbox")
    try:
        return {"added": _scan_inboxes()}
    except Exception as exc:
        raise HTTPException(503, f"Couldn't read Gmail ({type(exc).__name__})") from exc


@app.get("/api/calendar")
def calendar() -> dict[str, Any]:
    """Deadlines, event dates and follow-ups from both agents."""
    return {"items": [i.model_dump(mode="json") for i in _calendar_items()]}


@app.get("/api/calendar.ics")
def calendar_ics(everything: bool = False) -> Response:
    """The same calendar for Google or Outlook Calendar: your plans and promising events."""
    found = [i for i in _calendar_items() if everything or i.mine]
    return Response(
        agenda.to_ics(found, datetime.now(UTC)),
        media_type="text/calendar",
        headers={"Content-Disposition": 'attachment; filename="internships-and-opportunities.ics"'},
    )


@app.get("/api/opportunities")
def opportunities() -> dict[str, Any]:
    today = date.today()
    items = [
        o for o in OpportunityStore(get_settings()).load() if opportunity_run.upcoming(o, today)
    ]
    items.sort(key=lambda o: opportunity_run.next_date(o, today))
    return {"opportunities": [_opportunity_view(o) for o in items]}


@app.post("/api/opportunities/refresh")
def refresh_opportunities() -> dict[str, Any]:
    """Pull the hackathon, conference and research-deadline feeds (no AI)."""
    added = opportunity_run.refresh(get_settings())
    return {"added": [_opportunity_view(o) for o in added]}


@app.post("/api/opportunities/find-events")
def find_events() -> dict[str, Any]:
    """Web-search networking events near EVENT_CITIES (uses OpenAI)."""
    try:
        added = opportunity_run.find_events(get_settings())
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"added": [_opportunity_view(o) for o in added]}


class Cookie(BaseModel):
    """One browser cookie in Playwright's form; values are never logged."""

    model_config = {"extra": "allow"}
    name: str
    value: str
    domain: str
    path: str = "/"


class SessionsRequest(BaseModel):
    cookies: list[Cookie]


@app.post("/api/browser-sessions")
def browser_sessions(request: SessionsRequest) -> dict[str, Any]:
    """Sign-ins made on your laptop (`opportunities sign-in`), for the application browser."""
    from internship_agent.opportunities.browser import import_sessions

    allowed = tuple(d for _, _, domains in opportunity_run.SIGN_IN_SITES.values() for d in domains)
    cookies = [c.model_dump() for c in request.cookies if c.domain.lstrip(".").endswith(allowed)]
    try:
        added = import_sessions(get_settings().application_browser_dir, cookies)
    except Exception as exc:  # most often: the browser is busy applying right now
        raise HTTPException(
            409, f"Couldn't open the application browser ({type(exc).__name__})"
        ) from exc
    return {"added": added}


@app.post("/api/opportunities/apply")
def apply_to_event(request: KeyRequest) -> dict[str, Any]:
    """Apply to a hackathon or RSVP to an event now, in the saved browser (uses OpenAI)."""
    item = _opportunity(request.key)
    if item.kind not in opportunity_run.APPLIABLE:
        raise HTTPException(400, "Only hackathons and networking events can be applied to for you")
    try:
        opportunity_run.apply_events(get_settings(), [request.key])
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"opportunity": _opportunity_view(_opportunity(request.key))}


@app.post("/api/opportunities/apply/retry")
def allow_event_retry(request: KeyRequest) -> dict[str, Any]:
    """You checked it didn't go through: clear the attempt so it can be tried again."""
    item = _opportunity(request.key)
    if item.application is None or item.application.status == "submitted":
        raise HTTPException(400, "Only an attempt that didn't go through can be reopened")
    item.application = None
    OpportunityStore(get_settings()).upsert(item)
    return {"opportunity": _opportunity_view(item)}


@app.get("/api/opportunities/proof")
def event_proof(key: str) -> FileResponse:
    """Screenshot of the event's confirmation page, taken right after applying."""
    path = opportunity_run.proof_path(get_settings(), _opportunity(key).key)
    if not path.is_file():
        raise HTTPException(404, "No confirmation screenshot for this event")
    return FileResponse(path, media_type="image/png")


@app.post("/api/opportunities/strategy")
def opportunity_strategy(request: KeyRequest) -> dict[str, Any]:
    """Read the venue's call for papers and plan a submission (uses OpenAI)."""
    _opportunity(request.key)
    try:
        item = opportunity_run.plan_submission(get_settings(), request.key)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"opportunity": _opportunity_view(item)}


@app.post("/api/opportunities/status")
def opportunity_status(update: OpportunityStatusUpdate) -> dict[str, Any]:
    item = _opportunity(update.key)
    item.status = update.status
    OpportunityStore(get_settings()).upsert(item)
    return {"opportunity": _opportunity_view(item)}


@app.post("/api/application/submit")
def submit(request: SubmitApplicationRequest) -> dict[str, Any]:
    """Fill and submit one prepared, eligible application in the saved browser session."""
    _get(request.key)
    try:
        lead = submit_application(get_settings(), request.key, dry_run=request.dry_run)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    return {"lead": _view(lead)}
