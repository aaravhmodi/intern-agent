"""OpenAI calls. All output is parsed into Pydantic models before use."""

from openai import OpenAI

from internship_agent.leads.schemas import FitAssessment, FounderLead, OutreachDraft

FIT_INSTRUCTIONS = """\
You assess whether an early-stage startup is a good fit for a Winter 2027 (January-April)
software-engineering intern, given the candidate's resume. Be honest and specific: cite
concrete resume evidence and concrete facts about the startup. Penalize weak overlap with the
candidate's skills, roles that clearly need senior engineers, and missing information.
Never invent facts that are not in the input. Score 0-100; verdict strong >= 75,
possible 50-74, weak < 50."""

DRAFT_INSTRUCTIONS = """\
Write a short, genuine cold outreach from a University of Waterloo student asking a startup
founder about a Winter 2027 (Jan-Apr) software-engineering internship. Reference one specific
thing about what the company builds or its recent raise, and one or two concrete, relevant
resume items. No flattery, no buzzwords, no fabricated details. The X DM must be under
600 characters. The email must be under 150 words and end with a clear, low-effort ask."""


def _lead_context(lead: FounderLead) -> str:
    return lead.model_dump_json(exclude={"status", "fit", "draft"}, indent=2)


def assess_fit(client: OpenAI, model: str, resume: str, lead: FounderLead) -> FitAssessment:
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": FIT_INSTRUCTIONS},
            {"role": "user", "content": f"RESUME:\n{resume}\n\nSTARTUP:\n{_lead_context(lead)}"},
        ],
        text_format=FitAssessment,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no fit assessment")
    return FitAssessment.model_validate(response.output_parsed.model_dump())


def draft_outreach(client: OpenAI, model: str, resume: str, lead: FounderLead) -> OutreachDraft:
    fit = lead.fit.model_dump_json() if lead.fit else "not assessed"
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": DRAFT_INSTRUCTIONS},
            {
                "role": "user",
                "content": f"RESUME:\n{resume}\n\nSTARTUP:\n{_lead_context(lead)}\n\nFIT:\n{fit}",
            },
        ],
        text_format=OutreachDraft,
    )
    if response.output_parsed is None:
        raise ValueError("Model returned no draft")
    return OutreachDraft.model_validate(response.output_parsed.model_dump())
