"""Film 2: the job pipeline, following one email from send to reply."""

CLASSIFY_CODE = [
    "if _DECLINED.search(body[:4000]):",
    '    return "rejected"',
    'stage = classify_text(f"{subject}\\n{body[:4000]}")',
    "if stage is not Stage.OTHER:",
    "    return stage.value  # type: ignore[return-value]",
]

BEATS = [
    ("one", "Follow one email."),
    ("one", "At nine, the Toronto batch writes to a founder who just raised a seed round."),
    ("guess", "There's no published address, so the agent guesses the company's format:"),
    ("guess", "first name, at the company's domain."),
    ("guess", "If that bounces, it tries the next format, never the same one twice."),
    ("wait", "Now it waits."),
    ("wait", "Every half hour, both Gmail inboxes are read, read-only,"),
    ("wait", "so nothing is marked, moved or deleted."),
    ("follow", "Day five, still silence."),
    ("follow", "A follow-up goes out as a reply in the same thread,"),
    ("follow", "and if day ten is quiet too, one more. That's the limit."),
    ("match", "Then the founder writes back."),
    ("match", "The scan matches it to its lead: by address, then domain, then company name,"),
    ("match", "and a fixed set of patterns, no AI, reads it as an interview."),
    ("board", "On the pipeline board, the card jumps from Waiting to Interview,"),
    ("board", "and the phone buzzes with a link straight to it."),
    ("funnel", "Across every lead, the funnels show where things drop off:"),
    ("funnel", "emailed, delivered, replied, interview."),
    ("hood", "Inside the scan, a no is checked before anything else,"),
    ("hood", "so a polite rejection never shows up as a reply."),
    ("hood", "From that first answer on, the agent stays quiet... the conversation is yours."),
]

