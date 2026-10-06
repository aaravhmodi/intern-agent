"""OpenAI calls. All output is parsed into Pydantic models before use."""

from datetime import date
from typing import Literal

from openai import OpenAI
from pydantic import BaseModel, ConfigDict

from internship_agent.leads.schemas import (
    FitResult,
    Lead,
    LeadStatus,
    OutreachDraft,
    OutreachDraftResult,
    Preference,
    PreferenceEffect,
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
private startup; big = public company, large enterprise, bank, or established private company.
The candidate's own preferences are listed below with ids. Apply them: lower the score for
'downrank' rules, raise it for 'boost' rules, and list in violated_preference_ids every 'skip'
or 'downrank' rule this lead clearly breaks, based only on evidence in the input (for example,
the posting text says French is required). A requirement must be stated as required for this
role; company-wide boilerplate (e.g. "we may ask you to take a French proficiency test") does
not count. Do not guess; leave the list empty when unsure.

CANDIDATE PREFERENCES:
{preferences}"""

NOTE_INSTRUCTIONS = """\
You are the notes assistant in a candidate's internship-search dashboard. The candidate writes
short notes, optionally about the currently selected lead. Decide:
- lead_note: a concise, factual note to save on the selected lead, or null if no lead is
  selected or the message is not about it.
- status_change: "skipped" if they say they will not apply or are not interested; "applied"
  if they say they applied; "contacted" if they say they reached out; otherwise "none".
  Only change status when they clearly say so, and only when a lead is selected.
- new_preferences: general rules worth remembering for future leads, phrased as a rule
  ("Skip roles that require French", "Prefer early-stage AI startups"), with effect
  skip | downrank | boost. Only when the note implies a reusable preference. Do not duplicate
  existing preferences.
- reply: one or two short sentences telling the candidate what you saved or learned.
Never invent facts about the company.

EXISTING PREFERENCES:
{preferences}"""

# How the candidate wants to be pitched. Edit this to change every new draft.
# Based on what startup founders and forward-deployed-engineering (FDE) teams screen for:
# ownership, shipping to real users, measurable impact, working directly with
# non-technical stakeholders, and proof of work.
OUTREACH_FOCUS = """\
CORE STORY (always lead with this):
At Upside Robotics (SWE intern, Jan-Aug 2026), Aarav built a production operations dashboard
on his own, end to end: the Next.js/React frontend and the FastAPI backend on AWS ECS with RDS
PostgreSQL, Redis caching and Redshift. 35+ employees and executive stakeholders use it, and it
cut operational metric retrieval from weeks to minutes. He gathered the requirements himself,
working directly with the operations team and executives to decide what to build, then
shipped it. Say "I built and own(ed) it end to end" or "I built it solo, from gathering
requirements with ops and leadership to AWS deployment"; describe it as shipped and used by
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
  sitting with non-technical stakeholders (ops staff and executives at Upside) to turn a messy
  business need into requirements, then shipping a tool they rely on; full-stack Python +
  TypeScript; and AI in production.
- big companies: name the posting, then the core story and one proof point mapped to the team.

RULES: Never cite endpoint or module counts. CIBC only as brief AI/banking proof or for a CIBC or
banking role. Sole ownership and stakeholder requirements work apply only to the Upside
dashboard. Do not claim external customer interviews or anything not stated here or in the
resume.
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

ANSWER_INSTRUCTIONS = (
    """\
You prepare answers to a job application's questions for a University of Waterloo student
applying to a Winter 2027 (January-April, 4-month) software-engineering internship. Use only
facts from the resume and the focus notes; map them to the requirements in the posting text.
For each question index, return:
- answer: for long-text questions, 80-180 words, first person, concrete, leading with the
  impact story from the focus notes and tying it to this role's requirements; for short text,
  a brief direct answer; for single-select, exactly one option text copied verbatim; for
  multi-select, option texts copied verbatim and separated by "; "; for yes/no, "Yes" or "No";
  for dates, the format the question asks for (e.g. MM/DD/YYYY), otherwise YYYY-MM.
- needs_user_input: true when the resume and focus notes do not contain the answer (for
  example a LinkedIn or GitHub URL, or any personal fact), with answer left empty.
- note: at most one short sentence on what the answer draws on, or what the candidate must
  check.
Facts you may use: University of Waterloo, BASc Systems Design Engineering, expected
graduation May 2029; prior internships: CIBC (Aug-Dec 2025) and Upside Robotics (Jan-Aug 2026),
so the last internship was Upside Robotics; portfolio aaravmodi.ca. Never invent anything else.

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


class PreferenceDraft(BaseModel):
    model_config = ConfigDict(extra="forbid")

    rule: str
    effect: PreferenceEffect


class NoteResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lead_note: str | None
    status_change: Literal["none", "skipped", "applied", "contacted"]
    new_preferences: list[PreferenceDraft]
    reply: str


def format_preferences(prefs: list[Preference]) -> str:
    if not prefs:
        return "none yet"
    return "\n".join(f"- [{p.id}] ({p.effect.value}) {p.rule}" for p in prefs)


def _lead_context(lead: Lead) -> str:
    return lead.model_dump_json(
        exclude={
            "status",
            "fit",
            "draft",
            "email",
            "email_status",
            "email_source",
            "sent_at",
            "sent_to",
            "application",
        },
        indent=2,
    )


def assess_fit(
    client: OpenAI, model: str, resume: str, lead: Lead, prefs: list[Preference] | None = None
) -> FitResult:
    instructions = FIT_INSTRUCTIONS.format(preferences=format_preferences(prefs or []))
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": instructions},
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


def interpret_note(
    client: OpenAI, model: str, message: str, lead: Lead | None, prefs: list[Preference]
) -> NoteResult:
    context = _lead_context(lead) if lead else "No lead selected."
    status = lead.status.value if lead else "n/a"
    response = client.responses.parse(
        model=model,
        input=[
            {
                "role": "system",
                "content": NOTE_INSTRUCTIONS.format(preferences=format_preferences(prefs)),
            },
            {
                "role": "user",
                "content": f"SELECTED LEAD (status {status}):\n{context}\n\nNOTE:\n{message}",
            },
        ],
        text_format=NoteResult,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no interpretation")
    return NoteResult.model_validate(response.output_parsed.model_dump())


STATUS_FROM_NOTE = {
    "skipped": LeadStatus.SKIPPED,
    "applied": LeadStatus.APPLIED,
    "contacted": LeadStatus.CONTACTED,
}


class AnswerDraft(BaseModel):
    model_config = ConfigDict(extra="forbid")

    index: int
    answer: str
    needs_user_input: bool
    note: str


class AnswerDrafts(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answers: list[AnswerDraft]


def prepare_answers(
    client: OpenAI, model: str, resume: str, lead: Lead, questions: list[tuple[int, str]]
) -> list[AnswerDraft]:
    """Draft answers for (index, question description) pairs."""
    listing = "\n".join(f"[{i}] {text}" for i, text in questions)
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": ANSWER_INSTRUCTIONS},
            {
                "role": "user",
                "content": f"RESUME:\n{resume}\n\nPOSTING:\n{_lead_context(lead)}"
                f"\n\nQUESTIONS:\n{listing}",
            },
        ],
        text_format=AnswerDrafts,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no answers")
    return AnswerDrafts.model_validate(response.output_parsed.model_dump()).answers
