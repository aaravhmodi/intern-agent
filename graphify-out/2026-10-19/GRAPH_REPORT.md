# Graph Report - winter-2027-internship-agent  (2026-10-19)

## Corpus Check
- 78 files · ~195,962 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1085 nodes · 3141 edges · 53 communities (37 shown, 16 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 539 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9b9d83b3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_refill.py
- daily
- simplify.py
- ai.py
- Settings
- app.py
- browser.py
- FakeField
- command
- re
- test_leads.py
- internship_agent/cli.py
- json
- make_workflows.py
- notify.py
- FormQuestion
- get_settings
- tracking.py
- verification_mail.py
- find_more_postings
- run_followups
- OutlookClient
- client.py
- find_startups
- run-application-campaign-2026-10-16.sh
- Lead
- x_search.py
- workflows.py
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
- load_resume_text
- local_only
- ToolSession
- _numeric_answer
- Segment
- _react_select_answer
- Bot Auto application preview
- test_interview_events
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 116 edges
2. `Settings` - 63 edges
3. `get_settings()` - 48 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (53 total, 16 thin omitted)

### Community 0 - "test_refill.py"
Cohesion: 0.16
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 1 - "daily"
Cohesion: 0.29
Nodes (4): daily_cmd(), daily(), DailyReport, _incompatible_term()

### Community 2 - "simplify.py"
Cohesion: 0.11
Nodes (10): normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+2 more)

### Community 3 - "ai.py"
Cohesion: 0.06
Nodes (43): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+35 more)

### Community 4 - "Settings"
Cohesion: 0.11
Nodes (18): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Settings, prepare_all_cmd(), prepare_cmd(), answer_bank(), lead_store(), prepare_application() (+10 more)

### Community 5 - "app.py"
Cohesion: 0.15
Nodes (14): AnswerEdit, delete_preference(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, leads(), note() (+6 more)

### Community 6 - "browser.py"
Cohesion: 0.10
Nodes (20): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome() (+12 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 8 - "command"
Cohesion: 0.06
Nodes (29): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+21 more)

### Community 9 - "re"
Cohesion: 0.10
Nodes (21): _clean(), LeadKind, _slug(), candidate_domains(), _check(), company_name(), _description(), _fetch() (+13 more)

### Community 10 - "test_leads.py"
Cohesion: 0.08
Nodes (32): dashboard(), LeadStore, client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+24 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+3 more)

### Community 12 - "json"
Cohesion: 0.08
Nodes (33): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _ashby(), fetch_posting_text() (+25 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "notify.py"
Cohesion: 0.16
Nodes (16): category(), application_campaign(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 15 - "FormQuestion"
Cohesion: 0.16
Nodes (11): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), FormQuestion, test_yes_no_answer_matches_long_select_options() (+3 more)

### Community 16 - "get_settings"
Cohesion: 0.17
Nodes (17): get_settings(), allow_retry(), application_proof(), auto_apply(), daily_run(), draft(), find_more(), find_more_startups() (+9 more)

### Community 17 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 18 - "verification_mail.py"
Cohesion: 0.10
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 19 - "find_more_postings"
Cohesion: 0.16
Nodes (10): Big-company postings from the SimplifyJobs off-season list, find_more(), scrape_jobs_cmd(), is_workday(), open_postings(), refill(), fetch(), find_more_postings() (+2 more)

### Community 20 - "run_followups"
Cohesion: 0.05
Nodes (37): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+29 more)

### Community 21 - "OutlookClient"
Cohesion: 0.20
Nodes (8): OutlookClient, OutlookError, CalendarEvent, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 22 - "client.py"
Cohesion: 0.15
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 23 - "find_startups"
Cohesion: 0.18
Nodes (10): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups(), people_at() (+2 more)

### Community 25 - "Lead"
Cohesion: 0.16
Nodes (9): _email_cell(), _email_line(), render_outreach(), Lead, _identity(), load_inbox(), merge(), find_form_d_startups() (+1 more)

### Community 26 - "x_search.py"
Cohesion: 0.14
Nodes (8): StartupFindings, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 27 - "workflows.py"
Cohesion: 0.18
Nodes (6): common_questions(), handle_note(), NoteOutcome, preference_store(), _run_ai_cost(), post_confirms()

### Community 29 - "test_application_browser.py"
Cohesion: 0.25
Nodes (14): _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass() (+6 more)

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "startups.py"
Cohesion: 0.15
Nodes (6): parse_round(), _on_linkedin(), source_names(), names(), page_names(), source_confirms()

### Community 34 - "leads/schemas.py"
Cohesion: 0.14
Nodes (10): fit_to_limit(), EmailStatus, Region, Round, Verdict, check_outreach_text(), check_send(), SendBlocked (+2 more)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 41 - "README.md"
Cohesion: 0.11
Nodes (30): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+22 more)

### Community 43 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 48 - "Segment"
Cohesion: 0.18
Nodes (13): StartupFinding, Segment, mentions(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+5 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 52 - "send_email"
Cohesion: 0.15
Nodes (8): send(), SendRequest, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 344 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_refill.py`, `daily`, `simplify.py`, `ai.py`, `Settings`, `app.py`, `browser.py`, `command`, `re`, `test_leads.py`, `json`, `notify.py`, `FormQuestion`, `get_settings`, `find_more_postings`, `run_followups`, `find_startups`, `workflows.py`, `test_application_browser.py`, `startups.py`, `leads/schemas.py`, `test_daily_campaign.py`, `Segment`, `send_email`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 83 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 83 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1076923076923077 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `daily`, `ai.py`, `command`, `test_daily_campaign.py`, `internship_agent/cli.py`, `load_resume_text`, `json`, `FormQuestion`, `get_settings`, `find_more_postings`, `run_followups`, `send_email`, `client.py`, `find_startups`, `Lead`, `workflows.py`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `ai.py` be split into smaller, more focused modules?**
  _Cohesion score 0.057512797350195724 - nodes in this community are weakly interconnected._