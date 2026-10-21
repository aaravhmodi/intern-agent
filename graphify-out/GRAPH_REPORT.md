# Graph Report - opportunity-agent  (2026-10-21)

## Corpus Check
- 114 files · ~232,532 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 20 file(s) not represented in the graph (top: (none) 5, .service 5, .timer 5)

## Summary
- 1763 nodes · 5263 edges · 100 communities (76 shown, 24 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 883 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0f1a4843`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_pipeline.py
- Region
- notify.py
- Opportunity
- run_followups
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
- tracking.py
- app.py
- verification_mail.py
- Lead
- FormQuestion
- opportunities/ai.py
- OutlookClient
- run-application-campaign-2026-10-16.sh
- leads/cli.py
- x_search.py
- apply_events
- test_apply_events.py
- feeds.py
- find_site_emails
- run
- run-lowest-30-applications.sh
- find_startups
- leads/schemas.py
- patterns.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Settings
- README.md
- agenda.py
- test_chat.py
- mailbox.py
- typing
- Table
- workflows.py
- client.py
- EmailStatus
- job_pipeline
- test_people.py
- pytest
- Mailbox
- opportunities/browser.py
- set_status
- startup_jobs.py
- pipeline.py
- command
- test_auto_pick.py
- StepAction
- _get
- find_deadline
- followup_run.py
- local_only
- find-founders.md
- re
- batches
- check_events
- send
- run.py
- FakeField
- insights
- mailer.py
- candidate_context.md
- page_url
- followups.py
- config.py
- run-inbox-check.sh
- find-opportunities.md
- lead_store
- export.py
- _scan_inboxes
- open_login_browser
- test_the_scheduled_call_only_sends_when_follow_ups_are_switched_on
- LeadStatus
- outlook
- test_hidden_recaptcha_support_nodes_do_not_block
- Bot Auto application preview
- ToolSession
- emails.py
- rank
- run-email-batch.sh
- note
- daily_cmd
- test_interview_events
- find_more
- prepare_cmd
- scrape_jobs_cmd

## God Nodes (most connected - your core abstractions)
1. `Lead` - 161 edges
2. `Settings` - 120 edges
3. `get_settings()` - 80 edges
4. `Opportunity` - 73 edges
5. `LeadStatus` - 51 edges
6. `OpportunityStore` - 43 edges
7. `run_followups()` - 36 edges
8. `LeadKind` - 34 edges
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

## Communities (100 total, 24 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.14
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_pipeline.py"
Cohesion: 0.12
Nodes (17): _event(), FakeBox, lead(), mail(), _settings(), test_board_columns_follow_the_latest_email(), test_classifies_and_matches_pipeline_mail(), test_dashboard_shows_the_board() (+9 more)

### Community 2 - "Region"
Cohesion: 0.11
Nodes (11): Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+3 more)

### Community 3 - "notify.py"
Cohesion: 0.24
Nodes (12): _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer(), lead(), test_campaign_summary_reports_actual_result_and_shortfall() (+4 more)

### Community 4 - "Opportunity"
Cohesion: 0.22
Nodes (6): mark_cmd(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 5 - "run_followups"
Cohesion: 0.32
Nodes (17): run_followups(), emailed(), FakeMailbox, save(), settings(), test_a_bounced_address_gets_nothing(), test_a_check_only_run_records_replies_and_bounces_but_sends_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (21): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), _post_submit_outcome(), _posting_is_closed() (+13 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.19
Nodes (19): _answer_for(), _fill_form(), _numeric_answer(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+11 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 9 - "form_d.py"
Cohesion: 0.09
Nodes (20): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+12 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.20
Nodes (15): client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_favicon_is_served_for_every_path_browsers_ask_for(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_health_says_busy_while_a_long_job_runs(), test_index_serves_html() (+7 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+3 more)

### Community 12 - "json"
Cohesion: 0.18
Nodes (11): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.12
Nodes (17): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+9 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (22): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), auto_apply(), check_opportunities(), daily_run(), event_proof() (+14 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "app.py"
Cohesion: 0.10
Nodes (23): AnswerEdit, ask(), browser_sessions(), ChatRequest, CheckRequest, Cookie, delete_preference(), FindMoreRequest (+15 more)

### Community 19 - "verification_mail.py"
Cohesion: 0.09
Nodes (13): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+5 more)

### Community 20 - "Lead"
Cohesion: 0.17
Nodes (6): Lead, _identity(), LeadStore, normalize_url(), test_auto_apply_prepares_then_submits(), test_store_round_trip_and_upsert()

### Community 21 - "FormQuestion"
Cohesion: 0.10
Nodes (24): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+16 more)

### Community 22 - "opportunities/ai.py"
Cohesion: 0.23
Nodes (8): assess(), EventFinding, EventFindings, search_events(), write_strategy(), SubmissionStrategy, finding(), test_without_citations_strips_inline_links_only()

### Community 23 - "OutlookClient"
Cohesion: 0.20
Nodes (7): OutlookClient, OutlookError, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 25 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (9): post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 27 - "apply_events"
Cohesion: 0.14
Nodes (11): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _openai(), send_sessions(), sign_in() (+3 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "feeds.py"
Cohesion: 0.20
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 30 - "find_site_emails"
Cohesion: 0.29
Nodes (3): site_emails_cmd(), generic(), find_site_emails()

### Community 31 - "run"
Cohesion: 0.14
Nodes (10): allowed(), _host(), names_event(), nothing_to_sign_in(), _quote(), _refusal(), resolve(), run() (+2 more)

### Community 33 - "find_startups"
Cohesion: 0.11
Nodes (15): More people to connect with, chosen by company size, Search for recently funded startups (last 60 days; Canada, USA, Europe), PersonFinding, search_people(), Person, effective_segment(), _on_linkedin(), source_names() (+7 more)

### Community 34 - "leads/schemas.py"
Cohesion: 0.11
Nodes (18): StartupFinding, LeadKind, Round, Segment, Verdict, parse_round(), mentions(), names() (+10 more)

### Community 35 - "patterns.py"
Cohesion: 0.06
Nodes (29): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+21 more)

### Community 40 - "Settings"
Cohesion: 0.14
Nodes (8): Settings, append(), read_log(), inboxes(), inbox_send(), _run_ai_cost(), send_email(), sent_note()

### Community 41 - "README.md"
Cohesion: 0.11
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Big-company postings from the SimplifyJobs off-season list (+21 more)

### Community 42 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 43 - "test_chat.py"
Cohesion: 0.11
Nodes (18): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+10 more)

### Community 44 - "mailbox.py"
Cohesion: 0.17
Nodes (8): bounce_search(), GmailMailbox, _imap_date(), MailboxError, _quoted(), reply_search(), test_a_bounce_notice_from_the_company_is_not_a_reply(), test_bounces_from_gmail_and_from_microsoft_365_both_count()

### Community 45 - "typing"
Cohesion: 0.15
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 47 - "workflows.py"
Cohesion: 0.14
Nodes (13): expire_postings(), is_workday(), open_postings(), refill(), Note, merge(), add_team_contacts(), handle_note() (+5 more)

### Community 48 - "client.py"
Cohesion: 0.25
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 49 - "EmailStatus"
Cohesion: 0.15
Nodes (7): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 50 - "job_pipeline"
Cohesion: 0.19
Nodes (8): job_pipeline(), board(), _card(), display_company(), events(), InboxEvent, push_for(), scan()

### Community 51 - "test_people.py"
Cohesion: 0.19
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 52 - "pytest"
Cohesion: 0.25
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 54 - "opportunities/browser.py"
Cohesion: 0.14
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 55 - "set_status"
Cohesion: 0.40
Nodes (4): draft(), set_status(), StatusUpdate, Lead detail panel: fit, links, contact, actions

### Community 56 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 57 - "pipeline.py"
Cohesion: 0.19
Nodes (10): _bounced_lead(), classify(), _header(), _host(), _is_ats(), match(), sync(), to_event() (+2 more)

### Community 58 - "command"
Cohesion: 0.15
Nodes (11): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd(), guess_send_cmd(), inbox_send_cmd(), team_contacts_cmd() (+3 more)

### Community 59 - "test_auto_pick.py"
Cohesion: 0.23
Nodes (9): OpportunityAssessment, check(), hack(), reason(), test_auto_pick_marks_interested_and_says_why(), test_checks_saved_before_these_fields_are_never_picked(), test_only_realistic_reachable_sponsored_hackathons(), test_picks_sponsored_online_hackathons_with_recognition() (+1 more)

### Community 61 - "_get"
Cohesion: 0.15
Nodes (9): application_proof(), calendar(), calendar_ics(), _calendar_items(), dashboard_css(), _get(), health(), _icon() (+1 more)

### Community 62 - "find_deadline"
Cohesion: 0.24
Nodes (5): find_deadline(), posting(), test_expire_postings_skips_only_open_postings_past_deadline(), test_finds_a_stated_deadline(), test_ignores_text_without_a_full_dated_deadline()

### Community 63 - "followup_run.py"
Cohesion: 0.12
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), _site(), company_domain(), reply_subject() (+2 more)

### Community 64 - "local_only"
Cohesion: 0.33
Nodes (3): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, local_only()

### Community 65 - "find-founders.md"
Cohesion: 0.10
Nodes (14): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+6 more)

### Community 66 - "re"
Cohesion: 0.22
Nodes (11): fit_to_limit(), _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json() (+3 more)

### Community 67 - "batches"
Cohesion: 0.40
Nodes (3): batches(), lead(), test_each_run_of_sends_is_a_batch_with_its_bounces_and_replies()

### Community 68 - "check_events"
Cohesion: 0.12
Nodes (7): _candidate(), check_events(), one(), checked(), _keys(), without_citations(), load_resume_text()

### Community 69 - "send"
Cohesion: 0.17
Nodes (3): Internship agent coding instructions, send(), SendRequest

### Community 70 - "run.py"
Cohesion: 0.11
Nodes (17): list_cmd(), refresh_cmd(), auto_pick(), find_events(), import_inbox(), keep(), nearby(), next_date() (+9 more)

### Community 71 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 72 - "insights"
Cohesion: 0.33
Nodes (5): insights(), got(), split(), _pct(), _takeaways()

### Community 73 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 74 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 75 - "page_url"
Cohesion: 0.13
Nodes (9): page_url(), applied_push(), hack(), test_event_application_push_opens_the_event_or_the_plans_list(), tried(), test_every_linked_view_exists_in_the_dashboard(), test_job_pipeline_push_opens_the_company_or_the_board(), test_opportunity_push_opens_what_it_is_mostly_about() (+1 more)

### Community 76 - "followups.py"
Cohesion: 0.21
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), next_followup(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 77 - "config.py"
Cohesion: 0.13
Nodes (6): apply_cmd(), check_cmd(), find_events_cmd(), import_cmd(), strategy_cmd(), SubmissionTrack

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 81 - "lead_store"
Cohesion: 0.11
Nodes (16): answer_bank(), daily(), DailyReport, find_form_d_startups(), find_more_postings(), lead_store(), prepare_application(), _record_openai_usage() (+8 more)

### Community 82 - "export.py"
Cohesion: 0.50
Nodes (3): _email_line(), render_outreach(), test_render_outreach_flags_unverified_emails_and_skips_undrafted()

### Community 83 - "_scan_inboxes"
Cohesion: 0.29
Nodes (3): _scan_forever(), _scan_inboxes(), _start_inbox_scans()

### Community 86 - "LeadStatus"
Cohesion: 0.09
Nodes (21): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, no_real_services() (+13 more)

### Community 87 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 89 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 555 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **24 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_pipeline.py`, `Region`, `notify.py`, `run_followups`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `internship_agent/ai.py`, `get_settings`, `app.py`, `FormQuestion`, `leads/cli.py`, `find_site_emails`, `find_startups`, `leads/schemas.py`, `patterns.py`, `Settings`, `agenda.py`, `test_chat.py`, `typing`, `Table`, `workflows.py`, `EmailStatus`, `job_pipeline`, `pytest`, `set_status`, `pipeline.py`, `_get`, `find_deadline`, `followup_run.py`, `find-founders.md`, `batches`, `insights`, `followups.py`, `lead_store`, `export.py`, `LeadStatus`, `rank`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Are the 118 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 118 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_sign_in.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_sign_in.py`, `test_pipeline.py`, `Opportunity`, `run_followups`, `test_daily_campaign.py`, `internship_agent/cli.py`, `json`, `test_opportunities.py`, `get_settings`, `app.py`, `FormQuestion`, `leads/cli.py`, `apply_events`, `test_apply_events.py`, `find_site_emails`, `find_startups`, `patterns.py`, `test_chat.py`, `Table`, `workflows.py`, `client.py`, `job_pipeline`, `test_people.py`, `pipeline.py`, `command`, `test_auto_pick.py`, `_get`, `followup_run.py`, `local_only`, `check_events`, `run.py`, `config.py`, `lead_store`, `LeadStatus`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 102 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 102 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_pipeline.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11827956989247312 - nodes in this community are weakly interconnected._