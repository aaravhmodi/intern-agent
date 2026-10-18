# Graph Report - winter-2027-internship-agent  (2026-10-18)

## Corpus Check
- 76 files · ~193,149 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1031 nodes · 2977 edges · 62 communities (46 shown, 16 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 521 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2d1c1b2f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_refill.py
- leads/cli.py
- simplify.py
- README.md
- workflows.py
- test_leads.py
- browser.py
- FakeField
- Region
- Settings
- test_dashboard.py
- internship_agent/cli.py
- startups.py
- make_workflows.py
- pydantic
- Segment
- app.py
- tracking.py
- mailbox.py
- LeadKind
- run_followups
- search_x_raises
- FormQuestion
- OutlookClient
- run-application-campaign-2026-10-16.sh
- _get
- x_search.py
- Lead
- client.py
- test_application_browser.py
- outlook/schemas.py
- test_x_search.py
- run-lowest-30-applications.sh
- find_startups
- FakeToggle
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- notify.py
- Winter 2027 Internship Agent
- json
- ai.py
- Any
- test_hidden_recaptcha_support_nodes_do_not_block
- _numeric_answer
- mailer.py
- startup_jobs.py
- leads/schemas.py
- Bot Auto application preview
- followups.py
- send_email
- FakeMailbox
- candidate_context.md
- test_outlook_client.py
- _post_submit_outcome
- note
- emails.py
- _react_select_answer
- test_interview_events

## God Nodes (most connected - your core abstractions)
1. `Lead` - 110 edges
2. `Settings` - 62 edges
3. `get_settings()` - 45 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `prepare_application()` - 28 edges
7. `FormQuestion` - 27 edges
8. `find_startups()` - 27 edges
9. `Region` - 25 edges
10. `Segment` - 24 edges

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

## Communities (62 total, 16 thin omitted)

### Community 0 - "test_refill.py"
Cohesion: 0.14
Nodes (9): merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped() (+1 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.05
Nodes (43): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+35 more)

### Community 2 - "simplify.py"
Cohesion: 0.13
Nodes (6): cap_per_company(), is_software_role(), matching(), parse(), Posting, _TableParser

### Community 3 - "README.md"
Cohesion: 0.20
Nodes (16): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+8 more)

### Community 4 - "workflows.py"
Cohesion: 0.10
Nodes (18): auto_apply(), ApplicationPrep, answer_bank(), handle_note(), _incompatible_term(), lead_store(), NoteOutcome, _openai() (+10 more)

### Community 5 - "test_leads.py"
Cohesion: 0.08
Nodes (27): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), fit(), lead(), posting() (+19 more)

### Community 6 - "browser.py"
Cohesion: 0.13
Nodes (12): apply_to_posting(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _save_submission_diagnostic(), SubmissionResult (+4 more)

### Community 7 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 8 - "Region"
Cohesion: 0.31
Nodes (4): Region, Verdict, region_from_text(), regions_of()

### Community 9 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.16
Nodes (14): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+6 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "startups.py"
Cohesion: 0.16
Nodes (8): StartupFinding, _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 13 - "make_workflows.py"
Cohesion: 0.17
Nodes (9): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, n8n workflows (+1 more)

### Community 14 - "pydantic"
Cohesion: 0.09
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 15 - "Segment"
Cohesion: 0.15
Nodes (15): Round, Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+7 more)

### Community 16 - "app.py"
Cohesion: 0.15
Nodes (15): AnswerEdit, delete_preference(), find_more_startups(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, leads() (+7 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "mailbox.py"
Cohesion: 0.21
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 19 - "LeadKind"
Cohesion: 0.22
Nodes (9): Big-company postings from the SimplifyJobs off-season list, open_postings(), refill(), LeadKind, fetch(), to_lead(), find_more_postings(), scrape_jobs() (+1 more)

### Community 20 - "run_followups"
Cohesion: 0.10
Nodes (9): Internship tracker: follow-ups (weekdays 9:30 AM), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+1 more)

### Community 22 - "FormQuestion"
Cohesion: 0.12
Nodes (15): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+7 more)

### Community 23 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 25 - "_get"
Cohesion: 0.19
Nodes (9): Output, Output, allow_retry(), _get(), index(), KeyRequest, people(), prepare() (+1 more)

### Community 26 - "x_search.py"
Cohesion: 0.15
Nodes (13): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+5 more)

### Community 27 - "Lead"
Cohesion: 0.21
Nodes (6): find_more(), _view(), Lead, _identity(), LeadStore, test_post_submit_state_is_persisted_for_tracker()

### Community 28 - "client.py"
Cohesion: 0.20
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 29 - "test_application_browser.py"
Cohesion: 0.20
Nodes (19): _answer_for(), _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_closed_posting_text_is_detected() (+11 more)

### Community 30 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 31 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 33 - "find_startups"
Cohesion: 0.22
Nodes (8): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups(), people_at()

### Community 40 - "notify.py"
Cohesion: 0.07
Nodes (25): FitAssessment, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+17 more)

### Community 41 - "Winter 2027 Internship Agent"
Cohesion: 0.12
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP) (+4 more)

### Community 42 - "json"
Cohesion: 0.24
Nodes (10): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _log_xai(), test_ashby_parser() (+2 more)

### Community 43 - "ai.py"
Cohesion: 0.06
Nodes (32): Internship agent coding instructions, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note() (+24 more)

### Community 44 - "Any"
Cohesion: 0.17
Nodes (9): daily_run(), draft(), rescore(), set_status(), StatusUpdate, submit(), SubmitApplicationRequest, Lead detail panel: fit, links, contact, actions (+1 more)

### Community 47 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 48 - "startup_jobs.py"
Cohesion: 0.25
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 49 - "leads/schemas.py"
Cohesion: 0.24
Nodes (4): fit_to_limit(), _normalize(), Note, _slug()

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 51 - "followups.py"
Cohesion: 0.20
Nodes (7): company_domain(), first_name(), followup_body(), is_due(), last_contact(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 52 - "send_email"
Cohesion: 0.22
Nodes (7): Send email safeguards, send(), Email section with two-click send, check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 54 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 55 - "test_outlook_client.py"
Cohesion: 0.36
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 56 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

### Community 58 - "note"
Cohesion: 0.50
Nodes (3): note(), NoteRequest, Notes box that saves notes and learns rules

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 326 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_refill.py`, `leads/cli.py`, `simplify.py`, `workflows.py`, `test_leads.py`, `browser.py`, `Settings`, `test_dashboard.py`, `startups.py`, `Segment`, `app.py`, `LeadKind`, `run_followups`, `FormQuestion`, `_get`, `test_application_browser.py`, `find_startups`, `notify.py`, `ai.py`, `Any`, `leads/schemas.py`, `followups.py`, `send_email`, `field_validator`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_refill.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13970588235294118 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `find_startups`, `workflows.py`, `test_leads.py`, `notify.py`, `Winter 2027 Internship Agent`, `json`, `internship_agent/cli.py`, `Any`, `ai.py`, `app.py`, `LeadKind`, `run_followups`, `send_email`, `FormQuestion`, `Lead`, `client.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.054363796650014694 - nodes in this community are weakly interconnected._