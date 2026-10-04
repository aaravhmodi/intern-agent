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

## Dashboard

```text
uv run internship-agent dashboard        # http://127.0.0.1:8765 (local only)
```

Two searches, shown separately:

- **Startups** (early = pre-seed/seed, mid = Series A-D). "Search for startups" uses OpenAI web
  search for funding rounds announced in the last 60 days. A result is kept only if its cited
  article loads and names both the company and the founder. Also from the CLI:
  `leads find-startups --stage early --stage mid --count 8`.
- **Big companies**: open Winter 2027 postings from the public
  [SimplifyJobs off-season list](https://github.com/SimplifyJobs/Summer2027-Internships/blob/dev/README-Off-Season.md).
  "Mark applied" tops the open list back up to `TARGET_OPEN_POSTINGS` (default 15); postings
  you applied to or skipped are never re-added.

Select a company to see its fit score and reasons, contact, and editable drafts:

- **Send email** sends from Gmail after a second confirming click. Guessed addresses need
  "I've checked this address" ticked; a lead is never emailed twice unless you choose
  "Send again". Sends are logged to `data/sent-log.jsonl`. Setup: turn on 2-Step Verification,
  create an app password at https://myaccount.google.com/apppasswords, and put it in `.env` as
  `GMAIL_APP_PASSWORD` (with `GMAIL_ADDRESS`). Never use your normal Google password.
- **LinkedIn**: copies the connection note and opens the profile (or a people search). LinkedIn
  forbids automated invitations, so you paste and send it.
- **Open application** opens the posting; applications are submitted by you.

The server only answers requests from localhost and rejects cross-site requests, because it
can send email.

## Founder leads (X.com)

Find founders who recently raised (pre-seed to Series A) and might take a Winter 2027 intern:

1. In Claude Code, run `/find-founders 10 AI infra`. Claude uses Claude in Chrome to read
   X search, founder profiles and funding news (read-only: no posts, likes, follows or DMs),
   and writes `data/leads-inbox.json`. Every lead must cite a `source_url` for the raise.
2. `uv run internship-agent leads import data/leads-inbox.json`: validates and dedupes.
3. `uv run internship-agent leads score`: OpenAI (`OPENAI_MODEL`, default `gpt-6.1-sol`)
   scores fit 0-100 against the resume at `RESUME_PATH`, with reasons and concerns.
4. `uv run internship-agent leads list`: ranked by fit, then stage, then recency.
5. `uv run internship-agent leads draft <key>`: drafts an X DM and an email. Nothing is sent;
   after you send it yourself, run `leads mark <key> contacted` (or `skipped`).

Leads, the resume text cache and the inbox file stay local and are git-ignored.

## Other connectors

Gmail, Google Calendar and Google Drive are claude.ai connectors available to Claude Code
sessions; they are not called from the Python app.

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
