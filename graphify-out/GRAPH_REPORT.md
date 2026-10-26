# Graph Report - winter-2027-internship-agent  (2026-10-26)

## Corpus Check
- 143 files · ~650,198 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2052 nodes · 6116 edges · 111 communities (86 shown, 25 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1015 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `13c000e4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- simplify.py
- notify.py
- Table
- test_chat.py
- applications/browser.py
- test_application_browser.py
- ApplicationPrep
- form_d.py
- pytest
- internship_agent/cli.py
- json
- make_workflows.py
- README.md
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- discord.py
- QuestionKind
- check_events
- OutlookClient
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- Lead
- opportunities/schemas.py
- test_apply_events.py
- feeds.py
- command
- run
- run-lowest-30-applications.sh
- test_people.py
- find_startups
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- leads/schemas.py
- LeadStatus
- agenda.py
- Opportunity
- mailbox.py
- test_site_emails.py
- re
- preferences.py
- outlook/schemas.py
- send_email
- internship_agent/ai.py
- lead_store
- followups.py
- run_followups
- StepAction
- send
- opportunities/ai.py
- assess_fit
- followups_cmd
- test_auto_pick.py
- test_links.py
- FormQuestion
- datetime
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- _get
- find-founders.md
- urllib_parse
- typing
- workspace.py
- SentMessage
- run.py
- FakeField
- pipeline.py
- test_outlook_client.py
- candidate_context.md
- _scan_inboxes
- Settings
- pathlib
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- FakeToggle
- dashboard.py
- Workspace
- local_only
- AGENTS.md
- client.py
- opportunity_lite/cli.py
- Bot Auto application preview
- note
- connect
- inboxes
- run-email-batch.sh
- create_server
- pydantic
- os
- _post_submit_outcome
- test_scheduled_jobs.py
- answers.py
- _numeric_answer
- test_patterns.py
- ↗ Intern Agent
- web.py
- test_lite.py
- start.sh
- profile.example.md
- notify-failure.sh
- run-discord-scrape.sh
- intern-agent

## God Nodes (most connected - your core abstractions)
1. `Lead` - 189 edges
2. `Settings` - 123 edges
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
- `Application answers prepared from the resume` --references--> `prepare_answers()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (111 total, 25 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.15
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.07
Nodes (25): deliver(), build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment(), _event(), FakeBox (+17 more)

### Community 2 - "simplify.py"
Cohesion: 0.05
Nodes (36): Big-company postings from the SimplifyJobs off-season list, amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards() (+28 more)

### Community 3 - "notify.py"
Cohesion: 0.24
Nodes (12): _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer(), lead(), test_campaign_summary_reports_actual_result_and_shortfall() (+4 more)

### Community 5 - "test_chat.py"
Cohesion: 0.18
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.12
Nodes (16): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed() (+8 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.20
Nodes (17): _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_bachelor_degree_maps_to_greenhouse_degree_choice(), test_closed_posting_text_is_detected(), test_fill_form_blocks_unanswered_required_questions() (+9 more)

### Community 8 - "ApplicationPrep"
Cohesion: 0.06
Nodes (24): ApplicationPrep, FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare() (+16 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (17): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+9 more)

### Community 10 - "pytest"
Cohesion: 0.08
Nodes (37): dashboard(), _slug(), LeadStore, client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for() (+29 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.16
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "json"
Cohesion: 0.17
Nodes (12): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "README.md"
Cohesion: 0.11
Nodes (26): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+18 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (23): post(), get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run() (+15 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (25): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, delete_preference(), draft() (+17 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "discord.py"
Cohesion: 0.24
Nodes (4): application_url(), cards(), parse(), postings()

### Community 21 - "QuestionKind"
Cohesion: 0.20
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 22 - "check_events"
Cohesion: 0.13
Nodes (8): _candidate(), check_events(), one(), checked(), _keys(), _openai(), without_citations(), load_resume_text()

### Community 23 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 26 - "Lead"
Cohesion: 0.12
Nodes (13): hub(), in_area(), spread(), _email_line(), render_outreach(), point_at(), EmailStatus, Lead (+5 more)

### Community 27 - "opportunities/schemas.py"
Cohesion: 0.12
Nodes (12): next_step(), describe(), saved_browser(), sign_in_cmd(), apply_events(), step(), send_sessions(), sign_in() (+4 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.21
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "command"
Cohesion: 0.15
Nodes (6): browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd(), site_emails_cmd()

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "test_people.py"
Cohesion: 0.19
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 34 - "find_startups"
Cohesion: 0.19
Nodes (10): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), add_team_contacts(), find_people(), find_startups() (+2 more)

### Community 35 - "patterns.py"
Cohesion: 0.11
Nodes (13): guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), proven() (+5 more)

### Community 40 - "leads/schemas.py"
Cohesion: 0.09
Nodes (19): fit_to_limit(), FitResult, OutreachDraft, OutreachDraftResult, Round, Segment, Verdict, parse_round() (+11 more)

### Community 41 - "LeadStatus"
Cohesion: 0.09
Nodes (25): is_open(), rank(), drop_unavailable(), expire_closed(), is_workday(), open_postings(), refill(), LeadKind (+17 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "Opportunity"
Cohesion: 0.12
Nodes (13): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), mark_cmd(), refresh_cmd(), strategy_cmd(), auto_pick() (+5 more)

### Community 44 - "mailbox.py"
Cohesion: 0.16
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "test_site_emails.py"
Cohesion: 0.09
Nodes (8): test_postings_are_filtered_to_the_search_regions(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 46 - "re"
Cohesion: 0.24
Nodes (10): _clean(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+2 more)

### Community 47 - "preferences.py"
Cohesion: 0.16
Nodes (15): format_preferences(), apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings() (+7 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "send_email"
Cohesion: 0.13
Nodes (9): Send email safeguards, append(), check_outreach_text(), check_send(), SendBlocked, _log_xai(), _record_openai_usage(), send_email() (+1 more)

### Community 50 - "internship_agent/ai.py"
Cohesion: 0.07
Nodes (23): AnswerDraft, AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PersonFinding, PreferenceDraft, StartupFinding (+15 more)

### Community 51 - "lead_store"
Cohesion: 0.19
Nodes (9): Rules learned from notes (skip, downrank, boost), interpret_note(), find_form_d_startups(), handle_note(), lead_store(), NoteOutcome, rescore_open(), score() (+1 more)

### Community 52 - "followups.py"
Cohesion: 0.22
Nodes (6): first_name(), is_due(), last_contact(), next_followup(), test_a_follow_up_is_due_five_days_after_the_last_email(), test_nobody_gets_a_third_or_one_after_replying_or_being_skipped()

### Community 53 - "run_followups"
Cohesion: 0.10
Nodes (13): read_log(), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+5 more)

### Community 54 - "StepAction"
Cohesion: 0.14
Nodes (4): Element, _refusal(), PlaywrightPage, StepAction

### Community 56 - "opportunities/ai.py"
Cohesion: 0.23
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding(), test_without_citations_strips_inline_links_only()

### Community 57 - "assess_fit"
Cohesion: 0.26
Nodes (6): assess_fit(), draft_outreach(), _lead_context(), prepare_answers(), prepare_cover_letter(), search_startups()

### Community 58 - "followups_cmd"
Cohesion: 0.13
Nodes (11): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd(), scrape_discord_cmd() (+3 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "test_links.py"
Cohesion: 0.22
Nodes (6): hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about()

### Community 61 - "FormQuestion"
Cohesion: 0.35
Nodes (6): _answer_for(), AnswerBank, FormQuestion, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 62 - "datetime"
Cohesion: 0.22
Nodes (6): find_deadline(), posting(), test_expire_closed_skips_open_postings_that_are_gone(), test_expire_postings_skips_only_open_postings_past_deadline(), test_finds_a_stated_deadline(), test_ignores_text_without_a_full_dated_deadline()

### Community 64 - "_get"
Cohesion: 0.11
Nodes (12): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get(), health(), _icon() (+4 more)

### Community 65 - "find-founders.md"
Cohesion: 0.11
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+4 more)

### Community 66 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 67 - "typing"
Cohesion: 0.28
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "workspace.py"
Cohesion: 0.20
Nodes (11): draft_message(), Draft, Listing, filter_items(), load(), merge(), save(), searchable_text() (+3 more)

### Community 70 - "run.py"
Cohesion: 0.08
Nodes (22): Region, page_url(), Push, list_cmd(), applied_push(), find_events(), import_inbox(), keep() (+14 more)

### Community 71 - "FakeField"
Cohesion: 0.09
Nodes (6): FakeField, FakeLocator, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 72 - "pipeline.py"
Cohesion: 0.09
Nodes (23): board(), _bounced_lead(), _card(), classify(), confirmed_postings(), display_company(), events(), _header() (+15 more)

### Community 73 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "_scan_inboxes"
Cohesion: 0.29
Nodes (3): _scan_forever(), _scan_inboxes(), _start_inbox_scans()

### Community 76 - "Settings"
Cohesion: 0.33
Nodes (16): Settings, emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+8 more)

### Community 77 - "pathlib"
Cohesion: 0.10
Nodes (11): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+3 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.10
Nodes (16): common_questions(), expire_postings(), answer_bank(), daily(), DailyReport, _incompatible_term(), _only_live(), prepare_application() (+8 more)

### Community 83 - "dashboard.py"
Cohesion: 0.15
Nodes (12): _route(), KeyRequest, KeysRequest, _marks(), ProfileRequest, _read_map(), RefreshRequest, _send() (+4 more)

### Community 84 - "Workspace"
Cohesion: 0.19
Nodes (11): _drafts(), _listing(), _resume_chars(), state(), view(), background(), draft_id(), make_draft() (+3 more)

### Community 85 - "local_only"
Cohesion: 0.29
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 87 - "client.py"
Cohesion: 0.22
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "opportunity_lite/cli.py"
Cohesion: 0.29
Nodes (4): main(), _parser(), serve(), load_env()

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 91 - "connect"
Cohesion: 0.29
Nodes (4): run(), connect(), interview_events(), test_interview_events()

### Community 94 - "create_server"
Cohesion: 0.33
Nodes (7): create_server(), _allowed(), do_GET(), do_POST(), _json(), _send_bytes(), _message()

### Community 95 - "pydantic"
Cohesion: 0.10
Nodes (24): AshbyJob, AshbyResponse, Conference, Config, GitHubPosting, GreenhouseJob, GreenhouseLocation, GreenhouseResponse (+16 more)

### Community 97 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

### Community 99 - "answers.py"
Cohesion: 0.17
Nodes (7): category(), match_option(), normalize(), prefill(), validate(), save_answers(), test_yes_no_answer_matches_long_select_options()

### Community 101 - "test_patterns.py"
Cohesion: 0.17
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 107 - "web.py"
Cohesion: 0.29
Nodes (6): is_email(), Contact, WebPostings, find_contact(), published_on(), search_jobs()

### Community 111 - "test_lite.py"
Cohesion: 0.13
Nodes (9): prepare_email(), SendRequest, StoredDraft, _client_returning(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_resume_is_read_and_attached(), test_send_requires_explicit_confirmation_and_blocks_duplicate() (+1 more)

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 648 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **25 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `simplify.py`, `notify.py`, `Table`, `applications/browser.py`, `test_application_browser.py`, `ApplicationPrep`, `form_d.py`, `pytest`, `get_settings`, `app.py`, `discord.py`, `QuestionKind`, `leads/cli.py`, `find_startups`, `patterns.py`, `leads/schemas.py`, `LeadStatus`, `agenda.py`, `test_site_emails.py`, `preferences.py`, `send_email`, `internship_agent/ai.py`, `lead_store`, `followups.py`, `run_followups`, `assess_fit`, `FormQuestion`, `datetime`, `_get`, `find-founders.md`, `typing`, `pipeline.py`, `Settings`, `pathlib`, `workflows.py`, `answers.py`, `test_patterns.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 136 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 136 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06666666666666667 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `simplify.py`, `Table`, `test_chat.py`, `ApplicationPrep`, `json`, `test_opportunities.py`, `get_settings`, `app.py`, `QuestionKind`, `check_events`, `leads/cli.py`, `Lead`, `opportunities/schemas.py`, `test_apply_events.py`, `test_people.py`, `find_startups`, `patterns.py`, `LeadStatus`, `Opportunity`, `test_site_emails.py`, `preferences.py`, `send_email`, `lead_store`, `run_followups`, `followups_cmd`, `test_auto_pick.py`, `FormQuestion`, `_get`, `run.py`, `pipeline.py`, `pathlib`, `workflows.py`, `local_only`, `client.py`, `connect`, `inboxes`, `answers.py`, `test_patterns.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 105 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05297334244702666 - nodes in this community are weakly interconnected._