# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 98 files · ~117,382 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1512 nodes · 4526 edges · 69 communities (59 shown, 10 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 768 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e162f2bd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- typing
- answers.py
- Region
- PreparedAnswer
- run.py
- app.py
- applications/browser.py
- FakeField
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
- LeadKind
- agenda.py
- Settings
- test_chat.py
- opportunities/schemas.py
- test_people.py
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- opportunities/cli.py
- test_apply_events.py
- test_application_browser.py
- leads/schemas.py
- run
- run-lowest-30-applications.sh
- find-founders.md
- EmailStatus
- _get
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- leads/cli.py
- README.md
- pytest
- Lead
- mailbox.py
- config.py
- LeadStatus
- test_patterns.py
- startups.py
- re
- feeds.py
- FormQuestion
- startup_jobs.py
- lead_store
- PlaywrightPage
- AGENTS.md
- candidate_context.md
- verification_mail.py
- command
- _view
- apply_events
- prepare_application
- guess_email
- local_only
- send
- rank
- Opportunity
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 140 edges
2. `Settings` - 102 edges
3. `get_settings()` - 72 edges
4. `Opportunity` - 64 edges
5. `OpportunityStore` - 41 edges
6. `LeadStatus` - 40 edges
7. `run_followups()` - 35 edges
8. `Region` - 31 edges
9. `LeadKind` - 30 edges
10. `lead_store()` - 29 edges

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

## Communities (69 total, 10 thin omitted)

### Community 0 - "typing"
Cohesion: 0.22
Nodes (3): Element, _refusal(), StepAction

### Community 1 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+2 more)

### Community 2 - "Region"
Cohesion: 0.11
Nodes (13): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+5 more)

### Community 3 - "PreparedAnswer"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 4 - "run.py"
Cohesion: 0.09
Nodes (19): normalize_url(), refresh_cmd(), _candidate(), check_events(), one(), checked(), find_events(), keep() (+11 more)

### Community 5 - "app.py"
Cohesion: 0.13
Nodes (16): AnswerEdit, ask(), calendar(), _calendar_items(), ChatRequest, delete_preference(), find_more(), find_more_startups() (+8 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.10
Nodes (18): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _online_checks(), open_login_browser(), _post_submit_outcome(), _posting_is_closed() (+10 more)

### Community 7 - "FakeField"
Cohesion: 0.07
Nodes (7): FakeField, FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.07
Nodes (17): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+9 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (19): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+11 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.19
Nodes (14): dashboard(), client(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.14
Nodes (9): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+1 more)

### Community 12 - "json"
Cohesion: 0.15
Nodes (13): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+5 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.13
Nodes (17): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+9 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.17
Nodes (22): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+14 more)

### Community 16 - "get_settings"
Cohesion: 0.14
Nodes (19): get_settings(), allow_event_retry(), allow_retry(), apply_to_event(), check_opportunities(), CheckRequest, daily_run(), event_proof() (+11 more)

### Community 17 - "client.py"
Cohesion: 0.06
Nodes (35): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+27 more)

### Community 18 - "LeadKind"
Cohesion: 0.11
Nodes (15): is_workday(), open_postings(), refill(), LeadKind, _identity(), merge(), scrape_jobs(), startup_postings() (+7 more)

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "Settings"
Cohesion: 0.05
Nodes (43): Settings, append(), read_log(), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name() (+35 more)

### Community 21 - "test_chat.py"
Cohesion: 0.10
Nodes (18): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising() (+10 more)

### Community 22 - "opportunities/schemas.py"
Cohesion: 0.12
Nodes (12): assess(), EventFinding, EventFindings, next_step(), search_events(), write_strategy(), BrowserStep, EventApplication (+4 more)

### Community 23 - "test_people.py"
Cohesion: 0.14
Nodes (13): PersonFinding, _on_linkedin(), source_names(), fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact() (+5 more)

