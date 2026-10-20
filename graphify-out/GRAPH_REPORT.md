# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 100 files · ~121,563 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1584 nodes · 4752 edges · 75 communities (60 shown, 15 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 816 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9e279454`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_chat.py
- Region
- PreparedAnswer
- opportunities/cli.py
- test_followups.py
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- re
- test_dashboard.py
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- tracking.py
- app.py
- agenda.py
- run_followups
- feeds.py
- run.py
- test_ai.py
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- FakeField
- test_apply_events.py
- pytest
- Table
- run
- run-lowest-30-applications.sh
- test_people.py
- leads/schemas.py
- test_patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- config.py
- README.md
- _get
- local_only
- mailbox.py
- OutlookClient
- LeadStatus
- db.py
- EmailStatus
- send_email
- outlook/schemas.py
- FormQuestion
- find_startups
- Mailbox
- typing
- send
- candidate_context.md
- verification_mail.py
- leads/cli.py
- test_auto_pick.py
- followups.py
- _view
- fit_to_limit
- StepAction
- FakeToggle
- guess_email
- Lead
- _post_submit_outcome
- test_hidden_recaptcha_support_nodes_do_not_block
- _confirmation_quote
- Opportunity
- _field_label
- _numeric_answer
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 140 edges
2. `Settings` - 106 edges
3. `get_settings()` - 73 edges
4. `Opportunity` - 71 edges
5. `OpportunityStore` - 43 edges
6. `LeadStatus` - 40 edges
7. `run_followups()` - 35 edges
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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (75 total, 15 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.14
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_chat.py"
Cohesion: 0.11
Nodes (18): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+10 more)

### Community 2 - "Region"
Cohesion: 0.12
Nodes (10): Region, region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+2 more)

### Community 3 - "PreparedAnswer"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 4 - "opportunities/cli.py"
Cohesion: 0.12
Nodes (9): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), mark_cmd(), strategy_cmd(), applied_push() (+1 more)

