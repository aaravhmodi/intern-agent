"""OpenAI calls. All output is parsed into Pydantic models before use."""

from datetime import date

from openai import OpenAI
from pydantic import BaseModel, ConfigDict

from internship_agent.leads.schemas import (
    FitResult,
    Lead,
    OutreachDraft,
    OutreachDraftResult,
    Segment,
)

FIT_INSTRUCTIONS = """\
You assess whether a company is a good fit for a Winter 2027 (January-April)
software-engineering intern, given the candidate's resume. The lead is either a startup that
recently raised (kind=founder) or a published internship posting (kind=posting). Be honest and
specific: cite concrete resume evidence and concrete facts about the company or posting.
Penalize weak overlap with the candidate's skills, roles that clearly need senior engineers or
a different season, and missing information. Never invent facts that are not in the input.
Score 0-100; verdict strong >= 75, possible 50-74, weak < 50.
Also classify company_segment: early = pre-seed/seed startup; mid = Series A-D or growth-stage
private startup; big = public company, large enterprise, bank, or established private company."""

# How the candidate wants to be pitched. Edit this to change every new draft.
# Based on what startup founders and forward-deployed-engineering (FDE) teams screen for:
# ownership, shipping to real users, measurable impact, working directly with
# non-technical stakeholders, and proof of work.
OUTREACH_FOCUS = """\
CORE STORY (always lead with this):
At Upside Robotics (SWE intern, Jan-Aug 2026), Aarav built a production operations dashboard
on his own, end to end: the Next.js/React frontend and the FastAPI backend on AWS ECS with RDS
PostgreSQL, Redis caching and Redshift. 35+ employees and executive stakeholders use it, and it
cut operational metric retrieval from weeks to minutes. Say "I built and own(ed) it end to
end" or "I built it solo, from frontend to AWS deployment"; describe it as shipped and used by
real people, with the outcome before the stack.

SUPPORTING PROOF (pick at most one that matches the company):
- Data/infra: PostgreSQL-to-Redshift ETL loading 500K+ rows daily, 80% faster warehouse loads.
- Real-time/robotics: telemetry moved from polling to WebSockets and Zenoh, 50% lower latency.
- Reliability: production data services with failure alerts in under 5 minutes.
- Zero-to-one ownership (good for early-stage founders): founding software engineer at Enerzen,
  owning architecture for a 4-person team and deploying a pilot in Mississauga.
- AI in production (good for AI / forward-deployed roles): integrated ML anomaly detection
  through FastAPI at CIBC; shipped CRai, a CNN audio classifier served on Modal.
- AI agents and integrations (good for AI, agent, and forward-deployed roles): currently
  building a personal job-search agent that connects to Outlook through an MCP server, uses
  OpenAI structured outputs and web search with source verification, and runs a FastAPI
  dashboard he uses for his own internship search. Call it a personal project; no other users.

ANGLE BY AUDIENCE (use the lead's segment and posting_title):
- early/mid startups and founders: ownership and speed. Show you ship end to end for real users
  and can work without much direction. Under 100 words. Tie the core story to one specific
  thing the company builds.
- forward-deployed, solutions, or applied-AI roles (title or company mentions them): show
  turning a messy business need into a deployed tool non-technical people rely on (ops staff
  and executives at Upside), full-stack Python + TypeScript, and AI in production.
- big companies: name the posting, then the core story and one proof point mapped to the team.

RULES: Never cite endpoint or module counts. CIBC only as brief AI/banking proof or for a CIBC or
banking role. Sole ownership applies only to the Upside dashboard. Do not claim customer
interviews, requirements gathering, or anything not stated here or in the resume.
End the email with "Portfolio: aaravmodi.ca" on its own line before the sign-off."""

