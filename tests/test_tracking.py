from datetime import UTC, datetime

from internship_agent.outlook.schemas import CalendarEvent, MailMessage
from internship_agent.tracking import (
    Stage,
    application_updates,
    classify_text,
    guess_company,
    interview_events,
)


def message(subject: str, preview: str = "", name: str = "", address: str = "") -> MailMessage:
    return MailMessage.model_validate(
        {
            "id": subject,
            "subject": subject,
            "bodyPreview": preview,
            "from": {"emailAddress": {"name": name, "address": address}},
            "receivedDateTime": datetime(2026, 10, 1, tzinfo=UTC).isoformat(),
        }
    )


def test_classify_text_stages() -> None:
    assert classify_text("Thank you for applying to Stripe") is Stage.APPLIED
    assert classify_text("Your HackerRank online assessment") is Stage.ASSESSMENT
    assert classify_text("Let's schedule your interview") is Stage.INTERVIEW
    assert classify_text("Unfortunately we will not be moving forward") is Stage.REJECTED
    assert classify_text("We are pleased to offer you the role") is Stage.OFFER
    assert classify_text("Weekly newsletter") is Stage.OTHER


def test_rejection_beats_interview_wording() -> None:
    text = "Thank you for interviewing. Unfortunately, we have chosen other candidates."
    assert classify_text(text) is Stage.REJECTED


def test_guess_company_prefers_display_name_then_domain() -> None:
    assert guess_company(message("x", name="Shopify Recruiting")) == "Shopify"
    assert guess_company(message("x", name="", address="jobs@careers.stripe.com")) == "Stripe"
    assert guess_company(message("x", name="Acme", address="no-reply@myworkday.com")) == "Acme"


def test_application_updates_skips_unrelated_mail() -> None:
    updates = application_updates(
        [
            message("Thanks for your application", name="Datadog Careers"),
            message("Lunch on Friday?"),
            message("Winter 2027 intern opportunities", name="Jane Street"),
        ]
    )
    assert [(u.company, u.stage) for u in updates] == [
        ("Datadog", Stage.APPLIED),
        ("Jane Street", Stage.OTHER),
    ]


def test_interview_events() -> None:
    def event(subject: str) -> CalendarEvent:
        slot = {"dateTime": "2026-10-10T15:00:00", "timeZone": "UTC"}
        return CalendarEvent.model_validate(
            {"id": subject, "subject": subject, "start": slot, "end": slot}
        )

    found = interview_events([event("Ramp - Technical Interview"), event("CS 341 lecture")])
    assert [e.subject for e in found] == ["Ramp - Technical Interview"]
