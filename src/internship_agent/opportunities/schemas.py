import re
from datetime import date, datetime
from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, field_validator, model_validator

from internship_agent.leads.store import normalize_url


class OpportunityKind(StrEnum):
    HACKATHON = "hackathon"
    CONFERENCE = "conference"  # tech/industry conference: attend, volunteer or give a talk
    RESEARCH = "research"  # academic venue taking papers, posters or student submissions
    NETWORKING = "networking"  # meetups, mixers, demo nights, career fairs


class OpportunityStatus(StrEnum):
    NEW = "new"
    INTERESTED = "interested"
    REGISTERED = "registered"
    SUBMITTED = "submitted"
    SKIPPED = "skipped"


class SubmissionTrack(BaseModel):
    """Model output: one track of a venue that the candidate could submit to."""

    model_config = ConfigDict(extra="forbid")

    name: str
    deadline: str  # as the call states it, with its timezone; "" if not announced
    format: str  # length, template, archival or not
    eligibility: str
    source_url: str  # the call-for-papers page that states this track


class SubmissionStrategy(BaseModel):
    """Model output: how to get work accepted at (or otherwise into) a venue."""

    model_config = ConfigDict(extra="forbid")

    verdict: Literal["realistic", "stretch", "not this cycle"]
    summary: str
    tracks: list[SubmissionTrack]
    what_to_submit: str
    plan: list[str]
    funding: list[str]
    risks: list[str]


class OpportunityAssessment(BaseModel):
    """Model output: what going would be like for the candidate, from the event's own pages."""

    model_config = ConfigDict(extra="forbid")

    format: Literal["in person", "online", "hybrid", "unknown"]
    location: str  # venue and city as the event states them
    apply_by: date | None  # last day to apply or register, if the pages state one
    travel: Literal["covered", "partial", "none", "unknown"]
    travel_details: str  # what is paid for, caps, how and when to apply
    travel_source_url: str  # the page that states the travel support; "" if none
    cost: str  # ticket or registration price for a student
    effort: Literal["light", "moderate", "heavy"]
    effort_details: str  # hours, prep and what you must produce
    fit_score: int  # 0-100: worth it for this candidate
    fit: list[str]  # how the candidate's skills and projects apply
    highlights: list[str]  # what makes it fun or worth it
    summary: str

    @model_validator(mode="before")
    @classmethod
    def _stored_before_apply_by(cls, data: Any) -> Any:
        # Checks saved before apply_by existed load with none. No default on the field itself:
        # structured outputs need every field required in the schema.
        if isinstance(data, dict):
            data.setdefault("apply_by", None)
        return data


class StepAction(BaseModel):
    """Model output: one thing to do on the page, by the element's number in the snapshot."""

    model_config = ConfigDict(extra="forbid")

    # email_link opens the sign-in link the site just emailed (element is ignored).
    kind: Literal["fill", "select", "check", "uncheck", "click", "upload_resume", "email_link"]
    element: int
    # Text to type or the option to pick; "@bank:<question>" uses a saved personal answer,
    # filled in locally so personal details never reach the model; "@inbox_code" is the
    # sign-in code the site just emailed. "" for clicks and boxes.
    value: str


class BrowserStep(BaseModel):
    """Model output: what this page is and what to do next."""

    model_config = ConfigDict(extra="forbid")

    page: str  # one sentence: what the page shows
    actions: list[StepAction]
    # continue: act and look again. submitted: the page confirms the application or RSVP.
    # needs_you: a sign-in, or a required question the candidate's material doesn't answer.
    # blocked: closed, paid, ineligible, or anything that should not be submitted.
    outcome: Literal["continue", "submitted", "needs_you", "blocked"]
    reason: str


class EventApplication(BaseModel):
    """What happened when the agent applied or RSVPed."""

    status: Literal["submitted", "needs_you", "blocked", "uncertain", "failed", "ready"]
    detail: str
    at: datetime
    steps: list[str] = []  # what it saw and did, page by page, for review
    proof: bool = False  # a screenshot of the confirmation page was saved


class Opportunity(BaseModel):
    kind: OpportunityKind
    title: str
    url: str
    source: str  # devpost, mlh, confs.tech, ccfddl, web search, manual
    starts_on: date | None = None
    ends_on: date | None = None
    deadline: date | None = None
    deadline_label: str = ""  # what closes on `deadline`
    location: str = ""
    online: bool = False
    topics: list[str] = []
    details: str = ""
    rank: str = ""  # research venues: CORE or CCF rank
    status: OpportunityStatus = OpportunityStatus.NEW
    strategy: SubmissionStrategy | None = None
    assessment: OpportunityAssessment | None = None
    application: EventApplication | None = None

    @field_validator("url")
    @classmethod
    def _http(cls, value: str) -> str:
        if not value.startswith(("https://", "http://")):
            raise ValueError(f"not a web URL: {value!r}")
        return value

    @property
    def key(self) -> str:
        return normalize_url(self.url)

    @property
    def identity(self) -> set[str]:
        """The same event listed by two feeds shares its URL or its title and start date."""
        title = re.sub(r"[^a-z0-9]+", "-", self.title.lower()).strip("-")
        return {self.key, f"{title}@{self.starts_on}"}
