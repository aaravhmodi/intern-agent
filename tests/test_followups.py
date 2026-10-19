import json
from datetime import UTC, datetime, timedelta
from email.message import EmailMessage
from pathlib import Path
from typing import Any

import pytest
from fastapi.testclient import TestClient

from internship_agent import mailer
from internship_agent.config import Settings
from internship_agent.followup_run import run_followups
from internship_agent.leads.followups import (
    TEMPLATES,
    company_domain,
    followup_body,
    is_due,
    reply_subject,
)
from internship_agent.leads.schemas import Lead, LeadStatus
from internship_agent.leads.store import LeadStore
from internship_agent.mailbox import SentMessage

SENT = datetime(2026, 10, 6, 14, 0, tzinfo=UTC)
NOW = SENT + timedelta(days=6)


def emailed(company: str = "Blueprint", contact: str = "Pranav Seelam", **more: Any) -> Lead:
    data: dict[str, Any] = {
        "company": company,
        "contact_name": contact,
        "source_url": "https://example.com/raise",
        "announced_on": "2026-09-01",
        "status": LeadStatus.CONTACTED,
        "sent_at": SENT,
        "sent_to": f"{contact.split()[0].lower()}@{company.lower()}.io",
    }
    return Lead.model_validate({**data, **more})


class FakeMailbox:
    """What the inbox holds: who wrote back, whose address bounced, what was sent."""

    def __init__(self, replied: dict[str, datetime] | None = None, bounced: set[str] | None = None):
        self.replied = replied or {}
        self.gone = bounced or set()

    def heard_from(self, address: str, since: datetime) -> datetime | None:
        return self.replied.get(address)

    def bounced(self, address: str, since: datetime) -> bool:
        return address in self.gone

    def first_email(self, address: str, since: datetime) -> SentMessage | None:
        return SentMessage(
            message_id="<first@mail.gmail.com>", subject="Blueprint — Winter 2027 SWE internship?"
        )


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    return Settings(
        _env_file=None,
        data_dir=tmp_path,
        gmail_address="me@gmail.com",
        gmail_app_password="app-password",
        followups_enabled=True,
    )


@pytest.fixture
def outbox(monkeypatch: pytest.MonkeyPatch) -> list[EmailMessage]:
    sent: list[EmailMessage] = []
    monkeypatch.setattr(mailer, "send", lambda message, sender, password: sent.append(message))
    return sent


def save(settings: Settings, *leads: Lead) -> LeadStore:
    store = LeadStore(settings.data_dir / "leads.json")
    store.save(list(leads))
    return store


def test_a_follow_up_is_due_five_days_after_the_last_email() -> None:
    lead = emailed()

    assert not is_due(lead, SENT + timedelta(days=4, hours=23), 5)
    assert is_due(lead, SENT + timedelta(days=5), 5)
    # The second waits five days from the first follow-up, not from the first email.
    lead.followups = [SENT + timedelta(days=5)]
    assert not is_due(lead, SENT + timedelta(days=9), 5)
    assert is_due(lead, SENT + timedelta(days=10), 5)


def test_nobody_gets_a_third_or_one_after_replying_or_being_skipped() -> None:
    twice = emailed(followups=[SENT + timedelta(days=5), SENT + timedelta(days=10)])
    assert len(TEMPLATES) == 2 and not is_due(twice, SENT + timedelta(days=60), 5)
    assert not is_due(emailed(replied_at=SENT + timedelta(days=1)), NOW, 5)
    assert not is_due(emailed(followups_stopped="bounced"), NOW, 5)
    assert not is_due(emailed(status=LeadStatus.SKIPPED), NOW, 5)
    never_emailed = emailed(sent_at=None, sent_to=None, status=LeadStatus.DRAFTED)
    assert not is_due(never_emailed, NOW, 5)


def test_the_follow_up_names_them_the_company_and_the_first_email() -> None:
    first = followup_body(emailed())
    assert first.startswith("Hi Pranav,\n\nFollowing up again")
    assert "internship at Blueprint" in first and first.endswith("Aarav")

    last = followup_body(emailed(followups=[SENT + timedelta(days=5)]))
    assert last.startswith("Hi Pranav,\n\nFollowing up again") and "Blueprint" in last


def test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company() -> None:
    assert reply_subject("Winter 2027 internship?") == "Re: Winter 2027 internship?"
    assert reply_subject("RE: hello") == "RE: hello"
    assert company_domain("pranav@blueprint.io") == "blueprint.io"
    assert company_domain("founder@gmail.com") is None


def test_a_due_follow_up_is_sent_as_a_reply_and_recorded(
    settings: Settings, outbox: list[EmailMessage]
) -> None:
    store = save(settings, emailed())

    report = run_followups(settings, FakeMailbox(), now=NOW)

    assert [(item.company, item.number) for item in report.sent] == [("Blueprint", 1)]
    (message,) = outbox
    assert message["To"] == "pranav@blueprint.io"
    assert message["Subject"] == "Re: Blueprint — Winter 2027 SWE internship?"
    # In the same thread as the first email.
    assert message["In-Reply-To"] == "<first@mail.gmail.com>"
    assert message.get_content().startswith("Hi Pranav,")
    lead = store.load()[0]
    assert lead.followups == [NOW]
    assert lead.notes[-1].text == "Automatic follow-up 1 of 2 sent to pranav@blueprint.io."
    logged = json.loads((settings.data_dir / "sent-log.jsonl").read_text().splitlines()[-1])
    assert (logged["key"], logged["followup"]) == ("blueprint/pranav-seelam", 1)


