---
description: Find open Winter 2027 SWE internship postings and their hiring managers, then draft outreach
argument-hint: "[how many postings, default 15] [focus, e.g. 'Toronto' or 'ML infra']"
---

Find open software-engineering internship postings for Winter 2027 (January–April 2027),
identify a likely hiring manager or recruiter for each, and save them as leads.
Arguments: $ARGUMENTS

## Rules
- **Read-only.** Never apply, submit forms, sign in to applicant portals, message, connect or
  follow anyone. The user applies and sends outreach themselves.
- Use Claude in Chrome (load the `anthropic-skills:chrome-browser` skill first) in a new tab,
  at a human pace. Stop and ask on any login wall, rate limit or captcha.
- Only include postings that are open and explicitly mention Winter 2027, Jan–Apr 2027, or
  are an evergreen co-op/intern posting that accepts Winter terms. `posting_url` must be the
  posting itself, not a search page.
- Never guess a hiring manager. Use a named person only when public evidence ties them to
  the team (the posting names them, a team page, a "we're hiring interns" post, or a LinkedIn
  title like "Engineering Manager, <team>"). Otherwise use a named university recruiter, or
  leave `contact_name` empty.
- LinkedIn: light and read-only. At most a few profile views per company, only to confirm a
  name and title. Stop immediately on any warning.

## Where to look
1. Aggregators: the SimplifyJobs / Pitt CSC style internship lists on GitHub, and
   company careers pages (Greenhouse, Lever, Ashby, Workday boards).
2. Canadian sources: BetaKit hiring posts, company careers pages for Toronto/Waterloo startups.
3. For each posting, the company's team/about page, engineering blog, X, and (lightly)
   LinkedIn to find the hiring contact.

## Output
Append a JSON list to `data/leads-inbox.json` (create it if missing) with objects like:

```json
{
  "kind": "posting",
  "company": "Acme AI",
  "company_url": "https://acme.ai",
  "posting_title": "Software Engineering Intern (Winter 2027)",
  "posting_url": "https://jobs.ashbyhq.com/acme/123",
  "deadline": null,
  "source_url": "https://jobs.ashbyhq.com/acme/123",
  "what_they_build": "One or two factual sentences.",
  "location": "Toronto, ON (hybrid)",
  "hiring_signals": ["Posting says the team is hiring 3 interns"],
  "contact_name": "Jane Doe",
  "contact_role": "Engineering Manager, Platform",
  "linkedin_url": "https://www.linkedin.com/in/janedoe",
  "x_handle": null,
  "email": "jane.doe@acme.ai",
  "email_status": "pattern",
  "email_source": ""
}
```

Email rules are the same as `/find-founders`: `published` only when seen on a public page
(record it in `email_source`), `pattern` for a guess built with
`internship_agent.leads.emails.guess_email` from a publicly evident company format, otherwise
leave it empty.

Then run:

```
uv run internship-agent leads import data/leads-inbox.json
uv run internship-agent leads score
uv run internship-agent leads draft-all
uv run internship-agent leads export
```

Finish with a short summary: postings found, contacts found, emails published vs guessed,
and the strongest fits. Remind the user to apply through each `posting_url` themselves.
