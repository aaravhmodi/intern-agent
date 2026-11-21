"""Seed a throwaway data/ folder with made-up leads, inbox events and events for demo videos.

Every company, person and address here is invented; addresses use the reserved .example
domain so nothing can ever be emailed.
"""

import json
import random
import sys
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from internship_agent.leads.schemas import (
    EmailStatus,
    FitAssessment,
    Lead,
    LeadKind,
    LeadStatus,
    OutreachDraft,
    Region,
    Round,
    Segment,
    Verdict,
)
from internship_agent.opportunities.schemas import Opportunity, OpportunityKind, OpportunityStatus
from internship_agent.pipeline import InboxEvent

OUT = Path(sys.argv[1])
TODAY = date(2026, 11, 20)
NOW = datetime(2026, 11, 20, 15, 0, tzinfo=UTC)
random.seed(7)

STARTUPS = [
    (
        "Lumenforge",
        "GPU scheduling for AI training clusters",
        "Toronto, ON",
        Round.SEED,
        4_000_000,
        "Priya Natarajan",
        "CEO",
        Region.CANADA,
    ),
    (
        "Quillpath",
        "Compliance copilots for fintech teams",
        "New York, NY",
        Round.SERIES_A,
        18_000_000,
        "Daniel Okafor",
        "CTO",
        Region.USA,
    ),
    (
        "Brightkeel",
        "Realtime data pipelines for logistics",
        "Waterloo, ON",
        Round.PRE_SEED,
        1_500_000,
        "Maya Lindqvist",
        "Founder",
        Region.CANADA,
    ),
    (
        "Ferrolabs",
        "Vector search for scientific papers",
        "Berlin, Germany",
        Round.SEED,
        6_200_000,
        "Jonas Weber",
        "CEO",
        Region.EUROPE,
    ),
    (
        "Tidewell",
        "Backend infra for climate sensor networks",
        "San Francisco, CA",
        Round.SERIES_A,
        22_000_000,
        "Ana Ruiz",
        "CTO",
        Region.USA,
    ),
    (
        "Northpine AI",
        "Agents that reconcile invoices",
        "Toronto, ON",
        Round.SEED,
        3_100_000,
        "Chris Tan",
        "CEO",
        Region.CANADA,
    ),
    (
        "Orbitly",
        "Edge observability for IoT fleets",
        "London, UK",
        Round.SERIES_B,
        41_000_000,
        "Hannah Cole",
        "VP Engineering",
        Region.EUROPE,
    ),
    (
        "Saltmarsh",
        "Open-source feature store",
        "Austin, TX",
        Round.SEED,
        5_000_000,
        "Leo Martins",
        "Founder",
        Region.USA,
    ),
    (
        "Cindervale",
        "LLM evals for healthcare",
        "Montreal, QC",
        Round.PRE_SEED,
        900_000,
        "Sofia Haddad",
        "CEO",
        Region.CANADA,
    ),
    (
        "Gridline",
        "Postgres-native job queues",
        "New York, NY",
        Round.SEED,
        7_500_000,
        "Marcus Bell",
        "CTO",
        Region.USA,
    ),
    (
        "Halcyon Robotics",
        "Warehouse robot fleet software",
        "Amsterdam, Netherlands",
        Round.SERIES_A,
        16_000_000,
        "Eva de Vries",
        "CEO",
        Region.EUROPE,
    ),
    (
        "Pebblestack",
        "Developer portals from OpenAPI specs",
        "Vancouver, BC",
        Round.SEED,
        2_800_000,
        "Ryan Cho",
        "Founder",
        Region.CANADA,
    ),
    (
        "Wavecrest",
        "Streaming SQL for product analytics",
        "San Francisco, CA",
        Round.SERIES_A,
        25_000_000,
        "Nina Patel",
        "CTO",
        Region.USA,
    ),
    (
        "Kestrel Health",
        "Scheduling infra for clinics",
        "Toronto, ON",
        Round.SEED,
        4_400_000,
        "Omar Siddiqui",
        "CEO",
        Region.CANADA,
    ),
    (
        "Mossbridge",
        "Policy-as-code for data access",
        "Dublin, Ireland",
        Round.SEED,
        3_900_000,
        "Aoife Byrne",
        "CEO",
        Region.EUROPE,
    ),
    (
        "Ravenlight",
        "Fraud signals for marketplaces",
        "Chicago, IL",
        Round.SERIES_A,
        14_000_000,
        "Tom Becker",
        "CTO",
        Region.USA,
    ),
]
POSTINGS = [
    ("Arcadia Cloud", "Software Engineering Intern, Winter 2027", "Seattle, WA"),
    ("Bluefin Systems", "Backend Developer Co-op (Jan–Apr 2027)", "Toronto, ON"),
    ("Corvid Data", "Data Infrastructure Intern, Winter 2027", "New York, NY"),
    ("Driftwood Labs", "Platform Engineering Co-op", "Waterloo, ON"),
    ("Embergate", "Software Engineer Intern (Winter)", "San Francisco, CA"),
    ("Foxglove Finance", "Engineering Intern, Payments", "London, UK"),
]


