# Graph Report - winter-2027-internship-agent  (2026-10-25)

## Corpus Check
- 143 files · ~649,238 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2037 nodes · 6074 edges · 119 communities (93 shown, 26 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1006 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0c4ccb6a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- big_companies.py
- notify.py
- Opportunity
- test_followups.py
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- test_dashboard.py
- connect
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- Any
- tracking.py
- app.py
- verification_mail.py
- LeadStore
- FormQuestion
- opportunities/ai.py
- client.py
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- x_search.py
- run.py
- test_apply_events.py
- feeds.py
- urllib_parse
- run
- run-lowest-30-applications.sh
- test_people.py
- leads/schemas.py
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Settings
- README.md
- agenda.py
- test_chat.py
- mailbox.py
- test_refill.py
- Table
- Lead
- outlook/schemas.py
- EmailStatus
- sync
- test_ai.py
- pytest
- SentMessage
- opportunities/browser.py
- set_status
- datetime
- pipeline.py
- command
- test_auto_pick.py
- StepAction
- get_settings
- LeadStatus
- run_followups
- local_only
- find-founders.md
- re
- batches
- workspace.py
- AGENTS.md
- OpportunityStatus
- FakeToggle
- insights
- internship_agent/mailer.py
- candidate_context.md
- test_links.py
- followups.py
- command
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- export.py
- test_lite.py
- Workspace
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- preferences.py
- outlook
- dashboard.py
- Bot Auto application preview
- models.py
- guess_email
- ranking.py
- run-email-batch.sh
- create_server
- Listing
- test_tracking.py
- find_more
- test_verification_mail.py
- AnswerBank
- test_career_sites.py
- test_patterns.py
- test_agenda.py
- Region
- _view
- ↗ Intern Agent
- OutreachDraft
- web.py
- Snapshot
- followups_cmd
- test_scheduled_jobs.py
- os
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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (119 total, 26 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (19): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_confirmation_closes_the_open_posting_it_names() (+11 more)

### Community 2 - "big_companies.py"
Cohesion: 0.05
Nodes (31): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), application_url(), cards() (+23 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 4 - "Opportunity"
Cohesion: 0.14
Nodes (11): mark_cmd(), refresh_cmd(), auto_pick(), find_events(), plan_submission(), summary_push(), Opportunity, OpportunityStore (+3 more)

### Community 5 - "test_followups.py"
Cohesion: 0.32
Nodes (17): emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, _slug(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (17): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+9 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.18
Nodes (15): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_health_says_busy_while_a_long_job_runs() (+7 more)

### Community 11 - "connect"
Cohesion: 0.12
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.18
Nodes (11): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.17
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "Any"
Cohesion: 0.15
Nodes (17): post(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run(), draft() (+9 more)

### Community 17 - "tracking.py"
Cohesion: 0.30
Nodes (5): MailMessage, application_updates(), ApplicationUpdate, guess_company(), to_update()

### Community 18 - "app.py"
Cohesion: 0.08
Nodes (22): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, followups(), FollowupsRequest (+14 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (6): extract_sign_in(), _message_text(), _poll(), _raw_text(), wait_for_sign_in(), inbox()

### Community 20 - "LeadStore"
Cohesion: 0.33
Nodes (4): LeadStore, test_auto_apply_prepares_then_submits(), test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 21 - "FormQuestion"
Cohesion: 0.16
Nodes (17): match_option(), validate(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions() (+9 more)

### Community 22 - "opportunities/ai.py"
Cohesion: 0.26
Nodes (7): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding()

### Community 23 - "client.py"
Cohesion: 0.13
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 25 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (10): search_startups(), StartupFinding, StartupFindings, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising() (+2 more)

### Community 27 - "run.py"
Cohesion: 0.09
Nodes (18): next_step(), describe(), apply_events(), step(), _candidate(), check_events(), one(), checked() (+10 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.20
Nodes (14): _event(), landing(), _settings(), step(), steps(), test_allowed_sites(), test_apply_events_saves_the_result_and_marks_it_submitted(), fake_browser() (+6 more)

### Community 29 - "feeds.py"
Cohesion: 0.19
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 30 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 31 - "run"
Cohesion: 0.13
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), _quote(), _refusal(), resolve(), run() (+2 more)

### Community 33 - "test_people.py"
Cohesion: 0.13
Nodes (11): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names(), page_names(), source_confirms(), person(), test_a_linkedin_source_passes_without_being_fetched() (+3 more)

### Community 34 - "leads/schemas.py"
Cohesion: 0.13
Nodes (16): Round, Segment, Verdict, parse_round(), mentions(), names(), to_leads(), finding() (+8 more)

### Community 35 - "patterns.py"
Cohesion: 0.12
Nodes (12): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+4 more)

### Community 40 - "Settings"
Cohesion: 0.15
Nodes (8): Settings, append(), inboxes(), inbox_send(), _log_xai(), _run_ai_cost(), send_email(), sent_note()

### Community 41 - "README.md"
Cohesion: 0.12
Nodes (25): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Current setup, Development (+17 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 44 - "mailbox.py"
Cohesion: 0.17
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "test_refill.py"
Cohesion: 0.20
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 47 - "Lead"
Cohesion: 0.09
Nodes (25): Big-company postings from the SimplifyJobs off-season list, role_of(), is_workday(), open_postings(), refill(), Lead, LeadKind, merge() (+17 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.36
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "EmailStatus"
Cohesion: 0.13
Nodes (10): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends(), lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first() (+2 more)

### Community 50 - "sync"
Cohesion: 0.21
Nodes (8): board(), _card(), display_company(), events(), InboxEvent, push_for(), scan(), sync()

### Community 51 - "test_ai.py"
Cohesion: 0.21
Nodes (7): FitAssessment, FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 52 - "pytest"
Cohesion: 0.22
Nodes (16): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+8 more)

### Community 54 - "opportunities/browser.py"
Cohesion: 0.14
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "set_status"
Cohesion: 0.50
Nodes (3): set_status(), StatusUpdate, Lead detail panel: fit, links, contact, actions

### Community 56 - "datetime"
Cohesion: 0.12
Nodes (4): _identity(), normalize_url(), SubmissionTrack, test_tables()

### Community 57 - "pipeline.py"
Cohesion: 0.17
Nodes (11): company_domain(), _bounced_lead(), classify(), confirmed_postings(), _header(), _host(), _is_ats(), match() (+3 more)

### Community 58 - "command"
Cohesion: 0.11
Nodes (13): application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_startups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd() (+5 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.26
Nodes (8): OpportunityAssessment, check(), hack(), reason(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition(), test_push_names_what_was_picked()

### Community 61 - "get_settings"
Cohesion: 0.16
Nodes (12): get_settings(), application_proof(), calendar(), calendar_ics(), _calendar_items(), event_proof(), _get(), job_pipeline() (+4 more)

### Community 62 - "LeadStatus"
Cohesion: 0.14
Nodes (13): find_deadline(), drop_unavailable(), expire_closed(), expire_postings(), LeadStatus, Note, posting(), test_closed_or_blocked_applications_are_removed_but_a_missing_resume_is_not() (+5 more)

### Community 63 - "run_followups"
Cohesion: 0.12
Nodes (12): read_log(), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+4 more)

### Community 64 - "local_only"
Cohesion: 0.20
Nodes (6): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, dashboard_css(), _icon(), local_only()

### Community 65 - "find-founders.md"
Cohesion: 0.13
Nodes (10): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+2 more)

### Community 66 - "re"
Cohesion: 0.30
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "workspace.py"
Cohesion: 0.23
Nodes (8): filter_items(), load(), merge(), save(), searchable_text(), openai_client(), refresh(), test_merge_and_keyword_filter()

### Community 70 - "OpportunityStatus"
Cohesion: 0.23
Nodes (9): list_cmd(), keep(), nearby(), next_date(), pick_reason(), upcoming(), worth_checking(), OpportunityKind (+1 more)

### Community 71 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 72 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 73 - "internship_agent/mailer.py"
Cohesion: 0.16
Nodes (6): deliver(), build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "test_links.py"
Cohesion: 0.22
Nodes (6): hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about()

### Community 76 - "followups.py"
Cohesion: 0.27
Nodes (4): first_name(), is_due(), last_contact(), next_followup()

### Community 77 - "command"
Cohesion: 0.09
Nodes (9): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), sign_in_cmd(), strategy_cmd(), applied_push(), import_inbox() (+1 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.07
Nodes (31): wait_for_greenhouse_code(), common_questions(), normalize(), effective_segment(), to_people(), answer_bank(), daily(), DailyReport (+23 more)

### Community 83 - "test_lite.py"
Cohesion: 0.11
Nodes (12): prepare_email(), SendRequest, StoredDraft, _client_returning(), test_conferences_filter_past_and_allow_blank_dates(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_github_list_keeps_recent_open_rows_and_skips_bad_ones() (+4 more)

### Community 84 - "Workspace"
Cohesion: 0.19
Nodes (12): _drafts(), _listing(), _resume_chars(), state(), view(), Config, background(), draft_id() (+4 more)

### Community 86 - "preferences.py"
Cohesion: 0.15
Nodes (16): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings() (+8 more)

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "dashboard.py"
Cohesion: 0.13
Nodes (10): main(), _parser(), KeyRequest, KeysRequest, ProfileRequest, RefreshRequest, SendBody, serve() (+2 more)

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 90 - "models.py"
Cohesion: 0.15
Nodes (14): draft_message(), AshbyJob, AshbyResponse, Conference, Contact, Draft, GitHubPosting, GreenhouseJob (+6 more)

### Community 91 - "guess_email"
Cohesion: 0.38
Nodes (3): Output, _clean(), guess_email()

### Community 94 - "create_server"
Cohesion: 0.18
Nodes (13): create_server(), _allowed(), do_GET(), do_POST(), _json(), _route(), _send_bytes(), _marks() (+5 more)

### Community 95 - "Listing"
Cohesion: 0.24
Nodes (11): Listing, ashby(), collect(), conferences(), fetch_json(), github_list(), greenhouse(), lever() (+3 more)

### Community 96 - "test_tracking.py"
Cohesion: 0.29
Nodes (8): classify_text(), Stage, message(), test_application_updates_skips_unrelated_mail(), test_classify_text_stages(), test_guess_company_prefers_display_name_then_domain(), test_interview_events(), test_rejection_beats_interview_wording()

### Community 98 - "test_verification_mail.py"
Cohesion: 0.15
Nodes (6): _extract_code(), VerificationCode, message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 99 - "AnswerBank"
Cohesion: 0.20
Nodes (7): _answer_for(), AnswerBank, prefill(), test_prefill_uses_bank_and_flags_personal(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 100 - "test_career_sites.py"
Cohesion: 0.12
Nodes (3): test_postings_are_filtered_to_the_search_regions(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name()

### Community 101 - "test_patterns.py"
Cohesion: 0.20
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 102 - "test_agenda.py"
Cohesion: 0.23
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 103 - "Region"
Cohesion: 0.29
Nodes (8): hub(), in_area(), spread(), Region, founder(), test_hub_cities_and_europe_are_separate_batches(), test_spread_splits_evenly_and_keeps_fit_order(), test_unknown_area_is_rejected()

### Community 104 - "_view"
Cohesion: 0.18
Nodes (11): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), delete_preference(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest, PreferenceDelete (+3 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 106 - "OutreachDraft"
Cohesion: 0.18
Nodes (3): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 107 - "web.py"
Cohesion: 0.33
Nodes (4): is_email(), find_contact(), published_on(), search_jobs()

### Community 109 - "followups_cmd"
Cohesion: 0.29
Nodes (3): followups_cmd(), page_url(), test_page_urls_open_a_view_or_one_item()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 644 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `big_companies.py`, `notify.py`, `test_followups.py`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `internship_agent/ai.py`, `app.py`, `LeadStore`, `FormQuestion`, `leads/cli.py`, `leads/schemas.py`, `patterns.py`, `Settings`, `agenda.py`, `test_refill.py`, `Table`, `EmailStatus`, `sync`, `test_ai.py`, `pytest`, `set_status`, `datetime`, `pipeline.py`, `get_settings`, `LeadStatus`, `run_followups`, `find-founders.md`, `batches`, `insights`, `followups.py`, `workflows.py`, `export.py`, `preferences.py`, `ranking.py`, `AnswerBank`, `test_patterns.py`, `test_agenda.py`, `Region`, `_view`, `OutreachDraft`, `open_lead_store`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 135 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 135 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11693548387096774 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Opportunity`, `test_followups.py`, `test_daily_campaign.py`, `connect`, `json`, `test_opportunities.py`, `app.py`, `FormQuestion`, `client.py`, `leads/cli.py`, `run.py`, `test_apply_events.py`, `feeds.py`, `test_people.py`, `patterns.py`, `test_chat.py`, `Table`, `Lead`, `EmailStatus`, `sync`, `datetime`, `pipeline.py`, `command`, `get_settings`, `run_followups`, `local_only`, `OpportunityStatus`, `command`, `workflows.py`, `preferences.py`, `AnswerBank`, `test_patterns.py`, `test_agenda.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 104 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 104 INFERRED edges - model-reasoned connections that need verification._
- **Should `big_companies.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05442428730099963 - nodes in this community are weakly interconnected._