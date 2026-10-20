# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 90 files · ~106,583 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1301 nodes · 3882 edges · 70 communities (56 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 674 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `319f9c34`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_followups
- answers.py
- Region
- test_notes.py
- run.py
- app.py
- browser.py
- FakeField
- notify.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- startup_jobs.py
- make_workflows.py
- _use_gmail_for_applications
- test_opportunities.py
- get_settings
- tracking.py
- leads/store.py
- Any
- Settings
- OutlookClient
- client.py
- workflows.py
- run-application-campaign-2026-10-16.sh
- Lead
- typing
- opportunities/cli.py
- test_form_d.py
- test_application_browser.py
- leads/schemas.py
- candidate_context.md
- run-lowest-30-applications.sh
- startups.py
- test_interview_events
- test_patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Table
- README.md
- check_events
- outlook/schemas.py
- mailbox.py
- local_only
- internship_agent/ai.py
- test_leads.py
- Segment
- followups.py
- json
- FormQuestion
- send_email
- FakeMailbox
- LeadStore
- _TableParser
- opportunities/ai.py
- verification_mail.py
- leads/cli.py
- rescore_open
- test_devpost_dates
- test_people.py
- guess_email
- test_outlook_client.py
- re
- import_inbox
- Opportunity
- config.py
- find-opportunities.md
- submit_application

## God Nodes (most connected - your core abstractions)
1. `Lead` - 131 edges
2. `Settings` - 84 edges
3. `get_settings()` - 64 edges
4. `Opportunity` - 45 edges
5. `LeadStatus` - 38 edges
6. `run_followups()` - 36 edges
7. `Region` - 30 edges
8. `LeadKind` - 29 edges
9. `OpportunityStore` - 29 edges
10. `prepare_application()` - 29 edges

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

## Communities (70 total, 14 thin omitted)

### Community 0 - "run_followups"
Cohesion: 0.12
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 1 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 2 - "Region"
Cohesion: 0.14
Nodes (13): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+5 more)

### Community 3 - "test_notes.py"
Cohesion: 0.18
Nodes (13): NoteResult, PreferenceDraft, _normalize(), PreferenceStore, posting(), settings(), test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules() (+5 more)

### Community 4 - "run.py"
Cohesion: 0.13
Nodes (10): list_cmd(), _candidate(), keep(), nearby(), next_date(), refresh(), summary_push(), upcoming() (+2 more)

