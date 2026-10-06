from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

import pytest

from internship_agent.ai import StartupFinding
from internship_agent.leads.schemas import EmailStatus, Lead, Round, Segment
from internship_agent.leads.segments import effective_segment, parse_round
from internship_agent.leads.sending import SendBlocked, check_send
from internship_agent.mailer import MailError, build_message
from internship_agent.sources.startups import mentions, to_leads

TODAY = date(2026, 10, 4)


def lead(**overrides: Any) -> Lead:
    data: dict[str, Any] = {
        "contact_name": "Jane Doe",
        "company": "Acme",
        "announced_on": "2026-09-20",
        "source_url": "https://example.com",
    }
    return Lead.model_validate({**data, **overrides})


def finding(**overrides: Any) -> StartupFinding:
    data: dict[str, Any] = {
        "company": "Acme",
        "founder_name": "Jane Doe",
        "founder_role": "CTO",
        "round": "Seed - $3 million",
        "amount_usd": 3_000_000,
        "announced_on": date(2026, 9, 20),
        "source_url": "https://news.example.com/acme",
        "company_url": None,
        "what_they_build": "Tools.",
        "location": "Toronto",
    }
    return StartupFinding.model_validate({**data, **overrides})


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Pre-seed", Round.PRE_SEED),
        ("pre seed note", Round.PRE_SEED),
        ("Seed - $3 million", Round.SEED),
        ("Series A", Round.SERIES_A),
        ("series c extension", Round.SERIES_B),
        ("Growth equity", Round.OTHER),
    ],
)
def test_parse_round(text: str, expected: Round) -> None:
    assert parse_round(text) is expected


def test_effective_segment() -> None:
    assert effective_segment(lead(round="seed")) is Segment.EARLY
    assert effective_segment(lead(round="series-a")) is Segment.MID
    assert effective_segment(lead(round="series-a", segment="big")) is Segment.BIG
    posting = lead(kind="posting", posting_url="https://a.com/1", announced_on=None)
    assert effective_segment(posting) is None


def test_to_leads_filters_age_stage_and_unverifiable_sources() -> None:
    findings = [
        finding(company="Good"),
        finding(company="Old", announced_on=date(2026, 6, 1)),
        finding(company="Future", announced_on=date(2026, 12, 1)),
        finding(company="Late", round="Series E"),
        finding(company="Mid", round="Series A"),
        finding(company="Fake", source_url="https://news.example.com/404"),
        finding(company="NoFounder", founder_name=" "),
    ]
    leads = to_leads(
        findings, TODAY, 60, [Segment.EARLY], confirm=lambda f: not f.source_url.endswith("404")
    )
    assert [(x.company, x.segment, x.round) for x in leads] == [("Good", Segment.EARLY, Round.SEED)]


def test_check_send_blocks_unconfirmed_guess_and_resends() -> None:
    guessed = lead(email="jane@acme.com", email_status=EmailStatus.PATTERN)
    with pytest.raises(SendBlocked, match="guess"):
        check_send(guessed, "Jane@Acme.com ", confirm_unverified=False, resend=False)
    check_send(guessed, "jane@acme.com", confirm_unverified=True, resend=False)
    # A different address typed by the user is not the guess.
    check_send(guessed, "jane.doe@acme.com", confirm_unverified=False, resend=False)

    sent = lead(sent_at=datetime(2026, 10, 1, tzinfo=UTC), sent_to="jane@acme.com")
    with pytest.raises(SendBlocked, match="Already emailed"):
        check_send(sent, "jane@acme.com", confirm_unverified=True, resend=False)
    check_send(sent, "jane@acme.com", confirm_unverified=True, resend=True)


def test_build_message_with_attachment(tmp_path: Path) -> None:
    pdf = tmp_path / "resume.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")
    message = build_message("me@gmail.com", "jane@acme.com", " Hello ", "Body", pdf)
    assert message["To"] == "jane@acme.com" and message["Subject"] == "Hello"
    attachments = list(message.iter_attachments())
    assert attachments[0].get_filename() == "Aarav_Modi_Resume.pdf"


def test_build_message_requires_fields() -> None:
    with pytest.raises(MailError):
        build_message("me@gmail.com", "", "Hi", "Body")
    with pytest.raises(MailError):
        build_message("me@gmail.com", "a@b.com", "", "Body")


def test_mentions_requires_company_and_founder_ignoring_accents() -> None:
    page = "<p>Montreal-based Axya, led by CEO F&eacute;lix Bélisle, raised...</p>"
    assert mentions(page, finding(company="Axya Inc", founder_name="Felix Belisle"))
    assert not mentions(page, finding(company="Axya", founder_name="Jane Doe"))


def test_fit_to_limit_prefers_sentence_then_word_boundary() -> None:
    from internship_agent.leads.limits import fit_to_limit

    assert fit_to_limit("Short note.", 200) == "Short note."
    two = "I built a production dashboard used by 35+ people. " + "x" * 200
    assert fit_to_limit(two, 200) == "I built a production dashboard used by 35+ people."
    words = "word " * 60
    cut = fit_to_limit(words, 200)
    assert len(cut) <= 200 and cut.endswith("…") and not cut[:-1].endswith(" ")


def test_linkedin_note_never_exceeds_200_chars() -> None:
    from internship_agent.leads.schemas import OutreachDraft

    long_note = (
        "Hi Jane, I built an ops dashboard at Upside Robotics that cut metric retrieval "
        "from weeks to minutes for 35+ people. I'm applying for your Winter 2027 internship "
        "and would love to connect and hear what the team is building next. Thanks, Aarav"
    )
    assert len(long_note) > 200
    draft = OutreachDraft(x_dm="d", email_subject="s", email_body="b", linkedin_note=long_note)
    assert len(draft.linkedin_note) <= 200
