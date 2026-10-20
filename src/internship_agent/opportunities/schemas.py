import re
from datetime import date
from enum import StrEnum
from typing import Literal

from pydantic import BaseModel, ConfigDict, field_validator

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
