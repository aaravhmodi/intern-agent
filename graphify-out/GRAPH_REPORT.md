# Graph Report - winter-2027-internship-agent  (2026-10-25)

## Corpus Check
- 143 files · ~649,575 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2044 nodes · 6091 edges · 116 communities (90 shown, 26 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1015 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7072980`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- big_companies.py
- notify.py
- StepAction
- test_followups.py
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- pytest
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- Opportunity
- get_settings
- tracking.py
- app.py
- collections_abc
- simplify.py
- FormQuestion
- opportunities/ai.py
- client.py
- run-application-campaign-2026-10-16.sh
- _store
- x_search.py
- check_events
- test_apply_events.py
- feeds.py
- command
- run
- run-lowest-30-applications.sh
- test_people.py
- Segment
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Settings
- README.md
- agenda.py
- test_chat.py
- mailbox.py
- scrape_jobs
- posting_text.py
- Lead
- outlook/schemas.py
- send_email
- re
- test_ai.py
- test_outlook_client.py
- Mailbox
- opportunities/browser.py
- set_status
- apply_events
- to_event
- followups_cmd
- test_auto_pick.py
- EmailStatus
- _get
- LeadStatus
- run_followups
- local_only
- find-founders.md
- urllib_parse
- batches
- workspace.py
- AGENTS.md
- run.py
- FakeField
- pipeline.py
- test_notes.py
- candidate_context.md
- find-internships.md
- followups.py
- opportunities/schemas.py
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- leads/cli.py
- opportunity_lite/leads/sending.py
- Workspace
- SentMessage
- PreferenceStore
- outlook
- dashboard.py
- Bot Auto application preview
- send
- _scan_inboxes
- rank
- run-email-batch.sh
- create_server
- datetime
- test_interview_events
- results
- test_scheduled_jobs.py
- AnswerBank
- test_form_d.py
- test_patterns.py
- guess_email
- test_career_sites.py
- test_hidden_recaptcha_support_nodes_do_not_block
- ↗ Intern Agent
- leads/schemas.py
- web.py
- test_devpost_dates
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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (116 total, 26 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.13
Nodes (13): BrowserStep, FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site() (+5 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.07
Nodes (25): deliver(), build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment(), _event(), FakeBox (+17 more)

### Community 2 - "big_companies.py"
Cohesion: 0.13
Nodes (19): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards(), fetch() (+11 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (16): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+8 more)

### Community 4 - "StepAction"
Cohesion: 0.13
Nodes (4): Page, StepAction, SubmissionStrategy, SubmissionTrack

### Community 5 - "test_followups.py"
Cohesion: 0.22
Nodes (18): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+10 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.21
Nodes (15): _fill_form(), _numeric_answer(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass() (+7 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.06
Nodes (19): FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), submit() (+11 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (18): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+10 more)

### Community 10 - "pytest"
Cohesion: 0.05
Nodes (48): dashboard(), LeadStore, no_real_services(), _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items() (+40 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.17
Nodes (12): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.16
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 15 - "Opportunity"
Cohesion: 0.13
Nodes (27): mark_cmd(), auto_pick(), plan_submission(), Opportunity, OpportunityStore, _assessment(), _fake_ai(), _opp() (+19 more)

### Community 16 - "get_settings"
Cohesion: 0.15
Nodes (23): post(), get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run() (+15 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (22): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, delete_preference(), FindMoreRequest (+14 more)

### Community 19 - "collections_abc"
Cohesion: 0.14
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "simplify.py"
Cohesion: 0.07
Nodes (18): Big-company postings from the SimplifyJobs off-season list, application_url(), cards(), parse(), postings(), _cell(), parse(), postings() (+10 more)

### Community 21 - "FormQuestion"
Cohesion: 0.14
Nodes (19): category(), match_option(), validate(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions() (+11 more)

### Community 22 - "opportunities/ai.py"
Cohesion: 0.29
Nodes (7): assess(), EventFinding, EventFindings, search_events(), write_strategy(), test_find_events_keeps_only_dated_events_whose_page_names_them(), finding()

### Community 23 - "client.py"
Cohesion: 0.19
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "_store"
Cohesion: 0.26
Nodes (8): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), score_leads(), _store()

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (9): search_startups(), StartupFinding, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 27 - "check_events"
Cohesion: 0.12
Nodes (8): normalize_url(), _candidate(), check_events(), one(), checked(), _keys(), _openai(), without_citations()

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.25
Nodes (10): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+2 more)

### Community 30 - "command"
Cohesion: 0.12
Nodes (8): browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd(), show_lead(), site_emails_cmd()

### Community 31 - "run"
Cohesion: 0.13
Nodes (11): allowed(), _host(), names_event(), nothing_to_sign_in(), _quote(), _refusal(), resolve(), run() (+3 more)

### Community 33 - "test_people.py"
Cohesion: 0.22
Nodes (8): PersonFinding, _on_linkedin(), source_names(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 34 - "Segment"
Cohesion: 0.09
Nodes (23): More people to connect with, chosen by company size, search_people(), Person, Round, Segment, effective_segment(), parse_round(), to_people() (+15 more)

### Community 35 - "patterns.py"
Cohesion: 0.15
Nodes (9): bounced_addresses(), domain_of(), format_of(), next_guess(), point_at(), proven(), role_of(), wants_email() (+1 more)

### Community 40 - "Settings"
Cohesion: 0.15
Nodes (5): Settings, append(), read_log(), _logged_subject(), inboxes()

### Community 41 - "README.md"
Cohesion: 0.14
Nodes (21): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Development (+13 more)

### Community 42 - "agenda.py"
Cohesion: 0.22
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 44 - "mailbox.py"
Cohesion: 0.15
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "scrape_jobs"
Cohesion: 0.10
Nodes (14): expire_postings(), is_workday(), open_postings(), refill(), _only_live(), scrape_discord(), scrape_jobs(), posting() (+6 more)

### Community 46 - "posting_text.py"
Cohesion: 0.33
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 47 - "Lead"
Cohesion: 0.07
Nodes (18): Table, hub(), in_area(), spread(), Lead, LeadKind, _identity(), merge() (+10 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "send_email"
Cohesion: 0.24
Nodes (6): Send email safeguards, check_outreach_text(), check_send(), SendBlocked, send_email(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 50 - "re"
Cohesion: 0.24
Nodes (5): _clean(), _slug(), _meta(), mlh(), post_text()

### Community 51 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 52 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 54 - "opportunities/browser.py"
Cohesion: 0.14
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "set_status"
Cohesion: 0.15
Nodes (13): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), note(), NoteRequest, set_status(), StatusUpdate, Dashboard page (index.html) (+5 more)

### Community 56 - "apply_events"
Cohesion: 0.27
Nodes (6): next_step(), describe(), apply_events(), step(), sign_in(), step()

### Community 57 - "to_event"
Cohesion: 0.14
Nodes (11): company_domain(), _bounced_lead(), classify(), confirmed_postings(), _header(), _host(), _is_ats(), match() (+3 more)

### Community 58 - "followups_cmd"
Cohesion: 0.13
Nodes (10): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd(), scrape_discord_cmd() (+2 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "EmailStatus"
Cohesion: 0.25
Nodes (6): EmailStatus, lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 61 - "_get"
Cohesion: 0.12
Nodes (11): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), event_proof(), _get(), health() (+3 more)

### Community 62 - "LeadStatus"
Cohesion: 0.16
Nodes (11): find_deadline(), expire_closed(), ApplicationPrep, LeadStatus, posting(), test_closed_or_blocked_applications_are_removed_but_a_missing_resume_is_not(), tried(), test_expire_closed_skips_open_postings_that_are_gone() (+3 more)

### Community 63 - "run_followups"
Cohesion: 0.23
Nodes (8): FollowupReport, FollowupSent, _misaddressed(), _name(), run_followups(), _site(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 64 - "local_only"
Cohesion: 0.29
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 65 - "find-founders.md"
Cohesion: 0.20
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, export_drafts(), import_leads(), load_inbox()

### Community 66 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "workspace.py"
Cohesion: 0.17
Nodes (16): _listing(), draft_message(), Draft, Listing, filter_items(), load(), merge(), save() (+8 more)

### Community 70 - "run.py"
Cohesion: 0.08
Nodes (20): Region, page_url(), applied_push(), import_inbox(), keep(), nearby(), next_date(), pick_reason() (+12 more)

### Community 71 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 72 - "pipeline.py"
Cohesion: 0.15
Nodes (13): board(), _card(), display_company(), events(), InboxEvent, insights(), got(), split() (+5 more)

### Community 73 - "test_notes.py"
Cohesion: 0.33
Nodes (5): posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "find-internships.md"
Cohesion: 0.25
Nodes (5): Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look

### Community 76 - "followups.py"
Cohesion: 0.21
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), next_followup(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 77 - "opportunities/schemas.py"
Cohesion: 0.07
Nodes (18): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), refresh_cmd(), sign_in_cmd(), strategy_cmd() (+10 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.08
Nodes (26): common_questions(), normalize(), drop_unavailable(), Note, add_team_contacts(), answer_bank(), daily(), DailyReport (+18 more)

### Community 82 - "leads/cli.py"
Cohesion: 0.23
Nodes (4): _resume(), _email_line(), render_outreach(), load_resume_text()

### Community 83 - "opportunity_lite/leads/sending.py"
Cohesion: 0.22
Nodes (6): _send(), prepare_email(), SendRequest, StoredDraft, test_resume_is_read_and_attached(), test_send_requires_explicit_confirmation_and_blocks_duplicate()

### Community 84 - "Workspace"
Cohesion: 0.19
Nodes (9): main(), _drafts(), _resume_chars(), state(), view(), Config, load_env(), Workspace (+1 more)

### Community 86 - "PreferenceStore"
Cohesion: 0.28
Nodes (8): apply_violations(), PreferenceStore, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_preference_store_dedupes_and_removes(), test_rules_answers_and_logs_live_in_tables()

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "dashboard.py"
Cohesion: 0.14
Nodes (8): _parser(), KeyRequest, KeysRequest, ProfileRequest, RefreshRequest, SendBody, serve(), StatusRequest

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 92 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 94 - "create_server"
Cohesion: 0.19
Nodes (12): create_server(), _allowed(), do_GET(), do_POST(), _json(), _route(), _send_bytes(), _marks() (+4 more)

### Community 95 - "datetime"
Cohesion: 0.09
Nodes (24): AshbyJob, AshbyResponse, Conference, Contact, GitHubPosting, GreenhouseJob, GreenhouseLocation, GreenhouseResponse (+16 more)

### Community 97 - "results"
Cohesion: 0.38
Nodes (3): by_domain(), outcomes(), results()

### Community 99 - "AnswerBank"
Cohesion: 0.22
Nodes (6): _answer_for(), AnswerBank, prefill(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 101 - "test_patterns.py"
Cohesion: 0.20
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 106 - "leads/schemas.py"
Cohesion: 0.11
Nodes (6): fit_to_limit(), _normalize(), OutreachDraft, Verdict, test_fit_to_limit_prefers_sentence_then_word_boundary(), test_tables()

### Community 107 - "web.py"
Cohesion: 0.31
Nodes (5): is_email(), WebPostings, find_contact(), published_on(), search_jobs()

### Community 111 - "test_lite.py"
Cohesion: 0.21
Nodes (4): _client_returning(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_web_search_keeps_only_valid_posting_urls()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 646 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `big_companies.py`, `notify.py`, `test_followups.py`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `pytest`, `internship_agent/ai.py`, `get_settings`, `app.py`, `simplify.py`, `FormQuestion`, `_store`, `Segment`, `patterns.py`, `agenda.py`, `scrape_jobs`, `send_email`, `set_status`, `to_event`, `EmailStatus`, `_get`, `LeadStatus`, `run_followups`, `find-founders.md`, `batches`, `run.py`, `pipeline.py`, `test_notes.py`, `find-internships.md`, `followups.py`, `workflows.py`, `leads/cli.py`, `PreferenceStore`, `rank`, `datetime`, `results`, `AnswerBank`, `test_patterns.py`, `leads/schemas.py`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 136 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 136 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_sign_in.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1330049261083744 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `notify.py`, `test_followups.py`, `test_daily_campaign.py`, `form_d.py`, `pytest`, `internship_agent/cli.py`, `json`, `Opportunity`, `get_settings`, `app.py`, `simplify.py`, `FormQuestion`, `client.py`, `_store`, `check_events`, `test_apply_events.py`, `test_people.py`, `Segment`, `patterns.py`, `test_chat.py`, `scrape_jobs`, `Lead`, `send_email`, `apply_events`, `followups_cmd`, `test_auto_pick.py`, `EmailStatus`, `_get`, `run_followups`, `local_only`, `run.py`, `pipeline.py`, `test_notes.py`, `opportunities/schemas.py`, `workflows.py`, `leads/cli.py`, `PreferenceStore`, `AnswerBank`, `test_patterns.py`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 105 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06857142857142857 - nodes in this community are weakly interconnected._