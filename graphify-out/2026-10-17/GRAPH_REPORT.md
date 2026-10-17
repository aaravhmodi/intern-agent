# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~105,636 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 965 nodes · 2810 edges · 51 communities (40 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 493 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7ece933`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _view
- leads/cli.py
- Region
- test_daily_campaign.py
- notify.py
- workflows.py
- test_application_browser.py
- followups.py
- FakeField
- run_followups
- tracking.py
- internship_agent/cli.py
- app.py
- make_workflows.py
- FormQuestion
- prepare_application
- browser.py
- mailer.py
- startups.py
- find_startups
- test_dashboard.py
- README.md
- answers.py
- EmailStatus
- run-application-campaign-2026-10-16.sh
- Settings
- Lead
- test_x_search.py
- OutlookClient
- send_email
- test_outlook_client.py
- AGENTS.md
- mailbox.py
- candidate_context.md
- re
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- _get
- outlook/schemas.py
- handle_note
- ai.py
- local_only
- _TableParser
- SentMessage
- Segment
- test_hidden_recaptcha_support_nodes_do_not_block
- _numeric_answer
- client.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 109 edges
2. `Settings` - 59 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 26 edges
8. `Region` - 25 edges
9. `Segment` - 24 edges
10. `FormQuestion` - 24 edges

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

## Communities (51 total, 11 thin omitted)

### Community 0 - "_view"
Cohesion: 0.22
Nodes (14): daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), KeyRequest, leads(), people() (+6 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (39): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+31 more)

### Community 2 - "Region"
Cohesion: 0.14
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 3 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 4 - "notify.py"
Cohesion: 0.18
Nodes (15): category(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 5 - "workflows.py"
Cohesion: 0.18
Nodes (7): apply_violations(), LeadKind, LeadStatus, Note, _record_openai_usage(), score(), startup_postings()

### Community 6 - "test_application_browser.py"
Cohesion: 0.32
Nodes (13): _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+5 more)

### Community 7 - "followups.py"
Cohesion: 0.23
Nodes (6): first_name(), followup_body(), is_due(), last_contact(), test_a_follow_up_is_due_five_days_after_the_last_email(), test_nobody_gets_a_third_or_one_after_replying_or_being_skipped()

### Community 8 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 9 - "run_followups"
Cohesion: 0.11
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 10 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.14
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "app.py"
Cohesion: 0.18
Nodes (10): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, PreferenceDelete, SaveAnswersRequest, _sort_key() (+2 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "FormQuestion"
Cohesion: 0.24
Nodes (6): _answer_for(), AnswerBank, prefill(), FormQuestion, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 15 - "prepare_application"
Cohesion: 0.19
Nodes (9): answer_bank(), lead_store(), prepare_application(), refresh_saved_application(), rescore_open(), resume_text(), _retryable_block(), save_answers() (+1 more)

### Community 16 - "browser.py"
Cohesion: 0.13
Nodes (13): apply_to_posting(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _save_submission_diagnostic(), SubmissionResult (+5 more)

### Community 17 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 18 - "startups.py"
Cohesion: 0.16
Nodes (8): StartupFinding, _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 19 - "find_startups"
Cohesion: 0.18
Nodes (9): More people to connect with, chosen by company size, search_people(), Person, to_people(), find_people(), find_startups(), people_at(), _log_xai() (+1 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "README.md"
Cohesion: 0.15
Nodes (20): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+12 more)

### Community 22 - "answers.py"
Cohesion: 0.14
Nodes (14): common_questions(), match_option(), normalize(), validate(), QuestionKind, q(), test_ashby_parser(), test_category() (+6 more)

### Community 23 - "EmailStatus"
Cohesion: 0.24
Nodes (5): EmailStatus, Verdict, check_outreach_text(), check_send(), SendBlocked

### Community 25 - "Settings"
Cohesion: 0.22
Nodes (16): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+8 more)

### Community 26 - "Lead"
Cohesion: 0.05
Nodes (40): _email_line(), render_outreach(), is_workday(), open_postings(), refill(), Lead, _slug(), _identity() (+32 more)

### Community 27 - "test_x_search.py"
Cohesion: 0.32
Nodes (4): post_confirms(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 28 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 29 - "send_email"
Cohesion: 0.24
Nodes (5): Send email safeguards, send(), SendRequest, Email section with two-click send, send_email()

### Community 30 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 33 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 34 - "re"
Cohesion: 0.07
Nodes (30): _clean(), fit_to_limit(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _ashby() (+22 more)

### Community 40 - "_get"
Cohesion: 0.28
Nodes (8): _get(), index(), set_status(), StatusUpdate, Dashboard page (index.html), Lead detail panel: fit, links, contact, actions, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 41 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 42 - "handle_note"
Cohesion: 0.33
Nodes (4): note(), NoteRequest, Notes box that saves notes and learns rules, handle_note()

### Community 43 - "ai.py"
Cohesion: 0.06
Nodes (44): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+36 more)

### Community 44 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 47 - "Segment"
Cohesion: 0.16
Nodes (14): Round, Segment, effective_segment(), parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends() (+6 more)

### Community 52 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 295 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `_view`, `leads/cli.py`, `Region`, `test_daily_campaign.py`, `notify.py`, `workflows.py`, `test_application_browser.py`, `followups.py`, `run_followups`, `app.py`, `FormQuestion`, `prepare_application`, `browser.py`, `startups.py`, `find_startups`, `test_dashboard.py`, `answers.py`, `EmailStatus`, `Settings`, `send_email`, `_get`, `ai.py`, `Segment`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05765765765765766 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `_view`, `leads/cli.py`, `Region`, `test_daily_campaign.py`, `workflows.py`, `run_followups`, `handle_note`, `internship_agent/cli.py`, `local_only`, `ai.py`, `FormQuestion`, `prepare_application`, `find_startups`, `client.py`, `answers.py`, `Lead`, `send_email`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14333333333333334 - nodes in this community are weakly interconnected._