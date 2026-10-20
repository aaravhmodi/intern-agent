# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 88 files · ~104,062 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1243 nodes · 3683 edges · 64 communities (52 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 635 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d50ef2f0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- find_form_d_startups
- answers.py
- Region
- LeadStatus
- run.py
- app.py
- browser.py
- FakeField
- PreparedAnswer
- form_d.py
- test_leads.py
- internship_agent/cli.py
- startup_jobs.py
- make_workflows.py
- workflows.py
- test_opportunities.py
- get_settings
- tracking.py
- test_refill.py
- _opportunity_view
- Settings
- OutlookClient
- client.py
- find_startups
- run-application-campaign-2026-10-16.sh
- Lead
- typing
- config.py
- test_form_d.py
- test_application_browser.py
- AGENTS.md
- candidate_context.md
- run-lowest-30-applications.sh
- people.py
- test_interview_events
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- ApplicationPrep
- README.md
- test_hidden_recaptcha_support_nodes_do_not_block
- outlook/schemas.py
- local_only
- internship_agent/ai.py
- leads/schemas.py
- feeds.py
- json
- send_email
- opportunities/ai.py
- verification_mail.py
- leads/cli.py
- test_people.py
- re
- test_outlook_client.py
- posting_text.py
- list_cmd
- Opportunity
- db.py
- handle_note
- find-opportunities.md
- _numeric_answer
- lead_store

## God Nodes (most connected - your core abstractions)
1. `Lead` - 122 edges
2. `Settings` - 80 edges
3. `get_settings()` - 61 edges
4. `Opportunity` - 38 edges
5. `run_followups()` - 36 edges
6. `LeadStatus` - 35 edges
7. `Region` - 30 edges
8. `prepare_application()` - 29 edges
9. `Segment` - 27 edges
10. `FormQuestion` - 27 edges

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

## Communities (64 total, 12 thin omitted)

### Community 0 - "find_form_d_startups"
Cohesion: 0.18
Nodes (7): company_name(), filings(), form_d_paths(), index_url(), parse_filing(), _person(), find_form_d_startups()

### Community 1 - "answers.py"
Cohesion: 0.15
Nodes (8): AnswerBank, category(), match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 2 - "Region"
Cohesion: 0.11
Nodes (14): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+6 more)

### Community 3 - "LeadStatus"
Cohesion: 0.09
Nodes (17): PreferenceDraft, Table, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect (+9 more)

### Community 4 - "run.py"
Cohesion: 0.11
Nodes (12): refresh_cmd(), find_events(), keep(), nearby(), next_date(), _openai(), plan_submission(), refresh() (+4 more)

