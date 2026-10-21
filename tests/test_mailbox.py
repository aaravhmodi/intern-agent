from datetime import UTC, datetime

from internship_agent.mailbox import bounce_search, reply_search

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
