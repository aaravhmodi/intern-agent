# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 102 files · ~124,721 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1655 nodes · 4964 edges · 74 communities (60 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 839 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8e1d365c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- Region
- notify.py
- Opportunity
- run_followups
- typing
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- re
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- agenda.py
- followup_run.py
- answers.py
- opportunities/schemas.py
- test_people.py
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- x_search.py
- apply_events
- test_apply_events.py
- pytest
- Table
- run
- run-lowest-30-applications.sh
- startups.py
- leads/schemas.py
- test_patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- client.py
- README.md
- prepare_application
- local_only
- GmailMailbox
- OutlookClient
- LeadStatus
- test_refill.py
- export.py
- Settings
- outlook/schemas.py
- FormQuestion
- check_events
- SentMessage
- PlaywrightPage
- AGENTS.md
- datetime
- pipeline.py
- command
- test_auto_pick.py
- followups.py
- test_outlook_client.py
- test_pg_store.py
- Snapshot
- FakeToggle
- find-founders.md
- Lead
- ranking.py
- load_resume_text
- scrape_jobs_cmd
- run.py
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 149 edges
2. `Settings` - 112 edges
3. `get_settings()` - 76 edges
4. `Opportunity` - 71 edges
5. `LeadStatus` - 43 edges
6. `OpportunityStore` - 43 edges
7. `run_followups()` - 35 edges
8. `Region` - 32 edges
9. `run()` - 31 edges
10. `LeadKind` - 30 edges

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

## Communities (74 total, 14 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.19
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.06
Nodes (30): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+22 more)

### Community 2 - "Region"
Cohesion: 0.11
Nodes (14): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+6 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (15): category(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 4 - "Opportunity"
Cohesion: 0.09
Nodes (17): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), mark_cmd(), sign_in_cmd(), strategy_cmd() (+9 more)

### Community 5 - "run_followups"
Cohesion: 0.21
Nodes (19): run_followups(), emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+11 more)

### Community 6 - "typing"
Cohesion: 0.08
Nodes (21): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+13 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.11
Nodes (22): _fill_form(), _numeric_answer(), PreparedAnswer, FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_closed_posting_text_is_detected() (+14 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "form_d.py"
Cohesion: 0.05
Nodes (33): _clean(), guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes() (+25 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.19
Nodes (14): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "re"
Cohesion: 0.05
Nodes (44): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+36 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.17
Nodes (9): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, n8n workflows (+1 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.13
Nodes (17): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+9 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "get_settings"
Cohesion: 0.10
Nodes (36): get_settings(), allow_event_retry(), allow_retry(), application_proof(), apply_to_event(), auto_apply(), check_opportunities(), daily_run() (+28 more)

### Community 17 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 18 - "app.py"
Cohesion: 0.06
Nodes (29): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, FindMoreRequest, FindStartupsRequest (+21 more)

### Community 19 - "agenda.py"
Cohesion: 0.15
Nodes (11): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics() (+3 more)

### Community 20 - "followup_run.py"
Cohesion: 0.09
Nodes (12): append(), read_log(), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), _site() (+4 more)

### Community 21 - "answers.py"
Cohesion: 0.15
Nodes (11): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+3 more)

### Community 22 - "opportunities/schemas.py"
Cohesion: 0.14
Nodes (10): assess(), EventFinding, EventFindings, search_events(), write_strategy(), BrowserStep, OpportunityAssessment, SubmissionStrategy (+2 more)

### Community 23 - "test_people.py"
Cohesion: 0.19
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 25 - "leads/cli.py"
Cohesion: 0.20
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (11): StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 27 - "apply_events"
Cohesion: 0.16
Nodes (10): next_step(), describe(), saved_browser(), apply_events(), step(), _openai(), send_sessions(), sign_in() (+2 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.19
Nodes (14): _event(), landing(), _settings(), step(), steps(), test_allowed_sites(), test_apply_events_saves_the_result_and_marks_it_submitted(), fake_browser() (+6 more)

### Community 29 - "pytest"
Cohesion: 0.26
Nodes (13): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+5 more)

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "startups.py"
Cohesion: 0.16
Nodes (7): _on_linkedin(), source_names(), mentions(), names(), page_names(), source_confirms(), test_mentions_requires_company_and_founder_ignoring_accents()

### Community 34 - "leads/schemas.py"
Cohesion: 0.12
Nodes (19): EmailStatus, LeadKind, Round, Segment, Verdict, parse_round(), check_outreach_text(), check_send() (+11 more)

### Community 35 - "test_patterns.py"
Cohesion: 0.19
Nodes (10): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+2 more)

