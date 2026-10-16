# Graph Report - winter-2027-internship-agent  (2026-10-15)

## Corpus Check
- 66 files · ~85,291 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 844 nodes · 2454 edges · 37 communities (30 shown, 7 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 410 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8c6a1b58`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- leads/cli.py
- startups.py
- Segment
- re
- ai.py
- simplify.py
- run_followups
- send_email
- test_followups.py
- Winter 2027 Internship Agent
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- tracking.py
- find-internships.md
- Outlook and browser access is read-only; no automated LinkedIn or X actions
- x_search.py
- local_only
- outlook
- client.py
- startup_jobs.py
- workflows.py
- Lead
- LeadKind
- followups.py
- leads/schemas.py
- outlook/schemas.py
- FakeMailbox
- internship-agent
- Aarav Modi — application context
- AGENTS.md

## God Nodes (most connected - your core abstractions)
1. `Lead` - 92 edges
2. `Settings` - 48 edges
3. `get_settings()` - 38 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 33 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `Segment` - 24 edges
9. `prepare_application()` - 24 edges
10. `daily()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `Segment: early, mid or big` --references--> `Segment`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Posting lead JSON appended to data/leads-inbox.json` --references--> `Lead`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Fit score against the resume (0-100, reasons, talking points)` --references--> `assess_fit()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Search for recently funded startups (last 60 days; Canada, USA, Europe)` --references--> `search_startups()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Application answers prepared from the resume` --references--> `prepare_answers()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (37 total, 7 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.33
Nodes (9): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points), Search for recently funded startups (last 60 days; Canada, USA, Europe) (+1 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.09
Nodes (24): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, daily_cmd(), _draft(), draft_all(), draft_lead() (+16 more)

### Community 2 - "startups.py"
Cohesion: 0.16
Nodes (7): Region, region_from_text(), regions_of(), _fold(), mentions(), names(), source_confirms()

### Community 3 - "Segment"
Cohesion: 0.18
Nodes (13): Round, Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+5 more)

### Community 4 - "re"
Cohesion: 0.06
Nodes (49): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), ApplicationPrep (+41 more)

### Community 5 - "ai.py"
Cohesion: 0.06
Nodes (34): AnswerDraft, AnswerDrafts, CoverLetterDraft, format_preferences(), NoteResult, PeopleFindings, PersonFinding, PreferenceDraft (+26 more)

### Community 6 - "simplify.py"
Cohesion: 0.11
Nodes (10): Big-company postings from the SimplifyJobs off-season list, normalize_url(), cap_per_company(), is_software_role(), matching(), parse(), Posting, _TableParser (+2 more)

### Community 7 - "run_followups"
Cohesion: 0.12
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 8 - "send_email"
Cohesion: 0.15
Nodes (7): check_outreach_text(), build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "Winter 2027 Internship Agent"
Cohesion: 0.25
Nodes (8): Current setup, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does, Winter 2027 Internship Agent

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "app.py"
Cohesion: 0.10
Nodes (37): draft_outreach(), get_settings(), AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups() (+29 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 17 - "find-internships.md"
Cohesion: 0.13
Nodes (9): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+1 more)

### Community 18 - "Outlook and browser access is read-only; no automated LinkedIn or X actions"
Cohesion: 0.33
Nodes (4): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Send email safeguards, Email section with two-click send

### Community 19 - "x_search.py"
Cohesion: 0.15
Nodes (8): StartupFinding, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 22 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "client.py"
Cohesion: 0.12
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 24 - "startup_jobs.py"
Cohesion: 0.15
Nodes (12): _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json() (+4 more)

### Community 25 - "workflows.py"
Cohesion: 0.06
Nodes (37): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Rules learned from notes (skip, downrank, boost), More people to connect with, chosen by company size, assess_fit(), interpret_note(), _lead_context(), prepare_answers() (+29 more)

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (34): _email_line(), render_outreach(), is_workday(), open_postings(), refill(), Lead, OutreachDraft, _identity() (+26 more)

### Community 27 - "LeadKind"
Cohesion: 0.48
Nodes (3): is_open(), rank(), LeadKind

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 30 - "leads/schemas.py"
Cohesion: 0.21
Nodes (5): fit_to_limit(), EmailStatus, Verdict, check_send(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 32 - "outlook/schemas.py"
Cohesion: 0.26
Nodes (9): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient (+1 more)

### Community 40 - "Aarav Modi — application context"
Cohesion: 0.17
Nodes (11): Aarav Modi — application context, Agents and automation projects, CIBC, Enerzen — early-stage startup, Experience highlights, Homelab, How to tailor application materials, Profile (+3 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 249 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/cli.py`, `startups.py`, `Segment`, `re`, `ai.py`, `simplify.py`, `run_followups`, `send_email`, `test_followups.py`, `app.py`, `test_dashboard.py`, `find-internships.md`, `workflows.py`, `LeadKind`, `followups.py`, `leads/schemas.py`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 62 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09178743961352658 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `leads/cli.py`, `re`, `ai.py`, `run_followups`, `send_email`, `test_followups.py`, `internship_agent/cli.py`, `app.py`, `pydantic`, `client.py`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.05640203154236835 - nodes in this community are weakly interconnected._