# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~86,948 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 889 nodes · 2573 edges · 45 communities (37 shown, 8 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 426 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `18fd75e0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- store.py
- leads/cli.py
- startups.py
- LeadKind
- answers.py
- test_notes.py
- Region
- run_followups
- test_outreach.py
- Settings
- test_application_browser.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- json
- ai.py
- test_answers.py
- x_search.py
- typing
- re
- get_settings
- client.py
- startup_jobs.py
- Lead
- test_leads.py
- LeadStatus
- followups.py
- find_startups
- leads/schemas.py
- find-founders.md
- export_drafts
- FakeMailbox
- test_x_search.py
- Segment
- internship-agent
- browser.py
- Aarav Modi — application context
- AGENTS.md
- _TableParser
- open_login_browser

## God Nodes (most connected - your core abstractions)
1. `Lead` - 98 edges
2. `Settings` - 49 edges
3. `get_settings()` - 41 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `daily()` - 25 edges
9. `Segment` - 24 edges
10. `prepare_application()` - 24 edges

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

## Communities (45 total, 8 thin omitted)

### Community 0 - "store.py"
Cohesion: 0.10
Nodes (13): is_workday(), open_postings(), refill(), _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.25
Nodes (8): _draft(), draft_all(), draft_lead(), _openai(), _resume(), score_leads(), _store(), load_resume_text()

### Community 2 - "startups.py"
Cohesion: 0.13
Nodes (9): PersonFinding, _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms() (+1 more)

### Community 3 - "LeadKind"
Cohesion: 0.22
Nodes (7): LeadKind, Round, parse_round(), to_leads(), finding(), test_to_leads_filters_age_stage_and_unverifiable_sources(), test_to_leads_sets_region_and_drops_bad_handle()

### Community 4 - "answers.py"
Cohesion: 0.16
Nodes (9): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+1 more)

### Community 5 - "test_notes.py"
Cohesion: 0.15
Nodes (15): apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, posting(), settings() (+7 more)

### Community 6 - "Region"
Cohesion: 0.14
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 7 - "run_followups"
Cohesion: 0.12
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 8 - "test_outreach.py"
Cohesion: 0.08
Nodes (17): Send email safeguards, EmailStatus, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send() (+9 more)

### Community 9 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "test_application_browser.py"
Cohesion: 0.13
Nodes (11): _answer_for(), _fill_form(), _normalize(), FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match() (+3 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.17
Nodes (9): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, n8n workflows (+1 more)

### Community 14 - "app.py"
Cohesion: 0.05
Nodes (63): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+55 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "json"
Cohesion: 0.20
Nodes (14): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+6 more)

### Community 17 - "ai.py"
Cohesion: 0.19
Nodes (14): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+6 more)

### Community 18 - "test_answers.py"
Cohesion: 0.21
Nodes (13): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+5 more)

### Community 19 - "x_search.py"
Cohesion: 0.17
Nodes (6): search_startups(), StartupFinding, StartupFindings, post_confirms(), search_x_raises(), _tool_usage()

### Community 20 - "typing"
Cohesion: 0.18
Nodes (9): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+1 more)

### Community 21 - "re"
Cohesion: 0.29
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 22 - "get_settings"
Cohesion: 0.20
Nodes (7): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), show_lead()

### Community 23 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 24 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 25 - "Lead"
Cohesion: 0.16
Nodes (13): Lead, answer_bank(), daily(), DailyReport, lead_store(), NoteOutcome, prepare_application(), rescore_open() (+5 more)

### Community 26 - "test_leads.py"
Cohesion: 0.07
Nodes (28): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+20 more)

### Community 27 - "LeadStatus"
Cohesion: 0.27
Nodes (5): _email_cell(), list_leads(), is_open(), rank(), LeadStatus

### Community 28 - "followups.py"
Cohesion: 0.25
Nodes (5): Internship tracker: follow-ups (weekdays 9:30 AM), first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "find_startups"
Cohesion: 0.23
Nodes (7): effective_segment(), to_people(), find_people(), find_startups(), people_at(), _log_xai(), _openai()

### Community 30 - "leads/schemas.py"
Cohesion: 0.13
Nodes (8): fit_to_limit(), ApplicationPrep, FitAssessment, OutreachDraft, OutreachDraftResult, _slug(), Verdict, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 31 - "find-founders.md"
Cohesion: 0.22
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), mark_lead(), load_inbox()

### Community 32 - "export_drafts"
Cohesion: 0.24
Nodes (4): apply_cmd(), export_drafts(), find_startups_cmd(), followups_cmd()

### Community 34 - "test_x_search.py"
Cohesion: 0.22
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 36 - "Segment"
Cohesion: 0.31
Nodes (5): More people to connect with, chosen by company size, search_people(), Person, Segment, test_search_people_asks_for_roles_that_suit_the_company_size()

### Community 39 - "browser.py"
Cohesion: 0.32
Nodes (4): apply_to_posting(), SubmissionResult, _supported_url(), test_supported_submission_hosts_are_explicit()

### Community 40 - "Aarav Modi — application context"
Cohesion: 0.17
Nodes (11): Aarav Modi — application context, Agents and automation projects, CIBC, Enerzen — early-stage startup, Experience highlights, Homelab, How to tailor application materials, Profile (+3 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 264 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `store.py`, `leads/cli.py`, `startups.py`, `LeadKind`, `test_notes.py`, `Region`, `run_followups`, `test_outreach.py`, `Settings`, `test_application_browser.py`, `app.py`, `test_dashboard.py`, `json`, `ai.py`, `test_answers.py`, `test_leads.py`, `LeadStatus`, `followups.py`, `find_startups`, `leads/schemas.py`, `find-founders.md`, `Segment`, `browser.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `store.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10344827586206896 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `test_notes.py`, `Region`, `run_followups`, `test_outreach.py`, `internship_agent/cli.py`, `app.py`, `test_answers.py`, `typing`, `get_settings`, `client.py`, `Lead`, `find_startups`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `startups.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12987012987012986 - nodes in this community are weakly interconnected._