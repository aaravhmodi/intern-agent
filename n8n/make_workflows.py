"""Write the internship tracker's n8n workflows into workflows/, one JSON file each.

Load them on the server with:  bash ~/projects/intern-agent/n8n/install.sh
They read INTERN_AGENT_URL, NTFY_SERVER and NTFY_TOPIC from n8n's environment, and Gmail
through the "Gmail (read-only)" IMAP credential that install.sh creates from this app's .env.
"""

import json
import uuid
from pathlib import Path
from typing import Any

OUT = Path(__file__).parent / "workflows"
TZ = "America/Toronto"
GMAIL_CREDENTIAL = {"id": "gmailimapreadonly", "name": "Gmail (read-only)"}
Node = dict[str, Any]


def _id(name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"intern-agent-n8n/{name}"))


# Sorts each new email, matches it to a lead you applied to or contacted, and turns it into
# a push. No AI: plain rules, so it costs nothing. Receipts and unrelated mail are dropped.
MATCH_JS = r"""
const leads = $('Your leads').first().json.leads || [];
const watched = leads.filter((l) => ['applied', 'contacted'].includes(l.status) || l.sent_at);
const page = $env.INTERN_AGENT_URL;

const domainOf = (url) => {
  try { return new URL(url).hostname.replace(/^www\./, '').toLowerCase(); } catch { return ''; }
};
const addressOf = (from) => ((from.match(/<([^>]+)>/) || [, from])[1] || '').trim().toLowerCase();
const nameOf = (from) => from.replace(/<[^>]*>/, '').replace(/"/g, '').trim();
const escape = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const mentions = (text, company) =>
  company.length >= 3 && new RegExp(`\\b${escape(company)}\\b`, 'i').test(text);

// The reply itself, without the quoted thread underneath.
const snippet = (text) => {
  const lines = [];
  for (const line of (text || '').split(/\r?\n/)) {
    if (/^>|^On .+wrote:$|^-{2,}\s*Original Message/i.test(line.trim())) break;
    if (line.trim()) lines.push(line.trim());
  }
  const body = lines.join(' ').replace(/\s+/g, ' ');
  return body.length > 400 ? body.slice(0, 400) + '…' : body;
};

// First match wins. An invite often opens with "thank you for your interest", so the
// interview and rejection rules come before the receipt rule.
const KINDS = [
  { kind: 'next step', priority: 5, tag: 'tada', title: '🎉 Next step from',
    test: new RegExp('interview|schedule (a|some) (time|call|chat)|your availability|' +
      'online assessment|coding (challenge|assessment)|hackerrank|codesignal|take-home|' +
      'phone screen', 'i') },
  { kind: 'rejection', priority: 2, tag: 'envelope', title: 'Update from',
    test: new RegExp('unfortunately|not (be )?(moving|move) forward|other candidates|' +
      'regret to inform|position has been filled|decided to pursue', 'i') },
  { kind: 'receipt', skip: true,
    test: new RegExp('thank(s| you) for (applying|your (application|interest))|' +
      "application (was |has been )?received|we('ve| have) received your", 'i') },
];

const pushes = [];
for (const { json: mail } of $('New email').all()) {
  const from = mail.from || '';
  const address = addressOf(from);
  const domain = address.split('@')[1] || '';
  const subject = mail.subject || '(no subject)';
  const header = `${nameOf(from)} ${subject}`;
  const sameSite = (l) => {
    const site = domainOf(l.company_url);
    return Boolean(site && domain && (domain === site || domain.endsWith(`.${site}`)));
  };
  const lead = watched.find((l) =>
    [l.email, l.sent_to].filter(Boolean).map((e) => e.toLowerCase()).includes(address) ||
    sameSite(l) || mentions(header, l.company));
  if (!lead) continue;

  const text = `${subject}\n${mail.textPlain || ''}`;
  const kind = KINDS.find((k) => k.test.test(text)) ||
    { kind: 'reply', priority: 4, tag: 'incoming_envelope', title: '📬 Reply from' };
  if (kind.skip) continue;

  const role = lead.posting_title ? ` (${lead.posting_title})` : '';
  pushes.push({ json: {
    title: `${kind.title} ${lead.company}`.slice(0, 120),
    message: `${nameOf(from) || address}: "${subject}"\n\n${snippet(mail.textPlain)}\n\n` +
      `You ${lead.status === 'applied' ? 'applied' : 'reached out'}${role}. ` +
      '👉 Reply from Gmail; open the tracker to see the lead.',
    priority: kind.priority, tags: [kind.tag],
    click: `${page}/#/jobs/${encodeURIComponent(lead.key)}`,
  } });
}
return pushes;
"""


