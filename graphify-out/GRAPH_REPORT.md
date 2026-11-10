# Graph Report - team-filter  (2026-11-09)

## Corpus Check
- 139 files · ~291,308 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 32 file(s) not represented in the graph (top: .timer 12, .service 9, (none) 6)

## Summary
- 2084 nodes · 6268 edges · 113 communities (84 shown, 29 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1023 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e14d854d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_dashboard.py
- test_chat.py
- notify.py
- Table
- pytest
- typing
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- test_pipeline.py
- internship_agent/cli.py
- json
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
- Lead
- startups.py
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
- Segment
- re
- leads/cli.py
- apply_events
- mailbox.py
- agenda.py
- to_event
- test_notes.py
- outlook/schemas.py
- followup_run.py
- test_refill.py
- fit_to_limit
- lead_store
- followups.py
- StepAction
- LeadStore
- run.py
- Preference
- command
- test_auto_pick.py
- page_url
- AnswerBank
- LeadStatus
- startup_jobs.py
- _store
- find-founders.md
- send_email
- leads/schemas.py
- internship_agent/ai.py
- SentMessage
- export_drafts
- OpportunityStatus
- pipeline.py
- test_site_emails.py
- screenshot_path
- leads/store.py
- run_followups
- candidate_context.md
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- FakeField
- hiring_sheet.py
- Settings
- Mailbox
- AGENTS.md
- outlook
- test_job_feeds.py
- Bot Auto application preview
- _get
- classify_text
- command
- run-email-batch.sh
- insights
- test_outlook_client.py
- FakeToggle
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- test_scheduled_jobs.py
- inboxes
- open_login_browser
- test_patterns.py
- AgZen outreach drafts (not sent)
- .key
- send
- os
- run-lead-search.sh
- run-followups.sh
- _scan_inboxes
- submit
- start.sh
- notify-failure.sh
- run-discord-scrape.sh

## God Nodes (most connected - your core abstractions)
1. `Lead` - 211 edges
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
- `Application answers prepared from the resume` --references--> `prepare_answers()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (113 total, 29 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_dashboard.py"
Cohesion: 0.18
Nodes (16): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_health_says_busy_while_a_long_job_runs() (+8 more)

### Community 2 - "test_chat.py"
Cohesion: 0.10
Nodes (18): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+10 more)

### Community 3 - "notify.py"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 5 - "pytest"
Cohesion: 0.22
Nodes (16): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+8 more)

### Community 6 - "typing"
Cohesion: 0.12
Nodes (8): _confirmation_quote(), _confirmed(), _post_submit_outcome(), _save_screenshot(), SubmissionResult, _visible_captcha(), test_confirmation_quote_keeps_the_employers_line(), test_post_submit_invalid_and_challenge_states()

### Community 7 - "test_application_browser.py"
Cohesion: 0.11
Nodes (24): _field_label(), _fill_form(), _normalize(), _numeric_answer(), _posting_is_closed(), _react_select_answer(), FakePage, posting() (+16 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.08
Nodes (16): FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), submit() (+8 more)

### Community 9 - "form_d.py"
Cohesion: 0.09
Nodes (21): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+13 more)

### Community 10 - "test_pipeline.py"
Cohesion: 0.11
Nodes (23): _event(), FakeBox, lead(), mail(), _settings(), test_a_dragged_card_stays_put_until_a_newer_email(), test_a_founders_answer_is_read_without_the_quoted_thread(), test_board_columns_follow_the_latest_email() (+15 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.11
Nodes (20): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+12 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.17
Nodes (9): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, n8n workflows (+1 more)

### Community 14 - "README.md"
Cohesion: 0.10
Nodes (23): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume (+15 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (22): get_settings(), allow_event_retry(), apply_to_event(), check_opportunities(), daily_run(), delete_preference(), event_proof(), find_events() (+14 more)

### Community 17 - "tracking.py"
Cohesion: 0.35
Nodes (5): MailMessage, application_updates(), ApplicationUpdate, guess_company(), to_update()

### Community 18 - "app.py"
Cohesion: 0.08
Nodes (25): AnswerEdit, ask(), browser_sessions(), calendar_ics(), _calendar_items(), CardMove, ChatRequest, CheckRequest (+17 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (8): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in()

### Community 20 - "simplify.py"
Cohesion: 0.08
Nodes (16): Big-company postings from the SimplifyJobs off-season list, _cell(), parse(), postings(), region_from_text(), regions_of(), cap_per_company(), fetch() (+8 more)

### Community 21 - "FormQuestion"
Cohesion: 0.13
Nodes (21): category(), common_questions(), match_option(), prefill(), validate(), FormQuestion, QuestionKind, ashby_questions() (+13 more)

### Community 22 - "mailer.py"
Cohesion: 0.21
Nodes (6): build_message(), MailError, RecipientRefused, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 23 - "client.py"
Cohesion: 0.18
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 26 - "Lead"
Cohesion: 0.12
Nodes (9): hub(), in_area(), spread(), Lead, OutreachDraft, _role(), inbox_send(), test_a_skipped_posting_never_comes_back_from_another_source() (+1 more)

### Community 27 - "startups.py"
Cohesion: 0.13
Nodes (11): mentions(), names(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+3 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.15
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.23
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "Opportunity"
Cohesion: 0.15
Nodes (12): mark_cmd(), refresh_cmd(), auto_pick(), find_events(), import_inbox(), keep(), plan_submission(), Opportunity (+4 more)

### Community 31 - "run"
Cohesion: 0.11
Nodes (11): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), _refusal(), resolve() (+3 more)

### Community 33 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "test_people.py"
Cohesion: 0.23
Nodes (9): PersonFinding, _on_linkedin(), source_names(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_big_tech_teams_drafts_a_note_about_their_team_and_the_batches_skip_them(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size() (+1 more)

### Community 35 - "EmailStatus"
Cohesion: 0.09
Nodes (18): _clean(), guess_email(), name_words(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess() (+10 more)

### Community 40 - "Segment"
Cohesion: 0.11
Nodes (13): search_startups(), StartupFinding, Segment, source_confirms(), post_confirms(), post_id(), post_text(), search_x_raises() (+5 more)

### Community 41 - "re"
Cohesion: 0.14
Nodes (20): Round, parse_round(), _meta(), mlh(), amount_usd(), build_candidates(), _clean_company(), company_from_title() (+12 more)

### Community 42 - "leads/cli.py"
Cohesion: 0.14
Nodes (9): _draft(), draft_all(), draft_lead(), find_more(), _openai(), prepare_cmd(), _resume(), scrape_jobs_cmd() (+1 more)

### Community 43 - "apply_events"
Cohesion: 0.08
Nodes (17): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _candidate(), check_events(), one() (+9 more)

### Community 44 - "mailbox.py"
Cohesion: 0.16
Nodes (10): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_a_bounce_that_lands_before_sent_at_is_recorded_still_counts() (+2 more)

### Community 45 - "agenda.py"
Cohesion: 0.09
Nodes (24): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics() (+16 more)

### Community 46 - "to_event"
Cohesion: 0.16
Nodes (11): company_domain(), _bounced_lead(), confirmed_postings(), _header(), _host(), _is_ats(), match(), reclassify() (+3 more)

### Community 47 - "test_notes.py"
Cohesion: 0.19
Nodes (13): _normalize(), PreferenceStore, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_format_preferences() (+5 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "followup_run.py"
Cohesion: 0.17
Nodes (7): Internship tracker: follow-ups (weekdays 9:30 AM), FollowupReport, FollowupSent, _misaddressed(), _name(), _remind_unanswered(), _site()

### Community 50 - "test_refill.py"
Cohesion: 0.19
Nodes (7): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_posting_dates_come_from_the_source_or_the_day_found(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 52 - "lead_store"
Cohesion: 0.12
Nodes (17): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), merge(), to_people(), add_team_contacts(), find_big_tech_teams() (+9 more)

### Community 53 - "followups.py"
Cohesion: 0.15
Nodes (10): first_name(), followup_body(), is_due(), last_contact(), next_followup(), reply_subject(), test_a_follow_up_is_due_five_days_after_the_last_email(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company() (+2 more)

### Community 54 - "StepAction"
Cohesion: 0.13
Nodes (5): Element, import_sessions(), PlaywrightPage, saved_browser(), StepAction

### Community 55 - "LeadStore"
Cohesion: 0.38
Nodes (4): LeadStore, test_auto_apply_prepares_then_submits(), test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 56 - "run.py"
Cohesion: 0.09
Nodes (14): assess(), EventFinding, EventFindings, search_events(), write_strategy(), BrowserStep, EventApplication, SubmissionStrategy (+6 more)

### Community 57 - "Preference"
Cohesion: 0.15
Nodes (13): Rules learned from notes (skip, downrank, boost), assess_fit(), draft_outreach(), format_preferences(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter() (+5 more)

### Community 58 - "command"
Cohesion: 0.12
Nodes (14): application_campaign(), apply_cmd(), big_tech_teams_cmd(), daily_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd(), funding_news_cmd() (+6 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "page_url"
Cohesion: 0.15
Nodes (9): page_url(), summary_push(), hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about() (+1 more)

### Community 61 - "AnswerBank"
Cohesion: 0.33
Nodes (5): _answer_for(), AnswerBank, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 62 - "LeadStatus"
Cohesion: 0.11
Nodes (15): find_deadline(), apply_violations(), drop_unavailable(), expire_closed(), expire_postings(), ApplicationPrep, LeadStatus, Note (+7 more)

### Community 63 - "startup_jobs.py"
Cohesion: 0.10
Nodes (30): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead() (+22 more)

### Community 64 - "_store"
Cohesion: 0.15
Nodes (9): Founder leads flow: /find-founders, import, score, list, draft, mark, contacts_cmd(), _email_cell(), list_leads(), mark_lead(), prepare_all_cmd(), score_leads(), show_lead() (+1 more)

### Community 65 - "find-founders.md"
Cohesion: 0.11
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+4 more)

### Community 66 - "send_email"
Cohesion: 0.20
Nodes (5): check_outreach_text(), check_send(), SendBlocked, send_email(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 67 - "leads/schemas.py"
Cohesion: 0.10
Nodes (16): batches(), LeadKind, Region, Verdict, application_url(), cards(), parse(), postings() (+8 more)

### Community 68 - "internship_agent/ai.py"
Cohesion: 0.26
Nodes (8): AnswerDraft, AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PreferenceDraft, StartupFindings, FitResult

### Community 70 - "export_drafts"
Cohesion: 0.16
Nodes (6): contacts_vcf_cmd(), export_drafts(), _email_line(), render_outreach(), is_open(), rank()

### Community 71 - "OpportunityStatus"
Cohesion: 0.19
Nodes (8): list_cmd(), nearby(), next_date(), pick_reason(), to_apply(), upcoming(), worth_checking(), OpportunityStatus

### Community 72 - "pipeline.py"
Cohesion: 0.15
Nodes (12): _at(), board(), _board(), _card(), _column(), display_company(), events(), InboxEvent (+4 more)

### Community 73 - "test_site_emails.py"
Cohesion: 0.27
Nodes (5): lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 75 - "leads/store.py"
Cohesion: 0.09
Nodes (25): _identity(), normalize_url(), _company(), fetch(), HnPosting, item_url(), latest_thread_id(), _looks_like_job() (+17 more)

### Community 76 - "run_followups"
Cohesion: 0.35
Nodes (19): run_followups(), emailed(), FakeMailbox, save(), settings(), test_a_bounce_is_only_searched_for_in_the_first_week(), test_a_bounce_the_inbox_scan_found_stops_follow_ups_at_any_age(), test_a_bounced_address_gets_nothing() (+11 more)

### Community 77 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.08
Nodes (26): apply_to_posting(), _online_checks(), _supported_url(), normalize(), is_workday(), open_postings(), refill(), answer_bank() (+18 more)

### Community 82 - "FakeField"
Cohesion: 0.09
Nodes (6): FakeField, FakeLocator, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 83 - "hiring_sheet.py"
Cohesion: 0.25
Nodes (7): link(), _text(), to_lead(), to_leads(), test_import_skips_companies_already_stored(), test_link(), test_rows_become_company_leads()

### Community 84 - "Settings"
Cohesion: 0.16
Nodes (8): Settings, append(), read_log(), replace_log(), _logged_subject(), move(), moves(), _log_xai()

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "test_job_feeds.py"
Cohesion: 0.05
Nodes (12): test_a_busy_sec_is_asked_again_and_a_dead_day_is_skipped(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), test_amount_usd(), test_build_candidates_groups_filters_and_sorts(), test_company_from_title(), test_fetch_items_survives_failing_feeds(), test_non_startup_raises_are_excluded() (+4 more)

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 90 - "_get"
Cohesion: 0.11
Nodes (20): allow_retry(), auto_apply(), calendar(), draft(), _get(), index(), job_pipeline(), KeyRequest (+12 more)

### Community 91 - "classify_text"
Cohesion: 0.20
Nodes (10): classify(), classify_text(), Stage, message(), test_a_receipt_that_mentions_interviews_is_not_one(), test_application_updates_skips_unrelated_mail(), test_classify_text_stages(), test_guess_company_prefers_display_name_then_domain() (+2 more)

### Community 92 - "command"
Cohesion: 0.14
Nodes (6): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), strategy_cmd(), applied_push()

### Community 94 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 95 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 101 - "test_patterns.py"
Cohesion: 0.16
Nodes (14): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_a_refused_send_is_not_counted_as_emailed(), test_outcomes_learn_from_bounces_and_settled_sends(), test_per_company_emails_more_founders_before_the_format_is_proven() (+6 more)

### Community 102 - "AgZen outreach drafts (not sent)"
Cohesion: 0.40
Nodes (4): 1. Ian James, Chief Technology Officer, 2. Nicolas Malfroy-Camine, Head of Software Engineering, 3. Karter Krueger, Head of Perception Engineering, AgZen outreach drafts (not sent)

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **5 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 667 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **29 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_dashboard.py`, `test_chat.py`, `notify.py`, `Table`, `pytest`, `typing`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_pipeline.py`, `get_settings`, `app.py`, `simplify.py`, `FormQuestion`, `startups.py`, `test_people.py`, `EmailStatus`, `re`, `leads/cli.py`, `agenda.py`, `to_event`, `test_notes.py`, `followup_run.py`, `test_refill.py`, `lead_store`, `followups.py`, `LeadStore`, `run.py`, `Preference`, `AnswerBank`, `LeadStatus`, `startup_jobs.py`, `_store`, `find-founders.md`, `send_email`, `leads/schemas.py`, `internship_agent/ai.py`, `export_drafts`, `pipeline.py`, `test_site_emails.py`, `screenshot_path`, `leads/store.py`, `run_followups`, `workflows.py`, `hiring_sheet.py`, `_get`, `classify_text`, `insights`, `test_patterns.py`, `.key`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 148 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 148 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_chat.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10252100840336134 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_chat.py`, `Table`, `test_daily_campaign.py`, `test_pipeline.py`, `internship_agent/cli.py`, `json`, `README.md`, `test_opportunities.py`, `get_settings`, `app.py`, `simplify.py`, `FormQuestion`, `client.py`, `Lead`, `test_apply_events.py`, `feeds.py`, `Opportunity`, `test_people.py`, `EmailStatus`, `leads/cli.py`, `apply_events`, `to_event`, `test_notes.py`, `followup_run.py`, `lead_store`, `run.py`, `Preference`, `command`, `test_auto_pick.py`, `AnswerBank`, `_store`, `send_email`, `pipeline.py`, `test_site_emails.py`, `leads/store.py`, `run_followups`, `workflows.py`, `test_job_feeds.py`, `inboxes`, `test_patterns.py`, `.key`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 121 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 121 INFERRED edges - model-reasoned connections that need verification._
- **Should `Table` be split into smaller, more focused modules?**
  _Cohesion score 0.14619883040935672 - nodes in this community are weakly interconnected._