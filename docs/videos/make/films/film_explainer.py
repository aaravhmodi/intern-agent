"""Film 1: intern-agent, explained (about 80 seconds, GitDiagram style)."""

FOLLOWUP_CODE = [
    "def next_followup(lead: Lead, wait_days: int) -> datetime | None:",
    "    if lead.replied_at is not None or lead.followups_stopped:",
    "        return None",
    "    if len(lead.followups) >= len(TEMPLATES):",
    "        return None",
]

BEATS = [
    # 0 hook
    ("hook", "Landing a Winter co-op means hundreds of cold emails,"),
    ("hook", "and nobody has the hours to write them... so this agent does."),
    # 1 find
    ("find", "Every morning it finds startups that just raised money,"),
    ("find", "scores each one against the resume,"),
    ("find", "and drafts a short note to the founder."),
    # 2 send
    ("send", "Then it sends them, by itself."),
    ("send", "Five batches a day go out from Gmail, timed to each city's morning,"),
    ("send", "two hundred emails and more, without a single click."),
    # 3 follow up
    ("follow", "Five days and no reply?"),
    ("follow", "A follow-up goes out in the same thread,"),
    ("follow", "at most twice, and never once someone answers."),
    # 4 apply
    ("apply", "Job postings get the same treatment: overnight,"),
    ("apply", "it fills in Greenhouse, Ashby and Lever forms and saves the confirmation."),
    # 5 pipeline
    ("pipeline", "Everything that comes back lands in the job pipeline."),
    ("pipeline", "Both inboxes are read every half hour,"),
    ("pipeline", "and each email moves its company along: reply, interview, offer."),
    # 6 how
    ("how", "Underneath, systemd timers wake a FastAPI app,"),
    ("how", "every lead lives in Postgres,"),
    ("how", "and anything new buzzes the phone."),
    # 7 under the hood
    ("hood", "The clever part is where it stops."),
    ("hood", "One check runs before every follow-up: did they reply?"),
    ("hood", "If they did, the agent goes quiet... and the conversation is yours."),
]

