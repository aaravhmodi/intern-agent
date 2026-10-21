from contextlib import nullcontext
from datetime import date
from pathlib import Path
from typing import Annotated

import typer
from openai import OpenAI
from rich.console import Console
from rich.table import Table

from internship_agent import notify
from internship_agent.ai import draft_outreach
from internship_agent.config import Settings, get_settings
from internship_agent.followup_run import run_followups
from internship_agent.leads.export import render_outreach
from internship_agent.leads.ranking import rank
from internship_agent.leads.schemas import EmailStatus, Lead, LeadStatus, Region, Segment
from internship_agent.leads.store import (
    LeadStore,
    PostgresLeadStore,
    load_inbox,
    merge,
    open_lead_store,
)
from internship_agent.mailbox import GmailMailbox, MailboxError
from internship_agent.mailer import MailError
from internship_agent.resume import load_resume_text
from internship_agent.workflows import (
    CHANNELS,
    add_team_contacts,
    daily,
    find_form_d_startups,
    find_more_postings,
    find_site_emails,
    find_startups,
    guess_and_send,
    prepare_application,
    score,
    scrape_jobs,
    submit_application,
)

leads_app = typer.Typer(help="Founder and internship-posting leads, scored for fit.")
console = Console()
DEFAULT_OUTREACH = Path("data/outreach.md")


def _store(settings: Settings) -> LeadStore | PostgresLeadStore:
    return open_lead_store(settings.data_dir, settings.database_url)


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
    _openai(settings)
    todo = [lead for lead in _store(settings).load() if rescore or lead.fit is None][:limit]
    score(settings, todo)
    for lead in todo:
        if lead.fit:
            console.print(f"{lead.key}: {lead.fit.score} ({lead.fit.verdict.value})")
    console.print(f"Scored {len(todo)} lead(s).")


@leads_app.command("find-startups")
def find_startups_cmd(
    stage: Annotated[
        list[Segment] | None, typer.Option(help="Startup stages to search (default: early, mid).")
    ] = None,
    count: int = typer.Option(6, help="Startups to ask for per search pass."),
    region: Annotated[
        list[Region] | None,
        typer.Option(help="Regions to search (default: SEARCH_REGIONS, all three)."),
    ] = None,
    channel: Annotated[
        list[str] | None, typer.Option(help="Channels: news, x, linkedin (default: all).")
    ] = None,
) -> None:
    """Search recent raises across regions and channels, check their job boards, score."""
    added = find_startups(
        get_settings(),
        stage or [Segment.EARLY, Segment.MID],
        count,
        regions=region,
        channels=tuple(channel) if channel else CHANNELS,
        progress=console.print,
    )
    for lead in added:
        fit = f"{lead.fit.score}" if lead.fit else "-"
        what = lead.posting_title if lead.kind.value == "posting" else lead.round.value
        where = lead.region.value if lead.region else "?"
        console.print(f"+ ({where}) {lead.company} ({what}): {lead.contact_name} (fit {fit})")
    console.print(f"Added {len(added)} lead(s).")


@leads_app.command("show")
def show_lead(key: str) -> None:
    """Show one lead with its fit assessment and draft."""
    console.print_json(_store(get_settings()).get(key).model_dump_json())


def _draft(settings: Settings, client: OpenAI, resume: str, lead: Lead) -> None:
    lead.draft = draft_outreach(client, settings.openai_writing_model, resume, lead)
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


@leads_app.command("daily")
def daily_cmd() -> None:
    """Daily run: find postings, prepare materials, submit eligible applications, and report."""
    report = daily(get_settings(), log=console.print)
    for lead in report.prepared:
        fit = lead.fit.score if lead.fit else "-"
        console.print(f"ready: {lead.company}: {lead.posting_title} (fit {fit})")
    console.print(
        f"{len(report.new)} new, {len(report.skipped)} skipped by your rules, "
        f"{len(report.prepared)} prepared, {report.submitted} submitted, "
        f"{report.application_blocked} blocked, "
        f"{report.pushed} push(es) sent."
    )


@leads_app.command("scrape-jobs")
def scrape_jobs_cmd() -> None:
    """Store all available matching postings from the configured job sources."""
    settings = get_settings()
    new = scrape_jobs(settings, log=console.print)
    console.print(f"Scraped {len(new)} new posting(s).")