def test_someone_who_wrote_back_gets_nothing(
    settings: Settings, outbox: list[EmailMessage]
) -> None:
    store = save(settings, emailed())
    wrote = SENT + timedelta(days=2)

    report = run_followups(settings, FakeMailbox({"pranav@blueprint.io": wrote}), now=NOW)

    assert outbox == [] and report.sent == []
    assert report.replied == ["Pranav Seelam at Blueprint"]
    lead = store.load()[0]
    assert lead.replied_at == wrote and "wrote back on October 8" in lead.notes[-1].text
    # And never again, even long after.
    assert run_followups(settings, FakeMailbox(), now=NOW + timedelta(days=30)).sent == []


def test_a_bounced_address_gets_nothing(settings: Settings, outbox: list[EmailMessage]) -> None:
    store = save(settings, emailed())

    report = run_followups(settings, FakeMailbox(bounced={"pranav@blueprint.io"}), now=NOW)

    assert outbox == [] and report.bounced == ["Pranav Seelam at Blueprint"]
    assert store.load()[0].followups_stopped == "bounced"


def test_a_dry_run_shows_what_would_go_and_changes_nothing(
    settings: Settings, outbox: list[EmailMessage]
) -> None:
    store = save(settings, emailed(), emailed("Zip", "Vibhav Kotriwala"))
    before = store.load()

    report = run_followups(
        settings, FakeMailbox({"vibhav@zip.io": SENT + timedelta(days=1)}), now=NOW, dry_run=True
    )

    assert outbox == []
    assert [item.to for item in report.sent] == ["pranav@blueprint.io"]
    assert report.replied == ["Vibhav Kotriwala at Zip"]
    assert store.load() == before
    assert not (settings.data_dir / "sent-log.jsonl").exists()


def test_two_follow_ups_five_days_apart_then_it_stops(
    settings: Settings, outbox: list[EmailMessage]
) -> None:
    save(settings, emailed())
    quiet = FakeMailbox()

    for day in range(5, 40):
        run_followups(settings, quiet, now=SENT + timedelta(days=day))

    assert [message.get_content().split("\n")[2][:22] for message in outbox] == [
        "Following up again on ",
        "Following up again on ",
    ]
    final = run_followups(settings, quiet, now=SENT + timedelta(days=40))
    assert final.sent == [] and final.finished == 1


def test_only_so_many_go_out_in_one_run(settings: Settings, outbox: list[EmailMessage]) -> None:
    settings.followup_daily_limit = 2
    save(settings, *(emailed(f"Company{n}", f"Person{n} Name") for n in range(5)))

    report = run_followups(settings, FakeMailbox(), now=NOW)

    assert len(outbox) == 2 and len(report.sent) == 2 and report.held == 3


def test_a_refused_send_stops_the_run_without_recording_it(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    store = save(settings, emailed(), emailed("Zip", "Vibhav Kotriwala"))

    def refuse(message: EmailMessage, sender: str, password: str) -> None:
        raise mailer.MailError("Gmail rejected the login. Check GMAIL_APP_PASSWORD in .env.")

    monkeypatch.setattr(mailer, "send", refuse)

    report = run_followups(settings, FakeMailbox(), now=NOW)

    assert report.sent == [] and report.error.startswith("Gmail rejected the login")
    assert all(lead.followups == [] for lead in store.load())


def test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, outbox: list[EmailMessage]
) -> None:
    from internship_agent.dashboard import app as dashboard

    class OpenMailbox(FakeMailbox):
        def __enter__(self) -> "OpenMailbox":
            return self

        def __exit__(self, *error: object) -> None:
            return None

    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("GMAIL_ADDRESS", "me@gmail.com")
    monkeypatch.setenv("GMAIL_APP_PASSWORD", "app-password")
    monkeypatch.setattr(dashboard, "GmailMailbox", lambda address, password: OpenMailbox())
    LeadStore(tmp_path / "leads.json").save(
        [emailed(sent_at=datetime.now(UTC) - timedelta(days=6))]
    )
    client = TestClient(dashboard.app)

    monkeypatch.setenv("FOLLOWUPS_ENABLED", "false")
    off = client.post("/api/followups/run", json={"dry_run": False}).json()
    assert (off["enabled"], off["dry_run"], len(off["sent"])) == (False, True, 1)
    assert outbox == []

    monkeypatch.setenv("FOLLOWUPS_ENABLED", "true")
    on = client.post("/api/followups/run", json={"dry_run": False}).json()
    assert (on["enabled"], on["dry_run"], len(on["sent"])) == (True, False, 1)
    assert len(outbox) == 1


def test_an_email_sent_to_another_companys_address_is_not_followed_up(
    settings: Settings, outbox: list[EmailMessage]
) -> None:
    # Keenable's email had gone to Veeda's contact address.
    veeda = emailed(
        "Veeda", "Sanja Fidler", company_url="https://veeda.io", sent_to="contact@veeda.io"
    )
    keenable = emailed(
        "Keenable", "Matthias Petri", company_url="https://keenable.ai/", sent_to="contact@veeda.io"
    )
    store = save(settings, veeda, keenable)

    report = run_followups(settings, FakeMailbox(), now=NOW)

    assert [item.company for item in report.sent] == ["Veeda"] and len(outbox) == 1
    assert report.wrong_address == ["Matthias Petri at Keenable (sent to contact@veeda.io)"]
    assert store.get(keenable.key).followups_stopped == "wrong address"