### Community 5 - "app.py"
Cohesion: 0.13
Nodes (19): AnswerEdit, CheckRequest, delete_preference(), find_more_startups(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest (+11 more)

### Community 6 - "browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "FakeField"
Cohesion: 0.07
Nodes (7): FakeField, FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 8 - "notify.py"
Cohesion: 0.07
Nodes (29): category(), ApplicationPrep, FitAssessment, _clip(), _fit_bytes(), posting_push(), Push, send() (+21 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (19): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+11 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.15
Nodes (14): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.23
Nodes (17): _assessment(), _fake_ai(), _opp(), _settings(), test_check_events_saves_results_and_survives_one_failure(), fake(), test_check_keeps_confirmed_travel_and_cleans_output(), test_check_marks_unconfirmed_travel_unknown() (+9 more)

### Community 16 - "get_settings"
Cohesion: 0.20
Nodes (15): get_settings(), allow_retry(), application_proof(), auto_apply(), daily_run(), draft(), find_more(), _get() (+7 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "leads/store.py"
Cohesion: 0.13
Nodes (13): is_workday(), open_postings(), refill(), _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 19 - "Any"
Cohesion: 0.27
Nodes (8): check_opportunities(), find_events(), opportunities(), _opportunity(), opportunity_status(), opportunity_strategy(), _opportunity_view(), refresh_opportunities()

### Community 20 - "Settings"
Cohesion: 0.20
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.20
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "workflows.py"
Cohesion: 0.11
Nodes (15): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, check_outreach_text(), to_people(), find_people(), find_startups() (+7 more)

### Community 25 - "Lead"
Cohesion: 0.11
Nodes (12): _email_line(), render_outreach(), bounced_addresses(), domain_of(), format_of(), next_guess(), outcomes(), point_at() (+4 more)

### Community 26 - "typing"
Cohesion: 0.13
Nodes (11): StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 27 - "opportunities/cli.py"
Cohesion: 0.18
Nodes (5): OpportunityKind, OpportunityStatus, posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 29 - "test_application_browser.py"
Cohesion: 0.21
Nodes (16): _fill_form(), _numeric_answer(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+8 more)

### Community 30 - "leads/schemas.py"
Cohesion: 0.24
Nodes (7): apply_violations(), LeadKind, LeadStatus, Note, PreferenceEffect, Round, Verdict

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "startups.py"
Cohesion: 0.16
Nodes (5): _on_linkedin(), source_names(), mentions(), names(), source_confirms()

### Community 35 - "test_patterns.py"
Cohesion: 0.27
Nodes (6): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_published_address_is_used_as_is(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_the_usual_format_is_tried_most_until_it_bounces()

### Community 40 - "Table"
Cohesion: 0.12
Nodes (3): Table, PostgresLeadStore, test_post_submit_state_is_persisted_for_tracker()

### Community 41 - "README.md"
Cohesion: 0.10
Nodes (30): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+22 more)

### Community 42 - "check_events"
Cohesion: 0.11
Nodes (11): check_cmd(), find_events_cmd(), refresh_cmd(), strategy_cmd(), check_events(), one(), checked(), find_events() (+3 more)

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 44 - "mailbox.py"
Cohesion: 0.21
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, dashboard_css(), local_only()

### Community 46 - "internship_agent/ai.py"
Cohesion: 0.13
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 47 - "test_leads.py"
Cohesion: 0.25
Nodes (15): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+7 more)

### Community 48 - "Segment"
Cohesion: 0.16
Nodes (13): Segment, effective_segment(), parse_round(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+5 more)

### Community 49 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 50 - "json"
Cohesion: 0.20
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 51 - "FormQuestion"
Cohesion: 0.19
Nodes (16): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 52 - "send_email"
Cohesion: 0.06
Nodes (15): Internship agent coding instructions, Send email safeguards, check_send(), SendBlocked, build_message(), MailError, send(), send_email() (+7 more)

### Community 54 - "LeadStore"
Cohesion: 0.47
Nodes (3): LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.16
Nodes (10): assess(), EventFinding, EventFindings, search_events(), write_strategy(), OpportunityAssessment, SubmissionStrategy, SubmissionTrack (+2 more)

### Community 57 - "verification_mail.py"
Cohesion: 0.21
Nodes (4): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code()

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (41): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look (+33 more)

### Community 61 - "test_people.py"
Cohesion: 0.19
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 62 - "guess_email"
Cohesion: 0.24
Nodes (4): Output, _clean(), guess_email(), test_guess_email()

### Community 63 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 64 - "re"
Cohesion: 0.20
Nodes (12): fit_to_limit(), _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json() (+4 more)

### Community 70 - "Opportunity"
Cohesion: 0.26
Nodes (6): mark_cmd(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 72 - "config.py"
Cohesion: 0.13
Nodes (4): append(), read_log(), _record_openai_usage(), _run_ai_cost()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "submit_application"
Cohesion: 0.17
Nodes (7): submit(), SubmitApplicationRequest, answer_bank(), _incompatible_term(), refresh_saved_application(), save_answers(), submit_application()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 407 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `run_followups`, `answers.py`, `Region`, `test_notes.py`, `app.py`, `browser.py`, `notify.py`, `form_d.py`, `test_dashboard.py`, `get_settings`, `leads/store.py`, `Settings`, `workflows.py`, `opportunities/cli.py`, `test_application_browser.py`, `leads/schemas.py`, `startups.py`, `test_patterns.py`, `Table`, `internship_agent/ai.py`, `test_leads.py`, `Segment`, `followups.py`, `FormQuestion`, `send_email`, `LeadStore`, `leads/cli.py`, `rescore_open`, `submit_application`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Are the 93 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 93 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run_followups` be split into smaller, more focused modules?**
  _Cohesion score 0.12307692307692308 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `run_followups`, `answers.py`, `Region`, `test_notes.py`, `run.py`, `app.py`, `notify.py`, `form_d.py`, `internship_agent/cli.py`, `_use_gmail_for_applications`, `test_opportunities.py`, `get_settings`, `client.py`, `workflows.py`, `Lead`, `opportunities/cli.py`, `Table`, `check_events`, `local_only`, `FormQuestion`, `send_email`, `leads/cli.py`, `rescore_open`, `test_people.py`, `import_inbox`, `Opportunity`, `config.py`, `submit_application`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `append()`) actually correct?**
  _`Settings` has 70 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._