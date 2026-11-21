"""Film 3: one day of intern-agent, a short timeline cut (made for vertical feeds)."""

BEATS = [
    ("open", "Here's one day of intern-agent, start to finish."),
    ("night", "Two in the morning: it applies to every eligible posting, lowest fit first."),
    ("night", "Three thirty: the Europe batch, twenty emails."),
    ("morning", "Seven thirty: it hunts for new raises and the people behind them."),
    ("morning", "Then Toronto, New York and San Francisco, twenty emails each,"),
    ("morning", "and twenty more for everywhere else."),
    ("loop", "In between, follow-ups go out to anyone quiet for five days,"),
    ("loop", "and both inboxes are checked every half hour."),
    ("evening", "Nine thirty at night: it scrapes tomorrow's postings."),
    ("end", "Two hundred emails and more, zero clicks."),
    ("end", "And when someone answers... it's your turn."),
]

SCENES = [
    {
        "layout": {"col": ["title", "sub"]},
        "shots": [
            {
                "beat": 0,
                "transition": "cut",
                "elements": [
                    {"id": "title", "kind": "heading", "text": "One *day*"},
                    {
                        "id": "sub",
                        "kind": "chip",
                        "text": "intern-agent",
                        "tone": "accent",
                        "at": "intern-agent",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {
        "layout": {"row": ["apply", "eu"]},
        "shots": [
            {
                "beat": 1,
                "transition": "push",
                "elements": [
                    {
                        "id": "apply",
                        "kind": "box",
                        "label": "02:00 Apply",
                        "sub": "lowest fit first",
                        "icon": "browser",
                        "tone": "plain",
                    },
                ],
                "actions": [{"at": "eligible", "do": "pulse", "target": "apply"}],
            },
            {
                "beat": 2,
                "elements": [
                    {
                        "id": "eu",
                        "kind": "box",
                        "label": "03:30 Europe",
                        "sub": "20 emails",
                        "icon": "queue",
                        "tone": "accent",
                        "at": "Europe",
                    },
                    {"id": "a1", "kind": "arrow", "from": "apply", "to": "eu", "at": "thirty"},
                ],
                "actions": [],
            },
        ],
    },
    {
        "layout": {"row": ["find", {"col": ["to", "ny", "sf", "oth"]}]},
        "shots": [
            {
                "beat": 3,
                "transition": "slide",
                "elements": [
                    {
                        "id": "find",
                        "kind": "box",
                        "label": "07:30 Find leads",
                        "sub": "new raises + people",
                        "icon": "globe",
                        "tone": "plain",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 4,
                "elements": [
                    {
                        "id": "to",
                        "kind": "chip",
                        "text": "09:00 Toronto · 20",
                        "tone": "accent",
                        "at": "Toronto",
                    },
                    {
                        "id": "ny",
                        "kind": "chip",
                        "text": "10:30 New York · 20",
                        "tone": "accent",
                        "at": "York",
                    },
                    {
                        "id": "sf",
                        "kind": "chip",
                        "text": "13:00 SF · 20",
                        "tone": "accent",
                        "at": "Francisco",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 5,
                "elements": [
                    {
                        "id": "oth",
                        "kind": "chip",
                        "text": "15:30 Others · 20",
                        "tone": "accent",
                        "at": "twenty",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {
        "layout": {"row": ["fu", "inbox"]},
        "shots": [
            {
                "beat": 6,
                "transition": "push",
                "elements": [
                    {
                        "id": "fu",
                        "kind": "box",
                        "label": "Follow-ups",
                        "sub": "after 5 quiet days",
                        "icon": "clock",
                        "tone": "plain",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 7,
                "elements": [
                    {
                        "id": "inbox",
                        "kind": "box",
                        "label": "Inbox check",
                        "sub": "every 30 min",
                        "icon": "lock",
                        "tone": "soft",
                        "at": "inboxes",
                    },
                ],
                "actions": [{"at": "half", "do": "pulse", "target": "inbox"}],
            },
        ],
    },
    {
        "layout": {"row": ["scrape", {"col": ["fd", "hack"]}]},
        "shots": [
            {
                "beat": 8,
                "transition": "slide",
                "elements": [
                    {
                        "id": "scrape",
                        "kind": "box",
                        "label": "21:30 Scrape",
                        "sub": "tomorrow's postings",
                        "icon": "database",
                        "tone": "accent",
                    },
                    {
                        "id": "fd",
                        "kind": "chip",
                        "text": "SEC Form D founders",
                        "tone": "soft",
                        "at": "scrapes",
                    },
                    {
                        "id": "hack",
                        "kind": "chip",
                        "text": "hackathon feeds",
                        "tone": "soft",
                        "at": "postings",
                    },
                ],
                "actions": [],
            },
        ],
    },
    {
        "layout": {"col": ["n", {"row": ["clicks", "turn"]}]},
        "shots": [
            {
                "beat": 9,
                "transition": "zoom",
                "elements": [
                    {
                        "id": "n",
                        "kind": "number",
                        "value": 200,
                        "suffix": "+",
                        "label": "emails a day",
                    },
                    {
                        "id": "clicks",
                        "kind": "stamp",
                        "text": "0 clicks",
                        "tone": "accent",
                        "at": "zero",
                    },
                ],
                "actions": [],
            },
            {
                "beat": 10,
                "elements": [
                    {
                        "id": "turn",
                        "kind": "chip",
                        "text": "your turn",
                        "tone": "ok",
                        "at": "answers",
                    },
                ],
                "actions": [{"at": "turn", "do": "pulse", "target": "turn"}],
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
    "title": "One day, 200+ emails",
    "outro": "Every day. Without a click.",
    "beats": BEATS,
    "scenes": SCENES,
}
