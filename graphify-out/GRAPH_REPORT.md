# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 88 files · ~103,987 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1242 nodes · 3671 edges · 87 communities (63 shown, 24 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 627 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `166440de`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- score
- submit_application
- Region
- preferences.py
- run.py
- app.py
- browser.py
- FakeField
- leads/cli.py
- form_d.py
- test_dashboard.py
- internship_agent/cli.py
- startup_jobs.py
- make_workflows.py
- workflows.py
- test_opportunities.py
- get_settings
- tracking.py
- test_verification_mail.py
- command
- Settings
- OutlookClient
- client.py
- find_startups
- run-application-campaign-2026-10-16.sh
- Lead
- x_search.py
- datetime
- test_form_d.py
- test_application_browser.py
- AGENTS.md
- candidate_context.md
- run-lowest-30-applications.sh
- startups.py
- EmailStatus
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- README.md
- test_hidden_recaptcha_support_nodes_do_not_block
- outlook/schemas.py
- pathlib
- Winter 2027 Internship Agent
- internship_agent/ai.py
- mailbox.py
- test_outreach.py
- test_leads.py
- feeds.py
- json
- send_email
- followups_cmd
- run_followups
- leads/schemas.py
- opportunities/ai.py
- verification_mail.py
- find-founders.md
- SentMessage
- test_x_search.py
- typing
- guess_email
- test_outlook_client.py
- re
- export.py
- leads/store.py
- test_post_submit_outcomes_across_ats_pages
- find_events
- _confirmation_quote
- OpportunityStore
- test_notes.py
- db.py
- FakeToggle
- rank
- handle_note
- Table
- fit_to_limit
- post_text
- find-opportunities.md
- application_proof
- _field_label
- _numeric_answer
- _react_select_answer
- save_answers

## God Nodes (most connected - your core abstractions)
1. `Lead` - 122 edges
2. `Settings` - 79 edges
3. `get_settings()` - 61 edges
4. `Opportunity` - 37 edges
5. `run_followups()` - 36 edges
6. `LeadStatus` - 35 edges
7. `Region` - 30 edges
8. `prepare_application()` - 29 edges
9. `Segment` - 27 edges
10. `FormQuestion` - 27 edges

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

## Communities (87 total, 24 thin omitted)

### Community 0 - "score"
Cohesion: 0.33
Nodes (3): merge(), find_form_d_startups(), score()

### Community 1 - "submit_application"
Cohesion: 0.29
Nodes (4): submit(), SubmitApplicationRequest, _incompatible_term(), submit_application()

### Community 2 - "Region"
Cohesion: 0.06
Nodes (25): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Region, normalize_url(), region_from_text(), regions_of() (+17 more)

### Community 3 - "preferences.py"
Cohesion: 0.24
Nodes (10): apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules() (+2 more)

### Community 4 - "run.py"
Cohesion: 0.14
Nodes (10): collect_confs_tech(), confs_tech(), import_inbox(), keep(), nearby(), next_date(), refresh(), summary_push() (+2 more)

### Community 5 - "app.py"
Cohesion: 0.13
Nodes (16): AnswerEdit, delete_preference(), find_events(), FindMoreRequest, followups(), FollowupsRequest, _opportunity(), opportunity_status() (+8 more)

### Community 6 - "browser.py"
Cohesion: 0.14
Nodes (15): apply_to_posting(), _confirmed(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome(), _posting_is_closed(), _save_screenshot() (+7 more)

### Community 7 - "FakeField"
Cohesion: 0.15
Nodes (3): FakeField, FakeLocator, locator()

### Community 8 - "leads/cli.py"
Cohesion: 0.24
Nodes (10): _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), prepare_all_cmd(), _resume(), show_lead() (+2 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (18): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+10 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.14
Nodes (15): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html() (+7 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "startup_jobs.py"
Cohesion: 0.23
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "workflows.py"
Cohesion: 0.05
Nodes (48): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), ApplicationPrep (+40 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.15
Nodes (12): EventFinding, _opp(), _settings(), test_dashboard_lists_and_marks_opportunities(), test_devpost_dates(), test_find_events_keeps_only_dated_events_whose_page_names_them(), finding(), test_keep_drops_past_and_far_away_events() (+4 more)

### Community 16 - "get_settings"
Cohesion: 0.19
Nodes (20): get_settings(), allow_retry(), auto_apply(), daily_run(), draft(), find_more(), _get(), KeyRequest (+12 more)

### Community 17 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 18 - "test_verification_mail.py"
Cohesion: 0.17
Nodes (4): message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 19 - "command"
Cohesion: 0.18
Nodes (5): browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd()

### Community 20 - "Settings"
Cohesion: 0.20
Nodes (18): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+10 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.22
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "find_startups"
Cohesion: 0.19
Nodes (8): More people to connect with, chosen by company size, search_people(), Person, to_people(), find_people(), find_startups(), people_at(), startup_postings()

### Community 25 - "Lead"
Cohesion: 0.17
Nodes (6): Lead, _slug(), _identity(), LeadStore, test_post_submit_state_is_persisted_for_tracker(), test_store_round_trip_and_upsert()

### Community 26 - "x_search.py"
Cohesion: 0.21
Nodes (5): search_startups(), StartupFinding, StartupFindings, search_x_raises(), _tool_usage()

### Community 27 - "datetime"
Cohesion: 0.24
Nodes (3): list_cmd(), OpportunityKind, OpportunityStatus

### Community 29 - "test_application_browser.py"
Cohesion: 0.20
Nodes (17): _answer_for(), _fill_form(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+9 more)

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "startups.py"
Cohesion: 0.18
Nodes (6): _on_linkedin(), source_names(), mentions(), names(), page_names(), source_confirms()

### Community 34 - "EmailStatus"
Cohesion: 0.31
Nodes (5): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (12): FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new(), test_incompatible_eight_month_term_is_rejected() (+4 more)

### Community 41 - "README.md"
Cohesion: 0.13
Nodes (23): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+15 more)

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 45 - "Winter 2027 Internship Agent"
Cohesion: 0.12
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP) (+4 more)

