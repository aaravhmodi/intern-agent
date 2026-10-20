# Graph Report - opportunity-agent  (2026-10-20)

## Corpus Check
- 95 files · ~112,865 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 14 file(s) not represented in the graph (top: (none) 5, .service 3, .timer 3)

## Summary
- 1412 nodes · 4224 edges · 65 communities (51 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 722 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `053e5a46`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- followup_run.py
- FormQuestion
- Region
- notify.py
- run.py
- app.py
- browser.py
- FakeField
- test_chat.py
- form_d.py
- pytest
- internship_agent/cli.py
- json
- make_workflows.py
- internship_agent/ai.py
- test_opportunities.py
- get_settings
- datetime
- Lead
- agenda.py
- Settings
- OutlookClient
- client.py
- test_people.py
- run-application-campaign-2026-10-16.sh
- patterns.py
- x_search.py
- import_inbox
- test_notes.py
- test_application_browser.py
- fit_to_limit
- test_ai.py
- run-lowest-30-applications.sh
- find-internships.md
- sending.py
- _calendar_items
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- PostgresLeadStore
- README.md
- send_email
- outlook/schemas.py
- mailbox.py
- pathlib
- preferences.py
- Table
- leads/schemas.py
- followups.py
- feeds.py
- typing
- _TableParser
- FakeMailbox
- load_resume_text
- Dashboard page (index.html)
- verification_mail.py
- leads/cli.py
- application_proof
- re
- test_outlook_client.py
- Opportunity
- config.py
- find-opportunities.md
- workflows.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 140 edges
2. `Settings` - 99 edges
3. `get_settings()` - 67 edges
4. `Opportunity` - 55 edges
5. `LeadStatus` - 40 edges
6. `OpportunityStore` - 37 edges
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

## Communities (65 total, 14 thin omitted)

### Community 0 - "followup_run.py"
Cohesion: 0.18
Nodes (7): FollowupReport, FollowupSent, _misaddressed(), _name(), _site(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 1 - "FormQuestion"
Cohesion: 0.15
Nodes (13): _answer_for(), AnswerBank, category(), match_option(), normalize(), prefill(), validate(), FormQuestion (+5 more)

### Community 2 - "Region"
Cohesion: 0.12
Nodes (14): Big-company postings from the SimplifyJobs off-season list, Region, normalize_url(), region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role() (+6 more)

### Community 3 - "notify.py"
Cohesion: 0.18
Nodes (15): application_campaign(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 4 - "run.py"
Cohesion: 0.08
Nodes (20): check_cmd(), find_events_cmd(), list_cmd(), refresh_cmd(), strategy_cmd(), _candidate(), check_events(), one() (+12 more)

### Community 5 - "app.py"
Cohesion: 0.13
Nodes (22): AnswerEdit, ask(), ChatRequest, CheckRequest, delete_preference(), find_more(), find_more_startups(), FindMoreRequest (+14 more)

### Community 6 - "browser.py"
Cohesion: 0.09
Nodes (22): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+14 more)

### Community 7 - "FakeField"
Cohesion: 0.07
Nodes (7): FakeField, FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 8 - "test_chat.py"
Cohesion: 0.05
Nodes (26): FitAssessment, fake_get(), FakeResponses, _settings(), test_a_source_that_fails_is_noted_not_fatal(), test_answer_runs_tools_and_grounds_the_system_prompt(), test_chat_endpoint_needs_a_question(), test_profile_has_context_resume_website_and_github() (+18 more)

### Community 9 - "form_d.py"
Cohesion: 0.15
Nodes (11): candidate_domains(), company_name(), Filing, filings(), find_site(), form_d_paths(), index_url(), parse_filing() (+3 more)

### Community 10 - "pytest"
Cohesion: 0.08
Nodes (33): dashboard(), LeadStore, no_real_services(), client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key() (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.14
Nodes (9): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+1 more)

### Community 12 - "json"
Cohesion: 0.08
Nodes (31): answer(), build_profile(), ChatMessage, _matches(), profile(), read_repo(), readme(), _repos() (+23 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.14
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+4 more)

### Community 14 - "internship_agent/ai.py"
Cohesion: 0.18
Nodes (12): AnswerDraft, assess_fit(), draft_outreach(), format_preferences(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter() (+4 more)

### Community 15 - "test_opportunities.py"
Cohesion: 0.06
Nodes (39): assess(), EventFinding, EventFindings, search_events(), write_strategy(), OpportunityAssessment, SubmissionStrategy, SubmissionTrack (+31 more)

### Community 16 - "get_settings"
Cohesion: 0.12
Nodes (27): get_settings(), allow_retry(), auto_apply(), check_opportunities(), daily_run(), draft(), find_events(), _get() (+19 more)

### Community 17 - "datetime"
Cohesion: 0.16
Nodes (14): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), interview_events(), Stage, to_update() (+6 more)

### Community 18 - "Lead"
Cohesion: 0.09
Nodes (18): _email_line(), render_outreach(), is_workday(), open_postings(), refill(), Lead, _identity(), merge() (+10 more)

### Community 19 - "agenda.py"
Cohesion: 0.21
Nodes (8): _fold(), Item, items(), lead_items(), opportunity_items(), _promising(), _text(), to_ics()

### Community 20 - "Settings"
Cohesion: 0.18
Nodes (18): Settings, run_followups(), emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+10 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "client.py"
Cohesion: 0.22
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "test_people.py"
Cohesion: 0.16
Nodes (10): PersonFinding, _on_linkedin(), source_names(), page_names(), source_confirms(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 25 - "patterns.py"
Cohesion: 0.05
Nodes (27): guess_email(), bounced_addresses(), by_domain(), domain_of(), format_of(), next_guess(), outcomes(), point_at() (+19 more)

### Community 26 - "x_search.py"
Cohesion: 0.13
Nodes (10): search_startups(), StartupFinding, StartupFindings, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising() (+2 more)

### Community 28 - "test_notes.py"
Cohesion: 0.20
Nodes (10): AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PreferenceDraft, posting(), settings(), test_format_preferences() (+2 more)

### Community 29 - "test_application_browser.py"
Cohesion: 0.21
Nodes (16): _fill_form(), _numeric_answer(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+8 more)

### Community 31 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 33 - "find-internships.md"
Cohesion: 0.25
Nodes (5): Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look

### Community 34 - "sending.py"
Cohesion: 0.27
Nodes (5): Send email safeguards, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 35 - "_calendar_items"
Cohesion: 0.29
Nodes (4): calendar(), calendar_ics(), _calendar_items(), dashboard_css()

### Community 41 - "README.md"
Cohesion: 0.06
Nodes (30): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+22 more)

### Community 42 - "send_email"
Cohesion: 0.19
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 44 - "mailbox.py"
Cohesion: 0.11
Nodes (7): followups_cmd(), company_domain(), GmailMailbox, _imap_date(), Mailbox, MailboxError, _quoted()

### Community 45 - "pathlib"
Cohesion: 0.25
Nodes (3): posting(), test_a_stale_save_keeps_a_status_set_meanwhile(), test_tables()

### Community 46 - "preferences.py"
Cohesion: 0.26
Nodes (9): apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_preference_store_dedupes_and_removes() (+1 more)

### Community 48 - "leads/schemas.py"
Cohesion: 0.11
Nodes (20): is_open(), rank(), LeadKind, LeadStatus, Round, Segment, _slug(), Verdict (+12 more)

### Community 49 - "followups.py"
Cohesion: 0.23
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), next_followup(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 50 - "feeds.py"
Cohesion: 0.21
Nodes (13): ccfddl(), collect_ccfddl(), collect_confs_tech(), collect_devpost(), collect_mlh(), confs_tech(), _day(), devpost() (+5 more)

### Community 51 - "typing"
Cohesion: 0.19
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 55 - "Dashboard page (index.html)"
Cohesion: 0.50
Nodes (5): index(), Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 57 - "verification_mail.py"
Cohesion: 0.19
Nodes (5): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _get()

### Community 58 - "leads/cli.py"
Cohesion: 0.07
Nodes (29): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, apply_cmd(), browser_login(), daily_cmd() (+21 more)

### Community 62 - "re"
Cohesion: 0.18
Nodes (8): _clean(), _check(), _description(), _fetch(), founder_email(), _has_name(), _fold(), post_text()

### Community 63 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 70 - "Opportunity"
Cohesion: 0.26
Nodes (6): mark_cmd(), plan_submission(), Opportunity, OpportunityStore, test_add_new_dedupes_and_never_overwrites_status(), test_opportunities_live_in_a_table_and_keep_your_status()

### Community 72 - "config.py"
Cohesion: 0.15
Nodes (4): append(), read_log(), _logged_subject(), _record_openai_usage()

### Community 80 - "find-opportunities.md"
Cohesion: 0.50
Nodes (3): Output, Rules, Where to look

### Community 86 - "workflows.py"
Cohesion: 0.07
Nodes (32): More people to connect with, chosen by company size, search_people(), common_questions(), ApplicationPrep, Note, Person, effective_segment(), to_people() (+24 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 443 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `followup_run.py`, `FormQuestion`, `Region`, `notify.py`, `app.py`, `browser.py`, `test_chat.py`, `form_d.py`, `pytest`, `json`, `internship_agent/ai.py`, `test_opportunities.py`, `get_settings`, `agenda.py`, `Settings`, `patterns.py`, `test_notes.py`, `test_application_browser.py`, `fit_to_limit`, `find-internships.md`, `sending.py`, `PostgresLeadStore`, `send_email`, `pathlib`, `preferences.py`, `leads/schemas.py`, `followups.py`, `typing`, `leads/cli.py`, `workflows.py`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Are the 100 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `items()`) actually correct?**
  _`Lead` has 100 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `FormQuestion` be split into smaller, more focused modules?**
  _Cohesion score 0.1452991452991453 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `followup_run.py`, `FormQuestion`, `Region`, `run.py`, `app.py`, `test_chat.py`, `internship_agent/cli.py`, `json`, `make_workflows.py`, `test_opportunities.py`, `get_settings`, `Lead`, `client.py`, `test_people.py`, `patterns.py`, `import_inbox`, `test_notes.py`, `send_email`, `preferences.py`, `Table`, `typing`, `leads/cli.py`, `Opportunity`, `config.py`, `workflows.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 82 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `answer()`) actually correct?**
  _`Settings` has 82 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.12433862433862433 - nodes in this community are weakly interconnected._