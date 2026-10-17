# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 75 files · ~179,649 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1002 nodes · 2894 edges · 52 communities (43 shown, 9 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 500 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5a08aacf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Winter 2027 Internship Agent
- get_settings
- simplify.py
- app.py
- Settings
- leads/schemas.py
- browser.py
- assess_fit
- answers.py
- run_followups
- client.py
- internship_agent/cli.py
- Region
- make_workflows.py
- verification_mail.py
- leads/cli.py
- test_application_browser.py
- FakeField
- startups.py
- people.py
- test_dashboard.py
- notify.py
- re
- Segment
- run-application-campaign-2026-10-16.sh
- FormQuestion
- test_leads.py
- find-internships.md
- mailer.py
- Lead
- store.py
- README.md
- sending.py
- test_refill.py
- typing
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- rank
- find-founders.md
- LeadStatus
- guess_email
- followups_cmd
- test_notes.py
- AGENTS.md
- candidate_context.md
- ai.py
- LeadStore
- test_hidden_recaptcha_support_nodes_do_not_block

## God Nodes (most connected - your core abstractions)
1. `Lead` - 109 edges
2. `Settings` - 61 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 27 edges
8. `Region` - 25 edges
9. `FormQuestion` - 25 edges
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

## Communities (52 total, 9 thin omitted)

### Community 0 - "Winter 2027 Internship Agent"
Cohesion: 0.14
Nodes (10): Current setup, Dashboard, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does (+2 more)

### Community 1 - "get_settings"
Cohesion: 0.20
Nodes (7): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd()

### Community 2 - "simplify.py"
Cohesion: 0.11
Nodes (9): region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting, _TableParser (+1 more)

### Community 3 - "app.py"
Cohesion: 0.10
Nodes (32): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest (+24 more)

### Community 4 - "Settings"
Cohesion: 0.11
Nodes (19): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Settings, answer_bank(), find_people(), find_startups(), handle_note(), lead_store() (+11 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.16
Nodes (7): EmailStatus, LeadKind, Round, Verdict, effective_segment(), parse_round(), test_parse_round()

### Community 6 - "browser.py"
Cohesion: 0.12
Nodes (13): apply_to_posting(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _save_submission_diagnostic(), SubmissionResult (+5 more)

### Community 7 - "assess_fit"
Cohesion: 0.31
Nodes (7): assess_fit(), draft_outreach(), format_preferences(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter()

### Community 8 - "answers.py"
Cohesion: 0.15
Nodes (15): category(), common_questions(), match_option(), normalize(), validate(), QuestionKind, q(), test_ashby_parser() (+7 more)

### Community 9 - "run_followups"
Cohesion: 0.05
Nodes (37): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+29 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (36): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), run(), connect(), OutlookClient, OutlookError (+28 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "Region"
Cohesion: 0.13
Nodes (11): search_startups(), StartupFinding, Region, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "verification_mail.py"
Cohesion: 0.09
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 15 - "leads/cli.py"
Cohesion: 0.20
Nodes (9): _draft(), draft_all(), draft_lead(), _openai(), _resume(), score_leads(), show_lead(), _store() (+1 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.22
Nodes (14): _fill_form(), _numeric_answer(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+6 more)

### Community 17 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 18 - "startups.py"
Cohesion: 0.22
Nodes (4): _fold(), mentions(), names(), source_confirms()

### Community 19 - "people.py"
Cohesion: 0.18
Nodes (9): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, _on_linkedin(), source_names(), to_people(), page_names() (+1 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "notify.py"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 22 - "re"
Cohesion: 0.08
Nodes (25): fit_to_limit(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _ashby(), fetch_posting_text() (+17 more)

### Community 23 - "Segment"
Cohesion: 0.21
Nodes (11): Segment, to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+3 more)

### Community 25 - "FormQuestion"
Cohesion: 0.24
Nodes (6): _answer_for(), AnswerBank, prefill(), FormQuestion, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 26 - "test_leads.py"
Cohesion: 0.27
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 27 - "find-internships.md"
Cohesion: 0.17
Nodes (7): Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, export_drafts(), _email_line(), render_outreach()

### Community 28 - "mailer.py"
Cohesion: 0.23
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 29 - "Lead"
Cohesion: 0.13
Nodes (15): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, fetch(), daily(), DailyReport (+7 more)

### Community 30 - "store.py"
Cohesion: 0.18
Nodes (7): _slug(), _identity(), load_inbox(), merge(), normalize_url(), test_merge_keeps_existing_and_dedupes_incoming(), test_normalize_url_keeps_meaningful_query()

### Community 31 - "README.md"
Cohesion: 0.15
Nodes (21): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points) (+13 more)

### Community 32 - "sending.py"
Cohesion: 0.24
Nodes (3): check_outreach_text(), check_send(), SendBlocked

### Community 33 - "test_refill.py"
Cohesion: 0.18
Nodes (5): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 34 - "typing"
Cohesion: 0.18
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 41 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 42 - "find-founders.md"
Cohesion: 0.22
Nodes (6): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), mark_lead()

### Community 43 - "LeadStatus"
Cohesion: 0.20
Nodes (11): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, score() (+3 more)

### Community 44 - "guess_email"
Cohesion: 0.22
Nodes (5): Output, Output, _clean(), guess_email(), test_guess_email()

### Community 45 - "followups_cmd"
Cohesion: 0.25
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 46 - "test_notes.py"
Cohesion: 0.29
Nodes (6): posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns(), test_html_to_text_drops_scripts_and_tags()

### Community 48 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 49 - "ai.py"
Cohesion: 0.18
Nodes (10): AnswerDraft, AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PreferenceDraft, StartupFindings, FitResult (+2 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 312 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `simplify.py`, `app.py`, `Settings`, `leads/schemas.py`, `browser.py`, `assess_fit`, `answers.py`, `run_followups`, `leads/cli.py`, `test_application_browser.py`, `startups.py`, `people.py`, `test_dashboard.py`, `notify.py`, `re`, `Segment`, `FormQuestion`, `test_leads.py`, `find-internships.md`, `store.py`, `README.md`, `sending.py`, `test_refill.py`, `test_daily_campaign.py`, `rank`, `find-founders.md`, `LeadStatus`, `test_notes.py`, `ai.py`, `LeadStore`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Winter 2027 Internship Agent` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `typing`, `app.py`, `answers.py`, `run_followups`, `client.py`, `internship_agent/cli.py`, `LeadStatus`, `test_daily_campaign.py`, `test_notes.py`, `leads/cli.py`, `FormQuestion`, `Lead`, `README.md`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11076923076923077 - nodes in this community are weakly interconnected._