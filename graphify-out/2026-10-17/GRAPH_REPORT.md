# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~90,081 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 955 nodes · 2765 edges · 44 communities (32 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 481 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e05ce9fe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- leads/cli.py
- re
- posting_text.py
- json
- test_notes.py
- workflows.py
- app.py
- Winter 2027 Internship Agent
- Settings
- client.py
- internship_agent/cli.py
- get_settings
- make_workflows.py
- ai.py
- prepare_application
- browser.py
- startups.py
- candidate_context.md
- x_search.py
- test_dashboard.py
- test_daily_campaign.py
- find-founders.md
- Lead
- run-application-campaign-2026-10-16.sh
- followups_cmd
- test_leads.py
- _view
- datetime
- load_resume_text
- BaseModel
- _TableParser
- test_ai.py
- test_people.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- people.py
- store.py
- typing
- fit_to_limit
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 108 edges
2. `Settings` - 58 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 26 edges
8. `Region` - 25 edges
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

## Communities (44 total, 12 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.17
Nodes (20): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+12 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.24
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 2 - "re"
Cohesion: 0.13
Nodes (14): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+6 more)

### Community 3 - "posting_text.py"
Cohesion: 0.15
Nodes (17): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+9 more)

### Community 4 - "json"
Cohesion: 0.06
Nodes (40): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+32 more)

### Community 5 - "test_notes.py"
Cohesion: 0.15
Nodes (15): apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, posting(), settings() (+7 more)

### Community 6 - "workflows.py"
Cohesion: 0.12
Nodes (15): More people to connect with, chosen by company size, search_people(), LeadKind, Person, effective_segment(), to_people(), DailyReport, find_people() (+7 more)

### Community 7 - "app.py"
Cohesion: 0.16
Nodes (12): AnswerEdit, delete_preference(), find_more_startups(), FindStartupsRequest, FollowupsRequest, leads(), note(), NoteRequest (+4 more)

### Community 8 - "Winter 2027 Internship Agent"
Cohesion: 0.12
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP) (+4 more)

### Community 9 - "Settings"
Cohesion: 0.05
Nodes (38): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+30 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "get_settings"
Cohesion: 0.17
Nodes (8): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd(), show_lead()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "ai.py"
Cohesion: 0.21
Nodes (13): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+5 more)

### Community 15 - "prepare_application"
Cohesion: 0.18
Nodes (10): answer_bank(), daily(), lead_store(), prepare_application(), refresh_saved_application(), rescore_open(), resume_text(), _retryable_block() (+2 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (30): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+22 more)

### Community 17 - "startups.py"
Cohesion: 0.13
Nodes (16): Segment, parse_round(), _fold(), mentions(), names(), to_leads(), finding(), lead() (+8 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.13
Nodes (9): search_startups(), StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+1 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_caps_new_preparations(), load(), score_new() (+5 more)

### Community 22 - "find-founders.md"
Cohesion: 0.22
Nodes (6): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, export_drafts(), import_leads(), load_inbox()

### Community 23 - "Lead"
Cohesion: 0.15
Nodes (11): _email_line(), render_outreach(), EmailStatus, Lead, Round, _slug(), Verdict, check_outreach_text() (+3 more)

### Community 25 - "followups_cmd"
Cohesion: 0.25
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 26 - "test_leads.py"
Cohesion: 0.08
Nodes (26): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+18 more)

### Community 27 - "_view"
Cohesion: 0.12
Nodes (20): daily_run(), draft(), find_more(), FindMoreRequest, followups(), _get(), KeyRequest, people() (+12 more)

### Community 33 - "test_ai.py"
Cohesion: 0.27
Nodes (6): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 40 - "people.py"
Cohesion: 0.24
Nodes (5): PersonFinding, _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 42 - "store.py"
Cohesion: 0.11
Nodes (13): is_workday(), open_postings(), refill(), _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 49 - "send_email"
Cohesion: 0.09
Nodes (7): Internship agent coding instructions, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 292 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/cli.py`, `re`, `json`, `test_notes.py`, `workflows.py`, `app.py`, `Settings`, `ai.py`, `prepare_application`, `browser.py`, `startups.py`, `test_dashboard.py`, `test_daily_campaign.py`, `find-founders.md`, `test_leads.py`, `_view`, `datetime`, `BaseModel`, `store.py`, `fit_to_limit`, `send_email`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **Are the 77 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 77 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.12643678160919541 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `re`, `test_people.py`, `json`, `test_notes.py`, `workflows.py`, `app.py`, `Winter 2027 Internship Agent`, `client.py`, `internship_agent/cli.py`, `get_settings`, `prepare_application`, `send_email`, `test_daily_campaign.py`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Should `posting_text.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14814814814814814 - nodes in this community are weakly interconnected._