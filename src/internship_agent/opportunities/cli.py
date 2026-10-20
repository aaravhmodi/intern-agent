from datetime import date
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from internship_agent import notify
from internship_agent.config import get_settings
from internship_agent.opportunities import run
from internship_agent.opportunities.schemas import (
    Opportunity,
    OpportunityKind,
    OpportunityStatus,
)
from internship_agent.opportunities.store import OpportunityStore

opportunities_app = typer.Typer(
    help="Hackathons, tech conferences, research venues and networking events.",
    no_args_is_help=True,
)
console = Console()


@opportunities_app.command("refresh")
def refresh_cmd(
    events: bool = typer.Option(False, help="Also web-search networking events (uses OpenAI)."),
    push: bool = typer.Option(True, help="Send an ntfy summary when NTFY_TOPIC is set."),
    check: int | None = typer.Option(
        None, help="Events to check with AI afterwards (default DAILY_OPPORTUNITY_CHECKS)."
    ),
) -> None:
    """Pull Devpost, MLH, confs.tech and ccfddl; store new upcoming, nearby events."""
    settings = get_settings()
    added = run.refresh(settings, log=console.print)
    if events:
        try:
            found = run.find_events(settings)
            console.print(f"Event search: +{len(found)}")
            added += found
        except Exception as error:  # the feeds' results are already saved
            console.print(f"[red]Event search failed:[/red] {error}")
    assessed: list[Opportunity] = []
    limit = settings.daily_opportunity_checks if check is None else check
    if limit and settings.openai_api_key:
        assessed = run.check_events(settings, limit=limit, log=console.print)
        console.print(f"Checked {len(assessed)} events")
    picked = run.auto_pick(settings)
    for o in picked:
        console.print(f"Picked for you: {o.title} ({o.picked})")
    message = run.summary_push(
        added,
        OpportunityStore(settings).load(),
        date.today(),
        settings.dashboard_url,
        assessed,
        picked,
    )
    if push and message and settings.ntfy_topic:
        notify.send(settings.ntfy_server, settings.ntfy_topic, message)


@opportunities_app.command("check")
def check_cmd(
    keys: list[str] = typer.Argument(None, help="Event URLs; default: most worth checking."),  # noqa: B008
    limit: int = typer.Option(5, help="How many to check when no URL is given."),
) -> None:
    """Read each event's pages: where it is, in person or online, travel paid, effort, fit."""
    for o in run.check_events(get_settings(), keys or None, limit, log=console.print):
        a = o.assessment
        assert a is not None
        console.print(
            f"[bold]{o.title}[/bold] · {a.format}, {a.location} · travel {a.travel} · "
            f"{a.effort} effort · fit {a.fit_score}\n  {a.summary}\n  Travel: {a.travel_details}"
        )


@opportunities_app.command("list")
def list_cmd(
    kind: OpportunityKind | None = typer.Option(None, help="Only this kind."),  # noqa: B008
    limit: int = typer.Option(40, help="Rows to show."),
) -> None:
    """Upcoming opportunities, soonest deadline or start first."""
    items = [
        o
        for o in OpportunityStore(get_settings()).load()
        if (kind is None or o.kind is kind)
        and o.status is not OpportunityStatus.SKIPPED
        and run.upcoming(o, date.today())
    ]
    today = date.today()
    items.sort(key=lambda o: run.next_date(o, today))
    table = Table("Date", "Kind", "Title", "Where", "Status")
    for o in items[:limit]:
        open_deadline = o.deadline and o.deadline >= today
        when = (
            f"{o.deadline_label} {o.deadline}" if open_deadline else f"Starts {o.starts_on or '?'}"
        )
        table.add_row(when, o.kind.value, o.title, o.location, o.status.value)
    console.print(table if items else "Nothing yet. Run `opportunities refresh`.")


