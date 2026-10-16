# Graph Report - winter-2027-internship-agent  (2026-10-15)

## Corpus Check
- 66 files · ~85,226 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 842 nodes · 2448 edges · 40 communities (33 shown, 7 thin omitted)
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
- json
- test_notes.py
- find_startups
- run_followups
- send_email
- Settings
- ai.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- get_settings
- test_dashboard.py
- tracking.py
- test_leads.py
- test_people.py
- x_search.py
- followups_cmd
- app.py
- client.py
- OutlookClient
- re
- workflows.py
- Lead
- leads/schemas.py
- followups.py
- test_outlook_client.py
- send
- outlook/schemas.py
- SentMessage
- internship-agent
- Aarav Modi — application context
- AGENTS.md
- test_x_search.py

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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (40 total, 7 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.10
Nodes (30): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+22 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.10
Nodes (24): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, daily_cmd(), _draft(), draft_all(), draft_lead() (+16 more)

### Community 2 - "startups.py"
Cohesion: 0.14
Nodes (9): Region, region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), _fold(), mentions() (+1 more)

### Community 3 - "Segment"
Cohesion: 0.16
Nodes (14): Round, Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+6 more)

### Community 4 - "json"
Cohesion: 0.07
Nodes (36): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+28 more)

### Community 5 - "test_notes.py"
Cohesion: 0.13
Nodes (16): apply_violations(), _normalize(), PreferenceStore, FitAssessment, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 6 - "find_startups"
Cohesion: 0.18
Nodes (9): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups(), people_at() (+1 more)

### Community 7 - "run_followups"
Cohesion: 0.11
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 8 - "send_email"
Cohesion: 0.18
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 10 - "ai.py"
Cohesion: 0.14
Nodes (19): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+11 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "get_settings"
Cohesion: 0.21
Nodes (18): get_settings(), daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), _get(), leads() (+10 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 17 - "test_leads.py"
Cohesion: 0.08
Nodes (26): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+18 more)

### Community 18 - "test_people.py"
Cohesion: 0.16
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 19 - "x_search.py"
Cohesion: 0.16
Nodes (4): search_startups(), post_confirms(), search_x_raises(), _tool_usage()

### Community 21 - "app.py"
Cohesion: 0.18
Nodes (12): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, KeyRequest, NoteRequest, PreferenceDelete (+4 more)

### Community 22 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 24 - "re"
Cohesion: 0.07
Nodes (27): fit_to_limit(), _slug(), _on_linkedin(), source_names(), _ashby(), fetch_posting_text(), _get(), _greenhouse() (+19 more)

### Community 25 - "workflows.py"
Cohesion: 0.14
Nodes (10): ApplicationPrep, load_resume_text(), answer_bank(), handle_note(), NoteOutcome, _openai(), preference_store(), prepare_application() (+2 more)

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (25): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, _identity(), load_inbox(), merge() (+17 more)

### Community 27 - "leads/schemas.py"
Cohesion: 0.32
Nodes (5): is_open(), rank(), LeadKind, LeadStatus, Verdict

### Community 28 - "followups.py"
Cohesion: 0.25
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 29 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 30 - "send"
Cohesion: 0.24
Nodes (3): send(), check_send(), SendBlocked

### Community 32 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 40 - "Aarav Modi — application context"
Cohesion: 0.17
Nodes (11): Aarav Modi — application context, Agents and automation projects, CIBC, Enerzen — early-stage startup, Experience highlights, Homelab, How to tailor application materials, Profile (+3 more)

### Community 42 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 248 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `README.md`, `leads/cli.py`, `startups.py`, `Segment`, `json`, `test_notes.py`, `find_startups`, `run_followups`, `send_email`, `Settings`, `ai.py`, `get_settings`, `test_dashboard.py`, `test_leads.py`, `app.py`, `workflows.py`, `leads/schemas.py`, `followups.py`, `send`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 62 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 62 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.09879032258064516 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `README.md`, `leads/cli.py`, `json`, `test_notes.py`, `find_startups`, `run_followups`, `send_email`, `internship_agent/cli.py`, `make_workflows.py`, `get_settings`, `test_people.py`, `client.py`, `workflows.py`, `Lead`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 39 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 39 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09634551495016612 - nodes in this community are weakly interconnected._