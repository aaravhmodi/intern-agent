# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 105 files · ~128,024 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 16 file(s) not represented in the graph (top: (none) 5, .service 4, .timer 4)

## Summary
- 1692 nodes · 5072 edges · 87 communities (68 shown, 19 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 857 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `57d274c3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- Region
- answers.py
- OpportunityStore
- Settings
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- client.py
- app.py
- verification_mail.py
- FormQuestion
- run.py
- test_people.py
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- find_startups
- apply_events
- test_apply_events.py
- Opportunity
- re
- run
- run-lowest-30-applications.sh
- startups.py
- Segment
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- pytest
- README.md
- agenda.py
- test_chat.py
- mailbox.py
- test_form_d.py
- Table
- leads/schemas.py
- export.py
- send_email
- sync
- QuestionKind
- test_patterns.py
- Mailbox
- PlaywrightPage
- set_status
- test_verification_mail.py
- pipeline.py
- command
- test_auto_pick.py
- test_agenda.py
- _get
- test_tables
- followup_run.py
- FakeToggle
- find-founders.md
- OutreachDraft
- rank
- load_resume_text
- note
- list_cmd
- test_apply_events_saves_the_result_and_marks_it_submitted
- insights
- guess_email
- candidate_context.md
- _view
- LeadStore
- opportunities/cli.py
- run-inbox-check.sh
- find-opportunities.md
- _TableParser
- FakeResponses
- _scan_inboxes
- test_devpost_dates
- Lead

## God Nodes (most connected - your core abstractions)
1. `Lead` - 155 edges
2. `Settings` - 114 edges
3. `get_settings()` - 77 edges
4. `Opportunity` - 71 edges
5. `LeadStatus` - 46 edges
6. `OpportunityStore` - 43 edges
7. `run_followups()` - 36 edges
8. `LeadKind` - 32 edges
9. `Region` - 32 edges
10. `run()` - 31 edges

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

## Communities (87 total, 19 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.15
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (17): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_dashboard_shows_the_board() (+9 more)

### Community 2 - "Region"
Cohesion: 0.14
Nodes (13): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+5 more)

### Community 3 - "answers.py"
Cohesion: 0.15
Nodes (17): category(), prefill(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send() (+9 more)

### Community 4 - "OpportunityStore"
Cohesion: 0.25
Nodes (8): mark_cmd(), auto_pick(), plan_submission(), OpportunityStatus, OpportunityStore, test_auto_pick_marks_interested_and_says_why(), test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 5 - "Settings"
Cohesion: 0.06
Nodes (39): Settings, read_log(), _logged_subject(), run_followups(), first_name(), followup_body(), is_due(), last_contact() (+31 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.09
Nodes (14): FitAssessment, _slug(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "form_d.py"
Cohesion: 0.16
Nodes (10): company_name(), Filing, filings(), find_site(), form_d_paths(), _get(), index_url(), parse_filing() (+2 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.17
Nodes (14): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.16
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "json"
Cohesion: 0.08
Nodes (29): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+21 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.15
Nodes (17): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+9 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.21
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), CheckRequest, daily_run() (+11 more)

### Community 17 - "client.py"
Cohesion: 0.05
Nodes (37): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), run(), connect(), OutlookClient, OutlookError (+29 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (22): Screenshot: rules learned from notes, two skip and one boost, AnswerEdit, browser_sessions(), Cookie, delete_preference(), find_more(), find_more_startups(), FindMoreRequest (+14 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.17
Nodes (9): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+1 more)

### Community 21 - "FormQuestion"
Cohesion: 0.19
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), validate(), FormQuestion, test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 22 - "run.py"
Cohesion: 0.09
Nodes (19): normalize_url(), assess(), EventFinding, EventFindings, next_step(), search_events(), write_strategy(), _candidate() (+11 more)

### Community 23 - "test_people.py"
Cohesion: 0.20
Nodes (9): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size() (+1 more)

### Community 25 - "leads/cli.py"
Cohesion: 0.14
Nodes (15): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+7 more)

### Community 26 - "find_startups"
Cohesion: 0.11
Nodes (12): search_startups(), StartupFinding, find_startups(), post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+4 more)

### Community 27 - "apply_events"
Cohesion: 0.13
Nodes (10): describe(), done(), apply_events(), step(), proof_path(), send_sessions(), sign_in(), step() (+2 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.15
Nodes (10): Snapshot, FakePage, landing(), step(), steps(), test_allowed_sites(), fake_browser(), test_dry_run_only_says_what_it_would_do() (+2 more)

### Community 29 - "Opportunity"
Cohesion: 0.18
Nodes (15): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+7 more)

### Community 30 - "re"
Cohesion: 0.15
Nodes (10): candidate_domains(), _check(), _description(), _fetch(), founder_email(), _has_name(), generic(), personal() (+2 more)

### Community 31 - "run"
Cohesion: 0.10
Nodes (12): allowed(), Element, _host(), names_event(), nothing_to_sign_in(), Page, _quote(), _refusal() (+4 more)

### Community 33 - "startups.py"
Cohesion: 0.13
Nodes (10): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names(), to_people(), mentions(), names(), page_names() (+2 more)

### Community 34 - "Segment"
Cohesion: 0.15
Nodes (14): Segment, effective_segment(), parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+6 more)

### Community 35 - "patterns.py"
Cohesion: 0.12
Nodes (13): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+5 more)

### Community 40 - "pytest"
Cohesion: 0.25
Nodes (15): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+7 more)

### Community 41 - "README.md"
Cohesion: 0.12
Nodes (17): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Dashboard, Development (+9 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.37
Nodes (9): fake_get(), _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day(), test_read_repo_returns_the_readme_or_says_it_is_missing() (+1 more)

### Community 44 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "test_form_d.py"
Cohesion: 0.13
Nodes (5): test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), lead(), test_published_addresses_are_read_from_the_company_pages(), test_the_company_inbox_takes_over_after_two_bounces()

### Community 46 - "Table"
Cohesion: 0.09
Nodes (16): NoteResult, PreferenceDraft, Table, _normalize(), PreferenceStore, PreferenceEffect, PostgresLeadStore, posting() (+8 more)

### Community 47 - "leads/schemas.py"
Cohesion: 0.11
Nodes (18): is_workday(), open_postings(), refill(), LeadKind, LeadStatus, Round, Verdict, _identity() (+10 more)

### Community 49 - "send_email"
Cohesion: 0.09
Nodes (9): Internship agent coding instructions, Send email safeguards, append(), check_outreach_text(), check_send(), SendBlocked, _log_xai(), _record_openai_usage() (+1 more)

### Community 50 - "sync"
Cohesion: 0.21
Nodes (8): board(), _card(), display_company(), events(), InboxEvent, push_for(), scan(), sync()

### Community 51 - "QuestionKind"
Cohesion: 0.20
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 52 - "test_patterns.py"
Cohesion: 0.23
Nodes (10): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+2 more)

### Community 54 - "PlaywrightPage"
Cohesion: 0.16
Nodes (3): import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "set_status"
Cohesion: 0.20
Nodes (8): Screenshot: a startup's fit score (91, strong), reasons and talking points, ask(), ChatRequest, draft(), set_status(), StatusUpdate, Lead detail panel: fit, links, contact, actions, resume_text()

### Community 56 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 57 - "pipeline.py"
Cohesion: 0.17
Nodes (10): company_domain(), _bounced_lead(), classify(), _header(), _host(), _is_ats(), match(), to_event() (+2 more)

### Community 58 - "command"
Cohesion: 0.10
Nodes (13): application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd(), form_d_cmd() (+5 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.47
Nodes (7): check(), hack(), reason(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition(), test_push_names_what_was_picked()

### Community 60 - "test_agenda.py"
Cohesion: 0.21
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 61 - "_get"
Cohesion: 0.18
Nodes (7): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get(), job_pipeline()

### Community 63 - "followup_run.py"
Cohesion: 0.22
Nodes (5): FollowupReport, FollowupSent, _misaddressed(), _name(), _site()

### Community 64 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 65 - "find-founders.md"
Cohesion: 0.13
Nodes (10): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+2 more)

### Community 66 - "OutreachDraft"
Cohesion: 0.18
Nodes (3): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 69 - "note"
Cohesion: 0.22
Nodes (10): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), note(), NoteRequest, Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search (+2 more)

### Community 70 - "list_cmd"
Cohesion: 0.17
Nodes (9): list_cmd(), import_inbox(), keep(), nearby(), next_date(), pick_reason(), summary_push(), upcoming() (+1 more)

### Community 71 - "test_apply_events_saves_the_result_and_marks_it_submitted"
Cohesion: 0.25
Nodes (6): _event(), _settings(), test_apply_events_saves_the_result_and_marks_it_submitted(), test_dashboard_apply_rules(), test_to_apply_takes_interested_untried_open_events(), opp()

### Community 72 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 73 - "guess_email"
Cohesion: 0.24
Nodes (4): Output, _clean(), guess_email(), test_guess_email()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "_view"
Cohesion: 0.22
Nodes (6): rescore(), save(), SaveAnswersRequest, send(), SendRequest, _view()

### Community 76 - "LeadStore"
Cohesion: 0.47
Nodes (3): LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 77 - "opportunities/cli.py"
Cohesion: 0.12
Nodes (9): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), refresh_cmd(), sign_in_cmd(), strategy_cmd(), applied_push() (+1 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "Lead"
Cohesion: 0.08
Nodes (31): Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Fit score against the resume (0-100, reasons, talking points), Rules learned from notes (skip, downrank, boost), common_questions(), apply_violations(), ApplicationPrep, Lead, Note (+23 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 529 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Region`, `OpportunityStore`, `test_daily_campaign.py`, `json`, `test_opportunities.py`, `get_settings`, `client.py`, `app.py`, `leads/store.py`, `FormQuestion`, `run.py`, `test_people.py`, `leads/cli.py`, `find_startups`, `apply_events`, `Opportunity`, `patterns.py`, `README.md`, `test_chat.py`, `Table`, `send_email`, `sync`, `QuestionKind`, `test_patterns.py`, `set_status`, `pipeline.py`, `test_agenda.py`, `followup_run.py`, `list_cmd`, `test_apply_events_saves_the_result_and_marks_it_submitted`, `opportunities/cli.py`, `Lead`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 114 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 114 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11827956989247312 - nodes in this community are weakly interconnected._
- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `Region`, `answers.py`, `Settings`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `internship_agent/ai.py`, `app.py`, `leads/store.py`, `FormQuestion`, `leads/cli.py`, `find_startups`, `startups.py`, `Segment`, `patterns.py`, `pytest`, `agenda.py`, `test_form_d.py`, `Table`, `leads/schemas.py`, `export.py`, `send_email`, `sync`, `QuestionKind`, `test_patterns.py`, `set_status`, `pipeline.py`, `test_agenda.py`, `_get`, `followup_run.py`, `find-founders.md`, `OutreachDraft`, `rank`, `insights`, `_view`, `LeadStore`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Are the 96 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 96 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._