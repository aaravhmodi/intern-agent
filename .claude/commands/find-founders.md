---
description: Find founders on X who recently raised, save them as leads, and score their fit
argument-hint: "[how many leads, default 10] [focus, e.g. 'AI infra' or 'Toronto']"
---

Find founders of startups that announced a funding round in the last 60 days and who might
take a Winter 2027 (Jan–Apr) software-engineering intern. Arguments: $ARGUMENTS

## Rules
- **Read-only.** Never post, like, reply, follow, DM, or change anything on X or any other site.
  Outreach is drafted locally and sent by the user.
- Use Claude in Chrome (load the `anthropic-skills:chrome-browser` skill first) and open a new tab.
  Browse at a human pace. Stop and ask if X shows a login wall, a rate limit, or a captcha.
- Every lead needs a `source_url` for the raise: the founder's announcement post on X, a
  press release, or a news article. Do not guess rounds, amounts, dates, or handles. Leave a
  field empty if you could not confirm it.
- Prefer pre-seed, seed and Series A, software-heavy companies, and teams in Canada, the US, or remote.

## Where to look
1. X search (Latest tab), e.g. `"we raised" seed`, `"excited to announce" "pre-seed"`,
   `"Series A" "we're hiring" engineers`, limited to the last 60 days.
2. Funding news (TechCrunch, BetaKit for Canadian startups, company blogs). From each article,
   find the founder's X profile.
3. On each founder's profile and company site, note what they build, location, and hiring
   signals (careers page, "we're hiring" posts, intern mentions).

## Output
Write a JSON list to `data/leads-inbox.json` with objects of this shape (see
`src/internship_agent/leads/schemas.py`):

```json
{
  "founder_name": "Jane Doe",
  "company": "Acme AI",
  "role": "Co-founder & CTO",
  "x_handle": "janedoe",
  "company_url": "https://acme.ai",
  "round": "seed",
  "amount_usd": 4000000,
  "announced_on": "2026-09-20",
  "source_url": "https://x.com/janedoe/status/...",
  "what_they_build": "One or two factual sentences.",
  "location": "Toronto, ON",
  "hiring_signals": ["Careers page lists a founding engineer role"]
}
```

`round` is one of `pre-seed`, `seed`, `series-a`, `series-b`, `other`.

Then run:

```
uv run internship-agent leads import data/leads-inbox.json
uv run internship-agent leads score
uv run internship-agent leads list
```

Finish with the top leads, their fit verdicts and main concerns, and offer to run
`leads draft <key>` for the strongest ones.
