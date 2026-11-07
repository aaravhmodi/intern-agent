# Graph Report - lead-search-timer  (2026-11-07)

## Corpus Check
- 139 files · ~290,347 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 32 file(s) not represented in the graph (top: .timer 12, .service 9, (none) 6)

## Summary
- 2077 nodes · 6229 edges · 111 communities (89 shown, 22 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1014 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `429c1df4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- LeadStore
- big_companies.py
- notify.py
- Lead
- pytest
- applications/browser.py
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
- Region
- sign_in
- test_apply_events.py
- feeds.py
- Opportunity
- run
- run-lowest-30-applications.sh
- test_ai.py
- collections_abc
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- leads/schemas.py
- re
- agenda.py
- check_events
- mailbox.py
- contacts.py
- posting_text.py
- test_notes.py
- outlook/schemas.py
- to_event
- x_search.py
- fit_to_limit
- LeadKind
- run_followups
- StepAction
- insights
- opportunities/ai.py
- internship_agent/ai.py
- leads/cli.py
- test_auto_pick.py
- page_url
- pathlib
- LeadStatus
- startup_jobs.py
- _TableParser
- guess_email
- urllib_parse
- typing
- load_resume_text
- SentMessage
- sources/__init__.py
- OpportunityStatus
- pipeline.py
- test_outlook_client.py
- _get
- hn_hiring.py
- test_followups.py
- set_status
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- FakeField
- followups.py
- region_from_text
- hiring_sheet.py
- AGENTS.md
- outlook
- test_job_feeds.py
- Bot Auto application preview
- _view
- classify_text
- run.py
- run-email-batch.sh
- speedrun.py
- test_funding_news.py
- Snapshot
- import_inbox
- test_scheduled_jobs.py
- find_intern_roles
- urllib_request
- test_patterns.py
- AgZen outreach drafts (not sent)
- inboxes
- send
- test_tables
- run-lead-search.sh
- run-followups.sh
- start.sh
- notify-failure.sh
- run-discord-scrape.sh

## God Nodes (most connected - your core abstractions)
1. `Lead` - 208 edges
2. `Settings` - 137 edges
3. `get_settings()` - 85 edges
4. `Opportunity` - 73 edges
5. `LeadKind` - 60 edges
6. `LeadStatus` - 59 edges
7. `Region` - 52 edges
8. `OpportunityStore` - 43 edges
9. `run_followups()` - 42 edges
10. `lead_store()` - 35 edges

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

## Communities (111 total, 22 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "LeadStore"
Cohesion: 0.06
Nodes (37): dashboard(), LeadStore, _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked() (+29 more)

### Community 2 - "big_companies.py"
Cohesion: 0.28
Nodes (7): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), intern_roles()

### Community 3 - "notify.py"
Cohesion: 0.20
Nodes (13): category(), _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer(), lead() (+5 more)

### Community 4 - "Lead"
Cohesion: 0.06
Nodes (21): read_log(), replace_log(), Table, _email_line(), render_outreach(), apply_violations(), Lead, _identity() (+13 more)

### Community 5 - "pytest"
Cohesion: 0.18
Nodes (17): no_real_services(), fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.10
Nodes (19): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+11 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.17
Nodes (19): _fill_form(), _numeric_answer(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_closed_posting_text_is_detected(), test_fill_form_blocks_unanswered_required_questions() (+11 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (15): FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), submit() (+7 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (17): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+9 more)

### Community 10 - "test_pipeline.py"
Cohesion: 0.11
Nodes (23): _event(), FakeBox, lead(), mail(), _settings(), test_a_dragged_card_stays_put_until_a_newer_email(), test_a_founders_answer_is_read_without_the_quoted_thread(), test_board_columns_follow_the_latest_email() (+15 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.17
Nodes (12): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.09
Nodes (18): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules (+10 more)

### Community 14 - "README.md"
Cohesion: 0.11
Nodes (20): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Current setup (+12 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run(), draft() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.30
Nodes (5): MailMessage, application_updates(), ApplicationUpdate, guess_company(), to_update()

### Community 18 - "app.py"
Cohesion: 0.09
Nodes (20): AnswerEdit, ask(), browser_sessions(), CardMove, ChatRequest, CheckRequest, Cookie, FindMoreRequest (+12 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "simplify.py"
Cohesion: 0.08
Nodes (17): Big-company postings from the SimplifyJobs off-season list, application_url(), cards(), parse(), postings(), _cell(), parse(), postings() (+9 more)

### Community 21 - "FormQuestion"
Cohesion: 0.20
Nodes (16): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q() (+8 more)

### Community 22 - "mailer.py"
Cohesion: 0.21
Nodes (6): build_message(), MailError, RecipientRefused, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 23 - "client.py"
Cohesion: 0.19
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 26 - "Region"
Cohesion: 0.29
Nodes (8): hub(), in_area(), spread(), Region, founder(), test_hub_cities_and_europe_are_separate_batches(), test_spread_splits_evenly_and_keeps_fit_order(), test_unknown_area_is_rejected()

### Community 27 - "sign_in"
Cohesion: 0.18
Nodes (7): next_step(), describe(), sign_in_cmd(), step(), send_sessions(), sign_in(), step()

### Community 28 - "test_apply_events.py"
Cohesion: 0.23
Nodes (14): _event(), landing(), _settings(), step(), steps(), test_allowed_sites(), test_apply_events_saves_the_result_and_marks_it_submitted(), fake_browser() (+6 more)

### Community 29 - "feeds.py"
Cohesion: 0.18
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 30 - "Opportunity"
Cohesion: 0.18
Nodes (9): mark_cmd(), apply_events(), auto_pick(), _candidate(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status() (+1 more)

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "collections_abc"
Cohesion: 0.16
Nodes (10): More people to connect with, chosen by company size, PersonFinding, Person, _on_linkedin(), source_names(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 35 - "EmailStatus"
Cohesion: 0.11
Nodes (14): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+6 more)

### Community 40 - "leads/schemas.py"
Cohesion: 0.10
Nodes (20): Round, Segment, Verdict, parse_round(), mentions(), names(), to_leads(), finding() (+12 more)

### Community 41 - "re"
Cohesion: 0.19
Nodes (16): _slug(), amount_usd(), build_candidates(), _clean_company(), company_from_title(), _date(), fetch_items(), FundingCandidate (+8 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "check_events"
Cohesion: 0.08
Nodes (17): Push, send(), apply_cmd(), check_cmd(), find_events_cmd(), refresh_cmd(), strategy_cmd(), applied_push() (+9 more)

### Community 44 - "mailbox.py"
Cohesion: 0.14
Nodes (10): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_a_bounce_that_lands_before_sent_at_is_recorded_still_counts() (+2 more)

### Community 45 - "contacts.py"
Cohesion: 0.17
Nodes (16): company_key(), Contact, contact_type(), contacts_at(), contacts_from_leads(), add(), ContactType, _escape() (+8 more)

### Community 46 - "posting_text.py"
Cohesion: 0.38
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 47 - "test_notes.py"
Cohesion: 0.16
Nodes (14): _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules() (+6 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "to_event"
Cohesion: 0.13
Nodes (12): _bounced_lead(), classify(), confirmed_postings(), _header(), _host(), _is_ats(), match(), new_text() (+4 more)

### Community 50 - "x_search.py"
Cohesion: 0.17
Nodes (7): StartupFinding, StartupFindings, source_confirms(), post_id(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 52 - "LeadKind"
Cohesion: 0.14
Nodes (12): search_people(), is_open(), LeadKind, effective_segment(), merge(), to_people(), add_team_contacts(), find_startups() (+4 more)

### Community 53 - "run_followups"
Cohesion: 0.11
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), _remind_unanswered(), run_followups(), _site() (+4 more)

### Community 54 - "StepAction"
Cohesion: 0.11
Nodes (6): Element, _refusal(), import_sessions(), PlaywrightPage, saved_browser(), StepAction

### Community 55 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.23
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding(), test_without_citations_strips_inline_links_only()

### Community 57 - "internship_agent/ai.py"
Cohesion: 0.13
Nodes (17): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+9 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (44): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+36 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "page_url"
Cohesion: 0.18
Nodes (8): page_url(), hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about(), test_page_urls_open_a_view_or_one_item()

### Community 61 - "pathlib"
Cohesion: 0.14
Nodes (9): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer() (+1 more)

### Community 62 - "LeadStatus"
Cohesion: 0.08
Nodes (25): find_deadline(), drop_unavailable(), expire_closed(), expire_postings(), is_workday(), open_postings(), refill(), ApplicationPrep (+17 more)

### Community 63 - "startup_jobs.py"
Cohesion: 0.24
Nodes (14): _ashby(), _day(), _greenhouse(), _https(), _join(), _json(), _lever(), OpenRole (+6 more)

### Community 65 - "guess_email"
Cohesion: 0.29
Nodes (4): _clean(), guess_email(), name_words(), test_guess_email()

### Community 66 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 67 - "typing"
Cohesion: 0.28
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 70 - "sources/__init__.py"
Cohesion: 0.11
Nodes (4): test_postings_are_filtered_to_the_search_regions(), test_a_busy_sec_is_asked_again_and_a_dead_day_is_skipped(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name()

### Community 71 - "OpportunityStatus"
Cohesion: 0.17
Nodes (11): list_cmd(), keep(), nearby(), next_date(), pick_reason(), refresh(), to_apply(), upcoming() (+3 more)

### Community 72 - "pipeline.py"
Cohesion: 0.15
Nodes (12): _at(), board(), _board(), _card(), _column(), display_company(), events(), InboxEvent (+4 more)

### Community 73 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 74 - "_get"
Cohesion: 0.12
Nodes (11): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), event_proof(), _get(), _icon() (+3 more)

### Community 75 - "hn_hiring.py"
Cohesion: 0.21
Nodes (10): _company(), fetch(), HnPosting, item_url(), latest_thread_id(), _looks_like_job(), matching(), parse_comment() (+2 more)

### Community 76 - "test_followups.py"
Cohesion: 0.22
Nodes (22): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounce_is_only_searched_for_in_the_first_week(), test_a_bounce_the_inbox_scan_found_stops_follow_ups_at_any_age(), test_a_bounced_address_gets_nothing() (+14 more)

### Community 77 - "set_status"
Cohesion: 0.15
Nodes (13): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), note(), NoteRequest, set_status(), StatusUpdate, Dashboard page (index.html) (+5 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.06
Nodes (38): Send email safeguards, Settings, append(), common_questions(), check_outreach_text(), check_send(), move(), answer_bank() (+30 more)

### Community 82 - "FakeField"
Cohesion: 0.07
Nodes (7): FakeField, FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 83 - "followups.py"
Cohesion: 0.21
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), next_followup(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 84 - "region_from_text"
Cohesion: 0.21
Nodes (6): boards(), fetch(), postings(), to_lead(), region_from_text(), regions_of()

### Community 85 - "hiring_sheet.py"
Cohesion: 0.25
Nodes (7): link(), _text(), to_lead(), to_leads(), test_import_skips_companies_already_stored(), test_link(), test_rows_become_company_leads()

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "test_job_feeds.py"
Cohesion: 0.16
Nodes (5): test_feed_postings_survives_a_broken_feed(), test_find_intern_roles_falls_through_to_new_boards(), test_hn_thread_matching_and_leads(), test_speedrun_fetch_stops_at_total_pages(), test_speedrun_page_is_host_locked_and_filtered()

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 90 - "_view"
Cohesion: 0.23
Nodes (10): delete_preference(), find_more(), find_more_startups(), leads(), PreferenceDelete, rescore(), _sort_key(), _view() (+2 more)

### Community 91 - "classify_text"
Cohesion: 0.26
Nodes (9): classify_text(), Stage, message(), test_a_receipt_that_mentions_interviews_is_not_one(), test_application_updates_skips_unrelated_mail(), test_classify_text_stages(), test_guess_company_prefers_display_name_then_domain(), test_interview_events() (+1 more)

### Community 92 - "run.py"
Cohesion: 0.16
Nodes (3): BrowserStep, EventApplication, SubmissionTrack

### Community 94 - "speedrun.py"
Cohesion: 0.26
Nodes (7): wanted_location(), fetch(), matching(), parse_page(), SpeedrunJob, is_intern_engineering(), test_wanted_location()

### Community 95 - "test_funding_news.py"
Cohesion: 0.20
Nodes (5): test_amount_usd(), test_build_candidates_groups_filters_and_sorts(), test_company_from_title(), test_fetch_items_survives_failing_feeds(), test_non_startup_raises_are_excluded()

### Community 97 - "import_inbox"
Cohesion: 0.25
Nodes (3): import_cmd(), import_inbox(), proof_path()

### Community 99 - "find_intern_roles"
Cohesion: 0.29
Nodes (5): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), board_slugs(), find_intern_roles(), test_board_slugs_and_intern_filter()

### Community 100 - "urllib_request"
Cohesion: 0.38
Nodes (3): get_bytes(), get_json(), get_text()

### Community 101 - "test_patterns.py"
Cohesion: 0.10
Nodes (19): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_a_refused_send_is_not_counted_as_emailed(), test_outcomes_learn_from_bounces_and_settled_sends(), test_per_company_emails_more_founders_before_the_format_is_proven() (+11 more)

### Community 102 - "AgZen outreach drafts (not sent)"
Cohesion: 0.40
Nodes (4): 1. Ian James, Chief Technology Officer, 2. Nicolas Malfroy-Camine, Head of Software Engineering, 3. Karter Krueger, Head of Perception Engineering, AgZen outreach drafts (not sent)

### Community 104 - "send"
Cohesion: 0.40
Nodes (3): send(), SendRequest, SendBlocked

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **5 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 665 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **22 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `LeadStore`, `big_companies.py`, `notify.py`, `pytest`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_pipeline.py`, `app.py`, `simplify.py`, `FormQuestion`, `Region`, `EmailStatus`, `leads/schemas.py`, `re`, `agenda.py`, `contacts.py`, `test_notes.py`, `to_event`, `fit_to_limit`, `LeadKind`, `run_followups`, `insights`, `internship_agent/ai.py`, `leads/cli.py`, `pathlib`, `LeadStatus`, `typing`, `pipeline.py`, `_get`, `hn_hiring.py`, `test_followups.py`, `set_status`, `workflows.py`, `followups.py`, `region_from_text`, `hiring_sheet.py`, `_view`, `speedrun.py`, `test_patterns.py`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **Are the 146 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 146 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `LeadStore` be split into smaller, more focused modules?**
  _Cohesion score 0.05839727195225917 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `test_sign_in.py`, `LeadStore`, `Lead`, `test_daily_campaign.py`, `test_pipeline.py`, `internship_agent/cli.py`, `json`, `README.md`, `test_opportunities.py`, `get_settings`, `app.py`, `simplify.py`, `FormQuestion`, `client.py`, `sign_in`, `test_apply_events.py`, `Opportunity`, `collections_abc`, `EmailStatus`, `check_events`, `test_notes.py`, `to_event`, `LeadKind`, `run_followups`, `leads/cli.py`, `test_auto_pick.py`, `pathlib`, `LeadStatus`, `OpportunityStatus`, `pipeline.py`, `test_followups.py`, `test_job_feeds.py`, `_view`, `run.py`, `import_inbox`, `test_patterns.py`, `inboxes`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 119 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 119 INFERRED edges - model-reasoned connections that need verification._
- **Should `Lead` be split into smaller, more focused modules?**
  _Cohesion score 0.06219426974143955 - nodes in this community are weakly interconnected._