@opportunities_app.command("find-events")
def find_events_cmd(
    days: int = typer.Option(60, help="How far ahead to look."),
    count: int = typer.Option(10, help="Events to ask for."),
) -> None:
    """Web-search networking events near EVENT_CITIES; keeps only verified event pages."""
    added = run.find_events(get_settings(), days, count)
    for o in added:
        console.print(f"+ {o.starts_on} {o.title} ({o.location}) {o.url}")
    console.print(f"Added {len(added)}.")


@opportunities_app.command("strategy")
def strategy_cmd(key: str = typer.Argument(..., help="The opportunity's URL.")) -> None:
    """Read the venue's call for papers and plan a submission from your own work."""
    s = run.plan_submission(get_settings(), key).strategy
    assert s is not None
    console.print(f"[bold]{s.verdict}[/bold]: {s.summary}\n")
    for t in s.tracks:
        console.print(f"- {t.name}: {t.deadline} · {t.format} · {t.eligibility}\n  {t.source_url}")
    console.print(f"\nWhat to submit: {s.what_to_submit}")
    for title, lines in (("Plan", s.plan), ("Funding", s.funding), ("Risks", s.risks)):
        console.print(f"\n{title}:" + "".join(f"\n  - {x}" for x in lines))


@opportunities_app.command("import")
def import_cmd(path: Path) -> None:
    """Add opportunities from a JSON list (see .claude/commands/find-opportunities.md)."""
    console.print(f"Added {len(run.import_inbox(get_settings(), path))}.")


@opportunities_app.command("apply")
def apply_cmd(
    keys: list[str] = typer.Argument(None, help="Event URLs; default: all marked Interested."),  # noqa: B008
    dry_run: bool = typer.Option(False, help="Read the first page and say what it would do."),
) -> None:
    """Apply to hackathons and RSVP to events in the saved browser, from candidate_context.md.

    With no URL: every hackathon or networking event marked Interested that hasn't been tried,
    hasn't started and is still open (the daily run does this).
    """
    settings = get_settings()
    done = run.apply_events(settings, keys or None, dry_run=dry_run, log=console.print)
    if dry_run or not done:
        return
    console.print(f"Tried {len(done)}; submitted {sum(o.status == 'submitted' for o in done)}.")
    if settings.ntfy_topic:
        notify.send(
            settings.ntfy_server,
            settings.ntfy_topic,
            run.applied_push(done, settings.dashboard_url),
        )


@opportunities_app.command("sign-in")
def sign_in_cmd(
    site: list[str] = typer.Option(  # noqa: B008
        list(run.SIGN_IN_SITES), help="luma, eventbrite, mlh, devpost (default: all)."
    ),
    server: str | None = typer.Option(
        None, help="Dashboard to give the sign-ins to (default DASHBOARD_URL)."
    ),
) -> None:
    """Sign in or sign up to event sites with your Gmail, then give the server the sessions.

    Opens a browser window: it types GMAIL_ADDRESS, reads the code or link each site emails,
    and waits for you to tick any "verify you're human" box. Sites it can't finish (a password
    or Google sign-in) stay open for you to finish by hand.
    """
    settings = get_settings()
    unknown = [s for s in site if s not in run.SIGN_IN_SITES]
    if unknown:
        raise typer.BadParameter(f"Unknown site(s): {', '.join(unknown)}")

    def finish_by_hand(names: list[str]) -> None:
        input(f"Finish signing in to {', '.join(names)} in the browser window, then press Enter… ")

    results, cookies = run.sign_in(settings, site, log=console.print, finish_by_hand=finish_by_hand)
    target = server or settings.dashboard_url
    if not target:
        console.print(
            "Signed in here. Set DASHBOARD_URL (or pass --server) to give the server these too."
        )
        return
    added = run.send_sessions(target, cookies)
    console.print(f"Gave the server {added} sign-in cookies for {', '.join(site)}.")


@opportunities_app.command("mark")
def mark_cmd(key: str, status: OpportunityStatus) -> None:
    store = OpportunityStore(get_settings())
    item = store.get(key)
    item.status = status
    store.upsert(item)
    console.print(f"{item.title}: {status.value}")