def internship_replies() -> dict[str, Any]:
    names = ["New email", "Your leads", "Match to a lead", "Send to phone"]
    nodes: list[Node] = [
        {
            "id": _id(names[0]),
            "name": names[0],
            "type": "n8n-nodes-base.emailReadImap",
            "typeVersion": 2.2,
            "position": [0, 300],
            "credentials": {"imap": GMAIL_CREDENTIAL},
            "parameters": {
                "mailbox": "INBOX",
                # Read-only: never mark anything read or move it.
                "postProcessAction": "nothing",
                "format": "simple",
                "downloadAttachments": False,
                # Every new message by UID, even one you already opened on your phone.
                "options": {"customEmailConfig": '["ALL"]', "trackLastMessageId": True},
            },
        },
        {
            "id": _id(names[1]),
            "name": names[1],
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [220, 300],
            "executeOnce": True,
            "parameters": {
                "method": "GET",
                "url": "={{ $env.INTERN_AGENT_URL }}/api/leads",
                "options": {"timeout": 30000},
            },
        },
        {
            "id": _id(names[2]),
            "name": names[2],
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [440, 300],
            "parameters": {
                "mode": "runOnceForAllItems",
                "language": "javaScript",
                "jsCode": MATCH_JS,
            },
        },
        {
            "id": _id(names[3]),
            "name": names[3],
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [660, 300],
            "parameters": {
                "method": "POST",
                "url": "={{ $env.NTFY_SERVER }}",
                "sendBody": True,
                "contentType": "json",
                "specifyBody": "json",
                "jsonBody": "={{ JSON.stringify({ ...$json, topic: $env.NTFY_TOPIC }) }}",
                "options": {"timeout": 15000},
            },
        },
    ]
    connections = {
        a: {"main": [[{"node": b, "type": "main", "index": 0}]]}
        for a, b in zip(names, names[1:], strict=False)
    }
    return {
        "id": _id("internship replies").replace("-", "")[:16],
        "name": "Internship tracker: replies",
        "active": True,
        "nodes": nodes,
        "connections": connections,
        "pinData": {},
        "meta": {
            "notes": "Watches your Gmail inbox (read-only) and pushes when a company you applied "
            "to or contacted writes back: interviews and next steps are urgent, rejections are "
            "quiet, 'thanks for applying' receipts are skipped."
        },
        "settings": {
            "executionOrder": "v1",
            "timezone": TZ,
            # Every email runs this workflow; don't keep their contents in n8n's history.
            "saveDataSuccessExecution": "none",
            "saveDataErrorExecution": "all",
            "saveManualExecutions": False,
        },
        "tags": [],
    }


# Turns the follow-up run's result into one push: who got one, who replied, what stopped.
FOLLOWUPS_JS = r"""
const run = $input.first().json;
const page = $env.INTERN_AGENT_URL;
if (run.detail) {
  const message = `${run.detail}\n\nNothing was sent. ` +
    '👉 If this repeats tomorrow, ask Claude to look.';
  return [{ json: { title: "⚠️ Follow-ups didn't run", message, priority: 4,
                    tags: ['warning'], click: `${page}/#/jobs` } }];
}
const sent = run.sent || [];
const parts = [];
if (sent.length && !run.dry_run) {
  parts.push(`Sent ${sent.length} follow-up${sent.length === 1 ? '' : 's'}:\n` +
    sent.map((s) => `• ${s.contact || 'the team'} at ${s.company} (${s.number} of 2)`).join('\n'));
}
if ((run.replied || []).length) {
  parts.push(`Wrote back, so no follow-up:\n${run.replied.map((n) => `• ${n}`).join('\n')}`);
}
if ((run.bounced || []).length) {
  parts.push(`Bounced, so stopped:\n${run.bounced.map((n) => `• ${n}`).join('\n')}`);
}
if ((run.wrong_address || []).length) {
  parts.push('Sent to another company\'s address, so stopped (email them properly from the ' +
    `tracker):\n${run.wrong_address.map((n) => `• ${n}`).join('\n')}`);
}
if (run.held) parts.push(`${run.held} more are due and go out tomorrow (daily limit).`);
if (run.error) parts.push(`⚠️ Stopped early: ${run.error}`);
if (!parts.length) return [];  // a quiet day: nobody due, nobody new replied
const title = sent.length && !run.dry_run
  ? `📨 ${sent.length} follow-up${sent.length === 1 ? '' : 's'} sent`
  : '📨 Follow-ups: nothing sent today';
const message = parts.join('\n\n') + `\n\n${run.waiting || 0} still inside their 5 days.`;
return [{ json: { title, message, priority: run.error ? 4 : 3, tags: ['email'], click: `${page}/#/jobs` } }];
"""


