# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 74 files · ~90,633 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 976 nodes · 2817 edges · 57 communities (45 shown, 12 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 496 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fb0aabed`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- leads/cli.py
- Region
- startup_jobs.py
- FormQuestion
- LeadStatus
- find_startups
- app.py
- Winter 2027 Internship Agent
- test_followups.py
- tracking.py
- internship_agent/cli.py
- typing
- make_workflows.py
- ai.py
- workflows.py
- test_application_browser.py
- Segment
- candidate_context.md
- x_search.py
- test_dashboard.py
- FitAssessment
- answers.py
- leads/schemas.py
- run-application-campaign-2026-10-16.sh
- json
- test_leads.py
- _view
- run_followups
- RunBudget
- BaseModel
- _TableParser
- browser.py
- test_ai.py
- test_people.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- startups.py
- re
- Lead
- test_x_search.py
- fit_to_limit
- client.py
- OutlookClient
- test_outlook_client.py
- followups.py
- send_email
- AGENTS.md
- outlook/schemas.py
- Mailbox
- SentMessage
- test_daily_campaign.py
- apply_to_posting
- test_hidden_recaptcha_support_nodes_do_not_block

## God Nodes (most connected - your core abstractions)
1. `Lead` - 108 edges
2. `Settings` - 58 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 27 edges
8. `Region` - 25 edges
9. `Segment` - 24 edges
10. `LeadKind` - 23 edges

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

## Communities (57 total, 12 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.18
Nodes (19): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+11 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.05
Nodes (40): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+32 more)

### Community 2 - "Region"
Cohesion: 0.13
Nodes (14): Big-company postings from the SimplifyJobs off-season list, refill(), Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role() (+6 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "FormQuestion"
Cohesion: 0.19
Nodes (16): category(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+8 more)

### Community 5 - "LeadStatus"
Cohesion: 0.16
Nodes (14): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, PreferenceEffect, posting(), settings() (+6 more)

### Community 6 - "find_startups"
Cohesion: 0.14
Nodes (12): More people to connect with, chosen by company size, search_people(), LeadKind, Person, effective_segment(), to_people(), find_people(), find_startups() (+4 more)

### Community 7 - "app.py"
Cohesion: 0.14
Nodes (17): AnswerEdit, delete_preference(), followups(), FollowupsRequest, _get(), index(), leads(), note() (+9 more)

### Community 8 - "Winter 2027 Internship Agent"
Cohesion: 0.12
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP) (+4 more)

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "typing"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "ai.py"
Cohesion: 0.17
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 15 - "workflows.py"
Cohesion: 0.12
Nodes (19): Settings, common_questions(), ApplicationPrep, answer_bank(), daily(), DailyReport, _incompatible_term(), lead_store() (+11 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.12
Nodes (13): _fill_form(), FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_selects_saved_year_from_lever_radio_group() (+5 more)

### Community 17 - "Segment"
Cohesion: 0.18
Nodes (12): Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+4 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.22
Nodes (5): StartupFinding, StartupFindings, _slug(), search_x_raises(), _tool_usage()

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "FitAssessment"
Cohesion: 0.22
Nodes (7): FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_caps_new_preparations(), load(), score_new()

### Community 22 - "answers.py"
Cohesion: 0.14
Nodes (9): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options(), test_answer_mapping_uses_saved_answer_for_live_form_fields() (+1 more)

### Community 23 - "leads/schemas.py"
Cohesion: 0.20
Nodes (6): _email_line(), render_outreach(), EmailStatus, Round, Verdict, check_send()

### Community 25 - "json"
Cohesion: 0.18
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 26 - "test_leads.py"
Cohesion: 0.15
Nodes (18): LeadStore, fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input() (+10 more)

### Community 27 - "_view"
Cohesion: 0.16
Nodes (14): daily_run(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest, KeyRequest, people() (+6 more)

### Community 28 - "run_followups"
Cohesion: 0.15
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 29 - "RunBudget"
Cohesion: 0.14
Nodes (6): BudgetExhausted, RunBudget, FakeCounter, Result, test_budget_fails_closed_for_another_model(), test_budget_stops_before_request_that_exceeds_fifty_cents()

### Community 30 - "BaseModel"
Cohesion: 0.29
Nodes (3): FitResult, OutreachDraft, OutreachDraftResult

### Community 32 - "browser.py"
Cohesion: 0.13
Nodes (10): _field_label(), _normalize(), _numeric_answer(), _online_checks(), _posting_is_closed(), SubmissionResult, _visible_captcha(), test_closed_posting_text_is_detected() (+2 more)

### Community 33 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 40 - "startups.py"
Cohesion: 0.12
Nodes (9): _clean(), _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms() (+1 more)

### Community 41 - "re"
Cohesion: 0.26
Nodes (10): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+2 more)

### Community 42 - "Lead"
Cohesion: 0.10
Nodes (13): open_postings(), Lead, _identity(), merge(), normalize_url(), test_saving_answers_preserves_uncertain_submission(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 43 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 45 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 46 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 47 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 48 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 49 - "send_email"
Cohesion: 0.11
Nodes (10): send(), SendRequest, check_outreach_text(), SendBlocked, build_message(), MailError, send(), send_email() (+2 more)

### Community 51 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 54 - "test_daily_campaign.py"
Cohesion: 0.25
Nodes (4): test_incompatible_eight_month_term_is_rejected(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_scrape_stores_every_matching_non_workday_posting(), test_usage_log_contains_counts_without_prompt_content()

### Community 55 - "apply_to_posting"
Cohesion: 0.40
Nodes (3): apply_to_posting(), _supported_url(), is_workday()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 302 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/cli.py`, `Region`, `FormQuestion`, `LeadStatus`, `find_startups`, `app.py`, `test_followups.py`, `ai.py`, `workflows.py`, `test_application_browser.py`, `Segment`, `x_search.py`, `test_dashboard.py`, `FitAssessment`, `answers.py`, `leads/schemas.py`, `json`, `test_leads.py`, `_view`, `run_followups`, `BaseModel`, `browser.py`, `startups.py`, `fit_to_limit`, `followups.py`, `send_email`, `test_daily_campaign.py`, `apply_to_posting`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Are the 77 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 77 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05284810126582278 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `leads/cli.py`, `Region`, `test_people.py`, `FormQuestion`, `LeadStatus`, `find_startups`, `app.py`, `Winter 2027 Internship Agent`, `test_followups.py`, `Lead`, `internship_agent/cli.py`, `client.py`, `send_email`, `FitAssessment`, `answers.py`, `test_daily_campaign.py`, `run_followups`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 49 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 49 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.13054187192118227 - nodes in this community are weakly interconnected._