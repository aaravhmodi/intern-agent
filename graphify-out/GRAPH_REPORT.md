# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 92 files · ~108,533 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1341 nodes · 3996 edges · 68 communities (56 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 691 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7c68b8bf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_followups
- answers.py
- Region
- PreparedAnswer
- run.py
- app.py
- browser.py
- FakeToggle
- test_daily_campaign.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- startup_jobs.py
- make_workflows.py
- _use_gmail_for_applications
- test_opportunities.py
- get_settings
- tracking.py
- test_refill.py
- agenda.py
- Settings
- OutlookClient
- client.py
- find_startups
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- typing
- datetime
- test_application_browser.py
- leads/schemas.py
- candidate_context.md
- run-lowest-30-applications.sh
- test_agenda.py
- send_email
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Table
- README.md
- mailer.py
- outlook/schemas.py
- mailbox.py
- test_pg_store.py
- internship_agent/ai.py
- pytest
- startups.py
- followups.py
- json
- FormQuestion
- test_verification_mail.py
- FakeMailbox
- Lead
- leads/store.py
- opportunities/ai.py
- verification_mail.py
- leads/cli.py
- application_proof
- emails.py
- test_outlook_client.py
- re
- Opportunity
- config.py
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 136 edges
2. `Settings` - 85 edges
3. `get_settings()` - 65 edges
4. `Opportunity` - 51 edges
5. `LeadStatus` - 39 edges
6. `run_followups()` - 36 edges
7. `OpportunityStore` - 31 edges
8. `Region` - 30 edges
9. `LeadKind` - 29 edges
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

## Communities (68 total, 12 thin omitted)

### Community 0 - "run_followups"
Cohesion: 0.12
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 1 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 2 - "Region"
Cohesion: 0.11
Nodes (11): Region, nearby(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse() (+3 more)

### Community 3 - "PreparedAnswer"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 4 - "run.py"
Cohesion: 0.10
Nodes (19): list_cmd(), refresh_cmd(), _candidate(), check_events(), one(), checked(), find_events(), keep() (+11 more)

### Community 5 - "app.py"
Cohesion: 0.09
Nodes (22): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, AnswerEdit, calendar(), calendar_ics(), _calendar_items(), CheckRequest (+14 more)

### Community 6 - "browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "FakeToggle"
Cohesion: 0.10
Nodes (4): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator()

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "form_d.py"
Cohesion: 0.10
Nodes (19): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+11 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.19
Nodes (14): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "startup_jobs.py"
Cohesion: 0.14
Nodes (11): _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.20
Nodes (18): _assessment(), _fake_ai(), _opp(), _settings(), test_check_events_saves_results_and_survives_one_failure(), fake(), test_check_keeps_confirmed_travel_and_cleans_output(), test_check_marks_unconfirmed_travel_unknown() (+10 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (28): get_settings(), allow_retry(), check_opportunities(), daily_run(), delete_preference(), draft(), find_events(), find_more() (+20 more)

### Community 17 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 18 - "test_refill.py"
Cohesion: 0.16
Nodes (7): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.22
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "find_startups"
Cohesion: 0.20
Nodes (10): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups() (+2 more)

### Community 25 - "patterns.py"
Cohesion: 0.13
Nodes (11): Output, Output, guess_email(), bounced_addresses(), domain_of(), format_of(), next_guess(), outcomes() (+3 more)

### Community 26 - "x_search.py"
Cohesion: 0.12
Nodes (12): StartupFinding, StartupFindings, source_confirms(), post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+4 more)

### Community 27 - "typing"
Cohesion: 0.14
Nodes (4): check_cmd(), find_events_cmd(), import_cmd(), strategy_cmd()

### Community 29 - "test_application_browser.py"
Cohesion: 0.13
Nodes (18): _fill_form(), _numeric_answer(), FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+10 more)

