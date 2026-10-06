import re
from datetime import date, datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

_HANDLE = re.compile(r"^[A-Za-z0-9_]{1,15}$")
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")


class LeadKind(StrEnum):
    FOUNDER = "founder"  # startup that recently raised; cold outreach to a founder
    POSTING = "posting"  # published internship posting; outreach to the hiring manager


class Round(StrEnum):
    PRE_SEED = "pre-seed"
    SEED = "seed"
    SERIES_A = "series-a"
    SERIES_B = "series-b"
    OTHER = "other"


class Segment(StrEnum):
    EARLY = "early"  # pre-seed / seed startup
    MID = "mid"  # Series A-D or growth-stage private startup
    BIG = "big"  # public company, large enterprise, bank, or established private company


class EmailStatus(StrEnum):
    PUBLISHED = "published"  # seen on a public page (source in email_source)
    PATTERN = "pattern"  # unverified guess from the company's email format
    NONE = "none"


class LeadStatus(StrEnum):
    NEW = "new"
    SCORED = "scored"
    DRAFTED = "drafted"
    APPLIED = "applied"
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


class FitResult(BaseModel):
    """Model output for scoring: the fit, the company's segment, and broken preferences."""

    model_config = ConfigDict(extra="forbid")

    fit: FitAssessment
    company_segment: Segment
    violated_preference_ids: list[str]


class PreferenceEffect(StrEnum):
    SKIP = "skip"  # never pursue leads that break this rule
    DOWNRANK = "downrank"  # lower the fit score
    BOOST = "boost"  # raise the fit score


class Preference(BaseModel):
    """A rule learned from the user's notes, e.g. 'Skip roles that require French'."""

    id: str
    rule: str = Field(min_length=3, max_length=200)
    effect: PreferenceEffect
    created_at: datetime
    source_note: str = ""


class Note(BaseModel):
    at: datetime
    text: str = Field(min_length=1, max_length=2000)


class OutreachDraft(BaseModel):
    """A message for the user to review, edit, and send with an explicit click."""

    model_config = ConfigDict(extra="forbid")

    x_dm: str = Field(max_length=1000)
    email_subject: str = Field(max_length=120)
    email_body: str = Field(max_length=3000)
    linkedin_note: str = Field(default="", max_length=300)


class OutreachDraftResult(BaseModel):
    """Model output for drafting (no defaults, as required by structured outputs)."""

    model_config = ConfigDict(extra="forbid")

    x_dm: str = Field(max_length=1000)
    email_subject: str = Field(max_length=120)
    email_body: str = Field(max_length=3000)
    linkedin_note: str = Field(max_length=300)


class QuestionKind(StrEnum):
    TEXT = "text"
    LONG_TEXT = "long_text"
    SINGLE_SELECT = "single_select"
    MULTI_SELECT = "multi_select"
    YES_NO = "yes_no"
    DATE = "date"
    FILE = "file"
    OTHER = "other"


class FormQuestion(BaseModel):
    label: str
    required: bool = False
    kind: QuestionKind = QuestionKind.TEXT
    options: list[str] = Field(default_factory=list)


class PreparedAnswer(BaseModel):
    question: FormQuestion
    answer: str = ""
    needs_user_input: bool = False
    note: str = ""


class ApplicationPrep(BaseModel):
    prepared_at: datetime
    # "form": the board's real questions; "common": typical questions (form not public).
    source: str
    answers: list[PreparedAnswer]


class Lead(BaseModel):
    kind: LeadKind = LeadKind.FOUNDER
    company: str = Field(min_length=1)
    company_url: str | None = None
    what_they_build: str = ""
    location: str = ""
    hiring_signals: list[str] = Field(default_factory=list)
    source_url: str = Field(min_length=1, description="Evidence for the raise or the posting.")

    # Who to contact: the founder, or the hiring manager / recruiter for a posting.
    contact_name: str = ""
    contact_role: str = ""
    x_handle: str | None = None
    linkedin_url: str | None = None
    email: str | None = None
    email_status: EmailStatus = EmailStatus.NONE
    email_source: str = ""

    # Founder leads
    round: Round = Round.OTHER
    amount_usd: int | None = Field(default=None, ge=0)
    announced_on: date | None = None

    # Posting leads
    posting_title: str = ""
    posting_url: str | None = None
    deadline: date | None = None

    segment: Segment | None = None
    status: LeadStatus = LeadStatus.NEW
    fit: FitAssessment | None = None
    draft: OutreachDraft | None = None
    sent_at: datetime | None = None
    sent_to: str | None = None
    notes: list[Note] = Field(default_factory=list)
    application: ApplicationPrep | None = None
    # Posting description fetched for scoring (truncated); empty for founder leads.
    posting_text: str = ""

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

    @field_validator("email")
    @classmethod
    def _validate_email(cls, value: str | None) -> str | None:
        if not value:
            return None
        value = value.strip().lower()
        if not _EMAIL.match(value):
            raise ValueError(f"invalid email: {value!r}")
        return value

    @model_validator(mode="after")
    def _check_kind_fields(self) -> "Lead":
        if self.kind is LeadKind.FOUNDER and self.announced_on is None:
            raise ValueError("founder leads need announced_on")
        if self.kind is LeadKind.POSTING and not self.posting_url:
            raise ValueError("posting leads need posting_url")
        if self.email and self.email_status is EmailStatus.NONE:
            raise ValueError("email_status must say whether the email is published or a pattern")
        return self

    @property
    def key(self) -> str:
        who = self.contact_name or self.posting_title or "team"
        return f"{_slug(self.company)}/{_slug(who)}"

    @property
    def x_url(self) -> str | None:
        return f"https://x.com/{self.x_handle}" if self.x_handle else None


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
