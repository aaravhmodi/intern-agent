# Graph Report - winter-2027-internship-agent  (2026-10-19)

## Corpus Check
- 79 files · ~196,416 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1101 nodes · 3188 edges · 70 communities (55 shown, 15 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 547 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aa95f433`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- store.py
- daily
- Region
- test_notes.py
- workflows.py
- app.py
- browser.py
- FakeField
- leads/cli.py
- re
- test_dashboard.py
- internship_agent/cli.py
- pydantic
- make_workflows.py
- notify.py
- answers.py
- get_settings
- tracking.py
- mailer.py
- command
- Settings
- OutlookClient
- client.py
- find_startups
- run-application-campaign-2026-10-16.sh
- Lead
- x_search.py
- run_followups
- datetime
- test_application_browser.py
- AGENTS.md
- candidate_context.md
- run-lowest-30-applications.sh
- startups.py
- leads/schemas.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- README.md
- test_hidden_recaptcha_support_nodes_do_not_block
- outlook/schemas.py
- test_answers.py
- local_only
- ai.py
- mailbox.py
- test_outreach.py
- test_leads.py
- Bot Auto application preview
- json
- send_email
- export_drafts
- followups.py
- LeadKind
- Segment
- LeadStore
- find-founders.md
- FakeMailbox
- typing
- test_ai.py
- find-internships.md
- test_outlook_client.py
- _TableParser
- EmailStatus
- test_pg_store.py
- _post_submit_outcome
- open_lead_store
- _confirmation_quote

## God Nodes (most connected - your core abstractions)
1. `Lead` - 122 edges
2. `Settings` - 63 edges
3. `get_settings()` - 48 edges
4. `run_followups()` - 36 edges
5. `LeadStatus` - 35 edges
6. `prepare_application()` - 29 edges
7. `Segment` - 27 edges
8. `Region` - 27 edges
9. `FormQuestion` - 27 edges
10. `find_startups()` - 27 edges

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

## Communities (70 total, 15 thin omitted)

### Community 0 - "store.py"
Cohesion: 0.12
Nodes (13): Big-company postings from the SimplifyJobs off-season list, refill(), _identity(), merge(), normalize_url(), test_merge_keeps_existing_and_dedupes_incoming(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 1 - "daily"
Cohesion: 0.20
Nodes (6): daily_cmd(), open_postings(), daily(), _incompatible_term(), refresh_saved_application(), submit_application()

### Community 2 - "Region"
Cohesion: 0.15
Nodes (11): Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+3 more)

### Community 3 - "test_notes.py"
Cohesion: 0.15
Nodes (15): apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, NoteOutcome, posting(), settings() (+7 more)

### Community 4 - "workflows.py"
Cohesion: 0.17
Nodes (9): common_questions(), PreparedAnswer, answer_bank(), prepare_application(), _record_openai_usage(), _retryable_block(), _run_ai_cost(), _use_gmail_for_applications() (+1 more)

### Community 5 - "app.py"
Cohesion: 0.14
Nodes (14): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, note(), NoteRequest, PreferenceDelete (+6 more)

### Community 6 - "browser.py"
Cohesion: 0.10
Nodes (22): _answer_for(), apply_to_posting(), _confirmed(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks() (+14 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 8 - "leads/cli.py"
Cohesion: 0.20
Nodes (9): _draft(), draft_all(), draft_lead(), _openai(), _resume(), is_open(), rank(), LeadStatus (+1 more)

### Community 9 - "re"
Cohesion: 0.05
Nodes (37): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _clean(), guess_email(), fit_to_limit(), _slug() (+29 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.16
Nodes (13): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "pydantic"
Cohesion: 0.21
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "notify.py"
Cohesion: 0.20
Nodes (13): category(), _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer(), lead() (+5 more)

### Community 15 - "answers.py"
Cohesion: 0.16
Nodes (6): AnswerBank, match_option(), normalize(), prefill(), validate(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 16 - "get_settings"
Cohesion: 0.19
Nodes (19): get_settings(), allow_retry(), application_proof(), auto_apply(), daily_run(), delete_preference(), draft(), find_more() (+11 more)

### Community 17 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 18 - "mailer.py"
Cohesion: 0.09
Nodes (8): build_message(), send(), test_build_message_requires_fields(), test_build_message_with_attachment(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 19 - "command"
Cohesion: 0.14
Nodes (9): browser_login(), _email_cell(), list_leads(), mark_lead(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd(), show_lead() (+1 more)

### Community 20 - "Settings"
Cohesion: 0.20
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.22
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "find_startups"
Cohesion: 0.10
Nodes (17): More people to connect with, chosen by company size, find_more(), find_startups_cmd(), Person, effective_segment(), to_people(), find_more_postings(), find_people() (+9 more)

### Community 25 - "Lead"
Cohesion: 0.12
Nodes (5): Lead, PostgresLeadStore, DailyReport, test_post_submit_state_is_persisted_for_tracker(), test_saving_answers_preserves_uncertain_submission()

### Community 26 - "x_search.py"
Cohesion: 0.18
Nodes (6): search_startups(), StartupFinding, StartupFindings, post_confirms(), search_x_raises(), _tool_usage()

### Community 27 - "run_followups"
Cohesion: 0.11
Nodes (8): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), Mailbox

### Community 29 - "test_application_browser.py"
Cohesion: 0.24
Nodes (14): FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+6 more)

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "startups.py"
Cohesion: 0.21
Nodes (5): _on_linkedin(), source_names(), names(), page_names(), source_confirms()

### Community 34 - "leads/schemas.py"
Cohesion: 0.17
Nodes (7): Note, OutreachDraft, OutreachDraftResult, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.13
Nodes (12): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+4 more)

### Community 41 - "README.md"
Cohesion: 0.10
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+21 more)

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 44 - "test_answers.py"
Cohesion: 0.24
Nodes (6): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind(), test_yes_no_answer_matches_long_select_options()

### Community 45 - "local_only"
Cohesion: 0.29
Nodes (3): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, local_only()

### Community 46 - "ai.py"
Cohesion: 0.18
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 47 - "mailbox.py"
Cohesion: 0.19
Nodes (5): followups_cmd(), GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 48 - "test_outreach.py"
Cohesion: 0.21
Nodes (9): mentions(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_to_leads_filters_age_stage_and_unverifiable_sources() (+1 more)

### Community 49 - "test_leads.py"
Cohesion: 0.22
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+6 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 51 - "json"
Cohesion: 0.25
Nodes (11): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _log_xai() (+3 more)

### Community 52 - "send_email"
Cohesion: 0.28
Nodes (4): send(), SendRequest, MailError, send_email()

### Community 53 - "export_drafts"
Cohesion: 0.19
Nodes (6): application_campaign(), apply_cmd(), export_drafts(), form_d_cmd(), Push, send()

### Community 54 - "followups.py"
Cohesion: 0.20
Nodes (7): company_domain(), first_name(), followup_body(), is_due(), last_contact(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 55 - "LeadKind"
Cohesion: 0.19
Nodes (7): LeadKind, Round, Verdict, parse_round(), startup_postings(), test_parse_round(), test_regions_of()

### Community 56 - "Segment"
Cohesion: 0.26
Nodes (7): search_people(), Segment, person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 57 - "LeadStore"
Cohesion: 0.35
Nodes (4): LeadStore, test_auto_apply_prepares_then_submits(), test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 58 - "find-founders.md"
Cohesion: 0.24
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), score_leads()

### Community 60 - "typing"
Cohesion: 0.24
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 61 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 62 - "find-internships.md"
Cohesion: 0.22
Nodes (5): Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look

### Community 63 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 65 - "EmailStatus"
Cohesion: 0.53
Nodes (4): _email_line(), render_outreach(), EmailStatus, test_render_outreach_flags_unverified_emails_and_skips_undrafted()

### Community 67 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 348 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `store.py`, `daily`, `Region`, `test_notes.py`, `workflows.py`, `app.py`, `browser.py`, `leads/cli.py`, `re`, `test_dashboard.py`, `notify.py`, `answers.py`, `get_settings`, `command`, `Settings`, `find_startups`, `run_followups`, `test_application_browser.py`, `startups.py`, `leads/schemas.py`, `test_daily_campaign.py`, `test_answers.py`, `ai.py`, `test_outreach.py`, `test_leads.py`, `send_email`, `followups.py`, `LeadKind`, `Segment`, `LeadStore`, `find-founders.md`, `find-internships.md`, `EmailStatus`, `test_pg_store.py`, `open_lead_store`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Are the 85 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 85 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `store.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `daily`, `Region`, `test_notes.py`, `workflows.py`, `app.py`, `leads/cli.py`, `re`, `internship_agent/cli.py`, `answers.py`, `get_settings`, `command`, `client.py`, `find_startups`, `Lead`, `run_followups`, `test_daily_campaign.py`, `test_answers.py`, `local_only`, `json`, `send_email`, `Segment`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14855072463768115 - nodes in this community are weakly interconnected._