### Community 46 - "internship_agent/ai.py"
Cohesion: 0.19
Nodes (14): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+6 more)

### Community 47 - "mailbox.py"
Cohesion: 0.16
Nodes (5): GmailMailbox, _imap_date(), Mailbox, MailboxError, _quoted()

### Community 48 - "test_outreach.py"
Cohesion: 0.16
Nodes (11): OutreachDraft, parse_round(), to_leads(), finding(), lead(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round() (+3 more)

### Community 49 - "test_leads.py"
Cohesion: 0.25
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 50 - "feeds.py"
Cohesion: 0.20
Nodes (10): ccfddl(), collect_ccfddl(), collect_devpost(), collect_mlh(), _day(), devpost(), devpost_dates(), get() (+2 more)

### Community 51 - "json"
Cohesion: 0.38
Nodes (5): ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request()

### Community 52 - "send_email"
Cohesion: 0.18
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 53 - "followups_cmd"
Cohesion: 0.23
Nodes (5): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd()

### Community 54 - "run_followups"
Cohesion: 0.14
Nodes (13): FollowupReport, FollowupSent, _misaddressed(), _name(), run_followups(), _site(), company_domain(), first_name() (+5 more)

### Community 55 - "leads/schemas.py"
Cohesion: 0.29
Nodes (6): LeadKind, Round, Segment, Verdict, effective_segment(), test_effective_segment()

### Community 56 - "opportunities/ai.py"
Cohesion: 0.17
Nodes (6): EventFindings, search_events(), write_strategy(), without_citations(), SubmissionStrategy, SubmissionTrack

### Community 57 - "verification_mail.py"
Cohesion: 0.22
Nodes (4): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code()

### Community 58 - "find-founders.md"
Cohesion: 0.13
Nodes (11): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+3 more)

### Community 60 - "test_x_search.py"
Cohesion: 0.32
Nodes (4): post_confirms(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 61 - "typing"
Cohesion: 0.16
Nodes (11): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched() (+3 more)

### Community 62 - "guess_email"
Cohesion: 0.22
Nodes (5): Output, Output, _clean(), guess_email(), test_guess_email()

### Community 63 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 64 - "re"
Cohesion: 0.38
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 65 - "export.py"
Cohesion: 0.50
Nodes (3): _email_line(), render_outreach(), test_render_outreach_flags_unverified_emails_and_skips_undrafted()

### Community 66 - "leads/store.py"
Cohesion: 0.16
Nodes (6): load_inbox(), open_lead_store(), PostgresLeadStore, posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 68 - "find_events"
Cohesion: 0.17
Nodes (6): find_events_cmd(), import_cmd(), refresh_cmd(), strategy_cmd(), find_events(), _openai()

### Community 70 - "OpportunityStore"
Cohesion: 0.36
Nodes (4): mark_cmd(), plan_submission(), OpportunityStore, test_add_new_dedupes_and_never_overwrites_status()

### Community 71 - "test_notes.py"
Cohesion: 0.27
Nodes (7): PreferenceDraft, posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns(), test_html_to_text_drops_scripts_and_tags()

### Community 72 - "db.py"
Cohesion: 0.22
Nodes (4): append(), read_log(), _logged_subject(), _log_xai()

### Community 75 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 76 - "handle_note"
Cohesion: 0.33
Nodes (4): note(), NoteRequest, handle_note(), preference_store()

### Community 79 - "post_text"
Cohesion: 0.40
Nodes (3): post_id(), post_text(), test_only_a_link_to_a_post_has_a_post_id()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 392 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `score`, `submit_application`, `Region`, `preferences.py`, `app.py`, `browser.py`, `leads/cli.py`, `form_d.py`, `test_dashboard.py`, `workflows.py`, `get_settings`, `Settings`, `find_startups`, `test_application_browser.py`, `startups.py`, `EmailStatus`, `test_daily_campaign.py`, `README.md`, `internship_agent/ai.py`, `test_outreach.py`, `test_leads.py`, `send_email`, `run_followups`, `leads/schemas.py`, `find-founders.md`, `export.py`, `leads/store.py`, `test_notes.py`, `._connect`, `rank`, `save_answers`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 85 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 85 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.0632996632996633 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `score`, `submit_application`, `Region`, `preferences.py`, `run.py`, `leads/cli.py`, `internship_agent/cli.py`, `workflows.py`, `test_opportunities.py`, `get_settings`, `client.py`, `find_startups`, `Lead`, `datetime`, `test_daily_campaign.py`, `README.md`, `Winter 2027 Internship Agent`, `send_email`, `run_followups`, `typing`, `find_events`, `OpportunityStore`, `test_notes.py`, `db.py`, `handle_note`, `Table`, `save_answers`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `append()`) actually correct?**
  _`Settings` has 65 INFERRED edges - model-reasoned connections that need verification._
- **Should `run.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._