SCENES = [
    {  # one
        "layout": {"row": ["term", "founder"]},
        "shots": [
            {
                "beat": 0,
                "transition": "cut",
                "elements": [
                    {
                        "id": "term",
                        "kind": "terminal",
                        "title": "09:00 Toronto batch",
                        "lines": ["$ internship-agent leads guess-send --area toronto --send"],
                    },
                ],
                "actions": [],
            },
            {
                "beat": 1,
                "elements": [
                    {
                        "id": "founder",
                        "kind": "box",
                        "label": "Founder",
                        "sub": "seed round, last week",
                        "icon": "user",
                        "tone": "accent",
                        "at": "founder",
                    },
                    {
                        "id": "a",
                        "kind": "arrow",
                        "from": "term",
                        "to": "founder",
                        "flow": True,
                        "at": "writes",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # guess
        "layout": {"row": ["site", {"col": ["f1", "f2", "f3"]}]},
        "shots": [
            {
                "beat": 2,
                "transition": "push",
                "elements": [
                    {
                        "id": "site",
                        "kind": "box",
                        "label": "No published email",
                        "sub": "site checked",
                        "icon": "globe",
                        "tone": "ghost",
                    },
                ],
                "actions": [{"at": "guesses", "do": "pulse", "target": "site"}],
            },
            {
                "beat": 3,
                "elements": [
                    {"id": "f1", "kind": "chip", "text": "first@", "tone": "accent", "at": "first"},
                ],
                "actions": [],
            },
            {
                "beat": 4,
                "elements": [
                    {
                        "id": "f2",
                        "kind": "chip",
                        "text": "first.last@",
                        "tone": "plain",
                        "at": "next",
                    },
                    {
                        "id": "f3",
                        "kind": "chip",
                        "text": "careers@ after 2",
                        "tone": "soft",
                        "at": "never",
                    },
                ],
                "actions": [{"at": "bounces", "do": "cross", "target": "f1"}],
            },
        ],
    },
    {  # wait
        "layout": {"row": ["gmail", {"col": ["ro", "freq"]}]},
        "shots": [
            {
                "beat": 5,
                "transition": "slide",
                "elements": [
                    {
                        "id": "gmail",
                        "kind": "box",
                        "label": "Gmail ×2",
                        "sub": "main + outreach",
                        "icon": "lock",
                        "tone": "accent",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 6,
                "elements": [
                    {
                        "id": "freq",
                        "kind": "chip",
                        "text": "every 30 min",
                        "tone": "soft",
                        "at": "half",
                    },
                    {"id": "ro", "kind": "chip", "text": "read-only", "tone": "ok", "at": "read"},
                ],
                "actions": [],
            },
            {
                "beat": 7,
                "elements": [],
                "actions": [{"at": "nothing", "do": "check", "target": "ro"}],
            },
        ],
    },
    {  # follow
        "layout": {"row": ["d0", "d5", "d10"]},
        "shots": [
            {
                "beat": 8,
                "transition": "push",
                "elements": [
                    {
                        "id": "d0",
                        "kind": "box",
                        "label": "Day 0",
                        "sub": "first email",
                        "icon": "file",
                        "tone": "plain",
                    },
                    {
                        "id": "d5",
                        "kind": "box",
                        "label": "Day 5",
                        "sub": "silence",
                        "icon": "clock",
                        "tone": "ghost",
                        "at": "five",
                    },
                    {
                        "id": "e1",
                        "kind": "arrow",
                        "from": "d0",
                        "to": "d5",
                        "dashed": True,
                        "at": "five",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 9,
                "elements": [],
                "actions": [
                    {"at": "follow-up", "do": "replace", "target": "d5", "text": "Follow-up 1"},
                    {"at": "thread", "do": "pulse", "target": "d5"},
                ],
            },
            {
                "beat": 10,
                "elements": [
                    {
                        "id": "d10",
                        "kind": "box",
                        "label": "Follow-up 2",
                        "sub": "day 10, the last",
                        "icon": "clock",
                        "tone": "accent",
                        "at": "ten",
                    },
                    {
                        "id": "e2",
                        "kind": "arrow",
                        "from": "d5",
                        "to": "d10",
                        "dashed": True,
                        "at": "ten",
                    },
                    {"id": "lim", "kind": "stamp", "text": "max 2", "tone": "bad", "at": "one"},
                ],
                "actions": [],
            },
        ],
    },
    {  # match
        "layout": {"col": ["reply", {"row": ["m1", "m2", "m3"]}, "stage"]},
        "shots": [
            {
                "beat": 11,
                "transition": "zoom",
                "elements": [
                    {
                        "id": "reply",
                        "kind": "chip",
                        "text": "Re: Winter 2027 internship",
                        "tone": "accent",
                        "at": "writes",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 12,
                "elements": [
                    {
                        "id": "m1",
                        "kind": "box",
                        "label": "Address",
                        "icon": "user",
                        "tone": "plain",
                        "at": "address",
                    },
                    {
                        "id": "m2",
                        "kind": "box",
                        "label": "Domain",
                        "icon": "globe",
                        "tone": "plain",
                        "at": "domain",
                    },
                    {
                        "id": "m3",
                        "kind": "box",
                        "label": "Company name",
                        "icon": "file",
                        "tone": "plain",
                        "at": "company",
                    },
                    {"id": "g1", "kind": "arrow", "from": "m1", "to": "m2", "at": "domain"},
                    {"id": "g2", "kind": "arrow", "from": "m2", "to": "m3", "at": "company"},
                ],
                "actions": [{"at": "matches", "do": "pulse", "target": "reply"}],
            },
            {
                "beat": 13,
                "elements": [
                    {
                        "id": "stage",
                        "kind": "chip",
                        "text": "stage: interview",
                        "tone": "ok",
                        "at": "patterns",
                    },
                ],
                "actions": [{"at": "interview", "do": "pulse", "target": "stage"}],
            },
        ],
    },
    {  # board
        "layout": {"row": ["waiting", "interview", "phone"]},
        "shots": [
            {
                "beat": 14,
                "transition": "slide",
                "elements": [
                    {
                        "id": "waiting",
                        "kind": "box",
                        "label": "Waiting",
                        "icon": "clock",
                        "tone": "ghost",
                    },
                    {
                        "id": "interview",
                        "kind": "box",
                        "label": "Interview",
                        "icon": "user",
                        "tone": "ok",
                        "at": "jumps",
                    },
                    {
                        "id": "j",
                        "kind": "arrow",
                        "from": "waiting",
                        "to": "interview",
                        "flow": True,
                        "at": "jumps",
                    },
                ],
                "actions": [{"at": "Interview", "do": "pulse", "target": "interview"}],
            },
            {
                "beat": 15,
                "elements": [
                    {
                        "id": "phone",
                        "kind": "box",
                        "label": "Phone push",
                        "sub": "opens that card",
                        "icon": "bolt",
                        "tone": "accent",
                        "at": "phone",
                    },
                    {
                        "id": "k",
                        "kind": "arrow",
                        "from": "interview",
                        "to": "phone",
                        "flow": True,
                        "at": "buzzes",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {  # funnel
        "layout": {"row": ["bars", "note"]},
        "shots": [
            {
                "beat": 16,
                "transition": "push",
                "elements": [
                    {
                        "id": "bars",
                        "kind": "bars",
                        "unit": "",
                        "items": [
                            {"label": "Emailed", "value": 100},
                            {"label": "Delivered", "value": 94},
                            {"label": "Replied", "value": 50},
                            {"label": "Interview", "value": 19},
                        ],
                    },
                    {
                        "id": "note",
                        "kind": "text",
                        "text": "sample data",
                        "size": "s",
                        "tone": "muted",
                        "at": "funnels",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 17,
                "elements": [],
                "actions": [
                    {"at": "interview", "do": "pulse", "target": "note"},
                ],
            },
        ],
    },
    {  # hood
        "layout": {"row": ["code", "yours"]},
        "shots": [
            {
                "beat": 18,
                "transition": "slide",
                "elements": [
                    {
                        "id": "code",
                        "kind": "code",
                        "title": "src/internship_agent/pipeline.py",
                        "lines": CLASSIFY_CODE,
                        "focus": [1],
                    },
                ],
                "actions": [],
            },
            {
                "beat": 19,
                "elements": [],
                "actions": [
                    {"at": "rejection", "do": "highlight", "target": "code", "lines": [2]},
                ],
            },
            {
                "beat": 20,
                "elements": [
                    {
                        "id": "yours",
                        "kind": "stamp",
                        "text": "Yours now",
                        "tone": "ok",
                        "at": "quiet",
                    },
                ],
                "actions": [{"at": "answer", "do": "dim", "target": "code"}],
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
    "title": "The job pipeline",
    "outro": "It sends. It follows up. You talk.",
    "beats": BEATS,
    "scenes": SCENES,
    "code_files": ["src/internship_agent/pipeline.py"],
    "wps": 2.7,
}