SCENES = [
    {  # hook
        "layout": {"col": ["big", {"row": ["c1", "c2", "c3"]}]},
        "shots": [
            {
                "beat": 0,
                "transition": "cut",
                "elements": [
                    {
                        "id": "big",
                        "kind": "heading",
                        "text": "Hundreds of *cold emails*",
                        "at": "hundreds",
                    },
                    {
                        "id": "c1",
                        "kind": "chip",
                        "text": "Winter 2027 co-op",
                        "tone": "soft",
                        "at": "Winter",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 1,
                "elements": [
                    {"id": "c2", "kind": "chip", "text": "no time", "tone": "bad", "at": "nobody"},
                    {
                        "id": "c3",
                        "kind": "chip",
                        "text": "intern-agent",
                        "tone": "accent",
                        "at": "so",
                    },
                ],
                "actions": [
                    {"at": "agent", "do": "pulse", "target": "c3"},
                    {"at": "agent", "do": "cross", "target": "c2"},
                ],
            },
        ],
    },
    {  # find
        "layout": {"row": ["news", "fit", "draft"]},
        "shots": [
            {
                "beat": 2,
                "transition": "push",
                "elements": [
                    {
                        "id": "news",
                        "kind": "box",
                        "label": "Funding news",
                        "sub": "last 60 days",
                        "icon": "globe",
                        "tone": "plain",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 3,
                "elements": [
                    {
                        "id": "fit",
                        "kind": "box",
                        "label": "Fit 0–100",
                        "sub": "vs. the resume",
                        "icon": "cpu",
                        "tone": "plain",
                        "at": "scores",
                    },
                    {
                        "id": "a1",
                        "kind": "arrow",
                        "from": "news",
                        "to": "fit",
                        "flow": True,
                        "at": "scores",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 4,
                "elements": [
                    {
                        "id": "draft",
                        "kind": "box",
                        "label": "Email draft",
                        "sub": "to the founder",
                        "icon": "file",
                        "tone": "accent",
                        "at": "drafts",
                    },
                    {
                        "id": "a2",
                        "kind": "arrow",
                        "from": "fit",
                        "to": "draft",
                        "flow": True,
                        "at": "drafts",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # send
        "layout": {"row": ["term", {"col": ["count", "stamp"]}]},
        "shots": [
            {
                "beat": 5,
                "transition": "slide",
                "elements": [
                    {
                        "id": "term",
                        "kind": "terminal",
                        "title": "systemd timers (Toronto)",
                        "lines": ["$ systemctl --user list-timers", "03:30  email-batch@europe"],
                        "at": "sends",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 6,
                "elements": [],
                "actions": [
                    {
                        "at": "batches",
                        "do": "type",
                        "target": "term",
                        "line": "09:00  email-batch@toronto",
                    },
                    {
                        "at": "Gmail",
                        "do": "type",
                        "target": "term",
                        "line": "10:30  email-batch@new-york",
                    },
                    {
                        "at": "city's",
                        "do": "type",
                        "target": "term",
                        "line": "13:00  email-batch@sf",
                    },
                    {
                        "at": "morning",
                        "do": "type",
                        "target": "term",
                        "line": "15:30  email-batch@others",
                    },
                ],
            },
            {
                "beat": 7,
                "elements": [
                    {
                        "id": "count",
                        "kind": "number",
                        "value": 200,
                        "suffix": "+",
                        "label": "emails a day",
                        "at": "two",
                    },
                    {
                        "id": "stamp",
                        "kind": "stamp",
                        "text": "0 clicks",
                        "tone": "accent",
                        "at": "without",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # follow up
        "layout": {"row": ["sent", "wait", "fu"]},
        "shots": [
            {
                "beat": 8,
                "transition": "push",
                "elements": [
                    {
                        "id": "sent",
                        "kind": "box",
                        "label": "Email sent",
                        "icon": "file",
                        "tone": "plain",
                        "at": "Five",
                    },
                    {
                        "id": "wait",
                        "kind": "box",
                        "label": "5 days",
                        "sub": "no reply",
                        "icon": "clock",
                        "tone": "soft",
                        "at": "days",
                    },
                    {
                        "id": "w1",
                        "kind": "arrow",
                        "from": "sent",
                        "to": "wait",
                        "dashed": True,
                        "at": "days",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 9,
                "elements": [
                    {
                        "id": "fu",
                        "kind": "box",
                        "label": "Follow-up",
                        "sub": "same thread",
                        "icon": "queue",
                        "tone": "accent",
                        "at": "thread",
                    },
                    {
                        "id": "w2",
                        "kind": "arrow",
                        "from": "wait",
                        "to": "fu",
                        "flow": True,
                        "at": "goes",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 10,
                "elements": [],
                "actions": [
                    {"at": "twice", "do": "replace", "target": "fu", "text": "Follow-up ×2 max"},
                    {"at": "answers", "do": "check", "target": "fu"},
                ],
            },
        ],
    },
    {  # apply
        "layout": {"row": ["form", {"col": ["gh", "ash", "lev"]}]},
        "shots": [
            {
                "beat": 11,
                "transition": "slide",
                "elements": [
                    {
                        "id": "form",
                        "kind": "box",
                        "label": "Application form",
                        "sub": "answers from the resume",
                        "icon": "browser",
                        "tone": "accent",
                        "at": "postings",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 12,
                "elements": [
                    {
                        "id": "gh",
                        "kind": "chip",
                        "text": "Greenhouse",
                        "tone": "plain",
                        "at": "Greenhouse",
                    },
                    {"id": "ash", "kind": "chip", "text": "Ashby", "tone": "plain", "at": "Ashby"},
                    {"id": "lev", "kind": "chip", "text": "Lever", "tone": "plain", "at": "Lever"},
                ],
                "actions": [{"at": "confirmation", "do": "check", "target": "form"}],
            },
        ],
    },
    {  # pipeline
        "layout": {"row": [{"col": ["inbox", "every"]}, {"col": ["s1", "s2", "s3"]}]},
        "shots": [
            {
                "beat": 13,
                "transition": "zoom",
                "elements": [
                    {
                        "id": "inbox",
                        "kind": "box",
                        "label": "Job pipeline",
                        "sub": "both Gmail inboxes",
                        "icon": "database",
                        "tone": "accent",
                        "at": "pipeline",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 14,
                "elements": [
                    {
                        "id": "every",
                        "kind": "chip",
                        "text": "every 30 min",
                        "tone": "soft",
                        "at": "read",
                    },
                ],
                "actions": [{"at": "half", "do": "pulse", "target": "inbox"}],
            },
            {
                "beat": 15,
                "elements": [
                    {"id": "s1", "kind": "chip", "text": "Replied", "tone": "soft", "at": "reply"},
                    {
                        "id": "s2",
                        "kind": "chip",
                        "text": "Interview",
                        "tone": "ok",
                        "at": "interview",
                    },
                    {"id": "s3", "kind": "chip", "text": "Offer", "tone": "accent", "at": "offer"},
                    {
                        "id": "p1",
                        "kind": "arrow",
                        "from": "inbox",
                        "to": "s2",
                        "flow": True,
                        "at": "moves",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # how
        "layout": {"row": ["timer", "app", "db", "phone"]},
        "shots": [
            {
                "beat": 16,
                "transition": "push",
                "elements": [
                    {
                        "id": "timer",
                        "kind": "box",
                        "label": "systemd",
                        "icon": "clock",
                        "tone": "plain",
                        "at": "systemd",
                    },
                    {
                        "id": "app",
                        "kind": "box",
                        "label": "FastAPI",
                        "icon": "server",
                        "tone": "accent",
                        "at": "FastAPI",
                    },
                    {
                        "id": "h1",
                        "kind": "arrow",
                        "from": "timer",
                        "to": "app",
                        "flow": True,
                        "at": "wake",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 17,
                "elements": [
                    {
                        "id": "db",
                        "kind": "box",
                        "label": "Postgres",
                        "icon": "database",
                        "tone": "plain",
                        "at": "Postgres",
                    },
                    {"id": "h2", "kind": "arrow", "from": "app", "to": "db", "at": "lives"},
                ],
                "actions": [],
            },
            {
                "beat": 18,
                "elements": [
                    {
                        "id": "phone",
                        "kind": "box",
                        "label": "Phone push",
                        "icon": "bolt",
                        "tone": "plain",
                        "at": "anything",
                    },
                    {
                        "id": "h3",
                        "kind": "arrow",
                        "from": "db",
                        "to": "phone",
                        "flow": True,
                        "at": "new",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # under the hood
        "layout": {"row": ["code", "you"]},
        "shots": [
            {
                "beat": 19,
                "transition": "slide",
                "elements": [
                    {
                        "id": "code",
                        "kind": "code",
                        "title": "src/internship_agent/leads/followups.py",
                        "lines": FOLLOWUP_CODE,
                        "focus": [],
                        "at": "stops",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 20,
                "elements": [],
                "actions": [
                    {"at": "reply", "do": "highlight", "target": "code", "lines": [2]},
                    {"at": "check", "do": "focus", "target": "code"},
                ],
            },
            {
                "beat": 21,
                "elements": [
                    {
                        "id": "you",
                        "kind": "stamp",
                        "text": "Yours now",
                        "tone": "ok",
                        "at": "quiet",
                    },
                ],
                "actions": [{"at": "If", "do": "reset", "target": "code"}],
            },
        ],
    },
]

FILM = {
    "repo": "intern-agent",
    "description": (
        "Finds Winter 2027 internships, emails the people behind them, follows up and tracks"
        " every reply."
    ),
    "title": "intern-agent",
    "outro": "200+ emails a day. Replies are yours.",
    "beats": BEATS,
    "scenes": SCENES,
    "code_files": ["src/internship_agent/leads/followups.py"],
}
