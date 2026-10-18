# Graph Report - winter-2027-internship-agent  (2026-10-18)

## Corpus Check
- 76 files · ~193,307 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1046 nodes · 3017 edges · 50 communities (38 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 523 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `af20d080`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- typing
- command
- simplify.py
- README.md
- workflows.py
- test_ai.py
- browser.py
- FakeField
- startups.py
- run_followups
- test_dashboard.py
- internship_agent/cli.py
- people.py
- make_workflows.py
- verification_mail.py
- leads/cli.py
- app.py
- tracking.py
- notify.py
- LeadKind
- leads/schemas.py
- x_search.py
- FormQuestion
- OutlookClient
- run-application-campaign-2026-10-16.sh
- find-internships.md
- re
- find-founders.md
- client.py
- test_application_browser.py
- outlook/schemas.py
- test_x_search.py
- run-lowest-30-applications.sh
- test_people.py
- FakeToggle
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Lead
- ranking.py
- BaseModel
- ai.py
- load_resume_text
- test_hidden_recaptcha_support_nodes_do_not_block
- _numeric_answer
- test_outreach.py
- open_login_browser
- Bot Auto application preview

## God Nodes (most connected - your core abstractions)
1. `Lead` - 110 edges
2. `Settings` - 62 edges
3. `get_settings()` - 48 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `prepare_application()` - 28 edges
7. `FormQuestion` - 27 edges
8. `find_startups()` - 27 edges
9. `Region` - 25 edges
10. `Segment` - 24 edges

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

## Communities (50 total, 12 thin omitted)

### Community 0 - "typing"
Cohesion: 0.12
Nodes (9): _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+1 more)

### Community 1 - "command"
Cohesion: 0.13
Nodes (9): application_campaign(), apply_cmd(), daily_cmd(), export_drafts(), find_more(), find_startups_cmd(), followups_cmd(), prepare_cmd() (+1 more)

### Community 2 - "simplify.py"
Cohesion: 0.12
Nodes (10): Big-company postings from the SimplifyJobs off-season list, cap_per_company(), fetch(), is_software_role(), matching(), parse(), Posting, _TableParser (+2 more)

### Community 3 - "README.md"
Cohesion: 0.06
Nodes (29): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+21 more)

### Community 4 - "workflows.py"
Cohesion: 0.07
Nodes (36): More people to connect with, chosen by company size, search_people(), Settings, common_questions(), normalize(), ApplicationPrep, Person, Segment (+28 more)

### Community 5 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 6 - "browser.py"
Cohesion: 0.10
Nodes (17): apply_to_posting(), _field_label(), _normalize(), _online_checks(), _post_submit_outcome(), _posting_is_closed(), _react_select_answer(), _save_submission_diagnostic() (+9 more)

### Community 7 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 8 - "startups.py"
Cohesion: 0.15
Nodes (8): Region, parse_round(), region_from_text(), regions_of(), _fold(), names(), to_leads(), test_to_leads_sets_region_and_drops_bad_handle()

### Community 9 - "run_followups"
Cohesion: 0.05
Nodes (34): FollowupReport, FollowupSent, _name(), run_followups(), company_domain(), first_name(), followup_body(), is_due() (+26 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.15
Nodes (15): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+7 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "people.py"
Cohesion: 0.24
Nodes (5): PersonFinding, _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "verification_mail.py"
Cohesion: 0.10
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 15 - "leads/cli.py"
Cohesion: 0.25
Nodes (8): _draft(), draft_all(), draft_lead(), _openai(), prepare_all_cmd(), _resume(), show_lead(), _store()

### Community 16 - "app.py"
Cohesion: 0.08
Nodes (45): get_settings(), allow_retry(), AnswerEdit, _archive_messages_forever(), auto_apply(), daily_run(), delete_preference(), draft() (+37 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "notify.py"
Cohesion: 0.15
Nodes (15): _clip(), _fit_bytes(), history(), posting_push(), Push, send(), summary_push(), answer() (+7 more)

### Community 19 - "LeadKind"
Cohesion: 0.27
Nodes (7): is_workday(), open_postings(), refill(), LeadKind, scrape_jobs(), startup_postings(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 20 - "leads/schemas.py"
Cohesion: 0.10
Nodes (17): _misaddressed(), _site(), apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference (+9 more)

### Community 21 - "x_search.py"
Cohesion: 0.19
Nodes (5): search_startups(), StartupFinding, post_confirms(), search_x_raises(), _tool_usage()

### Community 22 - "FormQuestion"
Cohesion: 0.13
Nodes (12): _answer_for(), AnswerBank, category(), match_option(), prefill(), validate(), FormQuestion, written_answers() (+4 more)

### Community 23 - "OutlookClient"
Cohesion: 0.20
Nodes (7): OutlookClient, OutlookError, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 25 - "find-internships.md"
Cohesion: 0.13
Nodes (9): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+1 more)

### Community 26 - "re"
Cohesion: 0.07
Nodes (37): _logged_subject(), fit_to_limit(), QuestionKind, _slug(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions() (+29 more)

### Community 27 - "find-founders.md"
Cohesion: 0.19
Nodes (8): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), mark_lead(), score_leads(), load_inbox()

### Community 28 - "client.py"
Cohesion: 0.15
Nodes (5): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), ToolSession

### Community 29 - "test_application_browser.py"
Cohesion: 0.25
Nodes (14): _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass() (+6 more)

### Community 30 - "outlook/schemas.py"
Cohesion: 0.26
Nodes (9): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient (+1 more)

### Community 31 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 33 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 40 - "Lead"
Cohesion: 0.06
Nodes (33): _email_line(), render_outreach(), FitAssessment, Lead, LeadStore, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare() (+25 more)

### Community 41 - "ranking.py"
Cohesion: 0.28
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 42 - "BaseModel"
Cohesion: 0.29
Nodes (3): FitResult, OutreachDraft, OutreachDraftResult

### Community 43 - "ai.py"
Cohesion: 0.17
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 47 - "test_outreach.py"
Cohesion: 0.08
Nodes (20): Send email safeguards, EmailStatus, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send() (+12 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 331 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `typing`, `simplify.py`, `workflows.py`, `browser.py`, `startups.py`, `run_followups`, `test_dashboard.py`, `leads/cli.py`, `app.py`, `notify.py`, `LeadKind`, `leads/schemas.py`, `FormQuestion`, `find-internships.md`, `re`, `find-founders.md`, `test_application_browser.py`, `ranking.py`, `BaseModel`, `ai.py`, `test_outreach.py`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.11578947368421053 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `test_people.py`, `simplify.py`, `Lead`, `run_followups`, `internship_agent/cli.py`, `ai.py`, `make_workflows.py`, `leads/cli.py`, `app.py`, `LeadKind`, `leads/schemas.py`, `FormQuestion`, `re`, `client.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `command` be split into smaller, more focused modules?**
  _Cohesion score 0.12554112554112554 - nodes in this community are weakly interconnected._