DRAFT_INSTRUCTIONS = (
    """\
Write a short, genuine cold outreach from a University of Waterloo student about a Winter 2027
(Jan-Apr) software-engineering internship, addressed to contact_name (use "Hi <first name>,"
or "Hi there," if no name). For kind=founder, ask whether they would take an intern and
reference one specific thing about what the company builds or its recent raise. For
kind=posting, mention the posting_title, say the student has applied or is applying, and ask a
brief question about the team. Use only facts from the resume and the focus notes below.
No flattery, no buzzwords, no fabricated details. The X DM must be under 600 characters (write
it even if there is no X handle). The email must be under 150 words (100 for founders) and end
with a clear, low-effort ask. Sign off as Aarav. The LinkedIn connection note must be under 280
characters, with no greeting line breaks and no links.

FOCUS NOTES:
"""
    + OUTREACH_FOCUS
)

STARTUP_SEARCH_INSTRUCTIONS = """\
Use web search to find startups that publicly announced a funding round between {start} and
{end}. Prefer software/AI companies based in Canada (especially Toronto and Waterloo) or
hiring remotely in Canada, at stage: {stages}. For each, report only facts stated in the source
article: company, a named founder (prefer the CTO or technical co-founder) and their title,
round, amount in USD if stated, announcement date, the article URL, the company website if
stated, one factual sentence on what they build, and location. Skip any company where you
cannot cite a specific article. Exclude these already-known companies: {exclude}."""


class StartupFinding(BaseModel):
    model_config = ConfigDict(extra="forbid")

    company: str
    founder_name: str
    founder_role: str
    round: str
    amount_usd: int | None
    announced_on: date
    source_url: str
    company_url: str | None
    what_they_build: str
    location: str


class StartupFindings(BaseModel):
    model_config = ConfigDict(extra="forbid")

    startups: list[StartupFinding]


def _lead_context(lead: Lead) -> str:
    return lead.model_dump_json(
        exclude={
            "status",
            "fit",
            "draft",
            "email",
            "email_status",
            "email_source",
            "segment",
            "sent_at",
            "sent_to",
        },
        indent=2,
    )


def assess_fit(client: OpenAI, model: str, resume: str, lead: Lead) -> FitResult:
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": FIT_INSTRUCTIONS},
            {"role": "user", "content": f"RESUME:\n{resume}\n\nLEAD:\n{_lead_context(lead)}"},
        ],
        text_format=FitResult,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no fit assessment")
    return FitResult.model_validate(response.output_parsed.model_dump())


def draft_outreach(client: OpenAI, model: str, resume: str, lead: Lead) -> OutreachDraft:
    fit = lead.fit.model_dump_json() if lead.fit else "not assessed"
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": DRAFT_INSTRUCTIONS},
            {
                "role": "user",
                "content": f"RESUME:\n{resume}\n\nLEAD:\n{_lead_context(lead)}\n\nFIT:\n{fit}",
            },
        ],
        text_format=OutreachDraftResult,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no draft")
    return OutreachDraft.model_validate(response.output_parsed.model_dump())


def search_startups(
    client: OpenAI,
    model: str,
    start: date,
    end: date,
    stages: list[Segment],
    exclude: list[str],
    count: int,
) -> list[StartupFinding]:
    stage_text = ", ".join(
        "pre-seed or seed" if s is Segment.EARLY else "Series A to D" for s in stages
    )
    response = client.responses.parse(
        model=model,
        tools=[
            {
                "type": "web_search",
                "user_location": {"type": "approximate", "country": "CA", "city": "Toronto"},
            }
        ],
        input=[
            {
                "role": "system",
                "content": STARTUP_SEARCH_INSTRUCTIONS.format(
                    start=start, end=end, stages=stage_text, exclude=", ".join(exclude) or "none"
                ),
            },
            {"role": "user", "content": f"Find up to {count} startups."},
        ],
        text_format=StartupFindings,
    )
    if response.output_parsed is None:
        return []
    return StartupFindings.model_validate(response.output_parsed.model_dump()).startups
