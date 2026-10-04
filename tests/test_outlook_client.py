import json
from datetime import UTC, datetime
from typing import Any

import pytest
from mcp.types import CallToolResult, TextContent

from internship_agent.outlook.client import OutlookClient, OutlookError


class FakeSession:
    def __init__(self, payload: Any, is_error: bool = False) -> None:
        self.payload = payload
        self.is_error = is_error
        self.calls: list[tuple[str, dict[str, Any] | None]] = []

    async def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> Any:
        self.calls.append((name, arguments))
        text = self.payload if isinstance(self.payload, str) else json.dumps(self.payload)
        return CallToolResult(content=[TextContent(type="text", text=text)], isError=self.is_error)


async def test_search_messages_quotes_query_and_sorts_newest_first() -> None:
    session = FakeSession(
        {
            "value": [
                {"id": "a", "subject": "old", "receivedDateTime": "2026-09-01T00:00:00Z"},
                {"id": "b", "subject": "new", "receivedDateTime": "2026-10-01T00:00:00Z"},
            ]
        }
    )
    messages = await OutlookClient(session).search_messages("interview", top=5)

    assert [m.id for m in messages] == ["b", "a"]
    name, args = session.calls[0]
    assert name == "list-mail-messages"
    assert args is not None and args["search"] == '"interview"' and args["top"] == 5


async def test_calendar_view_parses_events() -> None:
    slot = {"dateTime": "2026-10-10T15:00:00.0000000", "timeZone": "UTC"}
    session = FakeSession(
        {"value": [{"id": "e", "subject": "Interview", "start": slot, "end": slot}]}
    )
    start = datetime(2026, 10, 4, tzinfo=UTC)

    events = await OutlookClient(session).calendar_view(start, start)

    assert events[0].subject == "Interview"
    assert session.calls[0][0] == "get-calendar-view"


async def test_tool_error_raises() -> None:
    with pytest.raises(OutlookError, match="failed"):
        await OutlookClient(FakeSession("Not logged in", is_error=True)).search_messages("x")


async def test_write_tools_are_blocked() -> None:
    session = FakeSession({})
    with pytest.raises(OutlookError, match="allowlist"):
        await OutlookClient(session)._call("send-mail", {})
    assert session.calls == []
