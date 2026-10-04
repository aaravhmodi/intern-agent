import re
from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator

_HANDLE = re.compile(r"^[A-Za-z0-9_]{1,15}$")


class Round(StrEnum):
    PRE_SEED = "pre-seed"
    SEED = "seed"
    SERIES_A = "series-a"
    SERIES_B = "series-b"
    OTHER = "other"


class LeadStatus(StrEnum):
    NEW = "new"
    SCORED = "scored"
    DRAFTED = "drafted"
    CONTACTED = "contacted"
    SKIPPED = "skipped"


class Verdict(StrEnum):
    STRONG = "strong"
    POSSIBLE = "possible"
    WEAK = "weak"


class FitAssessment(BaseModel):
    """Model output: validated before it is stored."""

    model_config = ConfigDict(extra="forbid")

    score: int = Field(ge=0, le=100)
    verdict: Verdict
    reasons: list[str] = Field(max_length=5)
    concerns: list[str] = Field(max_length=5)
    talking_points: list[str] = Field(max_length=5)


class OutreachDraft(BaseModel):
    """Model output: a message for the user to review and send themselves."""

    model_config = ConfigDict(extra="forbid")

    x_dm: str = Field(max_length=1000)
    email_subject: str = Field(max_length=120)
    email_body: str = Field(max_length=3000)


class FounderLead(BaseModel):
    founder_name: str = Field(min_length=1)
    company: str = Field(min_length=1)
    role: str = "Founder"
    x_handle: str | None = None
    company_url: str | None = None
    round: Round = Round.OTHER
    amount_usd: int | None = Field(default=None, ge=0)
    announced_on: date
    source_url: str = Field(min_length=1, description="Where the raise was announced.")
    what_they_build: str = ""
    location: str = ""
    hiring_signals: list[str] = Field(default_factory=list)
    status: LeadStatus = LeadStatus.NEW
    fit: FitAssessment | None = None
    draft: OutreachDraft | None = None

    @field_validator("x_handle")
    @classmethod
    def _normalize_handle(cls, value: str | None) -> str | None:
        if not value:
            return None
        handle = value.strip()
        for prefix in ("https://x.com/", "https://twitter.com/", "@"):
            handle = handle.removeprefix(prefix)
        handle = handle.strip("/")
        if not _HANDLE.match(handle):
            raise ValueError(f"invalid X handle: {value!r}")
        return handle

    @property
    def key(self) -> str:
        return f"{_slug(self.company)}/{_slug(self.founder_name)}"

    @property
    def x_url(self) -> str | None:
        return f"https://x.com/{self.x_handle}" if self.x_handle else None


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
