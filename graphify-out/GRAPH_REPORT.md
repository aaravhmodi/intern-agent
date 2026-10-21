# Graph Report - opportunity-agent  (2026-10-21)

## Corpus Check
- 111 files · ~230,113 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 18 file(s) not represented in the graph (top: (none) 5, .service 4, .timer 4)

## Summary
- 1744 nodes · 5217 edges · 97 communities (76 shown, 21 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 877 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3f8187b7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- Region
- notify.py
- Opportunity
- test_followups.py
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- re
- pytest
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- datetime
- answers.py
- opportunities/ai.py
- OutlookClient
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- x_search.py
- apply_events
- test_apply_events.py
- feeds.py
- find_site_emails
- typing
- run-lowest-30-applications.sh
- find_startups
- startups.py
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
- Lead
- workflows.py
- client.py
- EmailStatus
- Push
- FormQuestion
- test_patterns.py
- SentMessage
- PlaywrightPage
- lead_store
- test_verification_mail.py
- pipeline.py
- busy
- test_auto_pick.py
- test_agenda.py
- _get
- test_tables
- run_followups
- FakeToggle
- find-founders.md
- fit_to_limit
- LeadStatus
- check_events
- send
- run.py
- FakeField
- insights
- mailer.py
- candidate_context.md
- test_links.py
- followups.py
- command
- run-inbox-check.sh
- find-opportunities.md
- prepare_application
- test_answers.py
- _scan_inboxes
- daily
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- PreferenceStore
- outlook
- test_hidden_recaptcha_support_nodes_do_not_block
- Bot Auto application preview
- ToolSession
- _confirmation_quote
- _field_label
- _numeric_answer
- _react_select_answer
- test_post_submit_outcomes_across_ats_pages
- test_interview_events

## God Nodes (most connected - your core abstractions)
1. `Lead` - 159 edges
2. `Settings` - 120 edges
3. `get_settings()` - 80 edges
4. `Opportunity` - 73 edges
5. `LeadStatus` - 48 edges
6. `OpportunityStore` - 43 edges
7. `run_followups()` - 36 edges
8. `LeadKind` - 33 edges
9. `Region` - 32 edges
10. `lead_store()` - 32 edges

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

## Communities (97 total, 21 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.14
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (17): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_dashboard_shows_the_board() (+9 more)

### Community 2 - "Region"
Cohesion: 0.11
Nodes (13): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+5 more)

### Community 3 - "notify.py"
Cohesion: 0.21
Nodes (14): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer() (+6 more)

