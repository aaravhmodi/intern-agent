from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class _GraphModel(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)


class EmailAddress(_GraphModel):
    name: str = ""
    address: str = ""


class Recipient(_GraphModel):
    email_address: EmailAddress = Field(default_factory=EmailAddress, alias="emailAddress")


class MailMessage(_GraphModel):
    id: str
    subject: str = ""
    sender: Recipient | None = Field(default=None, alias="from")
    received_at: datetime | None = Field(default=None, alias="receivedDateTime")
    body_preview: str = Field(default="", alias="bodyPreview")
    web_link: str = Field(default="", alias="webLink")

    @property
    def sender_address(self) -> str:
        return self.sender.email_address.address if self.sender else ""

    @property
    def sender_name(self) -> str:
        return self.sender.email_address.name if self.sender else ""


class DateTimeTimeZone(_GraphModel):
    date_time: str = Field(alias="dateTime")
    time_zone: str = Field(default="UTC", alias="timeZone")


class Location(_GraphModel):
    display_name: str = Field(default="", alias="displayName")


class CalendarEvent(_GraphModel):
    id: str
    subject: str = ""
    start: DateTimeTimeZone
    end: DateTimeTimeZone
    location: Location = Field(default_factory=Location)
    body_preview: str = Field(default="", alias="bodyPreview")
    organizer: Recipient | None = None
    web_link: str = Field(default="", alias="webLink")
    is_online_meeting: bool = Field(default=False, alias="isOnlineMeeting")


class GraphMessagePage(_GraphModel):
    value: list[MailMessage] = Field(default_factory=list)


class GraphEventPage(_GraphModel):
    value: list[CalendarEvent] = Field(default_factory=list)
