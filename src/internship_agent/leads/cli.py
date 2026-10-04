from datetime import date
from pathlib import Path
from typing import Annotated

import typer
from openai import OpenAI
from rich.console import Console
from rich.table import Table

from internship_agent.ai import assess_fit, draft_outreach
from internship_agent.config import Settings, get_settings
from internship_agent.leads.export import render_outreach
from internship_agent.leads.ranking import rank
from internship_agent.leads.schemas import EmailStatus, Lead, LeadStatus
from internship_agent.leads.store import LeadStore, load_inbox, merge
from internship_agent.resume import load_resume_text
from internship_agent.workflows import find_more_postings

leads_app = typer.Typer(help="Founder and internship-posting leads, scored for fit.")
console = Console()
DEFAULT_OUTREACH = Path("data/outreach.md")


def _store(settings: Settings) -> LeadStore:
    return LeadStore(settings.data_dir / "leads.json")


def _openai(settings: Settings) -> OpenAI:
    if not settings.openai_api_key:
        console.print("[red]OPENAI_API_KEY is not set in .env[/red]")
        raise typer.Exit(1)
    return OpenAI(api_key=settings.openai_api_key)


def _resume(settings: Settings) -> str:
    return load_resume_text(settings.resume_path, settings.data_dir / "resume.txt")


def _email_cell(lead: Lead) -> str:
    if not lead.email:
        return "-"
    return f"{lead.email}?" if lead.email_status is EmailStatus.PATTERN else lead.email


@leads_app.command("import")
def import_leads(path: Path) -> None:
    """Import leads from a JSON list (e.g. data/leads-inbox.json written by Claude)."""
    store = _store(get_settings())
    leads, added = merge(store.load(), load_inbox(path))
    store.save(leads)
    console.print(f"Imported {added} new lead(s); {len(leads)} total.")


@leads_app.command("list")
def list_leads(
    days: int = typer.Option(90, help="Only founder raises from the last N days."),
) -> None:
    """Show open leads ranked by fit. A trailing ? marks an unverified (guessed) email."""
    ranked = rank(_store(get_settings()).load(), date.today(), days)
    table = Table("Fit", "Kind", "Company", "Contact", "Email", "Status")
    table.add_column("Key", overflow="fold")
    for lead in ranked:
        fit = f"{lead.fit.score} {lead.fit.verdict.value}" if lead.fit else "-"
        table.add_row(
            fit,
            lead.kind.value,
            lead.company,
            lead.contact_name or "-",
            _email_cell(lead),
            lead.status.value,
            lead.key,
        )
    console.print(table if ranked else "No leads yet.")


@leads_app.command("score")
def score_leads(
    limit: int = typer.Option(50, help="Maximum leads to score in this run."),
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


def _draft(settings: Settings, client: OpenAI, resume: str, lead: Lead) -> None:
    lead.draft = draft_outreach(client, settings.openai_model, resume, lead)
    if lead.status in (LeadStatus.NEW, LeadStatus.SCORED):
        lead.status = LeadStatus.DRAFTED


@leads_app.command("draft")
def draft_lead(key: str) -> None:
    """Draft an X DM and email for one lead. Nothing is sent."""
    settings = get_settings()
    store = _store(settings)
    lead = store.get(key)
    _draft(settings, _openai(settings), _resume(settings), lead)
    store.upsert(lead)
    assert lead.draft is not None
    console.print(f"[bold]Email: {lead.draft.email_subject}[/bold]\n{lead.draft.email_body}\n")
    console.print(f"[bold]X DM[/bold]\n{lead.draft.x_dm}")


@leads_app.command("draft-all")
def draft_all(
    min_score: int = typer.Option(50, help="Only draft leads with at least this fit score."),
    redraft: bool = typer.Option(False, help="Replace existing drafts."),
) -> None:
    """Draft outreach for every scored, open lead above the threshold. Nothing is sent."""
    settings = get_settings()
    store, client, resume = _store(settings), _openai(settings), _resume(settings)
    todo = [
        lead
        for lead in rank(store.load(), date.today())
        if lead.fit
        and lead.fit.score >= min_score
        and (redraft or lead.draft is None)
        and lead.status is not LeadStatus.CONTACTED
    ]
    for lead in todo:
        _draft(settings, client, resume, lead)
        store.upsert(lead)
        console.print(f"Drafted {lead.key}")
    console.print(f"Drafted {len(todo)} lead(s). Run `leads export` to review them.")


@leads_app.command("export")
def export_drafts(
    out: Annotated[Path, typer.Option(help="Markdown file to write.")] = DEFAULT_OUTREACH,
) -> None:
    """Write all drafts, best fit first, to a Markdown file for review."""
    leads = rank(_store(get_settings()).load(), date.today())
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_outreach(leads), encoding="utf-8")
    console.print(f"Wrote {sum(1 for x in leads if x.draft)} draft(s) to {out}")


@leads_app.command("find-more")
def find_more(
    target_open: int = typer.Option(15, help="Keep this many open (not applied) postings."),
) -> None:
    """Top up open postings from the public SimplifyJobs list and score new ones."""
    added = find_more_postings(get_settings(), target_open)
    for lead in added:
        fit = f"{lead.fit.score}" if lead.fit else "-"
        console.print(f"+ {lead.company}: {lead.posting_title} (fit {fit})")
    console.print(f"Added {len(added)} posting(s).")


@leads_app.command("mark")
def mark_lead(key: str, status: LeadStatus) -> None:
    """Record that you contacted or skipped a lead."""
    store = _store(get_settings())
    lead = store.get(key)
    lead.status = status
    store.upsert(lead)
    console.print(f"{key} -> {status.value}")