def slug(name: str) -> str:
    return "".join(c for c in name.lower() if c.isalnum())


def fit(score: int, company: str) -> FitAssessment:
    verdict = Verdict.STRONG if score >= 80 else Verdict.POSSIBLE if score >= 60 else Verdict.WEAK
    return FitAssessment(
        score=score,
        verdict=verdict,
        reasons=[
            "Backend and data pipeline work matches their stack",
            f"Built agent tooling close to what {company} ships",
            "Winter 2027 term lines up with their hiring",
        ],
        concerns=["Small team, may not have a formal intern program"],
        talking_points=[
            "Postgres-backed agent that runs on a schedule",
            "FastAPI dashboard with live inbox tracking",
        ],
    )


def draft(first: str, company: str) -> OutreachDraft:
    return OutreachDraft(
        x_dm=(
            f"Hi {first}, congrats on the round! I'm a Waterloo CS student looking for a"
            " Winter 2027 internship."
        ),
        email_subject=f"Winter 2027 software engineering internship at {company}",
        email_body=(
            f"Hi {first},\n\nCongrats on the recent raise. I'm a computer science student"
            " looking for a "
            f"Winter 2027 (Jan–Apr) software engineering internship, and {company}'s work lines up "
            "with what I've been building: backend services, data pipelines and agents that run on "
            "a schedule.\n\nWould you have 15 minutes next week to talk?\n\nAarav"
        ),
        linkedin_note=f"Hi {first}, congrats on the raise at {company}! Would love to connect.",
    )


leads: list[Lead] = []
events: list[InboxEvent] = []
outcomes = [
    "replied",
    "interview",
    "waiting",
    "waiting",
    "bounced",
    "replied",
    "assessment",
    "waiting",
    "offer",
    "waiting",
    "rejected",
    "replied",
    "waiting",
    "interview",
    "waiting",
    "waiting",
]
for i, (company, build, loc, rnd, amount, name, role, region) in enumerate(STARTUPS):
    first = name.split()[0]
    domain = f"{slug(company)}.example"
    sent = NOW - timedelta(days=random.randint(2, 18), hours=random.randint(0, 8))
    outcome = outcomes[i]
    segment = Segment.EARLY if rnd in (Round.PRE_SEED, Round.SEED) else Segment.MID
    lead = Lead(
        kind=LeadKind.FOUNDER,
        company=company,
        company_url=f"https://{domain}",
        what_they_build=build,
        location=loc,
        source_url=f"https://news.example/{slug(company)}-raises",
        contact_name=name,
        contact_role=role,
        email=f"{first.lower()}@{domain}",
        email_status=EmailStatus.PATTERN,
        round=rnd,
        amount_usd=amount,
        announced_on=TODAY - timedelta(days=random.randint(5, 55)),
        segment=segment,
        region=region,
        status=LeadStatus.CONTACTED,
        fit=fit(random.randint(62, 94), company),
        draft=draft(first, company),
        sent_at=sent,
        sent_to=f"{first.lower()}@{domain}",
        sent_from="outreach@aarav.example",
    )
    if outcome == "waiting" and (NOW - sent).days >= 5:
        lead.followups = [sent + timedelta(days=5)]
    if outcome == "bounced":
        lead.bounced_emails = [f"{first.lower()}@{domain}"]
        lead.followups_stopped = "bounced"
    if outcome in ("replied", "interview", "assessment", "offer", "rejected"):
        lead.replied_at = sent + timedelta(days=random.randint(1, 4), hours=3)
    leads.append(lead)
    stages = {
        "replied": ["reply"],
        "interview": ["reply", "interview"],
        "assessment": ["reply", "assessment"],
        "offer": ["reply", "interview", "offer"],
        "rejected": ["reply", "rejected"],
        "bounced": ["bounced"],
    }
    subjects = {
        "reply": f"Re: Winter 2027 software engineering internship at {company}",
        "interview": f"Interview invite: {company} engineering chat",
        "assessment": f"{company} take-home challenge",
        "offer": f"Offer: Winter 2027 internship at {company}",
        "rejected": f"Re: Winter 2027 internship at {company}",
        "bounced": "Delivery Status Notification (Failure)",
    }
    snippets = {
        "reply": "Thanks for reaching out! Happy to chat, does Tuesday work?",
        "interview": "We'd love to set up a 45-minute technical conversation with the team.",
        "assessment": "Here's a short take-home, usually about two hours.",
        "offer": "We're excited to offer you a Winter 2027 internship.",
        "rejected": "We don't have an intern role open this winter, but let's stay in touch.",
        "bounced": "Address not found. The email account you tried to reach does not exist.",
    }
    at = lead.replied_at or sent + timedelta(hours=1)
    for n, stage in enumerate(stages.get(outcome, [])):
        bounce = stage == "bounced"
        events.append(
            InboxEvent(
                message_id=f"<demo-{i}-{n}@mail.example>",
                inbox="outreach@aarav.example",
                received_at=at + timedelta(days=2 * n),
                sender="mailer-daemon@mail.example" if bounce else f"{first.lower()}@{domain}",
                sender_name="Mail Delivery Subsystem" if bounce else name,
                subject=subjects[stage],
                stage=stage,  # type: ignore[arg-type]
                company=company,
                lead_key=lead.key,
                snippet=snippets[stage],
            )
        )

