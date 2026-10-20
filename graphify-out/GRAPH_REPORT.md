# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 99 files · ~120,133 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1568 nodes · 4692 edges · 72 communities (56 shown, 16 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 796 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `799a9d7f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sign_in.py
- test_chat.py
- Region
- notify.py
- run.py
- test_followups.py
- applications/browser.py
- test_application_browser.py
- test_daily_campaign.py
- form_d.py
- pytest
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- app.py
- tracking.py
- test_refill.py
- agenda.py
- run_followups
- test_agenda.py
- opportunities/ai.py
- test_ai.py
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- find_events
- test_apply_events.py
- startup_jobs.py
- Table
- run
- run-lowest-30-applications.sh
- people.py
- leads/schemas.py
- test_people.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- outlook
- README.md
- typing
- Winter 2027 Internship Agent
- mailbox.py
- OutlookClient
- LeadStatus
- import_inbox
- test_outreach.py
- mailer.py
- client.py
- FormQuestion
- find_startups
- SentMessage
- collections_abc
- AGENTS.md
- candidate_context.md
- verification_mail.py
- leads/cli.py
- test_form_d.py
- apply_events
- test_x_search.py
- re
- StepAction
- ToolSession
- test_tables
- OutreachDraft
- test_interview_events
- Opportunity
- find-opportunities.md
- Lead

## God Nodes (most connected - your core abstractions)
1. `Lead` - 140 edges
2. `Settings` - 104 edges
3. `get_settings()` - 73 edges
4. `Opportunity` - 66 edges
5. `OpportunityStore` - 41 edges
6. `LeadStatus` - 40 edges
7. `run_followups()` - 35 edges
8. `Region` - 31 edges
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

## Communities (72 total, 16 thin omitted)

### Community 0 - "test_sign_in.py"
Cohesion: 0.17
Nodes (12): FakePage, mail(), scripted(), step(), test_a_quiet_page_after_signing_in_counts_but_a_code_page_does_not(), test_no_email_link_means_needs_you(), test_reads_a_fresh_code_only_from_the_site(), test_reads_the_sign_in_link_from_html() (+4 more)

### Community 1 - "test_chat.py"
Cohesion: 0.21
Nodes (10): fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github(), test_profile_is_cached_for_a_day() (+2 more)

### Community 2 - "Region"
Cohesion: 0.10
Nodes (13): Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+5 more)

### Community 3 - "notify.py"
Cohesion: 0.20
Nodes (13): category(), _clip(), _fit_bytes(), posting_push(), summary_push(), written_answers(), answer(), lead() (+5 more)

### Community 4 - "run.py"
Cohesion: 0.10
Nodes (14): normalize_url(), list_cmd(), keep(), _keys(), nearby(), next_date(), refresh(), to_apply() (+6 more)

### Community 5 - "test_followups.py"
Cohesion: 0.21
Nodes (18): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+10 more)

### Community 6 - "applications/browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "test_application_browser.py"
Cohesion: 0.07
Nodes (24): _fill_form(), _numeric_answer(), PreparedAnswer, FakeField, FakeLocator, FakePage, FakeToggle, posting() (+16 more)

