# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~89,078 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 921 nodes · 2665 edges · 54 communities (42 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 450 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d9968da8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- command
- re
- typing
- answers.py
- ai.py
- Lead
- run_followups
- mailer.py
- test_followups.py
- client.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- test_application_browser.py
- test_outreach.py
- test_x_search.py
- x_search.py
- json
- test_people.py
- notify.py
- Settings
- run-application-campaign-2026-10-16.sh
- browser.py
- test_leads.py
- Winter 2027 Internship Agent
- followups.py
- test_scrape_stores_every_matching_non_workday_posting
- startups.py
- candidate_context.md
- leads/cli.py
- SentMessage
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- find-founders.md
- find_more_postings
- Region
- get_settings
- Dashboard page (index.html)
- followups_cmd
- test_answers.py
- README.md
- config.py
- send_email
- AGENTS.md
- search_startups
- _TableParser
- ApplicationPrep

## God Nodes (most connected - your core abstractions)
1. `Lead` - 101 edges
2. `Settings` - 52 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `prepare_application()` - 25 edges
9. `Segment` - 24 edges
10. `LeadKind` - 23 edges

## Surprising Connections (you probably didn't know these)
- `Segment: early, mid or big` --references--> `Segment`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Posting lead JSON appended to data/leads-inbox.json` --references--> `Lead`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Fit score against the resume (0-100, reasons, talking points)` --references--> `assess_fit()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (54 total, 12 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.21
Nodes (6): fit_to_limit(), LeadKind, Round, Segment, Verdict, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 1 - "command"
Cohesion: 0.20
Nodes (10): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), prepare_all_cmd(), score_leads() (+2 more)

### Community 2 - "re"
Cohesion: 0.38
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 3 - "typing"
Cohesion: 0.12
Nodes (15): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+7 more)

### Community 4 - "answers.py"
Cohesion: 0.16
Nodes (10): _answer_for(), AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate() (+2 more)

### Community 5 - "ai.py"
Cohesion: 0.07
Nodes (33): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+25 more)

### Community 6 - "Lead"
Cohesion: 0.12
Nodes (15): search_people(), is_workday(), Lead, effective_segment(), merge(), to_people(), DailyReport, find_people() (+7 more)

### Community 7 - "run_followups"
Cohesion: 0.12
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (34): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+26 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.14
Nodes (9): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+1 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "app.py"
Cohesion: 0.10
Nodes (32): AnswerEdit, daily_run(), delete_preference(), draft(), find_more_startups(), FindMoreRequest, FindStartupsRequest, followups() (+24 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.15
Nodes (9): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+1 more)

### Community 17 - "test_outreach.py"
Cohesion: 0.15
Nodes (13): StartupFinding, parse_round(), mentions(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+5 more)

### Community 18 - "test_x_search.py"
Cohesion: 0.22
Nodes (6): post_confirms(), post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 19 - "x_search.py"
Cohesion: 0.24
Nodes (3): _slug(), search_x_raises(), _tool_usage()

### Community 20 - "json"
Cohesion: 0.25
Nodes (9): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), post_text(), test_ashby_parser() (+1 more)

### Community 21 - "test_people.py"
Cohesion: 0.09
Nodes (15): More people to connect with, chosen by company size, FitAssessment, Person, _on_linkedin(), source_names(), fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing() (+7 more)

### Community 22 - "notify.py"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 23 - "Settings"
Cohesion: 0.19
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Settings, answer_bank(), daily(), lead_store(), prepare_application(), rescore_open() (+4 more)

### Community 25 - "browser.py"
Cohesion: 0.13
Nodes (13): apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed(), SubmissionResult (+5 more)

### Community 26 - "test_leads.py"
Cohesion: 0.07
Nodes (28): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+20 more)

### Community 27 - "Winter 2027 Internship Agent"
Cohesion: 0.14
Nodes (10): Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does (+2 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 30 - "startups.py"
Cohesion: 0.24
Nodes (4): _fold(), names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 32 - "leads/cli.py"
Cohesion: 0.20
Nodes (6): _email_cell(), list_leads(), _resume(), is_open(), rank(), load_resume_text()

### Community 40 - "find-founders.md"
Cohesion: 0.22
Nodes (6): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, export_drafts(), import_leads(), load_inbox()

### Community 41 - "find_more_postings"
Cohesion: 0.27
Nodes (8): Big-company postings from the SimplifyJobs off-season list, find_more(), open_postings(), refill(), fetch(), find_more_postings(), scrape_jobs(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 42 - "Region"
Cohesion: 0.13
Nodes (11): Region, _identity(), normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching() (+3 more)

### Community 43 - "get_settings"
Cohesion: 0.18
Nodes (6): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd()

### Community 44 - "Dashboard page (index.html)"
Cohesion: 0.24
Nodes (8): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Send email safeguards, Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, Notes box that saves notes and learns rules, 'More people to connect with' section

### Community 45 - "followups_cmd"
Cohesion: 0.27
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 46 - "test_answers.py"
Cohesion: 0.27
Nodes (6): q(), test_category(), test_greenhouse_parser(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind(), test_yes_no_answer_matches_long_select_options()

### Community 47 - "README.md"
Cohesion: 0.42
Nodes (8): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points), Rules learned from notes (skip, downrank, boost), Application answers section

### Community 49 - "send_email"
Cohesion: 0.18
Nodes (7): send(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, send_email(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 51 - "search_startups"
Cohesion: 0.33
Nodes (3): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups()

### Community 53 - "ApplicationPrep"
Cohesion: 0.40
Nodes (4): ApplicationPrep, _retryable_block(), test_campaign_stops_after_target_confirmed_submissions(), prepare()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 276 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `command`, `typing`, `answers.py`, `ai.py`, `run_followups`, `test_followups.py`, `app.py`, `test_dashboard.py`, `test_application_browser.py`, `test_outreach.py`, `x_search.py`, `notify.py`, `Settings`, `browser.py`, `test_leads.py`, `followups.py`, `test_scrape_stores_every_matching_non_workday_posting`, `startups.py`, `leads/cli.py`, `find-founders.md`, `find_more_postings`, `Region`, `test_answers.py`, `send_email`, `ApplicationPrep`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.1164021164021164 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `command`, `ai.py`, `Lead`, `run_followups`, `find_more_postings`, `client.py`, `get_settings`, `internship_agent/cli.py`, `test_followups.py`, `app.py`, `test_answers.py`, `config.py`, `send_email`, `ApplicationPrep`, `test_people.py`, `test_scrape_stores_every_matching_non_workday_posting`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `ai.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07322068612391193 - nodes in this community are weakly interconnected._