### Community 30 - "leads/schemas.py"
Cohesion: 0.18
Nodes (8): fit_to_limit(), wants_email(), is_open(), rank(), LeadKind, LeadStatus, Verdict, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 34 - "send_email"
Cohesion: 0.22
Nodes (5): Send email safeguards, check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 35 - "EmailStatus"
Cohesion: 0.26
Nodes (7): EmailStatus, founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_published_address_is_used_as_is(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_the_usual_format_is_tried_most_until_it_bounces()

### Community 40 - "Table"
Cohesion: 0.13
Nodes (3): Table, _slug(), PostgresLeadStore

### Community 41 - "README.md"
Cohesion: 0.09
Nodes (30): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+22 more)

### Community 42 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 44 - "mailbox.py"
Cohesion: 0.21
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "test_pg_store.py"
Cohesion: 0.25
Nodes (3): posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 46 - "internship_agent/ai.py"
Cohesion: 0.05
Nodes (43): Internship agent coding instructions, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note() (+35 more)

### Community 47 - "pytest"
Cohesion: 0.19
Nodes (16): _email_line(), render_outreach(), fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input() (+8 more)

### Community 48 - "startups.py"
Cohesion: 0.13
Nodes (16): Round, Segment, parse_round(), mentions(), names(), to_leads(), finding(), lead() (+8 more)

### Community 49 - "followups.py"
Cohesion: 0.26
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), next_followup()

### Community 50 - "json"
Cohesion: 0.22
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 51 - "FormQuestion"
Cohesion: 0.19
Nodes (16): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 52 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 54 - "Lead"
Cohesion: 0.21
Nodes (4): Lead, LeadStore, test_auto_apply_prepares_then_submits(), test_store_round_trip_and_upsert()

### Community 55 - "leads/store.py"
Cohesion: 0.38
Nodes (4): _identity(), merge(), normalize_url(), test_merge_keeps_existing_and_dedupes_incoming()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.18
Nodes (9): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, SubmissionTrack, finding() (+1 more)

### Community 57 - "verification_mail.py"
Cohesion: 0.21
Nodes (4): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code()

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (36): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+28 more)

### Community 63 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 64 - "re"
Cohesion: 0.34
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 70 - "Opportunity"
Cohesion: 0.19
Nodes (7): mark_cmd(), import_inbox(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 72 - "config.py"
Cohesion: 0.20
Nodes (3): append(), read_log(), _log_xai()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.09
Nodes (24): Big-company postings from the SimplifyJobs off-season list, auto_apply(), is_workday(), open_postings(), refill(), fetch(), answer_bank(), daily() (+16 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 421 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `run_followups`, `answers.py`, `Region`, `PreparedAnswer`, `app.py`, `browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `get_settings`, `test_refill.py`, `agenda.py`, `Settings`, `find_startups`, `patterns.py`, `test_application_browser.py`, `leads/schemas.py`, `test_agenda.py`, `send_email`, `EmailStatus`, `Table`, `README.md`, `test_pg_store.py`, `internship_agent/ai.py`, `pytest`, `startups.py`, `followups.py`, `FormQuestion`, `leads/store.py`, `leads/cli.py`, `workflows.py`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Are the 97 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 97 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run_followups` be split into smaller, more focused modules?**
  _Cohesion score 0.12307692307692308 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `run_followups`, `answers.py`, `run.py`, `app.py`, `test_daily_campaign.py`, `form_d.py`, `internship_agent/cli.py`, `_use_gmail_for_applications`, `test_opportunities.py`, `get_settings`, `client.py`, `find_startups`, `patterns.py`, `typing`, `test_agenda.py`, `send_email`, `Table`, `README.md`, `internship_agent/ai.py`, `FormQuestion`, `leads/cli.py`, `Opportunity`, `config.py`, `workflows.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `append()`) actually correct?**
  _`Settings` has 71 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.10837438423645321 - nodes in this community are weakly interconnected._