### Community 4 - "Opportunity"
Cohesion: 0.24
Nodes (6): mark_cmd(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 5 - "test_followups.py"
Cohesion: 0.32
Nodes (17): emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.14
Nodes (15): apply_to_posting(), _confirmed(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome(), _posting_is_closed(), _save_screenshot() (+7 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.20
Nodes (17): _answer_for(), _fill_form(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+9 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "re"
Cohesion: 0.08
Nodes (23): _clean(), _slug(), candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing (+15 more)

### Community 10 - "pytest"
Cohesion: 0.08
Nodes (34): LeadStore, no_real_services(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+26 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+3 more)

### Community 12 - "json"
Cohesion: 0.08
Nodes (29): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+21 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.14
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+4 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.07
Nodes (27): Internship agent coding instructions, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note() (+19 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), CheckRequest, daily_run() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (21): AnswerEdit, ask(), browser_sessions(), ChatRequest, Cookie, delete_preference(), find_more_startups(), FindStartupsRequest (+13 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.17
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "datetime"
Cohesion: 0.14
Nodes (4): lead(), test_a_published_address_proves_the_company_format(), test_inbox_send_writes_each_shared_inbox_once_hiring_ones_first(), test_published_addresses_are_read_from_the_company_pages()

### Community 21 - "answers.py"
Cohesion: 0.18
Nodes (6): AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options()

### Community 22 - "opportunities/ai.py"
Cohesion: 0.23
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding(), test_without_citations_strips_inline_links_only()

### Community 23 - "OutlookClient"
Cohesion: 0.20
Nodes (7): OutlookClient, OutlookError, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 25 - "leads/cli.py"
Cohesion: 0.10
Nodes (22): Founder leads flow: /find-founders, import, score, list, draft, mark, application_campaign(), browser_login(), daily_cmd(), _draft(), draft_all(), draft_lead(), _email_cell() (+14 more)

### Community 26 - "x_search.py"
Cohesion: 0.12
Nodes (10): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+2 more)

### Community 27 - "apply_events"
Cohesion: 0.14
Nodes (11): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _openai(), send_sessions(), sign_in() (+3 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.22
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "find_site_emails"
Cohesion: 0.29
Nodes (3): site_emails_cmd(), generic(), find_site_emails()

### Community 31 - "typing"
Cohesion: 0.09
Nodes (14): allowed(), Element, _host(), names_event(), nothing_to_sign_in(), Page, _quote(), _refusal() (+6 more)

### Community 33 - "find_startups"
Cohesion: 0.10
Nodes (19): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), _on_linkedin(), source_names(), to_people() (+11 more)

### Community 34 - "startups.py"
Cohesion: 0.12
Nodes (14): Segment, mentions(), names(), source_confirms(), to_leads(), finding(), lead(), test_effective_segment() (+6 more)

### Community 35 - "patterns.py"
Cohesion: 0.13
Nodes (11): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+3 more)

### Community 40 - "Settings"
Cohesion: 0.18
Nodes (6): Settings, append(), read_log(), events(), inboxes(), _record_openai_usage()

### Community 41 - "README.md"
Cohesion: 0.11
Nodes (21): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Dashboard (+13 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 44 - "mailbox.py"
Cohesion: 0.12
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "test_refill.py"
Cohesion: 0.11
Nodes (7): test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 46 - "Lead"
Cohesion: 0.08
Nodes (11): Table, role_of(), Lead, _identity(), merge(), PostgresLeadStore, add_team_contacts(), inbox_send() (+3 more)

### Community 47 - "workflows.py"
Cohesion: 0.11
Nodes (16): is_workday(), open_postings(), refill(), LeadKind, Note, Round, Verdict, parse_round() (+8 more)

### Community 48 - "client.py"
Cohesion: 0.25
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "EmailStatus"
Cohesion: 0.18
Nodes (9): Send email safeguards, _email_line(), render_outreach(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, send_email() (+1 more)

### Community 50 - "Push"
Cohesion: 0.22
Nodes (6): Push, send(), apply_cmd(), applied_push(), push_for(), scan()

### Community 51 - "FormQuestion"
Cohesion: 0.27
Nodes (11): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+3 more)

### Community 52 - "test_patterns.py"
Cohesion: 0.17
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 54 - "PlaywrightPage"
Cohesion: 0.16
Nodes (3): import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "lead_store"
Cohesion: 0.14
Nodes (13): draft(), find_more(), FindMoreRequest, leads(), rescore(), set_status(), _sort_key(), StatusUpdate (+5 more)

### Community 56 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 57 - "pipeline.py"
Cohesion: 0.16
Nodes (11): company_domain(), _bounced_lead(), classify(), _header(), _host(), _is_ats(), match(), sync() (+3 more)

### Community 58 - "busy"
Cohesion: 0.18
Nodes (7): apply_cmd(), find_startups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd(), team_contacts_cmd(), busy()

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 61 - "_get"
Cohesion: 0.18
Nodes (7): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get(), job_pipeline()

### Community 63 - "run_followups"
Cohesion: 0.16
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), followup_body() (+3 more)

### Community 65 - "find-founders.md"
Cohesion: 0.12
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+4 more)

### Community 67 - "LeadStatus"
Cohesion: 0.19
Nodes (7): batches(), is_open(), rank(), LeadStatus, lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 68 - "check_events"
Cohesion: 0.10
Nodes (9): normalize_url(), _candidate(), check_events(), one(), checked(), _keys(), without_citations(), load_resume_text() (+1 more)

### Community 69 - "send"
Cohesion: 0.14
Nodes (12): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), note(), NoteRequest, send(), SendRequest, Dashboard page (index.html) (+4 more)

### Community 70 - "run.py"
Cohesion: 0.11
Nodes (17): page_url(), list_cmd(), refresh_cmd(), auto_pick(), find_events(), keep(), nearby(), next_date() (+9 more)

### Community 71 - "FakeField"
Cohesion: 0.15
Nodes (3): FakeField, FakeLocator, locator()

### Community 72 - "insights"
Cohesion: 0.19
Nodes (9): board(), _card(), display_company(), InboxEvent, insights(), got(), split(), _pct() (+1 more)

### Community 73 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "test_links.py"
Cohesion: 0.20
Nodes (7): hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about(), test_page_urls_open_a_view_or_one_item()

### Community 76 - "followups.py"
Cohesion: 0.27
Nodes (4): first_name(), is_due(), last_contact(), next_followup()

### Community 77 - "command"
Cohesion: 0.13
Nodes (6): check_cmd(), find_events_cmd(), import_cmd(), strategy_cmd(), import_inbox(), proof_path()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "prepare_application"
Cohesion: 0.24
Nodes (6): answer_bank(), prepare_application(), _retryable_block(), save_answers(), _use_gmail_for_applications(), test_application_email_uses_configured_gmail()

### Community 82 - "test_answers.py"
Cohesion: 0.43
Nodes (5): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind()

### Community 83 - "_scan_inboxes"
Cohesion: 0.29
Nodes (3): _scan_forever(), _scan_inboxes(), _start_inbox_scans()

### Community 84 - "daily"
Cohesion: 0.33
Nodes (4): daily(), DailyReport, _incompatible_term(), submit_application()

### Community 86 - "PreferenceStore"
Cohesion: 0.24
Nodes (10): apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules() (+2 more)

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 549 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `Region`, `notify.py`, `test_followups.py`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `re`, `pytest`, `internship_agent/ai.py`, `app.py`, `datetime`, `leads/cli.py`, `find_site_emails`, `find_startups`, `startups.py`, `patterns.py`, `agenda.py`, `test_refill.py`, `workflows.py`, `EmailStatus`, `test_patterns.py`, `lead_store`, `pipeline.py`, `test_agenda.py`, `_get`, `run_followups`, `find-founders.md`, `LeadStatus`, `insights`, `followups.py`, `prepare_application`, `test_answers.py`, `daily`, `PreferenceStore`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_sign_in.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14245014245014245 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Region`, `Opportunity`, `test_followups.py`, `test_daily_campaign.py`, `re`, `internship_agent/cli.py`, `json`, `make_workflows.py`, `internship_agent/ai.py`, `test_opportunities.py`, `get_settings`, `app.py`, `datetime`, `leads/cli.py`, `apply_events`, `test_apply_events.py`, `find_site_emails`, `find_startups`, `patterns.py`, `test_chat.py`, `Lead`, `workflows.py`, `client.py`, `EmailStatus`, `Push`, `test_patterns.py`, `lead_store`, `pipeline.py`, `busy`, `test_auto_pick.py`, `test_agenda.py`, `run_followups`, `check_events`, `run.py`, `command`, `prepare_application`, `test_answers.py`, `daily`, `PreferenceStore`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 102 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 102 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11827956989247312 - nodes in this community are weakly interconnected._