for j, (company, title, loc) in enumerate(POSTINGS):
    domain = f"{slug(company)}.example"
    lead = Lead(
        kind=LeadKind.POSTING,
        company=company,
        company_url=f"https://{domain}",
        location=loc,
        source_url=f"https://jobs.example/{slug(company)}",
        posting_title=title,
        posting_url=f"https://boards.example/{slug(company)}/intern",
        posted_on=TODAY - timedelta(days=random.randint(3, 20)),
        deadline=TODAY + timedelta(days=random.randint(4, 30)),
        segment=Segment.BIG,
        status=LeadStatus.APPLIED if j < 4 else LeadStatus.SCORED,
        fit=fit(random.randint(58, 88), company),
    )
    leads.append(lead)
    if j < 4:
        events.append(
            InboxEvent(
                message_id=f"<demo-post-{j}@ats.example>",
                inbox="main@aarav.example",
                received_at=NOW - timedelta(days=random.randint(1, 10)),
                sender="no-reply@greenhouse-mail.io",
                sender_name=f"{company} Recruiting",
                subject=f"Thank you for applying to {company}",
                stage="interview" if j == 0 else "applied",
                company=company,
                lead_key=lead.key,
                snippet="We received your application and our team will review it shortly.",
            )
        )

opportunities = [
    Opportunity(
        kind=OpportunityKind.HACKATHON,
        title="Northern Lights Hack 2027",
        url="https://events.example/northern-lights",
        source="devpost",
        starts_on=date(2027, 1, 16),
        ends_on=date(2027, 1, 18),
        deadline=date(2026, 12, 15),
        deadline_label="Apply by",
        location="Toronto, ON",
        topics=["AI", "infra"],
        status=OpportunityStatus.INTERESTED,
        picked="Sponsored, travel partly paid, fit 84",
    ),
    Opportunity(
        kind=OpportunityKind.HACKATHON,
        title="Data Systems Online Jam",
        url="https://events.example/data-jam",
        source="mlh",
        starts_on=date(2026, 12, 5),
        ends_on=date(2026, 12, 7),
        location="Online",
        online=True,
        topics=["data"],
    ),
    Opportunity(
        kind=OpportunityKind.CONFERENCE,
        title="Backend Summit North",
        url="https://events.example/backend-summit",
        source="confs.tech",
        starts_on=date(2027, 2, 10),
        location="Waterloo, ON",
        topics=["backend"],
    ),
    Opportunity(
        kind=OpportunityKind.NETWORKING,
        title="Startup Demo Night",
        url="https://events.example/demo-night",
        source="web search",
        starts_on=date(2026, 11, 27),
        location="Toronto, ON",
    ),
]

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "leads.json").write_text(
    json.dumps([lead.model_dump(mode="json") for lead in leads], indent=1)
)
(OUT / "pipeline.jsonl").write_text("".join(e.model_dump_json() + "\n" for e in events))
(OUT / "opportunities.json").write_text(
    json.dumps([o.model_dump(mode="json") for o in opportunities], indent=1)
)
print(f"{len(leads)} leads, {len(events)} inbox events, {len(opportunities)} events -> {OUT}")