@leads_app.command("form-d")
def form_d_cmd(
    days: Annotated[int, typer.Option(help="How many past days of filings to read.")] = 3,
    min_usd: Annotated[int, typer.Option(help="Skip raises smaller than this.")] = 0,
) -> None:
    """Add US tech startups that just filed an SEC Form D, with their site and an email."""
    new = find_form_d_startups(get_settings(), days=days, log=console.print, min_usd=min_usd)
    console.print(f"Added {len(new)} lead(s) from Form D filings.")


@leads_app.command("guess-send")
def guess_send_cmd(
    limit: Annotated[int, typer.Option(help="Most founders to email in this run.")] = 40,
    send: Annotated[bool, typer.Option(help="Actually send; without it, only list.")] = False,
) -> None:
    """Email founders at the address format most likely to work; retry bounced ones."""
    picked = guess_and_send(get_settings(), limit, send=send, log=console.print)
    console.print(f"{len(picked)} founder(s) {'emailed' if send else 'would be emailed'}.")


@leads_app.command("site-emails")
def site_emails_cmd() -> None:
    """Find addresses each startup publishes on its own site: people's, or careers@ and such."""
    people, companies = find_site_emails(get_settings(), log=console.print)
    console.print(f"{people} people got a published address; {companies} companies a shared inbox.")


@leads_app.command("team-contacts")
def team_contacts_cmd(
    min_usd: Annotated[int, typer.Option(help="Only startups that raised at least this.")] = (
        15_000_000
    ),
    limit: Annotated[int | None, typer.Option(help="Most companies to search.")] = None,
) -> None:
    """Find a recruiter and a senior engineer at each big startup, to email besides the CEO."""
    added = add_team_contacts(get_settings(), min_usd, limit, log=console.print)
    console.print(f"Added {len(added)} people.")


@leads_app.command("application-campaign")
def application_campaign(
    target: Annotated[int, typer.Option(help="Target number of confirmed submissions.")] = 20,
    for_date: Annotated[
        str | None, typer.Option(help="Run only on this YYYY-MM-DD date (configured zone).")
    ] = None,
    lowest_first: Annotated[
        bool, typer.Option(help="Work through the lowest fit scores first.")
    ] = False,
    skip_strong: Annotated[
        bool, typer.Option(help="Leave strong (green) fits for you; apply to the rest.")
    ] = False,
) -> None:
    """Run a dated application campaign and send its result through ntfy."""
    settings = get_settings()
    if for_date is not None:
        try:
            campaign_date = date.fromisoformat(for_date)
        except ValueError as error:
            raise typer.BadParameter("Use YYYY-MM-DD") from error
        if date.today() != campaign_date:
            console.print(f"Campaign date {for_date} is not today; no applications submitted.")
            return
    if not settings.ntfy_topic:
        console.print("[red]NTFY_TOPIC is required for an application campaign.[/red]")
        raise typer.Exit(1)
    if not settings.auto_submit_applications:
        console.print("[red]AUTO_SUBMIT_APPLICATIONS is disabled.[/red]")
        raise typer.Exit(1)
    try:
        report = daily(
            settings,
            log=console.print,
            target_submissions=target,
            lowest_first=lowest_first,
            skip_strong=skip_strong,
        )
    except Exception as error:
        console.print(f"Campaign stopped ({type(error).__name__}).")
        notify.send(
            settings.ntfy_server,
            settings.ntfy_topic,
            notify.Push(
                title="Internship agent: application campaign failed",
                message=(
                    "Campaign stopped before the final report "
                    f"({type(error).__name__}). Check the server log."
                ),
                priority=4,
                tags=["warning"],
            ),
        )
        raise typer.Exit(1) from error
    console.print(
        f"Target {target}; {report.submitted} confirmed submitted; "
        f"{report.attempted} attempted; {report.application_blocked} blocked/failed; "
        f"{report.pushed} ntfy report(s)."
    )


