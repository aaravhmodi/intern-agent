from datetime import date
from pathlib import Path

import typer
from openai import OpenAI
from rich.console import Console
from rich.table import Table

from internship_agent.ai import assess_fit, draft_outreach
from internship_agent.config import Settings, get_settings
from internship_agent.leads.ranking import rank
from internship_agent.leads.schemas import LeadStatus
from internship_agent.leads.store import LeadStore, load_inbox, merge
from internship_agent.resume import load_resume_text

leads_app = typer.Typer(help="Founders who recently raised, scored for internship fit.")
console = Console()


def _store(settings: Settings) -> LeadStore:
    return LeadStore(settings.data_dir / "leads.json")


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        console.print("[red]OPENAI_API_KEY is not set in .env[/red]")
        raise typer.Exit(1)
    return OpenAI(api_key=settings.openai_api_key)


def _resume(settings: Settings) -> str:
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")


@leads_app.command("import")
def import_leads(path: Path) -> None:
    """Import leads from a JSON list (e.g. data/leads-inbox.json written by Claude)."""
    store = _store(get_settings())
    leads, added = merge(store.load(), load_inbox(path))
    store.save(leads)
    console.print(f"Imported {added} new lead(s); {len(leads)} total.")


@leads_app.command("list")
def list_leads(
    days: int = typer.Option(90, help="Only raises from the last N days."),
) -> None:
    """Show leads ranked by fit score, then stage, then recency."""
    ranked = rank(_store(get_settings()).load(), date.today(), days)
    table = Table("Fit", "Round", "Raised", "Founder", "X", "Status")
    table.add_column("Key", overflow="fold")
    for lead in ranked:
        fit = f"{lead.fit.score} {lead.fit.verdict.value}" if lead.fit else "-"
        table.add_row(
            fit,
            lead.round.value,
            lead.announced_on.isoformat(),
            lead.founder_name,
            f"@{lead.x_handle}" if lead.x_handle else "-",
            lead.status.value,
            lead.key,
        )
    console.print(table if ranked else "No leads yet.")


@leads_app.command("score")
def score_leads(
    limit: int = typer.Option(10, help="Maximum leads to score in this run."),
    rescore: bool = typer.Option(False, help="Re-score leads that already have a fit."),
) -> None:
    """Score unscored leads against the resume with OpenAI."""
    settings = get_settings()
    store, client, resume = _store(settings), _openai(settings), _resume(settings)
    todo = [lead for lead in store.load() if rescore or lead.fit is None][:limit]
    for lead in todo:
        lead.fit = assess_fit(client, settings.openai_model, resume, lead)
        if lead.status is LeadStatus.NEW:
            lead.status = LeadStatus.SCORED
        store.upsert(lead)
        console.print(f"{lead.key}: {lead.fit.score} ({lead.fit.verdict.value})")
    console.print(f"Scored {len(todo)} lead(s).")


@leads_app.command("show")
def show_lead(key: str) -> None:
    """Show one lead with its fit assessment and draft."""
    console.print_json(_store(get_settings()).get(key).model_dump_json())


@leads_app.command("draft")
def draft_lead(key: str) -> None:
    """Draft an X DM and email for one lead. Nothing is sent."""
    settings = get_settings()
    store = _store(settings)
    lead = store.get(key)
    lead.draft = draft_outreach(_openai(settings), settings.openai_model, _resume(settings), lead)
    if lead.status in (LeadStatus.NEW, LeadStatus.SCORED):
        lead.status = LeadStatus.DRAFTED
    store.upsert(lead)
    console.print(f"[bold]X DM to {lead.x_url or lead.founder_name}[/bold]\n{lead.draft.x_dm}\n")
    console.print(f"[bold]Email: {lead.draft.email_subject}[/bold]\n{lead.draft.email_body}")


@leads_app.command("mark")
def mark_lead(key: str, status: LeadStatus) -> None:
    """Record that you contacted or skipped a lead."""
    store = _store(get_settings())
    lead = store.get(key)
    lead.status = status
    store.upsert(lead)
    console.print(f"{key} -> {status.value}")
