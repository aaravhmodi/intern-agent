"""Outreach batches: each run of first emails, with how many bounced, got a reply or wait.

A batch is a run of sends from the send log no more than GAP apart (follow-ups left out).
Each email's fate comes from its lead now: its address bounced, or that address got a reply.
"""

from datetime import datetime, timedelta
from typing import Any

from internship_agent.leads.schemas import Lead

GAP = timedelta(minutes=15)


def batches(leads: list[Lead], sent_log: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Newest first: when it started, the sender, and sent / bounced / replied / waiting."""
    by_key = {lead.key: lead for lead in leads}
    records = sorted(
        (r for r in sent_log if r.get("at") and r.get("to") and not r.get("followup")),
        key=lambda r: r["at"],
    )
    runs: list[list[dict[str, Any]]] = []
    for record in records:
        at = datetime.fromisoformat(record["at"])
        if runs and at - datetime.fromisoformat(runs[-1][-1]["at"]) <= GAP:
            runs[-1].append(record)
        else:
            runs.append([record])
    found = []
    for run in runs:
        bounced = replied = 0
        for record in run:
            lead, to = by_key.get(record.get("key", "")), record["to"].lower()
            if lead is None:
                continue
            current = lead.sent_to == to
            if to in lead.bounced_emails or (current and lead.followups_stopped == "bounced"):
                bounced += 1
            elif current and lead.replied_at is not None:
                replied += 1
        found.append(
            {
                "started": run[0]["at"],
                "from": run[0].get("from"),
                "sent": len(run),
                "bounced": bounced,
                "replied": replied,
                "waiting": len(run) - bounced - replied,
            }
        )
    return found[::-1]
