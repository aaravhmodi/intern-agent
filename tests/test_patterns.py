import random
from collections import Counter
from datetime import UTC, datetime, timedelta

from internship_agent.leads import patterns
from internship_agent.leads.schemas import EmailStatus, Lead, LeadKind, LeadStatus

NOW = datetime(2026, 10, 20, 12, tzinfo=UTC)


def founder(sent_to: str | None = None, ago: timedelta = timedelta(days=2), **kw: object) -> Lead:
    lead = Lead(
        kind=LeadKind.FOUNDER,
        company="Acme",
        company_url="https://www.acme.ai/",
        source_url="https://www.sec.gov/x/",
        contact_name="Jane Doe",
        announced_on=NOW.date(),
        **kw,  # type: ignore[arg-type]
    )
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
    assert patterns.wants_email(lead)
    patterns.point_at(lead, "jane.doe@acme.ai")
    assert lead.bounced_emails == ["jane@acme.ai"]
    assert (lead.sent_at, lead.sent_to, lead.followups, lead.followups_stopped) == (
        None,
        None,
        [],
        "",
    )
    assert (lead.email, lead.email_status) == ("jane.doe@acme.ai", EmailStatus.PATTERN)


def test_a_published_address_is_used_as_is() -> None:
    lead = founder(email="jd@acme.ai", email_status=EmailStatus.PUBLISHED)
    counts = {fmt: [0, 0] for fmt in patterns.PRIOR}
    assert patterns.next_guess(lead, "acme.ai", counts, random.Random(0)) == "jd@acme.ai"
    social = founder()
    social.company_url = "https://linkedin.com/company/acme"
    assert patterns.domain_of(social) is None
