# Graph Report - winter-2027-internship-agent  (2026-10-26)

## Corpus Check
- 143 files · ~650,320 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2054 nodes · 6121 edges · 106 communities (83 shown, 23 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1016 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d02898f6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- big_companies.py
- notify.py
- Lead
- pytest
- applications/browser.py
- test_application_browser.py
- ApplicationPrep
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- json
- make_workflows.py
- README.md
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- LeadKind
- FormQuestion
- internship_agent/mailer.py
- client.py
- run-application-campaign-2026-10-16.sh
- test_verification_mail.py
- workflows.py
- apply_events
- test_apply_events.py
- feeds.py
- test_lite.py
- opportunities/schemas.py
- run-lowest-30-applications.sh
- test_people.py
- Segment
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- leads/schemas.py
- test_refill.py
- agenda.py
- run.py
- mailbox.py
- test_site_emails.py
- re
- Table
- outlook/schemas.py
- internship_agent/leads/sending.py
- x_search.py
- OutreachDraft
- LeadStore
- run_followups
- PlaywrightPage
- insights
- opportunities/ai.py
- internship_agent/ai.py
- leads/cli.py
- test_auto_pick.py
- page_url
- answers.py
- LeadStatus
- test_form_d.py
- _TableParser
- find-internships.md
- urllib_parse
- batches
- pathlib
- SentMessage
- Region
- test_hidden_recaptcha_support_nodes_do_not_block
- pipeline.py
- test_outlook_client.py
- candidate_context.md
- answer_bank
- test_followups.py
- test_scrape_stores_every_matching_non_workday_posting
- run-inbox-check.sh
- find-opportunities.md
- lead_store
- FakeToggle
- dashboard.py
- Workspace
- AGENTS.md
- outlook
- opportunity_lite/cli.py
- Bot Auto application preview
- classify_text
- Settings
- run-email-batch.sh
- create_server
- typing
- conftest.py
- test_scheduled_jobs.py
- test_patterns.py
- ↗ Intern Agent
- web.py
- opportunity_lite/leads/sending.py
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

## Communities (106 total, 23 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.16
Nodes (13): BrowserStep, FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site() (+5 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.05
Nodes (37): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+29 more)

### Community 2 - "big_companies.py"
Cohesion: 0.12
Nodes (20): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards(), fetch() (+12 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 4 - "Lead"
Cohesion: 0.14
Nodes (12): _email_line(), render_outreach(), Lead, _identity(), load_inbox(), merge(), normalize_url(), _role() (+4 more)

### Community 5 - "pytest"
Cohesion: 0.22
Nodes (16): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+8 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.10
Nodes (19): _fill_form(), _numeric_answer(), FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions() (+11 more)

### Community 8 - "ApplicationPrep"
Cohesion: 0.10
Nodes (18): ApplicationPrep, FitAssessment, _slug(), test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load() (+10 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (17): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+9 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.16
Nodes (17): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+9 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.17
Nodes (12): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.17
Nodes (9): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, n8n workflows (+1 more)

### Community 14 - "README.md"
Cohesion: 0.07
Nodes (35): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+27 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "get_settings"
Cohesion: 0.11
Nodes (31): post(), get_settings(), allow_event_retry(), allow_retry(), application_proof(), apply_to_event(), auto_apply(), check_opportunities() (+23 more)

### Community 17 - "tracking.py"
Cohesion: 0.30
Nodes (5): MailMessage, application_updates(), ApplicationUpdate, guess_company(), to_update()

### Community 18 - "app.py"
Cohesion: 0.06
Nodes (32): AnswerEdit, ask(), browser_sessions(), calendar(), calendar_ics(), _calendar_items(), ChatRequest, CheckRequest (+24 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.18
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "LeadKind"
Cohesion: 0.08
Nodes (19): LeadKind, application_url(), cards(), parse(), postings(), _cell(), parse(), postings() (+11 more)

### Community 21 - "FormQuestion"
Cohesion: 0.19
Nodes (16): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 22 - "internship_agent/mailer.py"
Cohesion: 0.17
Nodes (5): deliver(), build_message(), send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 23 - "client.py"
Cohesion: 0.19
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 26 - "workflows.py"
Cohesion: 0.14
Nodes (7): hub(), in_area(), spread(), DailyReport, inbox_send(), NoteOutcome, startup_postings()

### Community 27 - "apply_events"
Cohesion: 0.13
Nodes (10): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _keys(), proof_path(), send_sessions() (+2 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.15
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.22
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "test_lite.py"
Cohesion: 0.19
Nodes (5): _client_returning(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_greenhouse_validates_and_keeps_source(), test_web_search_keeps_only_valid_posting_urls()

### Community 31 - "opportunities/schemas.py"
Cohesion: 0.09
Nodes (15): allowed(), Element, _host(), names_event(), nothing_to_sign_in(), Page, _quote(), _refusal() (+7 more)

### Community 33 - "test_people.py"
Cohesion: 0.16
Nodes (12): assess_fit(), FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person() (+4 more)

### Community 34 - "Segment"
Cohesion: 0.16
Nodes (13): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, Segment, effective_segment(), _on_linkedin(), source_names() (+5 more)

### Community 35 - "EmailStatus"
Cohesion: 0.11
Nodes (14): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+6 more)

### Community 40 - "leads/schemas.py"
Cohesion: 0.12
Nodes (13): Round, Verdict, parse_round(), mentions(), names(), to_leads(), finding(), test_linkedin_note_never_exceeds_200_chars() (+5 more)

### Community 41 - "test_refill.py"
Cohesion: 0.13
Nodes (12): is_workday(), open_postings(), refill(), _only_live(), scrape_discord(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key() (+4 more)

### Community 42 - "agenda.py"
Cohesion: 0.22
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "run.py"
Cohesion: 0.07
Nodes (33): check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), mark_cmd(), refresh_cmd(), strategy_cmd(), auto_pick() (+25 more)

### Community 44 - "mailbox.py"
Cohesion: 0.12
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "test_site_emails.py"
Cohesion: 0.21
Nodes (5): lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 46 - "re"
Cohesion: 0.38
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 47 - "Table"
Cohesion: 0.07
Nodes (20): Table, apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, PostgresLeadStore, posting() (+12 more)

### Community 48 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "internship_agent/leads/sending.py"
Cohesion: 0.20
Nodes (5): Send email safeguards, check_outreach_text(), check_send(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 50 - "x_search.py"
Cohesion: 0.12
Nodes (11): StartupFinding, source_confirms(), post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 51 - "OutreachDraft"
Cohesion: 0.18
Nodes (3): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 52 - "LeadStore"
Cohesion: 0.40
Nodes (3): LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 53 - "run_followups"
Cohesion: 0.10
Nodes (17): Internship tracker: follow-ups (weekdays 9:30 AM), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+9 more)

### Community 54 - "PlaywrightPage"
Cohesion: 0.16
Nodes (3): import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.26
Nodes (7): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding()

### Community 57 - "internship_agent/ai.py"
Cohesion: 0.15
Nodes (14): AnswerDraft, AnswerDrafts, CoverLetterDraft, format_preferences(), interpret_note(), _lead_context(), NoteResult, PeopleFindings (+6 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.06
Nodes (38): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, draft_outreach(), application_campaign(), apply_cmd() (+30 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "page_url"
Cohesion: 0.12
Nodes (10): page_url(), apply_cmd(), applied_push(), hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board() (+2 more)

### Community 61 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 62 - "LeadStatus"
Cohesion: 0.14
Nodes (13): find_deadline(), drop_unavailable(), expire_closed(), expire_postings(), LeadStatus, Note, posting(), test_closed_or_blocked_applications_are_removed_but_a_missing_resume_is_not() (+5 more)

### Community 65 - "find-internships.md"
Cohesion: 0.16
Nodes (7): Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email()

### Community 66 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "pathlib"
Cohesion: 0.23
Nodes (10): Listing, filter_items(), load(), merge(), save(), searchable_text(), search_jobs(), openai_client() (+2 more)

### Community 70 - "Region"
Cohesion: 0.21
Nodes (6): Region, founder(), test_hub_cities_and_europe_are_separate_batches(), test_spread_splits_evenly_and_keeps_fit_order(), test_unknown_area_is_rejected(), test_postings_are_filtered_to_the_search_regions()

### Community 72 - "pipeline.py"
Cohesion: 0.11
Nodes (18): board(), _bounced_lead(), _card(), classify(), confirmed_postings(), display_company(), events(), _header() (+10 more)

### Community 73 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "answer_bank"
Cohesion: 0.47
Nodes (4): answer_bank(), _submit(), _use_gmail_for_applications(), test_application_email_uses_configured_gmail()

### Community 76 - "test_followups.py"
Cohesion: 0.18
Nodes (19): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+11 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "lead_store"
Cohesion: 0.08
Nodes (18): Big-company postings from the SimplifyJobs off-season list, load_resume_text(), daily(), find_form_d_startups(), find_more_postings(), handle_note(), _incompatible_term(), lead_store() (+10 more)

### Community 83 - "dashboard.py"
Cohesion: 0.15
Nodes (12): _route(), KeyRequest, KeysRequest, _marks(), ProfileRequest, _read_map(), RefreshRequest, _send() (+4 more)

### Community 84 - "Workspace"
Cohesion: 0.18
Nodes (11): _drafts(), _listing(), _resume_chars(), state(), view(), background(), draft_id(), make_draft() (+3 more)

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 88 - "opportunity_lite/cli.py"
Cohesion: 0.29
Nodes (4): main(), _parser(), serve(), load_env()

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 91 - "classify_text"
Cohesion: 0.26
Nodes (9): classify_text(), Stage, message(), test_a_receipt_that_mentions_interviews_is_not_one(), test_application_updates_skips_unrelated_mail(), test_classify_text_stages(), test_guess_company_prefers_display_name_then_domain(), test_interview_events() (+1 more)

### Community 92 - "Settings"
Cohesion: 0.12
Nodes (8): Settings, append(), read_log(), inboxes(), _log_xai(), _run_ai_cost(), send_email(), sent_note()

### Community 94 - "create_server"
Cohesion: 0.33
Nodes (7): create_server(), _allowed(), do_GET(), do_POST(), _json(), _send_bytes(), _message()

### Community 95 - "typing"
Cohesion: 0.10
Nodes (24): AshbyJob, AshbyResponse, Conference, Config, GitHubPosting, GreenhouseJob, GreenhouseLocation, GreenhouseResponse (+16 more)

### Community 101 - "test_patterns.py"
Cohesion: 0.20
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 107 - "web.py"
Cohesion: 0.33
Nodes (4): is_email(), Contact, find_contact(), published_on()

### Community 111 - "opportunity_lite/leads/sending.py"
Cohesion: 0.18
Nodes (7): draft_message(), prepare_email(), SendRequest, StoredDraft, Draft, test_resume_is_read_and_attached(), test_send_requires_explicit_confirmation_and_blocks_duplicate()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 649 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **23 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `big_companies.py`, `notify.py`, `pytest`, `applications/browser.py`, `test_application_browser.py`, `ApplicationPrep`, `form_d.py`, `test_dashboard.py`, `README.md`, `get_settings`, `app.py`, `LeadKind`, `FormQuestion`, `workflows.py`, `test_people.py`, `Segment`, `EmailStatus`, `leads/schemas.py`, `test_refill.py`, `agenda.py`, `test_site_emails.py`, `Table`, `internship_agent/leads/sending.py`, `OutreachDraft`, `LeadStore`, `run_followups`, `insights`, `internship_agent/ai.py`, `leads/cli.py`, `answers.py`, `LeadStatus`, `find-internships.md`, `batches`, `Region`, `pipeline.py`, `answer_bank`, `test_followups.py`, `test_scrape_stores_every_matching_non_workday_posting`, `lead_store`, `Settings`, `test_patterns.py`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 136 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 136 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.053555750658472345 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Lead`, `ApplicationPrep`, `internship_agent/cli.py`, `json`, `README.md`, `test_opportunities.py`, `get_settings`, `app.py`, `LeadKind`, `FormQuestion`, `client.py`, `workflows.py`, `apply_events`, `test_apply_events.py`, `test_people.py`, `Segment`, `EmailStatus`, `test_refill.py`, `run.py`, `test_site_emails.py`, `Table`, `run_followups`, `leads/cli.py`, `test_auto_pick.py`, `answers.py`, `pipeline.py`, `answer_bank`, `test_followups.py`, `test_scrape_stores_every_matching_non_workday_posting`, `lead_store`, `test_patterns.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 105 INFERRED edges - model-reasoned connections that need verification._
- **Should `big_companies.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11806543385490754 - nodes in this community are weakly interconnected._