### Community 25 - "patterns.py"
Cohesion: 0.12
Nodes (12): bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at(), proven() (+4 more)

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (9): StartupFindings, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 27 - "opportunities/cli.py"
Cohesion: 0.12
Nodes (10): apply_cmd(), browser_login_cmd(), check_cmd(), find_events_cmd(), import_cmd(), list_cmd(), strategy_cmd(), applied_push() (+2 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.17
Nodes (16): Snapshot, _event(), FakePage, landing(), _settings(), step(), steps(), test_allowed_sites() (+8 more)

### Community 29 - "test_application_browser.py"
Cohesion: 0.17
Nodes (18): _fill_form(), _normalize(), _numeric_answer(), _react_select_answer(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_bachelor_degree_maps_to_greenhouse_degree_choice() (+10 more)

### Community 30 - "leads/schemas.py"
Cohesion: 0.13
Nodes (4): fit_to_limit(), test_funds_old_companies_and_odd_sizes_are_left_out(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 31 - "run"
Cohesion: 0.12
Nodes (9): allowed(), _host(), names_event(), Page, _quote(), resolve(), run(), done() (+1 more)

### Community 33 - "find-founders.md"
Cohesion: 0.13
Nodes (10): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+2 more)

### Community 34 - "EmailStatus"
Cohesion: 0.21
Nodes (8): _email_line(), render_outreach(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_render_outreach_flags_unverified_emails_and_skips_undrafted(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 35 - "_get"
Cohesion: 0.20
Nodes (7): calendar_ics(), dashboard_css(), _get(), note(), NoteRequest, submit(), SubmitApplicationRequest

### Community 40 - "leads/cli.py"
Cohesion: 0.19
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 41 - "README.md"
Cohesion: 0.11
Nodes (28): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+20 more)

### Community 42 - "pytest"
Cohesion: 0.25
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 43 - "Lead"
Cohesion: 0.21
Nodes (4): Lead, LeadStore, test_auto_apply_prepares_then_submits(), test_store_round_trip_and_upsert()

### Community 44 - "mailbox.py"
Cohesion: 0.11
Nodes (6): GmailMailbox, _imap_date(), Mailbox, MailboxError, _quoted(), SentMessage

### Community 45 - "config.py"
Cohesion: 0.19
Nodes (3): posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 46 - "LeadStatus"
Cohesion: 0.08
Nodes (19): Table, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect (+11 more)

### Community 47 - "test_patterns.py"
Cohesion: 0.19
Nodes (10): founder(), test_a_bounced_format_is_never_retried_and_the_domain_is_their_own(), test_a_format_that_reached_someone_is_used_for_the_rest_of_the_company(), test_a_published_address_is_used_as_is(), test_a_recruiter_waits_until_the_ceos_email_shows_the_format(), test_outcomes_learn_from_bounces_and_settled_sends(), test_pointing_at_a_new_guess_keeps_the_bounce_and_restarts_follow_ups(), test_roles_pick_the_email() (+2 more)

### Community 48 - "startups.py"
Cohesion: 0.12
Nodes (18): StartupFinding, Round, Segment, Verdict, parse_round(), mentions(), names(), source_confirms() (+10 more)

### Community 49 - "re"
Cohesion: 0.28
Nodes (10): _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+2 more)

### Community 50 - "feeds.py"
Cohesion: 0.19
Nodes (12): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+4 more)

### Community 51 - "FormQuestion"
Cohesion: 0.19
Nodes (16): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 52 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 53 - "lead_store"
Cohesion: 0.22
Nodes (7): auto_apply(), daily(), _incompatible_term(), lead_store(), refresh_saved_application(), save_answers(), submit_application()

### Community 56 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 57 - "verification_mail.py"
Cohesion: 0.22
Nodes (4): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code()

### Community 58 - "command"
Cohesion: 0.11
Nodes (12): application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd(), form_d_cmd() (+4 more)

### Community 59 - "_view"
Cohesion: 0.15
Nodes (10): screenshot_path(), application_proof(), draft(), leads(), set_status(), _sort_key(), StatusUpdate, _view() (+2 more)

### Community 60 - "apply_events"
Cohesion: 0.25
Nodes (4): describe(), apply_events(), step(), proof_path()

### Community 61 - "prepare_application"
Cohesion: 0.32
Nodes (5): answer_bank(), prepare_application(), _retryable_block(), _use_gmail_for_applications(), test_application_email_uses_configured_gmail()

### Community 62 - "guess_email"
Cohesion: 0.24
Nodes (4): Output, _clean(), guess_email(), test_guess_email()

### Community 63 - "local_only"
Cohesion: 0.29
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 70 - "Opportunity"
Cohesion: 0.22
Nodes (7): mark_cmd(), import_inbox(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.08
Nodes (20): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), load_resume_text(), to_people(), add_team_contacts(), DailyReport (+12 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 475 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `answers.py`, `Region`, `PreparedAnswer`, `app.py`, `applications/browser.py`, `test_daily_campaign.py`, `form_d.py`, `test_dashboard.py`, `json`, `internship_agent/ai.py`, `LeadKind`, `agenda.py`, `Settings`, `test_chat.py`, `patterns.py`, `test_application_browser.py`, `leads/schemas.py`, `find-founders.md`, `EmailStatus`, `_get`, `leads/cli.py`, `pytest`, `config.py`, `LeadStatus`, `test_patterns.py`, `startups.py`, `FormQuestion`, `lead_store`, `_view`, `prepare_application`, `rank`, `workflows.py`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 100 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 100 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.10752688172043011 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `answers.py`, `Region`, `run.py`, `test_daily_campaign.py`, `form_d.py`, `internship_agent/cli.py`, `json`, `test_opportunities.py`, `get_settings`, `client.py`, `LeadKind`, `test_chat.py`, `test_people.py`, `patterns.py`, `test_apply_events.py`, `leads/cli.py`, `config.py`, `LeadStatus`, `test_patterns.py`, `FormQuestion`, `lead_store`, `_view`, `apply_events`, `prepare_application`, `local_only`, `Opportunity`, `workflows.py`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 85 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 85 INFERRED edges - model-reasoned connections that need verification._
- **Should `run.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09103840682788052 - nodes in this community are weakly interconnected._