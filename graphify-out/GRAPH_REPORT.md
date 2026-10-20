# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 99 files · ~119,853 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1565 nodes · 4680 edges · 74 communities (56 shown, 18 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 793 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `71ddfebe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- AnswerBank
- Lead
- notify.py
- run.py
- test_followups.py
- applications/browser.py
- FakeField
- test_chat.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- re
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- app.py
- pydantic
- test_refill.py
- agenda.py
- run_followups
- test_agenda.py
- opportunities/ai.py
- typing
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- opportunities/schemas.py
- test_apply_events.py
- _fill_form
- Table
- apply.py
- run-lowest-30-applications.sh
- people.py
- EmailStatus
- test_application_browser.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- client.py
- README.md
- pytest
- LeadStore
- mailbox.py
- OutlookClient
- preferences.py
- test_patterns.py
- leads/schemas.py
- mailer.py
- outlook/schemas.py
- FormQuestion
- test_outlook_client.py
- SentMessage
- collections_abc
- AGENTS.md
- candidate_context.md
- verification_mail.py
- leads/cli.py
- test_post_submit_state_is_persisted_for_tracker
- apply_events
- _TableParser
- guess_email
- _calendar_items
- test_hidden_recaptcha_support_nodes_do_not_block
- export.py
- _react_select_answer
- OpportunityStore
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 140 edges
2. `Settings` - 104 edges
3. `get_settings()` - 73 edges
4. `Opportunity` - 66 edges
5. `OpportunityStore` - 41 edges
6. `LeadStatus` - 40 edges
7. `run_followups()` - 35 edges
8. `Region` - 31 edges
9. `LeadKind` - 30 edges
10. `run()` - 29 edges

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

## Communities (74 total, 18 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.12
Nodes (12): StepAction, FakePage, mail(), scripted(), step(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "AnswerBank"
Cohesion: 0.29
Nodes (6): _answer_for(), AnswerBank, test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 2 - "Lead"
Cohesion: 0.11
Nodes (11): Lead, _identity(), normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching() (+3 more)

### Community 3 - "notify.py"
Cohesion: 0.20
Nodes (14): _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers(), answer() (+6 more)

### Community 4 - "run.py"
Cohesion: 0.08
Nodes (23): refresh_cmd(), applied_push(), _candidate(), check_events(), one(), checked(), find_events(), import_inbox() (+15 more)

### Community 5 - "test_followups.py"
Cohesion: 0.21
Nodes (18): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+10 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.15
Nodes (13): apply_to_posting(), _confirmation_quote(), _confirmed(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome(), _posting_is_closed() (+5 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 8 - "test_chat.py"
Cohesion: 0.08
Nodes (22): ApplicationPrep, fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github() (+14 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (18): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+10 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.17
Nodes (14): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "re"
Cohesion: 0.06
Nodes (43): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+35 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.14
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "app.py"
Cohesion: 0.08
Nodes (52): get_settings(), allow_event_retry(), allow_retry(), AnswerEdit, application_proof(), apply_to_event(), ask(), auto_apply() (+44 more)

### Community 17 - "pydantic"
Cohesion: 0.16
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 18 - "test_refill.py"
Cohesion: 0.10
Nodes (9): test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped() (+1 more)

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "run_followups"
Cohesion: 0.11
Nodes (15): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+7 more)

### Community 21 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 22 - "opportunities/ai.py"
Cohesion: 0.19
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, SubmissionTrack, finding()

### Community 23 - "typing"
Cohesion: 0.14
Nodes (12): FitAssessment, FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person() (+4 more)

### Community 25 - "patterns.py"
Cohesion: 0.12
Nodes (12): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+4 more)

### Community 26 - "x_search.py"
Cohesion: 0.12
Nodes (11): StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 27 - "opportunities/schemas.py"
Cohesion: 0.10
Nodes (11): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), strategy_cmd(), OpportunityKind, OpportunityStatus (+3 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.16
Nodes (17): Snapshot, BrowserStep, _event(), FakePage, landing(), _settings(), step(), steps() (+9 more)

### Community 29 - "_fill_form"
Cohesion: 0.31
Nodes (13): _fill_form(), PreparedAnswer, FakePage, posting(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+5 more)

### Community 31 - "apply.py"
Cohesion: 0.11
Nodes (11): allowed(), _host(), names_event(), Page, _quote(), _refusal(), resolve(), run() (+3 more)

### Community 33 - "people.py"
Cohesion: 0.17
Nodes (8): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 34 - "EmailStatus"
Cohesion: 0.31
Nodes (5): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 35 - "test_application_browser.py"
Cohesion: 0.12
Nodes (9): _field_label(), _numeric_answer(), test_closed_posting_text_is_detected(), test_confirmation_quote_keeps_the_employers_line(), test_field_label_does_not_expose_generated_lever_field_ids(), test_numeric_input_format_uses_saved_salary_and_study_values(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages() (+1 more)

### Community 40 - "client.py"
Cohesion: 0.15
Nodes (5): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), no_real_services()

### Community 41 - "README.md"
Cohesion: 0.10
Nodes (28): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+20 more)

### Community 42 - "pytest"
Cohesion: 0.25
Nodes (15): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+7 more)

