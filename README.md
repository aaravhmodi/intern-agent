# Winter 2027 Internship Agent

Separate local-first agent for finding Winter 2027 software-engineering internships,
matching them against Aarav Modi's resume, and preparing application materials.

## Current setup

- Resume source: `../website/public/ModiAaravResume.pdf`
- Outlook Email and Outlook Calendar: optional, read-only inputs when connected
- LinkedIn: public-page discovery only until a supported connector is available
- Application submission: manual review required; this agent will not submit forms,
  send messages, or apply on the user's behalf by default

## Outlook integration (MCP)

Outlook mail and calendar are read through the
[Softeria Microsoft 365 MCP server](https://github.com/Softeria/ms-365-mcp-server),
launched over stdio with `--read-only --preset mail,calendar`. The Python client in
`src/internship_agent/outlook/` additionally only calls an allowlist of read tools
(`verify-login`, `list-mail-messages`, `get-mail-message`, `get-calendar-view`).
Microsoft's official Work IQ Mail/Calendar MCP servers were not used because they need
an M365 Copilot license and tenant admin registration, and don't support personal accounts.

Requirements: Python 3.12, [uv](https://docs.astral.sh/uv/), Node.js (for `npx`).

```text
uv sync
cp .env.example .env              # set OUTLOOK_ORG_MODE=true for a uwaterloo.ca mailbox
uv run internship-agent outlook login    # device-code sign-in; tokens go to the OS credential store
uv run internship-agent outlook status
uv run internship-agent inbox            # recruiting emails grouped by stage
uv run internship-agent interviews --days 30
```

`.mcp.json` registers the same read-only server for Claude Code sessions opened in this
folder. Run the login step first so it can reuse the cached token.

## Development

```text
uv run pytest
uv run ruff check .
uv run mypy src
```

## Planned commands

```text
internship-agent setup
internship-agent scan --season winter-2027
internship-agent matches
internship-agent prepare <job-id>
internship-agent applications
```

The initial build will store job listings, source URLs, resume evidence, fit scores,
tailored resume suggestions, and draft cover letters locally. It will deduplicate
listings across company sites and public job boards and preserve the original source
for every recommendation.
