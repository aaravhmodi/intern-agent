import asyncio
import subprocess
from collections.abc import Coroutine
from datetime import UTC, datetime, timedelta
from typing import Any

import typer
from rich.console import Console
from rich.table import Table

from internship_agent.config import get_settings
from internship_agent.outlook.client import OutlookError, connect
from internship_agent.tracking import RECRUITING_QUERY, application_updates, interview_events

app = typer.Typer(help="Winter 2027 internship agent.", no_args_is_help=True)
outlook_app = typer.Typer(help="Read-only Outlook integration via the MS 365 MCP server.")
app.add_typer(outlook_app, name="outlook")
console = Console()


@outlook_app.command("login")
def outlook_login() -> None:
    """Sign in to Outlook with the device-code flow (tokens stay in the OS credential store)."""
    settings = get_settings()
    cmd = [settings.outlook_mcp_command, *settings.outlook_server_args("--login")]
    raise typer.Exit(subprocess.call(cmd))


@outlook_app.command("status")
def outlook_status() -> None:
    """Check whether the Outlook MCP server has a signed-in account."""

    async def run() -> None:
        async with connect(get_settings()) as client:
            console.print(await client.verify_login())

    _run(run())


@app.command()
def inbox(top: int = typer.Option(50, help="Maximum emails to scan.")) -> None:
    """Summarize recruiting emails (applications, assessments, interviews, offers)."""

    async def run() -> None:
        async with connect(get_settings()) as client:
            messages = await client.search_messages(RECRUITING_QUERY, top=top)
        updates = application_updates(messages)
        table = Table("Received", "Company", "Stage", "Subject")
        for u in updates:
            table.add_row(u.received_at[:10], u.company, u.stage.value, u.subject)
        console.print(table if updates else "No recruiting emails found.")

    _run(run())


@app.command()
def interviews(days: int = typer.Option(30, help="Days ahead to look.")) -> None:
    """List upcoming interview-like events from the Outlook calendar."""

    async def run() -> None:
        start = datetime.now(UTC)
        async with connect(get_settings()) as client:
            events = await client.calendar_view(start, start + timedelta(days=days))
        found = interview_events(events)
        table = Table("Start", "Subject", "Location")
        for e in found:
            table.add_row(
                f"{e.start.date_time[:16]} {e.start.time_zone}", e.subject, e.location.display_name
            )
        console.print(table if found else "No interviews on the calendar.")

    _run(run())


def _run(coro: Coroutine[Any, Any, None]) -> None:
    try:
        asyncio.run(coro)
    except OutlookError as exc:
        console.print(f"[red]Outlook error:[/red] {exc}")
        raise typer.Exit(1) from exc
