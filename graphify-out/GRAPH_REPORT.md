# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 103 files · ~127,315 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 16 file(s) not represented in the graph (top: (none) 5, .service 4, .timer 4)

## Summary
- 1674 nodes · 5019 edges · 83 communities (68 shown, 15 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 847 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6b446c3b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- simplify.py
- notify.py
- Opportunity
- Settings
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- pytest
- internship_agent/cli.py
- json
- agenda.py
- assess_fit
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- verification_mail.py
- typing
- answers.py
- opportunities/ai.py
- test_ai.py
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- internship_agent/ai.py
- apply_events
- test_apply_events.py
- feeds.py
- Table
- run
- run-lowest-30-applications.sh
- Region
- leads/schemas.py
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- outlook
- README.md
- command
- test_chat.py
- mailbox.py
- client.py
- test_notes.py
- test_refill.py
- export.py
- send_email
- outlook/schemas.py
- FormQuestion
- checked
- Mailbox
- StepAction
- prepare_application
- test_verification_mail.py
- pipeline.py
- find_startups_cmd
- test_auto_pick.py
- test_agenda.py
- test_outlook_client.py
- test_tables
- test_people.py
- FakeToggle
- find-founders.md
- Person
- rank
- load_resume_text
- set_status
- run.py
- posting_text.py
- insights
- re
- test_x_search.py
- normalize_url
- open_lead_store
- apply_cmd
- run-inbox-check.sh
- find-opportunities.md
- test_interview_events
- Lead

## God Nodes (most connected - your core abstractions)
1. `Lead` - 153 edges
2. `Settings` - 113 edges
3. `get_settings()` - 76 edges
4. `Opportunity` - 71 edges
5. `LeadStatus` - 44 edges
6. `OpportunityStore` - 43 edges
7. `run_followups()` - 36 edges
8. `Region` - 32 edges
9. `run()` - 31 edges
10. `LeadKind` - 30 edges

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

## Communities (83 total, 15 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.16
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (17): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_dashboard_shows_the_board() (+9 more)

### Community 2 - "simplify.py"
Cohesion: 0.13
Nodes (6): cap_per_company(), is_software_role(), matching(), parse(), Posting, _TableParser

### Community 3 - "notify.py"
Cohesion: 0.16
Nodes (17): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+9 more)

### Community 4 - "Opportunity"
Cohesion: 0.17
Nodes (13): mark_cmd(), auto_pick(), plan_submission(), Opportunity, OpportunityStore, _event(), _settings(), test_apply_events_saves_the_result_and_marks_it_submitted() (+5 more)

### Community 5 - "Settings"
Cohesion: 0.07
Nodes (37): Settings, append(), read_log(), FollowupReport, FollowupSent, _logged_subject(), _name(), run_followups() (+29 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.12
Nodes (11): FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new(), test_incompatible_eight_month_term_is_rejected() (+3 more)

### Community 9 - "form_d.py"
Cohesion: 0.12
Nodes (18): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+10 more)

### Community 10 - "pytest"
Cohesion: 0.08
Nodes (33): dashboard(), LeadStore, no_real_services(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key() (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.18
Nodes (11): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+3 more)

### Community 13 - "agenda.py"
Cohesion: 0.06
Nodes (25): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+17 more)

