from datetime import UTC, datetime, timedelta

from internship_agent.mailbox import GmailMailbox, bounce_search, reply_search

SINCE = datetime(2026, 10, 19, 20, tzinfo=UTC)


def test_a_bounce_notice_from_the_company_is_not_a_reply() -> None:
    # Microsoft 365 bounces come from postmaster@ at the company's own domain (OpsMate's
    # was once counted as a reply), so replies leave such senders out.
    search = reply_search("@opsmateai.com", SINCE)
    assert search[:2] == ["FROM", '"@opsmateai.com"'] and search[-2:] == ["SINCE", "19-Oct-2026"]
    for system in ("postmaster", "mailer-daemon", "no-reply", "noreply"):
        assert f'"{system}"' in search and search[search.index(f'"{system}"') - 2] == "NOT"


def test_bounces_from_gmail_and_from_microsoft_365_both_count() -> None:
    assert bounce_search(" Jianjie@OpsMateAI.com", SINCE) == [
        "OR",
        "FROM",
        '"mailer-daemon"',
        "FROM",
        '"postmaster"',
        "SINCE",
        "19-Oct-2026",
        "BODY",
        '"jianjie@opsmateai.com"',
    ]


def test_a_bounce_that_lands_before_sent_at_is_recorded_still_counts() -> None:
    # Remedy Sports: the bounce's INTERNALDATE (whole seconds) fell just before the
    # sent_at recorded once the send returned, so it was missed and a follow-up went out.
    sent_at = datetime(2026, 10, 19, 20, 18, 45, 600000, tzinfo=UTC)
    box = GmailMailbox.__new__(GmailMailbox)
    box._search = lambda *_: [b"1"]  # type: ignore[method-assign]
    box._received = lambda _: [sent_at.replace(microsecond=0)]  # type: ignore[method-assign]
    assert box.bounced("john@remedysports.ai", sent_at)
    box._received = lambda _: [sent_at - timedelta(days=1)]  # type: ignore[method-assign]
    assert not box.bounced("john@remedysports.ai", sent_at)
