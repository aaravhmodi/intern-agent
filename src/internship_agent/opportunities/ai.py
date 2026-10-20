"""OpenAI web searches for events and submission strategies. Output is parsed by Pydantic."""

from datetime import date
from typing import Literal

from openai import OpenAI
from pydantic import BaseModel, ConfigDict

from internship_agent.opportunities.schemas import (
    Opportunity,
    OpportunityAssessment,
    SubmissionStrategy,
)

# What the model is told about an event; it reads the rest from the event's pages.
_FACTS = {
    "kind",
    "title",
    "url",
    "starts_on",
    "deadline",
    "deadline_label",
    "location",
    "topics",
    "details",
    "rank",
}

ASSESS_INSTRUCTIONS = """\
You help a University of Waterloo software-engineering co-op student, who lives in Waterloo and
Toronto, Canada and is a Canadian citizen, decide whether to go to the event below. Today is
{today}. Use web search to read the event's own pages (home, FAQ, travel or reimbursement,
schedule, registration, eligibility) and report only what they state:
- format and location: in person, online or hybrid; the venue and city.
- travel: "covered" if the organizers pay a student's way there (flights, buses, train or a
  reimbursement), "partial" if support is capped, limited, by lottery or application only,
  "none" if they say there is none, "unknown" if their pages do not say. travel_details: what
  is paid for, the cap, how and by when to apply, any bus from Waterloo or Toronto, and whether
  housing and food are free. travel_source_url: the page that says so ("" if none).
- cost: the price for a student to attend ("free" only if stated).
- effort: "light" (an evening or one day, no preparation), "moderate" (a weekend, or a few
  days of preparation), "heavy" (weeks of work: a paper, a long online build, a talk to
  prepare). effort_details: the hours, what you must prepare and produce.
- fit: two to four concrete ways the candidate's skills and projects (resume and context
  below) apply here: tracks, themes, sponsors' technology, the people attending. fit_score
  0-100: how worthwhile it is for him, weighing relevance to software-engineering internships
  and startups, what he would learn, and who he would meet.
- highlights: what makes it fun or worth the trip: the city, prizes, recruiters and sponsors
  attending, perks.
- summary: one or two sentences: should he go, and why.
If students from Canada or from other universities cannot take part, say so in the summary and
give a low fit_score. Never invent; write "not stated" where the pages are silent."""

EVENT_SEARCH_INSTRUCTIONS = """\
Use web search to find in-person tech events in or near {cities} between {start} and {end}
where a University of Waterloo software-engineering student can meet engineers, founders and
recruiters: networking nights, meetups, demo days, founder and builder mixers, career fairs,
tech talks, and hackathons. Look at Luma (luma.com, lu.ma), Eventbrite, Meetup, LinkedIn
event pages and organizers' LinkedIn posts, organizers' posts on X, and community calendars
such as TechTO, Toronto Tech Week, Communitech, Velocity, DMZ, MaRS, Google Developer Groups
and University of Waterloo clubs and societies.
For each event report only what a source states: title; url (the event's own registration or
listing page); starts_on (YYYY-MM-DD); location (venue or city); organizer; kind; and one
factual sentence on who attends and why it is useful. Skip events you cannot back with a
specific event page, recurring series without a dated next session, events costing over
CA$100, and these already-known events: {exclude}."""

STRATEGY_INSTRUCTIONS = """\
You plan how a University of Waterloo undergraduate (third-year Systems Design Engineering,
software-engineering co-op student) could get work accepted at, or otherwise get into, the
venue below. Today is {today}.
Use web search to read the venue's official pages for this edition: the main call for papers
and, more importantly for an undergraduate, every track an undergraduate can realistically
enter: ACM Student Research Competition (undergraduate category), undergraduate consortia,
student abstract and poster programs, late-breaking work, demos, tool and artifact tracks,
co-located workshops (say whether each is archival; non-archival work can later go to a full
venue), and for industry conferences talk, lightning-talk or workshop proposals. List only
tracks whose page you read, with the deadline as stated (and its timezone), the format and
length, eligibility (for example ACM student membership or an advisor's letter), and that
page's URL. Leave out tracks whose deadline has passed; if none is open, say so and point to
the next edition.
Then match the candidate's real work (resume and candidate context below) to the best track:
name the specific project, the contribution it could honestly support, and what is missing
(a baseline, an evaluation, a user study, related work, a faculty advisor). Never invent
results, metrics or co-authors, and treat prototypes as prototypes. A first paper is usually
more realistic as a workshop paper, poster, student research competition or late-breaking
entry than a main-track paper; set verdict honestly to "realistic", "stretch" or
"not this cycle".
plan: 4-8 concrete steps with dates, working back from the chosen deadline (for example: ask
a Waterloo professor working in this area to advise; run the evaluation; write in the
venue's template; get feedback two weeks before). funding: ways to attend affordably that
the venue states (student volunteer program, travel grants, student registration rates,
scholarships) plus University of Waterloo funding if relevant; only what you found.
risks: what could sink the submission."""


class EventFinding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    url: str
    starts_on: date
    location: str
    organizer: str
    kind: Literal["networking", "hackathon", "conference"]
    why: str


class EventFindings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    events: list[EventFinding]


def search_events(
    client: OpenAI,
    model: str,
    cities: list[str],
    start: date,
    end: date,
    exclude: list[str],
    count: int,
) -> list[EventFinding]:
    response = client.responses.parse(
        model=model,
        tools=[{"type": "web_search"}],
        input=[
            {
                "role": "system",
                "content": EVENT_SEARCH_INSTRUCTIONS.format(
                    cities=", ".join(cities),
                    start=start,
                    end=end,
                    exclude="; ".join(exclude) or "none",
                ),
            },
            {"role": "user", "content": f"Find up to {count} events."},
        ],
        text_format=EventFindings,
    )
    if response.output_parsed is None:
        return []
    return EventFindings.model_validate(response.output_parsed.model_dump()).events


def write_strategy(
    client: OpenAI, model: str, resume: str, context: str, venue: Opportunity, today: date
) -> SubmissionStrategy:
    facts = venue.model_dump_json(include=_FACTS, exclude_none=True)
    response = client.responses.parse(
        model=model,
        tools=[{"type": "web_search"}],
        input=[
            {"role": "system", "content": STRATEGY_INSTRUCTIONS.format(today=today)},
            {
                "role": "user",
                "content": f"VENUE:\n{facts}\n\nRESUME:\n{resume}\n\nCANDIDATE CONTEXT:\n{context}",
            },
        ],
        text_format=SubmissionStrategy,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no strategy")
    return SubmissionStrategy.model_validate(response.output_parsed.model_dump())


def assess(
    client: OpenAI, model: str, resume: str, context: str, event: Opportunity, today: date
) -> OpportunityAssessment:
    facts = event.model_dump_json(include=_FACTS | {"ends_on", "online"}, exclude_none=True)
    response = client.responses.parse(
        model=model,
        tools=[{"type": "web_search"}],
        input=[
            {"role": "system", "content": ASSESS_INSTRUCTIONS.format(today=today)},
            {
                "role": "user",
                "content": f"EVENT:\n{facts}\n\nRESUME:\n{resume}\n\nCANDIDATE CONTEXT:\n{context}",
            },
        ],
        text_format=OpportunityAssessment,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no assessment")
    return OpportunityAssessment.model_validate(response.output_parsed.model_dump())
