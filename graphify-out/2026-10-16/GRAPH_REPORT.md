# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~88,948 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 926 nodes · 2679 edges · 34 communities (28 shown, 6 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 452 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7525a1e4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- get_settings
- find-founders.md
- leads/cli.py
- typing
- re
- leads/schemas.py
- find_startups
- handle_note
- followups_cmd
- Settings
- client.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- _view
- test_dashboard.py
- browser.py
- Segment
- rank
- x_search.py
- app.py
- run-application-campaign-2026-10-16.sh
- Lead
- README.md
- startups.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- workflows.py
- Region
- test_people.py
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 102 edges
2. `Settings` - 52 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `prepare_application()` - 25 edges
9. `Segment` - 24 edges
10. `LeadKind` - 23 edges

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

## Communities (34 total, 6 thin omitted)

### Community 0 - "get_settings"
Cohesion: 0.17
Nodes (8): get_settings(), browser_login(), daily_cmd(), find_more(), mark_lead(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd()

### Community 1 - "find-founders.md"
Cohesion: 0.12
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+4 more)

### Community 2 - "leads/cli.py"
Cohesion: 0.26
Nodes (8): _draft(), draft_all(), draft_lead(), _openai(), _resume(), show_lead(), _store(), load_resume_text()

### Community 3 - "typing"
Cohesion: 0.11
Nodes (15): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+7 more)

### Community 4 - "re"
Cohesion: 0.05
Nodes (50): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), fit_to_limit() (+42 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.06
Nodes (45): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+37 more)

### Community 6 - "find_startups"
Cohesion: 0.20
Nodes (8): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, to_people(), find_startups(), people_at(), _log_xai()

### Community 7 - "handle_note"
Cohesion: 0.20
Nodes (8): Screenshot: rules learned from notes, two skip and one boost, Rules learned from notes (skip, downrank, boost), note(), NoteRequest, Notes box that saves notes and learns rules, handle_note(), NoteOutcome, rescore_open()

### Community 8 - "followups_cmd"
Cohesion: 0.27
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 9 - "Settings"
Cohesion: 0.07
Nodes (32): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+24 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.10
Nodes (6): GmailMailbox, _imap_date(), Mailbox, MailboxError, _quoted(), SentMessage

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "_view"
Cohesion: 0.14
Nodes (22): daily_run(), draft(), find_more(), find_more_startups(), _get(), index(), KeyRequest, people() (+14 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "browser.py"
Cohesion: 0.07
Nodes (26): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+18 more)

### Community 17 - "Segment"
Cohesion: 0.14
Nodes (14): Segment, effective_segment(), parse_round(), to_leads(), finding(), lead(), test_build_message_with_attachment(), test_check_send_blocks_unconfirmed_guess_and_resends() (+6 more)

### Community 18 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 19 - "x_search.py"
Cohesion: 0.11
Nodes (11): search_startups(), StartupFinding, StartupFindings, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 23 - "app.py"
Cohesion: 0.18
Nodes (11): AnswerEdit, delete_preference(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, leads(), PreferenceDelete (+3 more)

### Community 26 - "Lead"
Cohesion: 0.07
Nodes (30): Output, Output, _clean(), guess_email(), _email_line(), render_outreach(), EmailStatus, Lead (+22 more)

### Community 27 - "README.md"
Cohesion: 0.07
Nodes (27): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+19 more)

### Community 30 - "startups.py"
Cohesion: 0.14
Nodes (8): _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms(), test_mentions_requires_company_and_founder_ignoring_accents()

### Community 41 - "workflows.py"
Cohesion: 0.12
Nodes (22): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), LeadKind, fetch(), answer_bank(), daily() (+14 more)

### Community 42 - "Region"
Cohesion: 0.12
Nodes (10): Region, region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+2 more)

### Community 44 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 49 - "send_email"
Cohesion: 0.12
Nodes (12): Send email safeguards, send(), SendRequest, Email section with two-click send, check_outreach_text(), check_send(), SendBlocked, build_message() (+4 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 278 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `find-founders.md`, `leads/cli.py`, `typing`, `re`, `leads/schemas.py`, `find_startups`, `handle_note`, `Settings`, `workflows.py`, `Region`, `_view`, `test_dashboard.py`, `browser.py`, `Segment`, `rank`, `send_email`, `app.py`, `startups.py`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 71 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `find-founders.md` be split into smaller, more focused modules?**
  _Cohesion score 0.12380952380952381 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `leads/cli.py`, `re`, `leads/schemas.py`, `find_startups`, `handle_note`, `workflows.py`, `client.py`, `internship_agent/cli.py`, `test_people.py`, `make_workflows.py`, `send_email`, `app.py`, `Lead`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.10574712643678161 - nodes in this community are weakly interconnected._