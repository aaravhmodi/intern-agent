# Working memory

What an agent working on this repo should know, kept up to date as work happens. Newest log
entries at the bottom.

## Conventions

- Commits are authored and committed as **Aarav Modi** `<aaravmodi20@gmail.com>`, with no
  Claude co-author or session lines. Small, focused commits; one change each.
- Work happens on `claude/sharp-newton-4dv5kv`; `main` is fast-forwarded to it (no merge
  commits). Pushing to `main` deploys to the home server within a minute.
- `AGENTS.md` rules apply: type hints, Pydantic at AI and browser boundaries, no credentials in
  logs, tests for deterministic logic.

## Facts the docs depend on

- With Gmail connected (`GMAIL_ADDRESS` + app password), the agent sends on its own: five
  outreach batches of 20 (100 a day), 10 coffee-chat asks, and follow-ups (25 a run, six runs a
  day, after 5 quiet days, at most twice). Scheduled ceiling: 260 a day. Record: 350+ in one
  day with extra runs. The dashboard's own Send always needs a click.
- From the first reply on it's manual: the agent never writes to that person again.
- `FOLLOWUPS_ENABLED` defaults to `false` in code; the server must set it to `true`.

## Environment notes

- Cloud sessions are not on Tailscale and cannot reach the home server (`100.76.57.23`).
- A personal cloud environment "intern-agent video (GitDiagram)" holds OpenAI and OpenRouter
  keys as network secrets; requests with them returned 401, so the videos have no voice.
  Anthropic keys cannot be saved as network secrets.

## Demo videos (`docs/videos`)

- Explainers are drawn by GitDiagram's motion engine from hand-written scripts in
  `docs/videos/make/films/`, stored through `local-film-route.ts` (no API keys) and rendered by
  its MP4 renderer. Captions, no narration. Branding patch: github.com address, no GitDiagram
  logo, "made with GitDiagram" credit kept.
- The walkthrough records the real dashboard on invented data (`seed_demo.py`, `.example`
  addresses) with `record.js`, then `finish.py` adds cards and captions.
- Checks that caught real problems: elements cued on a line's last word appear too late; empty
  frames at a scene's first beat; labels that overflow boxes; setup hints in the demo dashboard
  ("Sending is off until Gmail is set up") contradicting the captions.

## Log

- 2026-11-21: README states outreach and follow-ups send automatically once Gmail is
  connected, documents the job pipeline end to end, the 200+ a day figure and the 350+ record.
- 2026-11-21: Four demo videos added (two explainers, a vertical short, a dashboard
  walkthrough) with the tooling to make them again.
- 2026-11-21: Video themes: `theme.py` maps GitDiagram's palette roles (paper, card, ink,
  accent, code colours, rgba glows) to clay, clay-dark and ocean, applied to the engine
  before each render; `make.py --theme <name>`. Dark themes need lighter secondary text
  (`ink_2`) or sub-labels on filled accent boxes disappear.
- 2026-11-21: Fixed the explainer's follow-up scene: "Follow-up ×2 max" overflowed its box;
  the box keeps its label and a "max 2" stamp sits under it. Replacing a box label with
  longer text is the usual cause of overflow.
- 2026-11-21: Theme renders committed under `docs/videos/themes/<theme>/` (explainer + one-day,
  landscape, ~5 MB a theme) with a poster each; README shows them in a "In other themes"
  table. Lavender stays the default at `docs/videos/*.mp4`.