### Community 8 - "test_daily_campaign.py"
Cohesion: 0.08
Nodes (16): ApplicationPrep, FitAssessment, _identity(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load() (+8 more)

### Community 9 - "form_d.py"
Cohesion: 0.11
Nodes (18): candidate_domains(), _check(), company_name(), _description(), _fetch(), Filing, filings(), find_site() (+10 more)

### Community 10 - "pytest"
Cohesion: 0.08
Nodes (32): LeadStore, no_real_services(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+24 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+3 more)

### Community 12 - "json"
Cohesion: 0.07
Nodes (34): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+26 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.16
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.18
Nodes (21): _assessment(), _fake_ai(), _opp(), _settings(), test_a_finished_check_is_saved_before_the_run_is_killed(), fake(), test_check_events_saves_results_and_survives_one_failure(), fake() (+13 more)

### Community 16 - "app.py"
Cohesion: 0.05
Nodes (67): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, get_settings(), allow_event_retry(), allow_retry(), AnswerEdit, application_proof(), apply_to_event() (+59 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "test_refill.py"
Cohesion: 0.14
Nodes (10): Big-company postings from the SimplifyJobs off-season list, refill(), merge(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+2 more)

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "run_followups"
Cohesion: 0.12
Nodes (15): FollowupReport, FollowupSent, _misaddressed(), _name(), run_followups(), _site(), company_domain(), first_name() (+7 more)

### Community 21 - "test_agenda.py"
Cohesion: 0.19
Nodes (8): _assessment(), _emailed(), _opp(), test_a_posting_deadline_shows_until_you_apply(), test_an_opportunity_gives_apply_deadline_and_event_items(), test_dashboard_exports_only_your_items_unless_asked(), test_follow_ups_land_on_their_due_day_or_today_if_overdue(), test_mine_means_planned_or_promising()

### Community 22 - "opportunities/ai.py"
Cohesion: 0.09
Nodes (15): assess(), EventFinding, EventFindings, search_events(), write_strategy(), check_events(), one(), checked() (+7 more)

### Community 23 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 25 - "patterns.py"
Cohesion: 0.06
Nodes (25): Output, guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes() (+17 more)

### Community 26 - "x_search.py"
Cohesion: 0.14
Nodes (9): search_startups(), StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+1 more)

### Community 27 - "find_events"
Cohesion: 0.12
Nodes (10): Push, send(), apply_cmd(), check_cmd(), find_events_cmd(), refresh_cmd(), strategy_cmd(), applied_push() (+2 more)

### Community 28 - "test_apply_events.py"
Cohesion: 0.15
Nodes (17): Snapshot, BrowserStep, _event(), FakePage, landing(), _settings(), step(), steps() (+9 more)

### Community 29 - "startup_jobs.py"
Cohesion: 0.25
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 31 - "run"
Cohesion: 0.11
Nodes (11): allowed(), _host(), names_event(), nothing_to_sign_in(), Page, _quote(), resolve(), run() (+3 more)

### Community 33 - "people.py"
Cohesion: 0.20
Nodes (6): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 34 - "leads/schemas.py"
Cohesion: 0.18
Nodes (9): open_postings(), EmailStatus, LeadKind, Round, Segment, Verdict, parse_round(), test_the_site_must_name_someone_on_the_filing_or_its_legal_name() (+1 more)

### Community 35 - "test_people.py"
Cohesion: 0.26
Nodes (7): PersonFinding, search_people(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 40 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 41 - "README.md"
Cohesion: 0.26
Nodes (11): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+3 more)

### Community 42 - "typing"
Cohesion: 0.29
Nodes (5): posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns()

### Community 43 - "Winter 2027 Internship Agent"
Cohesion: 0.22
Nodes (9): Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does (+1 more)

### Community 44 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 45 - "OutlookClient"
Cohesion: 0.20
Nodes (7): OutlookClient, OutlookError, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 46 - "LeadStatus"
Cohesion: 0.23
Nodes (9): apply_violations(), _normalize(), PreferenceStore, LeadStatus, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_preference_store_dedupes_and_removes() (+1 more)

### Community 47 - "import_inbox"
Cohesion: 0.25
Nodes (3): import_cmd(), import_inbox(), proof_path()

### Community 48 - "test_outreach.py"
Cohesion: 0.15
Nodes (12): mentions(), names(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+4 more)

### Community 49 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 50 - "client.py"
Cohesion: 0.25
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 51 - "FormQuestion"
Cohesion: 0.11
Nodes (24): _answer_for(), AnswerBank, common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+16 more)

### Community 52 - "find_startups"
Cohesion: 0.33
Nodes (4): effective_segment(), find_startups(), people_at(), startup_postings()

### Community 54 - "collections_abc"
Cohesion: 0.13
Nodes (4): Element, import_sessions(), PlaywrightPage, saved_browser()

### Community 56 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 57 - "verification_mail.py"
Cohesion: 0.09
Nodes (12): _extract_code(), extract_sign_in(), _message_text(), _poll(), _raw_text(), VerificationCode, wait_for_greenhouse_code(), wait_for_sign_in() (+4 more)

### Community 58 - "leads/cli.py"
Cohesion: 0.05
Nodes (39): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look (+31 more)

### Community 60 - "apply_events"
Cohesion: 0.12
Nodes (11): next_step(), describe(), sign_in_cmd(), apply_events(), step(), _candidate(), send_sessions(), sign_in() (+3 more)

### Community 61 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 62 - "re"
Cohesion: 0.24
Nodes (4): _clean(), fit_to_limit(), _slug(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 70 - "Opportunity"
Cohesion: 0.24
Nodes (6): mark_cmd(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "Lead"
Cohesion: 0.06
Nodes (38): Send email safeguards, Settings, append(), read_log(), _logged_subject(), is_workday(), Lead, Note (+30 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 490 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `Region`, `notify.py`, `run.py`, `test_followups.py`, `applications/browser.py`, `test_application_browser.py`, `test_daily_campaign.py`, `form_d.py`, `pytest`, `json`, `internship_agent/ai.py`, `app.py`, `test_refill.py`, `agenda.py`, `run_followups`, `test_agenda.py`, `patterns.py`, `Table`, `leads/schemas.py`, `test_people.py`, `typing`, `LeadStatus`, `test_outreach.py`, `FormQuestion`, `find_startups`, `leads/cli.py`, `OutreachDraft`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 100 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 100 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.10416666666666667 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Lead` to `test_sign_in.py`, `test_chat.py`, `Region`, `run.py`, `test_followups.py`, `test_daily_campaign.py`, `internship_agent/cli.py`, `json`, `test_opportunities.py`, `app.py`, `run_followups`, `test_agenda.py`, `opportunities/ai.py`, `patterns.py`, `find_events`, `test_apply_events.py`, `Table`, `test_people.py`, `typing`, `LeadStatus`, `import_inbox`, `client.py`, `FormQuestion`, `find_startups`, `leads/cli.py`, `apply_events`, `.gmail_account`, `Opportunity`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Should `run.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0975609756097561 - nodes in this community are weakly interconnected._