def internship_followups() -> dict[str, Any]:
    names = ["Weekdays at 9:30", "Send what's due", "Say what happened", "Send to phone"]
    nodes: list[Node] = [
        {
            "id": _id(names[0]),
            "name": names[0],
            "type": "n8n-nodes-base.scheduleTrigger",
            "typeVersion": 1.2,
            "position": [0, 300],
            "parameters": {
                "rule": {"interval": [{"field": "cronExpression", "expression": "30 9 * * 1-5"}]}
            },
        },
        {
            "id": _id(names[1]),
            "name": names[1],
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [220, 300],
            "parameters": {
                "method": "POST",
                "url": "={{ $env.INTERN_AGENT_URL }}/api/followups/run",
                "sendBody": True,
                "contentType": "json",
                "specifyBody": "json",
                # The tracker only sends when FOLLOWUPS_ENABLED is on; otherwise this is
                # a dry run whatever is asked for here.
                "jsonBody": "={{ JSON.stringify({ dry_run: false }) }}",
                # Checking Gmail for each person takes a while; errors come back as data.
                "options": {"timeout": 600000, "response": {"response": {"neverError": True}}},
            },
        },
        {
            "id": _id(names[2]),
            "name": names[2],
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [440, 300],
            "parameters": {
                "mode": "runOnceForAllItems",
                "language": "javaScript",
                "jsCode": FOLLOWUPS_JS,
            },
        },
        {
            "id": _id(names[3]),
            "name": names[3],
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [660, 300],
            "parameters": {
                "method": "POST",
                "url": "={{ $env.NTFY_SERVER }}",
                "sendBody": True,
                "contentType": "json",
                "specifyBody": "json",
                "jsonBody": "={{ JSON.stringify({ ...$json, topic: $env.NTFY_TOPIC }) }}",
                "options": {"timeout": 15000},
            },
        },
    ]
    connections = {
        a: {"main": [[{"node": b, "type": "main", "index": 0}]]}
        for a, b in zip(names, names[1:], strict=False)
    }


    return {
        "id": _id("internship followups").replace("-", "")[:16],
        "name": "Internship tracker: follow-ups",
        "active": True,
        "nodes": nodes,
        "connections": connections,
        "pinData": {},
        "meta": {
            "notes": "On weekday mornings, asks the tracker to follow up on emails with no "
            "reply after 5 days (twice at most, never after a reply or a bounce), then pushes "
            "who got one and who wrote back. Has no Run-it-now trigger on purpose: it sends "
            "real email."
        },
        "settings": {
            "executionOrder": "v1",
            "timezone": TZ,
            "saveDataSuccessExecution": "all",
            "saveDataErrorExecution": "all",
        },
        "tags": [],
    }


def internship_daily_prep() -> dict[str, Any]:
    """Discover jobs, prepare materials, and submit eligible applications each morning."""
    trigger = "Every morning at 8"
    run = "Find jobs, prepare materials, and submit eligible applications"
    nodes: list[Node] = [
        {
            "id": _id(trigger),
            "name": trigger,
            "type": "n8n-nodes-base.scheduleTrigger",
            "typeVersion": 1.2,
            "position": [0, 300],
            "parameters": {
                "rule": {"interval": [{"field": "cronExpression", "expression": "0 8 * * *"}]}
            },
        },
        {
            "id": _id(run),
            "name": run,
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.2,
            "position": [240, 300],
            "parameters": {
                "method": "POST",
                "url": "={{ $env.INTERN_AGENT_URL }}/api/daily/run",
                "options": {"timeout": 900000},
            },
        },
    ]
    return {
        "id": _id("internship daily preparation").replace("-", "")[:16],
        "name": "Internship tracker: daily applications",
        "active": True,
        "nodes": nodes,
        "connections": {
            trigger: {"main": [[{"node": run, "type": "main", "index": 0}]]}
        },
        "pinData": {},
        "meta": {
            "notes": "Every morning at 8 AM America/Toronto, finds postings, "
            "prepares tailored answers "
            "and cover letters, and submits complete non-Workday Greenhouse, Ashby, and Lever "
            "applications through the saved browser profile. CAPTCHA, unsupported, and "
            "incomplete forms are reported as blocked for manual completion. Pushes counts to ntfy."
        },
        "settings": {
            "executionOrder": "v1",
            "timezone": TZ,
            "saveDataSuccessExecution": "none",
            "saveDataErrorExecution": "all",
        },
        "tags": [],
    }
if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for build, file in (
        (internship_replies, "replies.json"),
        (internship_followups, "followups.json"),
        (internship_daily_prep, "daily-prep.json"),
    ):
        flow = build()
        (OUT / file).write_text(
            json.dumps(flow, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n"
        )
        print(f"{file:<16} {flow['name']}  {len(flow['nodes'])} nodes")