### Community 40 - "client.py"
Cohesion: 0.15
Nodes (5): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), no_real_services()

### Community 41 - "README.md"
Cohesion: 0.06
Nodes (40): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules (+32 more)

### Community 42 - "prepare_application"
Cohesion: 0.14
Nodes (8): daily_cmd(), prepare_all_cmd(), prepare_cmd(), daily(), prepare_application(), refresh_saved_application(), _retryable_block(), submit_application()

### Community 43 - "local_only"
Cohesion: 0.22
Nodes (5): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, dashboard_css(), local_only()

### Community 44 - "GmailMailbox"
Cohesion: 0.13
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 46 - "LeadStatus"
Cohesion: 0.17
Nodes (16): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 47 - "test_refill.py"
Cohesion: 0.17
Nodes (8): refill(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 48 - "export.py"
Cohesion: 0.50
Nodes (3): _email_line(), render_outreach(), test_render_outreach_flags_unverified_emails_and_skips_undrafted()

### Community 49 - "Settings"
Cohesion: 0.22
Nodes (5): Settings, inboxes(), answer_bank(), save_answers(), _use_gmail_for_applications()

### Community 50 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 51 - "FormQuestion"
Cohesion: 0.17
Nodes (17): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+9 more)

### Community 52 - "check_events"
Cohesion: 0.14
Nodes (7): normalize_url(), _candidate(), check_events(), one(), checked(), _keys(), without_citations()

### Community 54 - "PlaywrightPage"
Cohesion: 0.15
Nodes (3): Element, _refusal(), PlaywrightPage

### Community 57 - "pipeline.py"
Cohesion: 0.05
Nodes (29): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+21 more)

### Community 58 - "command"
Cohesion: 0.15
Nodes (9): application_campaign(), apply_cmd(), browser_login(), find_more(), find_startups_cmd(), followups_cmd(), form_d_cmd(), guess_send_cmd() (+1 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.38
Nodes (8): check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition(), test_push_names_what_was_picked()

### Community 60 - "followups.py"
Cohesion: 0.23
Nodes (6): Internship tracker: follow-ups (weekdays 9:30 AM), first_name(), followup_body(), is_due(), last_contact(), next_followup()

### Community 61 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 62 - "test_pg_store.py"
Cohesion: 0.29
Nodes (3): posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 63 - "Snapshot"
Cohesion: 0.21
Nodes (3): Snapshot, StepAction, FakePage

### Community 64 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 65 - "find-founders.md"
Cohesion: 0.11
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+4 more)

### Community 66 - "Lead"
Cohesion: 0.14
Nodes (8): role_of(), Lead, _identity(), LeadStore, merge(), test_auto_apply_prepares_then_submits(), test_merge_keeps_existing_and_dedupes_incoming(), test_store_round_trip_and_upsert()

### Community 70 - "run.py"
Cohesion: 0.13
Nodes (13): refresh_cmd(), find_events(), import_inbox(), keep(), nearby(), pick_reason(), proof_path(), refresh() (+5 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.10
Nodes (18): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), to_people(), add_team_contacts(), DailyReport (+10 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 515 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `Region`, `notify.py`, `run_followups`, `typing`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `internship_agent/ai.py`, `get_settings`, `app.py`, `agenda.py`, `followup_run.py`, `answers.py`, `leads/cli.py`, `pytest`, `Table`, `startups.py`, `leads/schemas.py`, `test_patterns.py`, `README.md`, `prepare_application`, `LeadStatus`, `test_refill.py`, `export.py`, `Settings`, `FormQuestion`, `pipeline.py`, `followups.py`, `test_pg_store.py`, `find-founders.md`, `ranking.py`, `workflows.py`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 108 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 108 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.059887005649717516 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Region`, `Opportunity`, `run_followups`, `test_daily_campaign.py`, `form_d.py`, `internship_agent/cli.py`, `re`, `test_opportunities.py`, `get_settings`, `app.py`, `followup_run.py`, `answers.py`, `test_people.py`, `leads/cli.py`, `apply_events`, `test_apply_events.py`, `Table`, `test_patterns.py`, `client.py`, `README.md`, `prepare_application`, `local_only`, `LeadStatus`, `FormQuestion`, `check_events`, `pipeline.py`, `test_auto_pick.py`, `run.py`, `workflows.py`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 94 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 94 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.10606060606060606 - nodes in this community are weakly interconnected._