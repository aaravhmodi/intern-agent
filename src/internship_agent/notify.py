"""Phone push notifications through ntfy (https://ntfy.sh). Only ever sends to your own topic."""

import json
import urllib.request

from pydantic import BaseModel

from internship_agent.leads.answers import category
from internship_agent.leads.schemas import Lead, PreparedAnswer

# ntfy turns messages over 4096 bytes into file attachments; stay comfortably under.
MESSAGE_BYTES = 3800


class Push(BaseModel):
    title: str
    message: str
    click: str | None = None
    priority: int = 3
    tags: list[str] = []


def written_answers(lead: Lead) -> list[PreparedAnswer]:
    """Answers the AI wrote for this posting (not saved personal answers or blanks)."""
    if lead.application is None:
        return []
    return [
        a
        for a in lead.application.answers
        if a.answer
        and not a.needs_user_input
        and category(a.question) == "ai"
        and a.note != "From your saved answers."
    ]


def _clip(text: str, chars: int) -> str:
    text = " ".join(text.split())
    return text if len(text) <= chars else text[: chars - 1].rstrip() + "…"


def _fit_bytes(text: str, limit: int) -> str:
    data = text.encode("utf-8")
    if len(data) <= limit:
        return text
    return data[: limit - 40].decode("utf-8", "ignore").rstrip() + "\n… (rest on the dashboard)"


def posting_push(lead: Lead) -> Push:
    """One posting: its fit, the AI-written answers to its questions, and what is left to you."""
    score = lead.fit.score if lead.fit else None
    title = f"{lead.company}: {lead.posting_title or 'Internship'}"
    if score is not None:
        title += f" ({score})"
    lines: list[str] = []
    if lead.location:
        lines.append(f"📍 {lead.location}")
    answers = written_answers(lead)
    if answers:
        per_answer = max(250, (MESSAGE_BYTES - 400) // len(answers) - 60)
        for a in answers:
            lines.append(f"\nQ: {_clip(a.question.label, 140)}\nA: {_clip(a.answer, per_answer)}")
    else:
        lines.append("\nNo job-specific questions on the form.")
    if lead.application is not None:
        left = [a.question.label for a in lead.application.answers if a.needs_user_input]
        if left:
            lines.append(f"\nYou fill in ({len(left)}): " + _clip("; ".join(left), 300))
    return Push(
        title=_clip(title, 120),
        message=_fit_bytes("\n".join(lines), MESSAGE_BYTES),
        click=lead.posting_url,
        priority=4 if score is not None and score >= 80 else 3,
        tags=["briefcase"],
    )


def summary_push(new: list[Lead], prepared: list[Lead], dashboard_url: str | None) -> Push:
    ranked = sorted(prepared, key=lambda lead: -(lead.fit.score if lead.fit else 0))
    top = ", ".join(f"{lead.company} {lead.fit.score}" for lead in ranked[:3] if lead.fit)
    message = f"{len(new)} new posting(s); answers ready for {len(prepared)}."
    if top:
        message += f"\nTop: {top}"
    return Push(
        title="Internship agent: today's postings",
        message=message,
        click=dashboard_url,
        tags=["sunrise"],
    )


def send(server: str, topic: str, push: Push) -> None:
    body = {"topic": topic, **push.model_dump(exclude_none=True)}
    request = urllib.request.Request(
        server.rstrip("/"),
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15):
        pass
