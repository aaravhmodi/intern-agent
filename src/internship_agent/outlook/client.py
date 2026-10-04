"""Read-only Outlook access through the Microsoft 365 MCP server (stdio)."""

import json
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Any, Protocol

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import CallToolResult, TextContent
from pydantic import ValidationError

from internship_agent.config import Settings
from internship_agent.outlook.schemas import (
    CalendarEvent,
    GraphEventPage,
    GraphMessagePage,
    MailMessage,
)

# Defence in depth: the server already runs with --read-only, but this client only
# ever calls tools that read the signed-in user's mail and calendar.
ALLOWED_TOOLS = frozenset(
    {"verify-login", "list-mail-messages", "get-mail-message", "get-calendar-view"}
)

MESSAGE_FIELDS = "id,subject,from,receivedDateTime,bodyPreview,webLink"
EVENT_FIELDS = "id,subject,start,end,location,bodyPreview,organizer,webLink,isOnlineMeeting"


class OutlookError(RuntimeError):
    pass


class ToolSession(Protocol):
    async def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> Any: ...


class OutlookClient:
    def __init__(self, session: ToolSession) -> None:
        self._session = session

    async def _call(self, tool: str, arguments: dict[str, Any]) -> Any:
        if tool not in ALLOWED_TOOLS:
            raise OutlookError(f"Tool {tool!r} is not on the read-only allowlist")
        result: CallToolResult = await self._session.call_tool(tool, arguments)
        text = "".join(c.text for c in result.content if isinstance(c, TextContent))
        if result.isError:
            raise OutlookError(f"{tool} failed: {text[:300]}")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text

    async def verify_login(self) -> Any:
        return await self._call("verify-login", {})

    async def search_messages(self, query: str, top: int = 50) -> list[MailMessage]:
        """Search the mailbox with a KQL query, newest first."""
        data = await self._call(
            "list-mail-messages",
            {"search": f'"{query}"', "top": top, "select": MESSAGE_FIELDS},
        )
        try:
            page = GraphMessagePage.model_validate(data)
        except ValidationError as exc:
            raise OutlookError(f"Unexpected list-mail-messages response: {exc}") from exc
        return sorted(page.value, key=lambda m: m.received_at or datetime.min, reverse=True)

    async def calendar_view(
        self, start: datetime, end: datetime, top: int = 100
    ) -> list[CalendarEvent]:
        data = await self._call(
            "get-calendar-view",
            {
                "startDateTime": start.isoformat(),
                "endDateTime": end.isoformat(),
                "top": top,
                "select": EVENT_FIELDS,
                "orderby": "start/dateTime",
            },
        )
        try:
            return GraphEventPage.model_validate(data).value
        except ValidationError as exc:
            raise OutlookError(f"Unexpected get-calendar-view response: {exc}") from exc


@asynccontextmanager
async def connect(settings: Settings) -> AsyncIterator[OutlookClient]:
    """Start the MCP server as a subprocess and yield a read-only client."""
    params = StdioServerParameters(
        command=settings.outlook_mcp_command, args=settings.outlook_server_args()
    )
    # Server logs go to devnull so auth details can never leak into our output.
    with open(os.devnull, "w") as errlog:
        async with stdio_client(params, errlog=errlog) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield OutlookClient(session)
