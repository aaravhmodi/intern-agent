import random
from collections import Counter
from datetime import UTC, datetime, timedelta
from pathlib import Path

from internship_agent import workflows
from internship_agent.config import Settings
from internship_agent.leads import patterns
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, LeadStatus
from internship_agent.leads.store import LeadStore

NOW = datetime(2026, 10, 20, 12, tzinfo=UTC)


def founder(sent_to: str | None = None, ago: timedelta = timedelta(days=2), **kw: object) -> Lead:
    data: dict[str, object] = {
        "kind": LeadKind.FOUNDER,
        "company": "Acme",
        "company_url": "https://www.acme.ai/",
        "source_url": "https://www.sec.gov/x/",
        "contact_name": "Jane Doe",
        "announced_on": NOW.date(),
    }
    lead = Lead.model_validate({**data, **kw})
    if sent_to:
        lead.sent_to, lead.sent_at, lead.status = sent_to, NOW - ago, LeadStatus.CONTACTED
    return lead


def test_outcomes_learn_from_bounces_and_settled_sends() -> None:
    leads = [
        founder("jane@acme.ai", followups_stopped="bounced"),
        founder("jane.doe@acme.ai", bounced_emails=["jane@acme.ai"]),
        founder("jdoe@acme.ai", ago=timedelta(hours=2)),  # too early to tell
        founder("j.doe@acme.ai", ago=timedelta(hours=2), followups_stopped="bounced"),
    ]
    counts = patterns.outcomes(leads, NOW)
    assert counts["first"] == [0, 2]
    assert counts["first.last"] == [1, 0]
    assert counts["flast"] == [0, 0]
    assert counts["f.last"] == [0, 0]  # a bounce is not counted before deliveries can be
    # ...but at the company itself it already rules the format out.
    assert patterns.by_domain(leads, NOW)["acme.ai"]["f.last"] is False
    assert patterns.guess_email("Søren Brøkær", "pandektes.com", "first.last") == (
        "soren.brokaer@pandektes.com"
    )


def test_a_bounced_format_is_never_retried_and_the_domain_is_their_own() -> None:
    lead = founder("jane@acme.ai", followups_stopped="bounced", bounced_emails=["jdoe@acme.ai"])
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    rng = random.Random(1)
    for _ in range(200):
        guess = patterns.next_guess(lead, "acme.ai", counts, rng)
        assert guess not in {"jane@acme.ai", "jdoe@acme.ai"}
        assert guess and guess.endswith("@acme.ai")


def test_the_usual_format_is_tried_most_until_it_bounces() -> None:
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    rng = random.Random(2)
    picks = Counter(patterns.next_guess(founder(), "acme.ai", counts, rng) for _ in range(500))
    assert picks.most_common(1)[0][0] == "jane@acme.ai"
    counts["first"] = [5, 60]  # first@ keeps bouncing everywhere
    picks = Counter(patterns.next_guess(founder(), "acme.ai", counts, rng) for _ in range(500))
    assert picks.most_common(1)[0][0] == "jane.doe@acme.ai"


def test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups() -> None:
    lead = founder("jane@acme.ai", followups_stopped="bounced", followups=[NOW])
    assert patterns.wants_email(lead, retries=True) and not patterns.wants_email(lead)
    patterns.point_at(lead, "jane.doe@acme.ai")
    assert lead.bounced_emails == ["jane@acme.ai"]
    assert (lead.sent_at, lead.sent_to, lead.followups, lead.followups_stopped) == (
        None,
        None,
        [],
        "",
    )
    assert (lead.email, lead.email_status) == ("jane.doe@acme.ai", EmailStatus.PATTERN)


def test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company() -> None:
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    known = patterns.by_domain(
        [founder("jane@acme.ai"), founder("x@acme.ai", contact_name="Al Bo"), founder()], NOW
    )
    assert known == {"acme.ai": {"first": True}}  # x@ is no format of Al Bo's name
    sam = founder(contact_name="Sam Lee", contact_role="Senior Software Engineer")
    for seed in range(50):
        assert patterns.next_guess(
            sam, "acme.ai", counts, random.Random(seed), known["acme.ai"]
        ) == ("sam@acme.ai")
    # A format that bounced at the company is not tried for anyone there.
    bounced = {"first": False}
    for seed in range(50):
        guess = patterns.next_guess(sam, "acme.ai", counts, random.Random(seed), bounced)
        assert guess != "sam@acme.ai"
    assert not patterns.proven(bounced) and patterns.proven(known["acme.ai"])


def test_a_recruiter_waits_until_the_ceos_email_shows_the_format(tmp_path: Path) -> None:
    beta = {"company": "Beta", "company_url": "https://beta.io"}
    LeadStore(tmp_path / "leads.json").save(
        [
            founder("jane@acme.ai", ago=NOW - datetime.now(UTC) + timedelta(days=2)),
            founder(contact_name="Sam Lee", contact_role="Technical Recruiter"),
            founder(contact_name="Bo Chen", **beta),
            founder(contact_name="Di Wu", contact_role="Senior Software Engineer", **beta),
        ]
    )
    picked = workflows.guess_and_send(Settings(_env_file=None, data_dir=tmp_path), 10)
    # Acme's format is proven, so its recruiter goes; Beta's engineer waits for its CEO's.
    assert [lead.contact_name for lead, _ in picked] == ["Sam Lee", "Bo Chen"]
    assert picked[0][1] == "sam@acme.ai" and picked[1][1].endswith("@beta.io")


def test_roles_pick_the_email() -> None:
    def role(title: str) -> str:
        return patterns.role_of(founder(contact_role=title))

    assert role("Technical Recruiter") == role("Head of Talent") == "recruiter"
    assert role("Senior Software Engineer") == role("Staff Engineer") == "engineer"
    assert role("Chief Executive Officer") == role("CTO") == role("VP of Engineering") == "founder"
    assert role("Founding Engineer") == "founder"
    assert role("Member of Technical Staff") == "engineer"


def test_a_published_address_is_used_as_is() -> None:
    lead = founder(email="jd@acme.ai", email_status=EmailStatus.PUBLISHED)
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    assert patterns.next_guess(lead, "acme.ai", counts, random.Random(0)) == "jd@acme.ai"
    social = founder()
    social.company_url = "https://linkedin.com/company/acme"
    assert patterns.domain_of(social) is None


def test_the_sent_note_says_when_and_from_where_in_toronto_time() -> None:
    settings = Settings(_env_file=None)
    at = datetime(2026, 10, 21, 0, 3, tzinfo=UTC)  # 8:03 PM the evening before, in Toronto
    note = workflows.sent_note(settings, "paul@nodal.io", "itsaaravmodi@gmail.com", at)
    assert note.text == "Emailed paul@nodal.io from itsaaravmodi@gmail.com on Oct 20 at 8:03 PM."
    assert note.at == at
    assert (
        workflows.sent_note(settings, "a@b.co", None, at).text
        == "Emailed a@b.co on Oct 20 at 8:03 PM."
    )


def test_three_guesses_and_then_only_the_company_inbox() -> None:
    lead = founder("jdoe@acme.ai", followups_stopped="bounced")
    lead.bounced_emails = ["jane@acme.ai", "jane.doe@acme.ai"]
    assert not patterns.wants_email(lead, retries=True)  # three misses: no more guessing
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    assert patterns.next_guess(lead, "acme.ai", counts, random.Random(0)) is None
    lead.company_email = "careers@acme.ai"
    assert patterns.next_guess(lead, "acme.ai", counts, random.Random(0)) == "careers@acme.ai"
