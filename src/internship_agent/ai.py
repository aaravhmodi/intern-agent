"""OpenAI calls. All output is parsed into Pydantic models before use."""

from openai import OpenAI

from internship_agent.leads.schemas import FitAssessment, Lead, OutreachDraft

FIT_INSTRUCTIONS = """\
You assess whether a company is a good fit for a Winter 2027 (January-April)
software-engineering intern, given the candidate's resume. The lead is either a startup that
recently raised (kind=founder) or a published internship posting (kind=posting). Be honest and
specific: cite concrete resume evidence and concrete facts about the company or posting.
Penalize weak overlap with the candidate's skills, roles that clearly need senior engineers or
a different season, and missing information. Never invent facts that are not in the input.
Score 0-100; verdict strong >= 75, possible 50-74, weak < 50."""

DRAFT_INSTRUCTIONS = """\
Write a short, genuine cold outreach from a University of Waterloo student about a Winter 2027
(Jan-Apr) software-engineering internship, addressed to contact_name (use "Hi <first name>,"
or "Hi there," if no name). For kind=founder, ask whether they would take an intern and
reference one specific thing about what the company builds or its recent raise. For
kind=posting, mention the posting_title, say the student has applied or is applying, and ask a
brief question about the team. Use one or two concrete, relevant resume items. No flattery, no
buzzwords, no fabricated details. The X DM must be under 600 characters (write it even if
there is no X handle). The email must be under 150 words and end with a clear, low-effort ask.
Sign off as Aarav."""


def _lead_context(lead: Lead) -> str:
    return lead.model_dump_json(
        exclude={"status", "fit", "draft", "email", "email_status", "email_source"}, indent=2
    )


def assess_fit(client: OpenAI, model: str, resume: str, lead: Lead) -> FitAssessment:
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": FIT_INSTRUCTIONS},
            {"role": "user", "content": f"RESUME:\n{resume}\n\nLEAD:\n{_lead_context(lead)}"},
        ],
        text_format=FitAssessment,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no fit assessment")
    return FitAssessment.model_validate(response.output_parsed.model_dump())


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
        text_format=OutreachDraft,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no draft")
    return OutreachDraft.model_validate(response.output_parsed.model_dump())