@leads_app.command("followups")
def followups_cmd(
    send: Annotated[
        bool, typer.Option("--send", help="Send them. Without this, only show what would go.")
    ] = False,
    check_only: Annotated[
        bool,
        typer.Option(
            "--check-only",
            help="Record replies and bounces in both inboxes and push new replies; send nothing.",
        ),
    ] = False,
) -> None:
    """Follow up on emails with no reply after 5 days, at most twice per person."""
    settings = get_settings()
    # n8n already pushes replies in the main inbox; this covers the outreach Gmail's.
    waiting = {
        lead.key
        for lead in _store(settings).load()
        if lead.sent_from and lead.sent_at and lead.replied_at is None
    }
    if send and not settings.followups_enabled:
        console.print("[red]Set FOLLOWUPS_ENABLED=true in .env to send follow-ups.[/red]")
        raise typer.Exit(1)
    if not settings.gmail_address or not settings.gmail_app_password:
        console.print("[red]Set GMAIL_ADDRESS and GMAIL_APP_PASSWORD in .env first.[/red]")
        raise typer.Exit(1)
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
                dry_run=not (send or check_only),
                pause_seconds=2,
                outreach_mailbox=outreach,
                send_due=not check_only,
            )
    except (MailboxError, MailError) as exc:
        console.print(f"[red]{exc}[/red]")
        raise typer.Exit(1) from exc
    replied = [lead for lead in _store(settings).load() if lead.key in waiting and lead.replied_at]
    if check_only and replied and settings.ntfy_topic:
        names = ", ".join(f"{lead.contact_name} ({lead.company})" for lead in replied)
        notify.send(
            settings.ntfy_server,
            settings.ntfy_topic,
            notify.Push(
                title=f"New reply: {names}"[:120],
                message=f"{names} wrote back to {settings.outreach_gmail_address}. Answer from "
                "that inbox so it stays in the same thread.",
                priority=4,
                tags=["email"],
            ),
        )
    for item in report.sent:
        verb = "sent" if send else "would send"
        console.print(f"{verb} follow-up {item.number}: {item.contact} at {item.company}")
    for name in report.replied:
        console.print(f"replied, no follow-up: {name}")
    for name in report.bounced:
        console.print(f"bounced, no follow-up: {name}")
    console.print(
        f"{len(report.sent)} {'sent' if send else 'due'}, {len(report.replied)} replied, "
        f"{report.waiting} waiting, {report.finished} finished without a reply."
    )
    if report.error:
        console.print(f"[red]Stopped early: {report.error}[/red]")
        raise typer.Exit(1)


@leads_app.command("prepare")
def prepare_cmd(key: str) -> None:
    """Prepare answers to a posting's application questions."""
    lead = prepare_application(get_settings(), key)
    assert lead.application is not None
    console.print(f"[bold]{lead.company}[/bold] ({lead.application.source} questions)")
    for item in lead.application.answers:
        flag = "[yellow]needs you[/yellow] " if item.needs_user_input else ""
        console.print(f"- {flag}{item.question.label}\n  {item.answer or item.note}")


@leads_app.command("prepare-all")
def prepare_all_cmd() -> None:
    """Prepare application answers for every open posting that has none yet."""
    settings = get_settings()
    todo = [
        lead.key
        for lead in _store(settings).load()
        if lead.kind.value == "posting"
        and lead.application is None
        and lead.status.value not in ("applied", "contacted", "skipped")
    ]
    for key in todo:
        lead = prepare_application(settings, key)
        assert lead.application is not None
        missing = sum(1 for a in lead.application.answers if a.needs_user_input)
        console.print(f"{key}: {len(lead.application.answers)} questions, {missing} need you")
    console.print(f"Prepared {len(todo)} application(s).")


@leads_app.command("browser-login")
def browser_login() -> None:
    """Open the saved browser once so you can sign in to supported job sites."""
    from internship_agent.applications.browser import open_login_browser

    settings = get_settings()
    open_login_browser(settings.application_browser_dir)


@leads_app.command("apply")
def apply_cmd(
    key: str,
    dry_run: Annotated[bool, typer.Option(help="Fill the form without submitting it.")] = False,
) -> None:
    """Submit one prepared, non-Workday application (or preview with --dry-run)."""
    lead = submit_application(get_settings(), key, dry_run=dry_run)
    assert lead.application is not None
    console.print(f"{lead.application.submission_status}: {lead.application.submission_detail}")


@leads_app.command("mark")
def mark_lead(key: str, status: LeadStatus) -> None:
    """Record that you contacted or skipped a lead."""
    store = _store(get_settings())
    lead = store.get(key)
    lead.status = status
    store.upsert(lead)
    console.print(f"{key} -> {status.value}")