### Community 14 - "assess_fit"
Cohesion: 0.31
Nodes (7): assess_fit(), draft_outreach(), format_preferences(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter()

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.10
Nodes (31): get_settings(), allow_event_retry(), allow_retry(), application_proof(), apply_to_event(), auto_apply(), check_opportunities(), CheckRequest (+23 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.07
Nodes (27): AnswerEdit, browser_sessions(), calendar(), calendar_ics(), _calendar_items(), Cookie, dashboard_css(), delete_preference() (+19 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.15
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 20 - "typing"
Cohesion: 0.15
Nodes (3): _misaddressed(), _site(), SubmissionTrack

### Community 21 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 22 - "opportunities/ai.py"
Cohesion: 0.23
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding(), test_without_citations_strips_inline_links_only()

### Community 23 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 25 - "leads/cli.py"
Cohesion: 0.21
Nodes (11): application_campaign(), _draft(), draft_all(), draft_lead(), followups_cmd(), mark_lead(), _openai(), _resume() (+3 more)

### Community 26 - "internship_agent/ai.py"
Cohesion: 0.14
Nodes (10): AnswerDraft, AnswerDrafts, CoverLetterDraft, PeopleFindings, search_startups(), StartupFinding, StartupFindings, post_confirms() (+2 more)

### Community 27 - "apply_events"
Cohesion: 0.12
Nodes (12): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _openai(), proof_path(), send_sessions() (+4 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.16
Nodes (10): Snapshot, FakePage, landing(), step(), steps(), test_allowed_sites(), fake_browser(), test_dry_run_only_says_what_it_would_do() (+2 more)

### Community 29 - "feeds.py"
Cohesion: 0.20
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "Table"
Cohesion: 0.15
Nodes (3): Table, PostgresLeadStore, test_a_stale_save_keeps_a_status_set_meanwhile()

### Community 31 - "run"
Cohesion: 0.11
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+2 more)

### Community 33 - "Region"
Cohesion: 0.16
Nodes (10): Region, Segment, region_from_text(), regions_of(), mentions(), names(), source_confirms(), to_leads() (+2 more)

### Community 34 - "leads/schemas.py"
Cohesion: 0.12
Nodes (14): fit_to_limit(), Round, Verdict, parse_round(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+6 more)

### Community 35 - "patterns.py"
Cohesion: 0.06
Nodes (27): Output, Output, guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess() (+19 more)

### Community 40 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 41 - "README.md"
Cohesion: 0.05
Nodes (35): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+27 more)

### Community 42 - "command"
Cohesion: 0.15
Nodes (6): browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd()

### Community 43 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 44 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "client.py"
Cohesion: 0.19
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 46 - "test_notes.py"
Cohesion: 0.15
Nodes (16): NoteResult, PreferenceDraft, _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings() (+8 more)

### Community 47 - "test_refill.py"
Cohesion: 0.11
Nodes (8): test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 49 - "send_email"
Cohesion: 0.17
Nodes (6): Send email safeguards, Email section with two-click send, check_outreach_text(), SendBlocked, send_email(), _use_gmail_for_applications()

### Community 50 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 51 - "FormQuestion"
Cohesion: 0.19
Nodes (16): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 52 - "checked"
Cohesion: 0.33
Nodes (3): one(), checked(), without_citations()

### Community 54 - "StepAction"
Cohesion: 0.13
Nodes (6): Element, _refusal(), import_sessions(), PlaywrightPage, saved_browser(), StepAction

### Community 55 - "prepare_application"
Cohesion: 0.13
Nodes (9): ask(), ChatRequest, ApplicationPrep, prepare_application(), _record_openai_usage(), resume_text(), _retryable_block(), test_post_submit_state_is_persisted_for_tracker() (+1 more)

### Community 56 - "test_verification_mail.py"
Cohesion: 0.16
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 57 - "pipeline.py"
Cohesion: 0.12
Nodes (18): company_domain(), board(), _bounced_lead(), _card(), classify(), display_company(), events(), _header() (+10 more)

### Community 58 - "find_startups_cmd"
Cohesion: 0.23
Nodes (5): apply_cmd(), find_startups_cmd(), form_d_cmd(), guess_send_cmd(), team_contacts_cmd()

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 60 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 61 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 63 - "test_people.py"
Cohesion: 0.22
Nodes (8): PersonFinding, _on_linkedin(), source_names(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 64 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 65 - "find-founders.md"
Cohesion: 0.13
Nodes (11): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+3 more)

### Community 66 - "Person"
Cohesion: 0.14
Nodes (4): FitResult, OutreachDraft, OutreachDraftResult, Person

### Community 67 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 69 - "set_status"
Cohesion: 0.16
Nodes (13): Screenshot: prepared application answers, one marked 'Needs you', Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Rules learned from notes (skip, downrank, boost), index(), set_status(), StatusUpdate, Dashboard page (index.html) (+5 more)

### Community 70 - "run.py"
Cohesion: 0.08
Nodes (22): check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), refresh_cmd(), strategy_cmd(), _candidate(), check_events() (+14 more)

### Community 71 - "posting_text.py"
Cohesion: 0.38
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 72 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 73 - "re"
Cohesion: 0.32
Nodes (3): _clean(), _slug(), post_text()

### Community 74 - "test_x_search.py"
Cohesion: 0.29
Nodes (4): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_only_a_link_to_a_post_has_a_post_id()

### Community 75 - "normalize_url"
Cohesion: 0.40
Nodes (3): normalize_url(), _keys(), test_normalize_url_keeps_meaningful_query()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "Lead"
Cohesion: 0.08
Nodes (38): Big-company postings from the SimplifyJobs off-season list, More people to connect with, chosen by company size, search_people(), apply_violations(), is_workday(), open_postings(), refill(), Lead (+30 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 521 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `simplify.py`, `notify.py`, `Settings`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `pytest`, `agenda.py`, `assess_fit`, `get_settings`, `app.py`, `typing`, `answers.py`, `leads/cli.py`, `internship_agent/ai.py`, `Table`, `Region`, `leads/schemas.py`, `patterns.py`, `test_notes.py`, `test_refill.py`, `export.py`, `send_email`, `FormQuestion`, `prepare_application`, `pipeline.py`, `test_agenda.py`, `find-founders.md`, `Person`, `rank`, `set_status`, `insights`, `open_lead_store`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 112 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 112 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12413793103448276 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `notify.py`, `Opportunity`, `test_daily_campaign.py`, `internship_agent/cli.py`, `json`, `agenda.py`, `test_opportunities.py`, `get_settings`, `app.py`, `typing`, `answers.py`, `leads/cli.py`, `apply_events`, `Table`, `patterns.py`, `test_chat.py`, `client.py`, `test_notes.py`, `send_email`, `FormQuestion`, `checked`, `prepare_application`, `pipeline.py`, `test_auto_pick.py`, `test_agenda.py`, `test_people.py`, `run.py`, `Lead`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Are the 95 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 95 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12631578947368421 - nodes in this community are weakly interconnected._