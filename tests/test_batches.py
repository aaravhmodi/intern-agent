from internship_agent.batches import batches
from internship_agent.leads.schemas import Lead, LeadStatus


def lead(name: str, sent_to: str, **more: object) -> Lead:
    data = {
        "company": name,
        "contact_name": "Jane Doe",
        "source_url": "https://example.com/raise",
        "announced_on": "2026-10-01",
        "status": LeadStatus.CONTACTED,
        "sent_at": "2026-10-20T20:00:00Z",
        "sent_to": sent_to,
    }
    return Lead.model_validate({**data, **more})


def test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies() -> None:
    leads = [
        lead("Acme", "jane@acme.ai", replied_at="2026-10-21T10:00:00Z"),
        lead("Beta", "jane.doe@beta.io", bounced_emails=["jane@beta.io"]),
        lead("Gamma", "jane@gamma.co", followups_stopped="bounced"),
    ]
    log = [
        {"at": "2026-10-20T20:00:00+00:00", "key": "acme/jane-doe", "to": "jane@acme.ai"},
        {"at": "2026-10-20T20:01:00+00:00", "key": "beta/jane-doe", "to": "jane@beta.io"},
        {"at": "2026-10-20T20:02:00+00:00", "key": "gamma/jane-doe", "to": "jane@gamma.co"},
        {"at": "2026-10-20T20:03:00+00:00", "key": "acme/jane-doe", "to": "x", "followup": 1},
        # An hour later: a new batch, the retry at Beta, still waiting.
        {
            "at": "2026-10-20T21:05:00+00:00",
            "key": "beta/jane-doe",
            "to": "jane.doe@beta.io",
            "from": "backup@gmail.com",
        },
    ]
    newest, first = batches(leads, log)
    assert first == {
        "started": "2026-10-20T20:00:00+00:00",
        "from": None,
        "sent": 3,
        "bounced": 2,
        "replied": 1,
        "waiting": 0,
    }
    assert (newest["sent"], newest["waiting"], newest["from"]) == (1, 1, "backup@gmail.com")
