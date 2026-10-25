# Graph Report - winter-2027-internship-agent  (2026-10-25)

## Corpus Check
- 143 files · ~649,988 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 31 file(s) not represented in the graph (top: .timer 10, (none) 7, .service 7)

## Summary
- 2051 nodes · 6110 edges · 109 communities (85 shown, 24 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1015 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `48002fc2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- big_companies.py
- notify.py
- internship_agent/mailer.py
- run_followups
- applications/browser.py
- test_application_browser.py
- ApplicationPrep
- form_d.py
- pytest
- connect
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- tracking.py
- BaseModel
- verification_mail.py
- simplify.py
- QuestionKind
- EventFinding
- OutlookClient
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- Region
- run.py
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
- db.py
- README.md
- Opportunity
- OpportunityStore
- mailbox.py
- test_refill.py
- re
- Table
- client.py
- EmailStatus
- post_text
- test_verification_mail.py
- post
- Mailbox
- collections_abc
- people
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- pipeline.py
- help
- test_auto_pick.py
- test_links.py
- _get
- Lead
- Winter 2027 Internship Agent
- app.py
- find-founders.md
- urllib_parse
- batches
- workspace.py
- find_deadline
- OpportunityStatus
- FakeToggle
- insights
- followups_cmd
- candidate_context.md
- inboxes
- followup_run.py
- leads/schemas.py
- run-inbox-check.sh
- find-opportunities.md
- workflows.py
- export.py
- dashboard.py
- Workspace
- test_tables
- outlook
- opportunity_lite/cli.py
- Bot Auto application preview
- _view
- _scan_inboxes
- ranking.py
- run-email-batch.sh
- create_server
- sources.py
- test_scheduled_jobs.py
- FormQuestion
- test_patterns.py
- ↗ Intern Agent
- fit_to_limit
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

## Communities (109 total, 24 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.07
Nodes (29): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+21 more)

### Community 2 - "big_companies.py"
Cohesion: 0.12
Nodes (20): amazon_roles(), _get(), microsoft_roles(), posting_is_gone(), postings(), to_lead(), boards(), fetch() (+12 more)

### Community 3 - "notify.py"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 4 - "internship_agent/mailer.py"
Cohesion: 0.16
Nodes (6): deliver(), build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 5 - "run_followups"
Cohesion: 0.32
Nodes (17): run_followups(), emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "ApplicationPrep"
Cohesion: 0.10
Nodes (17): ApplicationPrep, FitAssessment, test_campaign_moves_on_when_the_scrape_or_one_application_fails(), load(), prepare(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare() (+9 more)

### Community 9 - "form_d.py"
Cohesion: 0.13
Nodes (17): candidate_domains(), _check(), company_name(), _description(), Filing, filings(), find_site(), form_d_paths() (+9 more)

### Community 10 - "pytest"
Cohesion: 0.07
Nodes (39): dashboard(), OutreachDraft, _slug(), LeadStore, test_post_submit_state_is_persisted_for_tracker(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof() (+31 more)

### Community 11 - "connect"
Cohesion: 0.11
Nodes (11): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+3 more)

### Community 12 - "json"
Cohesion: 0.17
Nodes (12): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.11
Nodes (20): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, format_preferences(), interpret_note(), _lead_context(), NoteResult (+12 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.21
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.16
Nodes (16): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), CheckRequest, event_proof() (+8 more)

### Community 17 - "tracking.py"
Cohesion: 0.21
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "BaseModel"
Cohesion: 0.14
Nodes (9): AnswerEdit, browser_sessions(), Cookie, followups(), FollowupsRequest, OpportunityStatusUpdate, SessionsRequest, submit() (+1 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.15
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "simplify.py"
Cohesion: 0.07
Nodes (16): application_url(), cards(), parse(), _cell(), parse(), postings(), region_from_text(), regions_of() (+8 more)

### Community 21 - "QuestionKind"
Cohesion: 0.20
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 22 - "EventFinding"
Cohesion: 0.50
Nodes (3): EventFinding, EventFindings, finding()

### Community 23 - "OutlookClient"
Cohesion: 0.15
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 25 - "leads/cli.py"
Cohesion: 0.20
Nodes (10): draft_outreach(), _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), prepare_all_cmd(), _resume() (+2 more)

### Community 26 - "Region"
Cohesion: 0.16
Nodes (12): hub(), in_area(), spread(), Region, inbox_send(), founder(), test_hub_cities_and_europe_are_separate_batches(), test_spread_splits_evenly_and_keeps_fit_order() (+4 more)

### Community 27 - "run.py"
Cohesion: 0.06
Nodes (27): assess(), next_step(), search_events(), write_strategy(), describe(), saved_browser(), apply_cmd(), sign_in_cmd() (+19 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.15
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.19
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 30 - "command"
Cohesion: 0.18
Nodes (5): browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd()

### Community 31 - "run"
Cohesion: 0.10
Nodes (12): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), _refusal(), resolve() (+4 more)

### Community 33 - "test_people.py"
Cohesion: 0.07
Nodes (18): Internship agent coding instructions, FitResult, OutreachDraftResult, _on_linkedin(), source_names(), names(), page_names(), source_confirms() (+10 more)

### Community 34 - "Segment"
Cohesion: 0.09
Nodes (23): More people to connect with, chosen by company size, search_people(), Person, Round, Segment, Verdict, effective_segment(), parse_round() (+15 more)

### Community 35 - "patterns.py"
Cohesion: 0.11
Nodes (13): Output, guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes() (+5 more)

### Community 40 - "db.py"
Cohesion: 0.17
Nodes (6): append(), read_log(), _logged_subject(), events(), scan(), _log_xai()

### Community 41 - "README.md"
Cohesion: 0.36
Nodes (9): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points), Rules learned from notes (skip, downrank, boost) (+1 more)

### Community 42 - "Opportunity"
Cohesion: 0.15
Nodes (9): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics() (+1 more)

### Community 43 - "OpportunityStore"
Cohesion: 0.25
Nodes (7): mark_cmd(), auto_pick(), plan_submission(), OpportunityStore, test_auto_pick_marks_interested_and_says_why(), test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 44 - "mailbox.py"
Cohesion: 0.17
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "test_refill.py"
Cohesion: 0.07
Nodes (10): test_postings_are_filtered_to_the_search_regions(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_posting_dates_come_from_the_source_or_the_day_found() (+2 more)

### Community 46 - "re"
Cohesion: 0.26
Nodes (9): _clean(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+1 more)

### Community 47 - "Table"
Cohesion: 0.09
Nodes (15): Table, _normalize(), PreferenceStore, PreferenceEffect, PostgresLeadStore, posting(), settings(), test_apply_violations_never_touches_applied_leads() (+7 more)

### Community 48 - "client.py"
Cohesion: 0.25
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "EmailStatus"
Cohesion: 0.21
Nodes (7): Send email safeguards, EmailStatus, check_outreach_text(), check_send(), SendBlocked, send_email(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 50 - "post_text"
Cohesion: 0.40
Nodes (3): post_id(), post_text(), test_only_a_link_to_a_post_has_a_post_id()

### Community 51 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 52 - "post"
Cohesion: 0.21
Nodes (10): post(), daily_run(), delete_preference(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest, PreferenceDelete (+2 more)

### Community 54 - "collections_abc"
Cohesion: 0.13
Nodes (3): Element, import_sessions(), PlaywrightPage

### Community 55 - "people"
Cohesion: 0.18
Nodes (11): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), note(), NoteRequest, people(), Dashboard page (index.html), Email section with two-click send (+3 more)

### Community 57 - "pipeline.py"
Cohesion: 0.17
Nodes (11): _bounced_lead(), classify(), confirmed_postings(), _header(), _host(), _is_ats(), match(), sync() (+3 more)

### Community 58 - "help"
Cohesion: 0.13
Nodes (10): application_campaign(), apply_cmd(), find_startups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd(), scrape_discord_cmd(), site_emails_cmd() (+2 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.47
Nodes (7): check(), hack(), reason(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition(), test_push_names_what_was_picked()

### Community 60 - "test_links.py"
Cohesion: 0.24
Nodes (7): hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about(), test_page_urls_open_a_view_or_one_item()

### Community 61 - "_get"
Cohesion: 0.14
Nodes (10): application_proof(), calendar(), calendar_ics(), _calendar_items(), _get(), job_pipeline(), prepare(), save() (+2 more)

### Community 62 - "Lead"
Cohesion: 0.09
Nodes (23): role_of(), apply_violations(), drop_unavailable(), expire_closed(), expire_postings(), Lead, LeadKind, LeadStatus (+15 more)

### Community 63 - "Winter 2027 Internship Agent"
Cohesion: 0.25
Nodes (8): Current setup, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does, Winter 2027 Internship Agent

### Community 64 - "app.py"
Cohesion: 0.12
Nodes (12): Dashboard, ask(), ChatRequest, dashboard_css(), health(), _icon(), leads(), local_only() (+4 more)

### Community 65 - "find-founders.md"
Cohesion: 0.12
Nodes (13): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+5 more)

### Community 66 - "urllib_parse"
Cohesion: 0.20
Nodes (4): _fetch(), generic(), personal(), published()

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "workspace.py"
Cohesion: 0.19
Nodes (11): draft_message(), Draft, Listing, filter_items(), load(), merge(), save(), searchable_text() (+3 more)

### Community 69 - "find_deadline"
Cohesion: 0.29
Nodes (3): find_deadline(), test_finds_a_stated_deadline(), test_ignores_text_without_a_full_dated_deadline()

### Community 70 - "OpportunityStatus"
Cohesion: 0.09
Nodes (17): find_events_cmd(), import_cmd(), list_cmd(), refresh_cmd(), strategy_cmd(), find_events(), import_inbox(), keep() (+9 more)

### Community 71 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 72 - "insights"
Cohesion: 0.16
Nodes (10): board(), _card(), display_company(), InboxEvent, insights(), got(), split(), _pct() (+2 more)

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 76 - "followup_run.py"
Cohesion: 0.11
Nodes (14): FollowupReport, FollowupSent, _misaddressed(), _name(), _site(), company_domain(), first_name(), followup_body() (+6 more)

### Community 77 - "leads/schemas.py"
Cohesion: 0.07
Nodes (17): _identity(), normalize_url(), check_cmd(), SubmissionTrack, _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply() (+9 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "workflows.py"
Cohesion: 0.07
Nodes (39): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Big-company postings from the SimplifyJobs off-season list, Settings, common_questions(), is_workday(), open_postings(), refill() (+31 more)

### Community 83 - "dashboard.py"
Cohesion: 0.11
Nodes (16): _route(), KeyRequest, KeysRequest, _marks(), ProfileRequest, _read_map(), RefreshRequest, _send() (+8 more)

### Community 84 - "Workspace"
Cohesion: 0.19
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

### Community 90 - "_view"
Cohesion: 0.22
Nodes (7): draft(), send(), SendRequest, set_status(), StatusUpdate, _view(), Lead detail panel: fit, links, contact, actions

### Community 92 - "ranking.py"
Cohesion: 0.28
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 94 - "create_server"
Cohesion: 0.26
Nodes (8): create_server(), _allowed(), do_GET(), do_POST(), _json(), _send_bytes(), _message(), save_env()

### Community 95 - "sources.py"
Cohesion: 0.10
Nodes (25): AshbyJob, AshbyResponse, Conference, Config, Contact, GitHubPosting, GreenhouseJob, GreenhouseLocation (+17 more)

### Community 99 - "FormQuestion"
Cohesion: 0.16
Nodes (12): _answer_for(), AnswerBank, category(), match_option(), normalize(), prefill(), validate(), FormQuestion (+4 more)

### Community 101 - "test_patterns.py"
Cohesion: 0.17
Nodes (12): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+4 more)

### Community 105 - "↗ Intern Agent"
Cohesion: 0.15
Nodes (11): Intern Agent walkthrough, Try it yourself, ⌨️ Command line, 🤝 Contributing, ↗ Intern Agent, 📄 License, 🔒 Privacy, 🚀 Quick start (+3 more)

### Community 107 - "web.py"
Cohesion: 0.31
Nodes (5): is_email(), WebPostings, find_contact(), published_on(), search_jobs()

### Community 111 - "test_lite.py"
Cohesion: 0.15
Nodes (5): _client_returning(), test_contact_must_appear_on_its_source_page(), test_env_file_fills_unset_values_only(), test_web_search_keeps_only_valid_posting_urls(), no_real_services()

### Community 112 - "start.sh"
Cohesion: 0.50
Nodes (3): DISPLAY, HOME, start.sh script

## Knowledge Gaps
- **6 isolated node(s):** `cmd`, `DISPLAY`, `HOME`, `intern-agent`, `internship-agent` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 650 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `big_companies.py`, `notify.py`, `run_followups`, `applications/browser.py`, `test_application_browser.py`, `ApplicationPrep`, `form_d.py`, `pytest`, `internship_agent/ai.py`, `simplify.py`, `QuestionKind`, `leads/cli.py`, `Region`, `Segment`, `patterns.py`, `Opportunity`, `test_refill.py`, `Table`, `EmailStatus`, `pipeline.py`, `_get`, `app.py`, `find-founders.md`, `batches`, `insights`, `followup_run.py`, `leads/schemas.py`, `workflows.py`, `export.py`, `_view`, `ranking.py`, `FormQuestion`, `test_patterns.py`, `fit_to_limit`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Are the 136 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 136 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `DISPLAY`, `HOME` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06918238993710692 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `test_sign_in.py`, `test_pipeline.py`, `run_followups`, `ApplicationPrep`, `pytest`, `connect`, `json`, `test_opportunities.py`, `get_settings`, `QuestionKind`, `leads/cli.py`, `Region`, `run.py`, `test_apply_events.py`, `feeds.py`, `test_people.py`, `Segment`, `patterns.py`, `db.py`, `OpportunityStore`, `Table`, `client.py`, `EmailStatus`, `pipeline.py`, `help`, `Lead`, `app.py`, `OpportunityStatus`, `inboxes`, `followup_run.py`, `leads/schemas.py`, `FormQuestion`, `test_patterns.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 105 INFERRED edges - model-reasoned connections that need verification._
- **Should `big_companies.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12162162162162163 - nodes in this community are weakly interconnected._