# Graph Report - team-filter  (2026-11-09)

## Corpus Check
- 139 files · ~291,130 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 32 file(s) not represented in the graph (top: .timer 12, .service 9, (none) 6)

## Summary
- 2082 nodes · 6259 edges · 108 communities (87 shown, 21 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1020 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7d7b019e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_dashboard.py
- test_chat.py
- notify.py
- leads/store.py
- pytest
- applications/browser.py
- test_application_browser.py
- ApplicationPrep
- form_d.py
- test_pipeline.py
- internship_agent/cli.py
- Settings
- make_workflows.py
- README.md
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- simplify.py
- FormQuestion
- mailer.py
- client.py
- run-application-campaign-2026-10-16.sh
- test_verification_mail.py
- Region
- test_agenda.py
- test_apply_events.py
- feeds.py
- Opportunity
- run
- run-lowest-30-applications.sh
- test_ai.py
- test_people.py
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- leads/schemas.py
- re
- agenda.py
- run.py
- mailbox.py
- contacts.py
- posting_text.py
- PreferenceStore
- outlook/schemas.py
- page_url
- test_refill.py
- fit_to_limit
- Lead
- run_followups
- StepAction
- LeadStore
- opportunities/ai.py
- internship_agent/ai.py
- leads/cli.py
- test_auto_pick.py
- internship_agent/__init__.py
- answers.py
- LeadStatus
- startup_jobs.py
- _TableParser
- guess_email
- html
- typing
- test_notes.py
- SentMessage
- keep
- pipeline.py
- test_site_emails.py
- _get
- hn_hiring.py
- test_followups.py
- candidate_context.md
- GmailMailbox
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- FakeToggle
- test_form_d.py
- job_pipeline
- draft
- AGENTS.md
- outlook
- test_job_feeds.py
- Bot Auto application preview
- _view
- classify_text
- opportunities/schemas.py
- run-email-batch.sh
- save
- test_funding_news.py
- Snapshot
- test_scheduled_jobs.py
- test_patterns.py
- AgZen outreach drafts (not sent)
- send
- pathlib
- run-lead-search.sh
- run-followups.sh
- start.sh
- notify-failure.sh
- run-discord-scrape.sh

## God Nodes (most connected - your core abstractions)
1. `Lead` - 209 edges
2. `Settings` - 139 edges
3. `get_settings()` - 86 edges
4. `Opportunity` - 73 edges
5. `LeadKind` - 60 edges
6. `LeadStatus` - 60 edges
7. `Region` - 52 edges
8. `OpportunityStore` - 43 edges
9. `run_followups()` - 42 edges
10. `lead_store()` - 36 edges

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

## Communities (108 total, 21 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_dashboard.py"
Cohesion: 0.18
Nodes (16): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_health_says_busy_while_a_long_job_runs() (+8 more)

### Community 2 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (15): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer() (+7 more)

### Community 4 - "leads/store.py"
Cohesion: 0.10
Nodes (3): Table, load_inbox(), PostgresLeadStore

### Community 5 - "pytest"
Cohesion: 0.25
Nodes (15): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+7 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.10
Nodes (21): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), _post_submit_outcome(), _posting_is_closed() (+13 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "ApplicationPrep"
Cohesion: 0.09
Nodes (18): ApplicationPrep, FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare() (+10 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (18): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+10 more)

### Community 10 - "test_pipeline.py"
Cohesion: 0.11
Nodes (23): _event(), FakeBox, lead(), mail(), _settings(), test_a_dragged_card_stays_put_until_a_newer_email(), test_a_founders_answer_is_read_without_the_quoted_thread(), test_board_columns_follow_the_latest_email() (+15 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "Settings"
Cohesion: 0.10
Nodes (18): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+10 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "README.md"
Cohesion: 0.11
Nodes (30): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+22 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), CheckRequest, daily_run() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.35
Nodes (5): MailMessage, application_updates(), ApplicationUpdate, guess_company(), to_update()

### Community 18 - "app.py"
Cohesion: 0.08
Nodes (24): AnswerEdit, browser_sessions(), CardMove, Cookie, delete_preference(), find_more(), FindMoreRequest, followups() (+16 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "simplify.py"
Cohesion: 0.08
Nodes (15): normalize_url(), application_url(), cards(), parse(), postings(), _cell(), parse(), postings() (+7 more)

### Community 21 - "FormQuestion"
Cohesion: 0.21
Nodes (15): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q() (+7 more)

### Community 22 - "mailer.py"
Cohesion: 0.21
Nodes (6): build_message(), MailError, RecipientRefused, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 23 - "client.py"
Cohesion: 0.14
Nodes (9): OutlookClient, OutlookError, ToolSession, CalendarEvent, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises() (+1 more)

### Community 25 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 26 - "Region"
Cohesion: 0.11
Nodes (21): hub(), in_area(), spread(), Region, matching(), wanted_location(), fetch(), matching() (+13 more)

### Community 27 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 28 - "test_apply_events.py"
Cohesion: 0.23
Nodes (14): _event(), landing(), _settings(), step(), steps(), test_allowed_sites(), test_apply_events_saves_the_result_and_marks_it_submitted(), fake_browser() (+6 more)

### Community 29 - "feeds.py"
Cohesion: 0.22
Nodes (11): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+3 more)

### Community 30 - "Opportunity"
Cohesion: 0.22
Nodes (7): mark_cmd(), auto_pick(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "test_people.py"
Cohesion: 0.38
Nodes (6): person(), test_a_linkedin_source_passes_without_being_fetched(), test_big_tech_teams_drafts_a_note_about_their_team_and_the_batches_skip_them(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 35 - "EmailStatus"
Cohesion: 0.08
Nodes (19): _email_line(), render_outreach(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes() (+11 more)

### Community 40 - "leads/schemas.py"
Cohesion: 0.06
Nodes (26): search_startups(), StartupFinding, is_open(), LeadKind, Segment, Verdict, mentions(), source_confirms() (+18 more)

### Community 41 - "re"
Cohesion: 0.17
Nodes (17): Round, parse_round(), amount_usd(), build_candidates(), _clean_company(), company_from_title(), _date(), fetch_items() (+9 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "run.py"
Cohesion: 0.07
Nodes (21): next_step(), describe(), apply_events(), step(), _candidate(), check_events(), one(), checked() (+13 more)

### Community 44 - "mailbox.py"
Cohesion: 0.13
Nodes (8): bounce_search(), _imap_date(), _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_a_bounce_that_lands_before_sent_at_is_recorded_still_counts(), test_an_evening_send_searches_from_gmails_day_not_utcs(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "contacts.py"
Cohesion: 0.09
Nodes (24): company_key(), Contact, contact_type(), contacts_at(), contacts_from_leads(), add(), ContactType, _escape() (+16 more)

### Community 46 - "posting_text.py"
Cohesion: 0.33
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 47 - "PreferenceStore"
Cohesion: 0.26
Nodes (8): apply_violations(), PreferenceStore, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_preference_store_dedupes_and_removes(), test_rules_answers_and_logs_live_in_tables()

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "page_url"
Cohesion: 0.19
Nodes (7): page_url(), Push, send(), apply_cmd(), refresh_cmd(), applied_push(), summary_push()

### Community 50 - "test_refill.py"
Cohesion: 0.19
Nodes (7): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_posting_dates_come_from_the_source_or_the_day_found(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 52 - "Lead"
Cohesion: 0.08
Nodes (25): More people to connect with, chosen by company size, search_people(), role_of(), Lead, OutreachDraft, Person, _slug(), effective_segment() (+17 more)

### Community 53 - "run_followups"
Cohesion: 0.10
Nodes (17): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), _remind_unanswered(), run_followups(), _site() (+9 more)

### Community 54 - "StepAction"
Cohesion: 0.11
Nodes (6): Element, _refusal(), import_sessions(), PlaywrightPage, saved_browser(), StepAction

### Community 55 - "LeadStore"
Cohesion: 0.33
Nodes (4): LeadStore, test_auto_apply_prepares_then_submits(), test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.26
Nodes (7): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding()

### Community 57 - "internship_agent/ai.py"
Cohesion: 0.16
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (44): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+36 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.20
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "internship_agent/__init__.py"
Cohesion: 0.20
Nodes (7): hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about(), test_page_urls_open_a_view_or_one_item()

### Community 61 - "answers.py"
Cohesion: 0.14
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 62 - "LeadStatus"
Cohesion: 0.21
Nodes (9): find_deadline(), LeadStatus, posting(), test_closed_or_blocked_applications_are_removed_but_a_missing_resume_is_not(), tried(), test_expire_closed_skips_open_postings_that_are_gone(), test_expire_postings_skips_only_open_postings_past_deadline(), test_finds_a_stated_deadline() (+1 more)

### Community 63 - "startup_jobs.py"
Cohesion: 0.10
Nodes (28): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards(), fetch() (+20 more)

### Community 65 - "guess_email"
Cohesion: 0.23
Nodes (6): Output, Output, _clean(), guess_email(), name_words(), test_guess_email()

### Community 66 - "html"
Cohesion: 0.16
Nodes (6): _meta(), mlh(), _fetch(), generic(), personal(), published()

### Community 67 - "typing"
Cohesion: 0.28
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "test_notes.py"
Cohesion: 0.29
Nodes (7): NoteResult, PreferenceDraft, posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns()

### Community 71 - "keep"
Cohesion: 0.23
Nodes (7): import_inbox(), keep(), nearby(), next_date(), pick_reason(), upcoming(), worth_checking()

### Community 72 - "pipeline.py"
Cohesion: 0.08
Nodes (28): company_domain(), _at(), board(), _board(), _bounced_lead(), _card(), _column(), confirmed_postings() (+20 more)

### Community 73 - "test_site_emails.py"
Cohesion: 0.27
Nodes (5): lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 74 - "_get"
Cohesion: 0.12
Nodes (10): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get() (+2 more)

### Community 75 - "hn_hiring.py"
Cohesion: 0.17
Nodes (12): _company(), fetch(), HnPosting, item_url(), latest_thread_id(), _looks_like_job(), parse_comment(), parse_thread() (+4 more)

### Community 76 - "test_followups.py"
Cohesion: 0.16
Nodes (24): emailed(), FakeMailbox, outbox(), reply_event(), save(), settings(), test_a_bounce_is_only_searched_for_in_the_first_week(), test_a_bounce_the_inbox_scan_found_stops_follow_ups_at_any_age() (+16 more)

### Community 77 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.07
Nodes (31): Big-company postings from the SimplifyJobs off-season list, common_questions(), drop_unavailable(), expire_closed(), expire_postings(), is_workday(), open_postings(), refill() (+23 more)

### Community 82 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 83 - "test_form_d.py"
Cohesion: 0.25
Nodes (3): test_a_busy_sec_is_asked_again_and_a_dead_day_is_skipped(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name()

### Community 84 - "job_pipeline"
Cohesion: 0.33
Nodes (4): job_pipeline(), read_log(), moves(), _run_ai_cost()

### Community 85 - "draft"
Cohesion: 0.40
Nodes (4): ask(), ChatRequest, draft(), resume_text()

### Community 86 - "AGENTS.md"
Cohesion: 0.17
Nodes (3): Internship agent coding instructions, _on_linkedin(), source_names()

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "test_job_feeds.py"
Cohesion: 0.18
Nodes (4): test_feed_postings_survives_a_broken_feed(), test_find_intern_roles_falls_through_to_new_boards(), test_speedrun_fetch_stops_at_total_pages(), test_speedrun_page_is_host_locked_and_filtered()

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 90 - "_view"
Cohesion: 0.14
Nodes (9): find_more_startups(), FindStartupsRequest, rescore(), set_status(), StatusUpdate, submit(), SubmitApplicationRequest, _view() (+1 more)

### Community 91 - "classify_text"
Cohesion: 0.17
Nodes (11): classify(), new_text(), classify_text(), Stage, message(), test_a_receipt_that_mentions_interviews_is_not_one(), test_application_updates_skips_unrelated_mail(), test_classify_text_stages() (+3 more)

### Community 92 - "opportunities/schemas.py"
Cohesion: 0.13
Nodes (9): check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), sign_in_cmd(), strategy_cmd(), OpportunityKind, OpportunityStatus (+1 more)

### Community 94 - "save"
Cohesion: 0.50
Nodes (3): save(), SaveAnswersRequest, save_answers()

### Community 95 - "test_funding_news.py"
Cohesion: 0.20
Nodes (5): test_amount_usd(), test_build_candidates_groups_filters_and_sorts(), test_company_from_title(), test_fetch_items_survives_failing_feeds(), test_non_startup_raises_are_excluded()

### Community 101 - "test_patterns.py"
Cohesion: 0.16
Nodes (14): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_a_refused_send_is_not_counted_as_emailed(), test_outcomes_learn_from_bounces_and_settled_sends(), test_per_company_emails_more_founders_before_the_format_is_proven() (+6 more)

### Community 102 - "AgZen outreach drafts (not sent)"
Cohesion: 0.40
Nodes (4): 1. Ian James, Chief Technology Officer, 2. Nicolas Malfroy-Camine, Head of Software Engineering, 3. Karter Krueger, Head of Perception Engineering, AgZen outreach drafts (not sent)

### Community 105 - "pathlib"
Cohesion: 0.13
Nodes (5): _normalize(), no_real_services(), posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **5 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 666 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_dashboard.py`, `notify.py`, `leads/store.py`, `pytest`, `applications/browser.py`, `test_application_browser.py`, `ApplicationPrep`, `form_d.py`, `test_pipeline.py`, `Settings`, `app.py`, `simplify.py`, `FormQuestion`, `Region`, `test_agenda.py`, `EmailStatus`, `leads/schemas.py`, `re`, `agenda.py`, `contacts.py`, `PreferenceStore`, `test_refill.py`, `fit_to_limit`, `run_followups`, `LeadStore`, `internship_agent/ai.py`, `leads/cli.py`, `answers.py`, `LeadStatus`, `startup_jobs.py`, `typing`, `test_notes.py`, `pipeline.py`, `test_site_emails.py`, `_get`, `hn_hiring.py`, `test_followups.py`, `workflows.py`, `_view`, `classify_text`, `save`, `test_patterns.py`, `pathlib`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Are the 146 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 146 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/store.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09971509971509972 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_chat.py`, `notify.py`, `leads/store.py`, `ApplicationPrep`, `test_pipeline.py`, `internship_agent/cli.py`, `test_opportunities.py`, `get_settings`, `app.py`, `FormQuestion`, `client.py`, `Region`, `test_agenda.py`, `test_apply_events.py`, `feeds.py`, `Opportunity`, `test_people.py`, `EmailStatus`, `run.py`, `PreferenceStore`, `Lead`, `run_followups`, `leads/cli.py`, `test_auto_pick.py`, `answers.py`, `test_notes.py`, `keep`, `pipeline.py`, `test_site_emails.py`, `_get`, `test_followups.py`, `workflows.py`, `job_pipeline`, `draft`, `test_job_feeds.py`, `_view`, `opportunities/schemas.py`, `save`, `test_patterns.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 121 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 121 INFERRED edges - model-reasoned connections that need verification._
- **Should `applications/browser.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._