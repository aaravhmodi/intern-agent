# Graph Report - winter-2027-internship-agent  (2026-10-25)

## Corpus Check
- 143 files · ~649,367 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2038 nodes · 6078 edges · 115 communities (88 shown, 27 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1007 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b363e861`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- big_companies.py
- notify.py
- OpportunityStore
- run_followups
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- re
- pytest
- internship_agent/cli.py
- Settings
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- simplify.py
- QuestionKind
- opportunities/ai.py
- client.py
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- x_search.py
- run.py
- test_apply_events.py
- Opportunity
- find_site_emails
- run
- run-lowest-30-applications.sh
- test_people.py
- leads/schemas.py
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- inboxes
- README.md
- agenda.py
- test_chat.py
- mailbox.py
- test_refill.py
- opportunity_lite/cli.py
- Lead
- outlook/schemas.py
- internship_agent/leads/sending.py
- read_log
- test_ai.py
- test_outlook_client.py
- Mailbox
- StepAction
- lead_store
- test_tables
- pipeline.py
- command
- test_auto_pick.py
- submit_application
- _get
- test_deadlines.py
- followup_run.py
- local_only
- find-founders.md
- find_events
- batches
- pathlib
- AGENTS.md
- list_cmd
- FakeToggle
- insights
- send_email
- candidate_context.md
- page_url
- followups.py
- config.py
- run-inbox-check.sh
- find-opportunities.md
- prepare_application
- export.py
- opportunity_lite/leads/sending.py
- Workspace
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- Table
- outlook
- dashboard.py
- Bot Auto application preview
- send
- _scan_inboxes
- LeadStatus
- run-email-batch.sh
- create_server
- datetime
- test_interview_events
- scrape_jobs_cmd
- test_verification_mail.py
- FormQuestion
- test_career_sites.py
- test_patterns.py
- Region
- ↗ Intern Agent
- fit_to_limit
- web.py
- Snapshot
- test_lite.py
- start.sh
- open_lead_store
- profile.example.md
- notify-failure.sh
- run-discord-scrape.sh
- intern-agent

## God Nodes (most connected - your core abstractions)
1. `Lead` - 188 edges
2. `Settings` - 122 edges
3. `get_settings()` - 81 edges
4. `Opportunity` - 73 edges
5. `LeadStatus` - 59 edges
6. `LeadKind` - 48 edges
7. `OpportunityStore` - 43 edges
8. `Region` - 42 edges
9. `run_followups()` - 36 edges
10. `lead_store()` - 34 edges

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

## Communities (115 total, 27 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.16
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (19): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_confirmation_closes_the_open_posting_it_names() (+11 more)

### Community 2 - "big_companies.py"
Cohesion: 0.12
Nodes (21): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards(), fetch() (+13 more)

### Community 3 - "notify.py"
Cohesion: 0.21
Nodes (14): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer() (+6 more)

### Community 4 - "OpportunityStore"
Cohesion: 0.28
Nodes (7): mark_cmd(), auto_pick(), plan_submission(), OpportunityStatus, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 5 - "run_followups"
Cohesion: 0.32
Nodes (17): run_followups(), emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "re"
Cohesion: 0.08
Nodes (22): _clean(), _normalize(), candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing (+14 more)

### Community 10 - "pytest"
Cohesion: 0.05
Nodes (46): dashboard(), LeadStore, no_real_services(), _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items() (+38 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "Settings"
Cohesion: 0.13
Nodes (16): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+8 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.16
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "get_settings"
Cohesion: 0.15
Nodes (19): post(), get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), check_opportunities(), CheckRequest, daily_run() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (21): AnswerEdit, ask(), browser_sessions(), ChatRequest, Cookie, delete_preference(), find_more(), find_more_startups() (+13 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.15
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "simplify.py"
Cohesion: 0.07
Nodes (16): Big-company postings from the SimplifyJobs off-season list, application_url(), cards(), parse(), postings(), _cell(), parse(), postings() (+8 more)

### Community 21 - "QuestionKind"
Cohesion: 0.20
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 22 - "opportunities/ai.py"
Cohesion: 0.26
Nodes (7): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding()

### Community 23 - "client.py"
Cohesion: 0.19
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "leads/cli.py"
Cohesion: 0.18
Nodes (11): daily_cmd(), _draft(), draft_all(), draft_lead(), _email_cell(), find_more(), list_leads(), _openai() (+3 more)

### Community 26 - "x_search.py"
Cohesion: 0.11
Nodes (12): search_startups(), StartupFinding, StartupFindings, source_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+4 more)

### Community 27 - "run.py"
Cohesion: 0.09
Nodes (19): normalize_url(), next_step(), describe(), saved_browser(), apply_events(), step(), _candidate(), check_events() (+11 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.20
Nodes (14): _event(), landing(), _settings(), step(), steps(), test_allowed_sites(), test_apply_events_saves_the_result_and_marks_it_submitted(), fake_browser() (+6 more)

### Community 29 - "Opportunity"
Cohesion: 0.17
Nodes (15): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+7 more)

### Community 30 - "find_site_emails"
Cohesion: 0.29
Nodes (3): site_emails_cmd(), generic(), find_site_emails()

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "test_people.py"
Cohesion: 0.16
Nodes (11): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, _on_linkedin(), source_names(), person(), test_a_linkedin_source_passes_without_being_fetched() (+3 more)

### Community 34 - "leads/schemas.py"
Cohesion: 0.09
Nodes (22): Round, Segment, _slug(), Verdict, effective_segment(), parse_round(), to_people(), mentions() (+14 more)

### Community 35 - "EmailStatus"
Cohesion: 0.08
Nodes (21): Output, guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes() (+13 more)

### Community 41 - "README.md"
Cohesion: 0.10
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+21 more)

### Community 42 - "agenda.py"
Cohesion: 0.22
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 44 - "mailbox.py"
Cohesion: 0.15
Nodes (9): company_domain(), bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply() (+1 more)

### Community 45 - "test_refill.py"
Cohesion: 0.20
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 46 - "opportunity_lite/cli.py"
Cohesion: 0.29
Nodes (4): main(), _parser(), serve(), load_env()

### Community 47 - "Lead"
Cohesion: 0.09
Nodes (29): drop_unavailable(), expire_closed(), expire_postings(), is_workday(), open_postings(), refill(), Lead, LeadKind (+21 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "internship_agent/leads/sending.py"
Cohesion: 0.28
Nodes (4): Send email safeguards, check_outreach_text(), check_send(), SendBlocked

### Community 50 - "read_log"
Cohesion: 0.50
Nodes (3): read_log(), _logged_subject(), events()

### Community 51 - "test_ai.py"
Cohesion: 0.24
Nodes (6): OutreachDraftResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 52 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 54 - "StepAction"
Cohesion: 0.12
Nodes (4): Element, _refusal(), PlaywrightPage, StepAction

### Community 55 - "lead_store"
Cohesion: 0.12
Nodes (14): draft(), job_pipeline(), leads(), rescore(), set_status(), _sort_key(), StatusUpdate, _view() (+6 more)

### Community 57 - "pipeline.py"
Cohesion: 0.17
Nodes (11): _bounced_lead(), classify(), confirmed_postings(), _header(), _host(), _is_ats(), match(), sync() (+3 more)

### Community 58 - "command"
Cohesion: 0.14
Nodes (11): application_campaign(), apply_cmd(), browser_login(), find_startups_cmd(), followups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd() (+3 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "submit_application"
Cohesion: 0.22
Nodes (5): auto_apply(), submit(), SubmitApplicationRequest, refresh_saved_application(), submit_application()

### Community 61 - "_get"
Cohesion: 0.15
Nodes (9): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get(), health(), _icon() (+1 more)

### Community 62 - "test_deadlines.py"
Cohesion: 0.20
Nodes (8): find_deadline(), posting(), test_closed_or_blocked_applications_are_removed_but_a_missing_resume_is_not(), tried(), test_expire_closed_skips_open_postings_that_are_gone(), test_expire_postings_skips_only_open_postings_past_deadline(), test_finds_a_stated_deadline(), test_ignores_text_without_a_full_dated_deadline()

### Community 63 - "followup_run.py"
Cohesion: 0.20
Nodes (7): FollowupReport, FollowupSent, _misaddressed(), _name(), _site(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 64 - "local_only"
Cohesion: 0.29
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 65 - "find-founders.md"
Cohesion: 0.12
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+4 more)

### Community 66 - "find_events"
Cohesion: 0.33
Nodes (3): find_events_cmd(), find_events(), page_names()

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "pathlib"
Cohesion: 0.23
Nodes (9): Listing, filter_items(), load(), merge(), save(), searchable_text(), openai_client(), refresh() (+1 more)

### Community 70 - "list_cmd"
Cohesion: 0.24
Nodes (7): list_cmd(), keep(), nearby(), next_date(), pick_reason(), upcoming(), worth_checking()

### Community 71 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 72 - "insights"
Cohesion: 0.19
Nodes (9): board(), _card(), display_company(), InboxEvent, insights(), got(), split(), _pct() (+1 more)

### Community 73 - "send_email"
Cohesion: 0.15
Nodes (7): deliver(), build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "page_url"
Cohesion: 0.09
Nodes (15): page_url(), Push, send(), apply_cmd(), refresh_cmd(), applied_push(), summary_push(), push_for() (+7 more)

### Community 76 - "followups.py"
Cohesion: 0.21
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), next_followup(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 77 - "config.py"
Cohesion: 0.08
Nodes (8): append(), check_cmd(), import_cmd(), sign_in_cmd(), strategy_cmd(), import_inbox(), proof_path(), SubmissionTrack

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "prepare_application"
Cohesion: 0.12
Nodes (10): prepare_all_cmd(), prepare_cmd(), load_resume_text(), add_team_contacts(), _openai(), prepare_application(), _record_openai_usage(), resume_text() (+2 more)

### Community 83 - "opportunity_lite/leads/sending.py"
Cohesion: 0.18
Nodes (7): draft_message(), prepare_email(), SendRequest, StoredDraft, Draft, test_resume_is_read_and_attached(), test_send_requires_explicit_confirmation_and_blocks_duplicate()

### Community 84 - "Workspace"
Cohesion: 0.18
Nodes (11): _drafts(), _listing(), _resume_chars(), state(), view(), background(), draft_id(), make_draft() (+3 more)

### Community 86 - "Table"
Cohesion: 0.07
Nodes (25): Table, apply_violations(), PreferenceStore, Preference, PreferenceEffect, PostgresLeadStore, _ashby(), fetch_posting_text() (+17 more)

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "dashboard.py"
Cohesion: 0.15
Nodes (12): _route(), KeyRequest, KeysRequest, _marks(), ProfileRequest, _read_map(), RefreshRequest, _send() (+4 more)

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 92 - "LeadStatus"
Cohesion: 0.31
Nodes (4): mark_lead(), is_open(), rank(), LeadStatus

### Community 94 - "create_server"
Cohesion: 0.33
Nodes (7): create_server(), _allowed(), do_GET(), do_POST(), _json(), _send_bytes(), _message()

### Community 95 - "datetime"
Cohesion: 0.09
Nodes (24): AshbyJob, AshbyResponse, Conference, Config, GitHubPosting, GreenhouseJob, GreenhouseLocation, GreenhouseResponse (+16 more)

### Community 98 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 99 - "FormQuestion"
Cohesion: 0.16
Nodes (12): _answer_for(), AnswerBank, common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+4 more)

### Community 101 - "test_patterns.py"
Cohesion: 0.17
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 103 - "Region"
Cohesion: 0.21
Nodes (10): hub(), in_area(), spread(), Region, _log_xai(), founder(), test_hub_cities_and_europe_are_separate_batches(), test_spread_splits_evenly_and_keeps_fit_order() (+2 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 107 - "web.py"
Cohesion: 0.29
Nodes (6): is_email(), Contact, WebPostings, find_contact(), published_on(), search_jobs()

### Community 111 - "test_lite.py"
Cohesion: 0.24
Nodes (4): _client_returning(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_web_search_keeps_only_valid_posting_urls()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

### Community 113 - "open_lead_store"
Cohesion: 0.33
Nodes (3): load_inbox(), open_lead_store(), scan()

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 644 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `big_companies.py`, `notify.py`, `run_followups`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `re`, `pytest`, `Settings`, `internship_agent/ai.py`, `app.py`, `simplify.py`, `QuestionKind`, `leads/cli.py`, `find_site_emails`, `test_people.py`, `leads/schemas.py`, `EmailStatus`, `agenda.py`, `test_refill.py`, `internship_agent/leads/sending.py`, `lead_store`, `pipeline.py`, `submit_application`, `_get`, `test_deadlines.py`, `followup_run.py`, `find-founders.md`, `batches`, `insights`, `send_email`, `followups.py`, `prepare_application`, `export.py`, `Table`, `LeadStatus`, `datetime`, `FormQuestion`, `test_patterns.py`, `Region`, `fit_to_limit`, `open_lead_store`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 135 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 135 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11693548387096774 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `OpportunityStore`, `run_followups`, `test_daily_campaign.py`, `pytest`, `internship_agent/cli.py`, `test_opportunities.py`, `get_settings`, `app.py`, `simplify.py`, `QuestionKind`, `client.py`, `leads/cli.py`, `run.py`, `test_apply_events.py`, `Opportunity`, `find_site_emails`, `test_people.py`, `leads/schemas.py`, `EmailStatus`, `inboxes`, `test_chat.py`, `Lead`, `read_log`, `lead_store`, `pipeline.py`, `command`, `test_auto_pick.py`, `submit_application`, `_get`, `followup_run.py`, `local_only`, `find_events`, `list_cmd`, `send_email`, `config.py`, `prepare_application`, `Table`, `FormQuestion`, `test_patterns.py`, `Region`, `open_lead_store`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 104 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 104 INFERRED edges - model-reasoned connections that need verification._
- **Should `big_companies.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11538461538461539 - nodes in this community are weakly interconnected._