### Community 5 - "app.py"
Cohesion: 0.11
Nodes (16): AnswerEdit, application_proof(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, OpportunityStatusUpdate, PreferenceDelete (+8 more)

### Community 6 - "browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (4): FakeField, FakeLocator, FakeToggle, locator()

### Community 8 - "PreparedAnswer"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 9 - "form_d.py"
Cohesion: 0.18
Nodes (11): candidate_domains(), _check(), _description(), _fetch(), Filing, find_site(), founder_email(), _has_name() (+3 more)

### Community 10 - "test_leads.py"
Cohesion: 0.08
Nodes (33): dashboard(), LeadStore, client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "workflows.py"
Cohesion: 0.12
Nodes (15): common_questions(), answer_bank(), daily(), DailyReport, NoteOutcome, _openai(), prepare_application(), _record_openai_usage() (+7 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.15
Nodes (11): _opp(), _settings(), test_dashboard_lists_and_marks_opportunities(), test_devpost_dates(), test_find_events_keeps_only_dated_events_whose_page_names_them(), finding(), test_keep_drops_past_and_far_away_events(), test_mlh_parses_cards_and_never_reads_india_as_indiana() (+3 more)

### Community 16 - "get_settings"
Cohesion: 0.21
Nodes (19): get_settings(), allow_retry(), auto_apply(), daily_run(), delete_preference(), draft(), find_more(), find_more_startups() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "test_refill.py"
Cohesion: 0.16
Nodes (9): is_workday(), open_postings(), refill(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped() (+1 more)

### Community 19 - "_opportunity_view"
Cohesion: 0.38
Nodes (5): find_events(), _opportunity(), opportunity_status(), opportunity_strategy(), _opportunity_view()

### Community 20 - "Settings"
Cohesion: 0.05
Nodes (40): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+32 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.20
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "find_startups"
Cohesion: 0.18
Nodes (10): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups() (+2 more)

### Community 25 - "Lead"
Cohesion: 0.09
Nodes (11): Lead, _identity(), merge(), normalize_url(), test_incompatible_eight_month_term_is_rejected(), test_post_submit_state_is_persisted_for_tracker(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_saving_answers_preserves_uncertain_submission() (+3 more)

### Community 26 - "typing"
Cohesion: 0.11
Nodes (11): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 27 - "config.py"
Cohesion: 0.16
Nodes (4): OpportunityStatus, posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 29 - "test_application_browser.py"
Cohesion: 0.20
Nodes (17): _answer_for(), _fill_form(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+9 more)

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "people.py"
Cohesion: 0.16
Nodes (6): _on_linkedin(), source_names(), mentions(), names(), page_names(), source_confirms()

### Community 40 - "ApplicationPrep"
Cohesion: 0.22
Nodes (8): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new()

### Community 41 - "README.md"
Cohesion: 0.12
Nodes (26): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+18 more)

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 45 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 46 - "internship_agent/ai.py"
Cohesion: 0.16
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 48 - "leads/schemas.py"
Cohesion: 0.15
Nodes (15): LeadKind, Round, Segment, Verdict, parse_round(), to_leads(), finding(), lead() (+7 more)

### Community 50 - "feeds.py"
Cohesion: 0.21
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 51 - "json"
Cohesion: 0.21
Nodes (15): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q() (+7 more)

### Community 52 - "send_email"
Cohesion: 0.07
Nodes (16): Send email safeguards, EmailStatus, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send() (+8 more)

### Community 56 - "opportunities/ai.py"
Cohesion: 0.21
Nodes (6): EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, SubmissionTrack

### Community 57 - "verification_mail.py"
Cohesion: 0.19
Nodes (5): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _get()

### Community 58 - "leads/cli.py"
Cohesion: 0.06
Nodes (37): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+29 more)

### Community 61 - "test_people.py"
Cohesion: 0.16
Nodes (11): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched() (+3 more)

### Community 62 - "re"
Cohesion: 0.16
Nodes (7): Output, Output, _clean(), guess_email(), fit_to_limit(), _slug(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 63 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 64 - "posting_text.py"
Cohesion: 0.33
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 68 - "list_cmd"
Cohesion: 0.15
Nodes (5): find_events_cmd(), import_cmd(), list_cmd(), strategy_cmd(), import_inbox()

### Community 70 - "Opportunity"
Cohesion: 0.29
Nodes (5): mark_cmd(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 72 - "db.py"
Cohesion: 0.29
Nodes (3): append(), read_log(), _log_xai()

### Community 76 - "handle_note"
Cohesion: 0.33
Nodes (4): note(), NoteRequest, handle_note(), preference_store()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "lead_store"
Cohesion: 0.22
Nodes (6): set_status(), StatusUpdate, Lead detail panel: fit, links, contact, actions, lead_store(), rescore_open(), save_answers()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 391 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `find_form_d_startups`, `answers.py`, `Region`, `LeadStatus`, `app.py`, `browser.py`, `PreparedAnswer`, `form_d.py`, `test_leads.py`, `workflows.py`, `get_settings`, `test_refill.py`, `Settings`, `find_startups`, `config.py`, `test_application_browser.py`, `ApplicationPrep`, `internship_agent/ai.py`, `leads/schemas.py`, `json`, `send_email`, `leads/cli.py`, `lead_store`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 85 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 85 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.10606060606060606 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `find_form_d_startups`, `answers.py`, `Region`, `LeadStatus`, `run.py`, `app.py`, `internship_agent/cli.py`, `workflows.py`, `test_opportunities.py`, `get_settings`, `client.py`, `find_startups`, `Lead`, `config.py`, `ApplicationPrep`, `local_only`, `json`, `send_email`, `leads/cli.py`, `test_people.py`, `list_cmd`, `Opportunity`, `db.py`, `handle_note`, `lead_store`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 66 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `append()`) actually correct?**
  _`Settings` has 66 INFERRED edges - model-reasoned connections that need verification._
- **Should `LeadStatus` be split into smaller, more focused modules?**
  _Cohesion score 0.09042553191489362 - nodes in this community are weakly interconnected._