### Community 5 - "test_followups.py"
Cohesion: 0.21
Nodes (18): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+10 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.12
Nodes (16): apply_to_posting(), _confirmed(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _react_select_answer(), _save_screenshot() (+8 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.23
Nodes (16): _answer_for(), _fill_form(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+8 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.09
Nodes (15): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+7 more)

### Community 9 - "re"
Cohesion: 0.10
Nodes (19): _clean(), candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings() (+11 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.17
Nodes (14): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "json"
Cohesion: 0.07
Nodes (32): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+24 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.11
Nodes (21): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+13 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.16
Nodes (24): EventFinding, _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure() (+16 more)

### Community 16 - "get_settings"
Cohesion: 0.16
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run(), delete_preference() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.11
Nodes (18): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, FindStartupsRequest, followups() (+10 more)

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "run_followups"
Cohesion: 0.23
Nodes (8): FollowupReport, FollowupSent, _misaddressed(), _name(), run_followups(), _site(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 21 - "feeds.py"
Cohesion: 0.20
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 22 - "run.py"
Cohesion: 0.05
Nodes (28): assess(), EventFindings, next_step(), search_events(), write_strategy(), describe(), done(), sign_in_cmd() (+20 more)

### Community 23 - "test_ai.py"
Cohesion: 0.27
Nodes (6): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 25 - "patterns.py"
Cohesion: 0.12
Nodes (12): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+4 more)

### Community 26 - "x_search.py"
Cohesion: 0.11
Nodes (12): StartupFinding, StartupFindings, _slug(), post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+4 more)

### Community 27 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "pytest"
Cohesion: 0.27
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 31 - "run"
Cohesion: 0.15
Nodes (9): allowed(), _host(), names_event(), nothing_to_sign_in(), _quote(), _refusal(), resolve(), run() (+1 more)

### Community 33 - "test_people.py"
Cohesion: 0.14
Nodes (9): _on_linkedin(), source_names(), page_names(), source_confirms(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size() (+1 more)

### Community 34 - "leads/schemas.py"
Cohesion: 0.09
Nodes (19): LeadKind, Round, Segment, Verdict, parse_round(), mentions(), names(), to_leads() (+11 more)

### Community 35 - "test_patterns.py"
Cohesion: 0.19
Nodes (10): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+2 more)

### Community 40 - "config.py"
Cohesion: 0.19
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 41 - "README.md"
Cohesion: 0.10
Nodes (27): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Current setup, Development (+19 more)

### Community 42 - "_get"
Cohesion: 0.15
Nodes (9): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), event_proof(), _get(), note() (+1 more)

### Community 43 - "local_only"
Cohesion: 0.29
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 44 - "mailbox.py"
Cohesion: 0.19
Nodes (5): company_domain(), GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "OutlookClient"
Cohesion: 0.15
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 46 - "LeadStatus"
Cohesion: 0.07
Nodes (23): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, no_real_services(), posting() (+15 more)

### Community 47 - "db.py"
Cohesion: 0.13
Nodes (6): append(), read_log(), _logged_subject(), _log_xai(), _record_openai_usage(), _run_ai_cost()

### Community 48 - "EmailStatus"
Cohesion: 0.21
Nodes (8): _email_line(), render_outreach(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_render_outreach_flags_unverified_emails_and_skips_undrafted(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 49 - "send_email"
Cohesion: 0.15
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 50 - "outlook/schemas.py"
Cohesion: 0.26
Nodes (9): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient (+1 more)

### Community 51 - "FormQuestion"
Cohesion: 0.12
Nodes (22): AnswerBank, common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion, QuestionKind (+14 more)

### Community 52 - "find_startups"
Cohesion: 0.26
Nodes (6): More people to connect with, chosen by company size, Person, effective_segment(), to_people(), find_startups(), people_at()

### Community 54 - "typing"
Cohesion: 0.12
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "send"
Cohesion: 0.18
Nodes (3): Internship agent coding instructions, send(), SendRequest

### Community 56 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 57 - "verification_mail.py"
Cohesion: 0.08
Nodes (13): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+5 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.06
Nodes (38): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+30 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.29
Nodes (8): check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition(), test_push_names_what_was_picked()

### Community 60 - "followups.py"
Cohesion: 0.26
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), next_followup()

### Community 61 - "_view"
Cohesion: 0.24
Nodes (10): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), find_more(), FindMoreRequest, leads(), rescore(), _sort_key(), _view() (+2 more)

### Community 65 - "guess_email"
Cohesion: 0.33
Nodes (3): Output, guess_email(), test_guess_email()

### Community 66 - "Lead"
Cohesion: 0.20
Nodes (4): Lead, LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 67 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

### Community 70 - "Opportunity"
Cohesion: 0.11
Nodes (17): refresh_cmd(), auto_pick(), find_events(), import_inbox(), keep(), nearby(), next_date(), pick_reason() (+9 more)

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.09
Nodes (31): Big-company postings from the SimplifyJobs off-season list, Settings, refill(), Note, merge(), fetch(), add_team_contacts(), answer_bank() (+23 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 495 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_chat.py`, `Region`, `PreparedAnswer`, `test_followups.py`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `re`, `test_dashboard.py`, `json`, `internship_agent/ai.py`, `app.py`, `agenda.py`, `run_followups`, `patterns.py`, `x_search.py`, `pytest`, `Table`, `leads/schemas.py`, `test_patterns.py`, `_get`, `LeadStatus`, `EmailStatus`, `send_email`, `FormQuestion`, `find_startups`, `leads/cli.py`, `followups.py`, `_view`, `workflows.py`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 100 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 100 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_sign_in.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `test_sign_in.py`, `test_chat.py`, `opportunities/cli.py`, `test_followups.py`, `test_daily_campaign.py`, `internship_agent/cli.py`, `json`, `internship_agent/ai.py`, `test_opportunities.py`, `get_settings`, `run_followups`, `run.py`, `patterns.py`, `test_apply_events.py`, `Table`, `test_people.py`, `test_patterns.py`, `config.py`, `local_only`, `LeadStatus`, `db.py`, `send_email`, `FormQuestion`, `find_startups`, `leads/cli.py`, `test_auto_pick.py`, `Opportunity`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 89 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 89 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_chat.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10984848484848485 - nodes in this community are weakly interconnected._