### Community 43 - "LeadStore"
Cohesion: 0.57
Nodes (3): LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 44 - "mailbox.py"
Cohesion: 0.16
Nodes (5): GmailMailbox, _imap_date(), Mailbox, MailboxError, _quoted()

### Community 45 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 46 - "preferences.py"
Cohesion: 0.16
Nodes (16): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 47 - "test_patterns.py"
Cohesion: 0.19
Nodes (10): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+2 more)

### Community 48 - "leads/schemas.py"
Cohesion: 0.10
Nodes (19): fit_to_limit(), Region, Round, Segment, Verdict, parse_round(), mentions(), names() (+11 more)

### Community 49 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 50 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 51 - "FormQuestion"
Cohesion: 0.12
Nodes (22): category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion, QuestionKind (+14 more)

### Community 52 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 54 - "collections_abc"
Cohesion: 0.13
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 56 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 57 - "verification_mail.py"
Cohesion: 0.08
Nodes (13): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+5 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (40): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look (+32 more)

### Community 60 - "apply_events"
Cohesion: 0.18
Nodes (8): next_step(), describe(), sign_in_cmd(), apply_events(), step(), send_sessions(), sign_in(), step()

### Community 62 - "guess_email"
Cohesion: 0.24
Nodes (4): Output, _clean(), guess_email(), test_guess_email()

### Community 63 - "_calendar_items"
Cohesion: 0.15
Nodes (7): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, calendar(), calendar_ics(), _calendar_items(), dashboard_css(), local_only()

### Community 70 - "OpportunityStore"
Cohesion: 0.25
Nodes (4): mark_cmd(), OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.06
Nodes (43): Big-company postings from the SimplifyJobs off-season list, Settings, append(), read_log(), is_workday(), open_postings(), refill(), LeadKind (+35 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 489 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `AnswerBank`, `notify.py`, `test_followups.py`, `applications/browser.py`, `test_chat.py`, `form_d.py`, `test_dashboard.py`, `internship_agent/ai.py`, `app.py`, `test_refill.py`, `agenda.py`, `run_followups`, `test_agenda.py`, `patterns.py`, `opportunities/schemas.py`, `_fill_form`, `Table`, `people.py`, `EmailStatus`, `pytest`, `LeadStore`, `preferences.py`, `test_patterns.py`, `leads/schemas.py`, `FormQuestion`, `leads/cli.py`, `test_post_submit_state_is_persisted_for_tracker`, `export.py`, `._fit_linkedin_note`, `workflows.py`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 100 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 100 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_sign_in.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12315270935960591 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `test_sign_in.py`, `AnswerBank`, `run.py`, `test_followups.py`, `test_chat.py`, `internship_agent/cli.py`, `re`, `test_opportunities.py`, `app.py`, `run_followups`, `test_agenda.py`, `typing`, `patterns.py`, `opportunities/schemas.py`, `test_apply_events.py`, `Table`, `client.py`, `preferences.py`, `test_patterns.py`, `FormQuestion`, `leads/cli.py`, `test_post_submit_state_is_persisted_for_tracker`, `apply_events`, `_calendar_items`, `.gmail_account`, `OpportunityStore`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Should `Lead` be split into smaller, more focused modules?**
  _Cohesion score 0.11375661375661375 - nodes in this community are weakly interconnected._