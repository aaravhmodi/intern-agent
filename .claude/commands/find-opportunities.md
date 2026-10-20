---
description: Find tech events, hackathons and student research calls on LinkedIn, X and Luma, and save them to the opportunity agent
argument-hint: "[focus, e.g. 'AI meetups in Toronto' or 'HCI student research'] [how many, default 10]"
---

Find upcoming opportunities that the public feeds (Devpost, MLH, confs.tech, ccfddl) miss:
networking events, demo nights, career fairs and hackathons near Toronto and Waterloo that are
announced on social media, plus student research calls (undergraduate research competitions,
student abstract and poster tracks, workshops). Arguments: $ARGUMENTS

## Rules
- **Read-only.** Never register, RSVP, post, like, reply, follow, connect, DM, or change
  anything on any site. The user registers themselves.
- Use Claude in Chrome (load the `anthropic-skills:chrome-browser` skill first) and open a new tab.
  Browse at a human pace. Stop and ask if a site shows a login wall, a rate limit, or a captcha.
- Every opportunity needs `url`: the event's own registration or listing page (Luma,
  Eventbrite, Meetup, the organizer's site, or the call for papers). A LinkedIn or X post alone
  is not enough; follow it to the event page. Never guess a date or a link; skip what you
  cannot confirm.
- Only events from today to 90 days out, in person near Toronto/Waterloo (Kitchener,
  Mississauga, Hamilton) or online. Skip anything over CA$100.

## Where to look
1. Luma: `https://luma.com/toronto` and `https://luma.com/discover`, plus calendars of TechTO,
   Toronto Tech Week, DMZ, MaRS, Communitech and Velocity.
2. LinkedIn (light: a few searches): Events search for "Toronto tech", "Waterloo AI",
   "founders networking Toronto"; posts by organizers announcing an event.
3. X (Latest tab): `Toronto tech event`, `Waterloo hackathon`, `"demo night" Toronto`.
4. Meetup and Eventbrite searches for Toronto/Waterloo tech, AI, startup and developer events.
5. University of Waterloo: WUSA club events, Velocity, Hack the North, UW AI and data science
   clubs.
6. Research calls: student research competitions and student/poster/late-breaking tracks of
   upcoming CS conferences (ACM SRC, AAAI student abstracts, CHI late-breaking work,
   NeurIPS/ICML workshops). Use the official call page as `url`.

## Output
Write a JSON list to `data/opportunities-inbox.json` with objects of this shape (see
`src/internship_agent/opportunities/schemas.py`):

```json
{
  "kind": "networking",
  "title": "TechTO Together Toronto",
  "url": "https://luma.com/techto-together",
  "source": "luma",
  "starts_on": "2026-11-12",
  "ends_on": "2026-11-12",
  "deadline": null,
  "deadline_label": "",
  "location": "Toronto, ON, Canada",
  "online": false,
  "topics": ["founders", "AI"],
  "details": "Organizer: TechTO. Who attends and why it is useful, in one or two factual sentences."
}
```

`kind` is one of `hackathon`, `conference`, `research`, `networking`. For a research call set
`deadline` to the submission deadline and `deadline_label` to what closes (e.g. "SRC abstracts
due"); for an event with a registration cutoff, the same.

Then run:

```
uv run internship-agent opportunities import data/opportunities-inbox.json
uv run internship-agent opportunities list
```

Finish with the best few, why each is worth going to, and for research calls offer to run
`uv run internship-agent opportunities strategy <url>` to plan a submission.
