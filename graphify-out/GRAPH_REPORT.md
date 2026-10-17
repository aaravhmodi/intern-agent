# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 75 files · ~169,199 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 992 nodes · 2880 edges · 50 communities (40 shown, 10 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 499 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ee3e6589`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- get_settings
- simplify.py
- _view
- workflows.py
- leads/schemas.py
- browser.py
- ai.py
- app.py
- Settings
- client.py
- internship_agent/cli.py
- typing
- config.py
- send_email
- assess_fit
- find-founders.md
- leads/cli.py
- startups.py
- people.py
- test_dashboard.py
- notify.py
- answers.py
- test_outreach.py
- run-application-campaign-2026-10-16.sh
- test_notes.py
- test_leads.py
- Lead
- find_startups
- test_people.py
- AnswerBank
- AGENTS.md
- note
- candidate_context.md
- re
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- json
- FitAssessment
- pydantic
- LeadStore
- submit_application
- local_only
- find_more_postings
- fit_to_limit

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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (50 total, 10 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.16
Nodes (18): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Development (+10 more)

### Community 1 - "get_settings"
Cohesion: 0.14
Nodes (11): get_settings(), application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd() (+3 more)

### Community 2 - "simplify.py"
Cohesion: 0.06
Nodes (19): _identity(), merge(), normalize_url(), region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role() (+11 more)

### Community 3 - "_view"
Cohesion: 0.23
Nodes (13): daily_run(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, people(), prepare() (+5 more)

### Community 4 - "workflows.py"
Cohesion: 0.11
Nodes (18): is_workday(), open_postings(), refill(), ApplicationPrep, daily(), DailyReport, NoteOutcome, _openai() (+10 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.22
Nodes (7): is_open(), rank(), LeadKind, LeadStatus, Round, Verdict, effective_segment()

### Community 6 - "browser.py"
Cohesion: 0.06
Nodes (35): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+27 more)

### Community 7 - "ai.py"
Cohesion: 0.18
Nodes (14): AnswerDraft, AnswerDrafts, CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context(), NoteResult (+6 more)

### Community 8 - "app.py"
Cohesion: 0.12
Nodes (17): AnswerEdit, delete_preference(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, leads(), PreferenceDelete (+9 more)

### Community 9 - "Settings"
Cohesion: 0.05
Nodes (38): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+30 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (34): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+26 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+2 more)

### Community 12 - "typing"
Cohesion: 0.13
Nodes (11): StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 13 - "config.py"
Cohesion: 0.09
Nodes (12): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+4 more)

### Community 14 - "send_email"
Cohesion: 0.11
Nodes (11): send(), SendRequest, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send() (+3 more)

### Community 15 - "assess_fit"
Cohesion: 0.18
Nodes (9): assess_fit(), FitResult, OutreachDraft, OutreachDraftResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates() (+1 more)

### Community 16 - "find-founders.md"
Cohesion: 0.11
Nodes (13): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+5 more)

### Community 17 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 18 - "startups.py"
Cohesion: 0.21
Nodes (6): _fold(), mentions(), names(), page_names(), source_confirms(), test_mentions_requires_company_and_founder_ignoring_accents()

### Community 19 - "people.py"
Cohesion: 0.18
Nodes (6): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names(), to_people(), people_at()

### Community 20 - "test_dashboard.py"
Cohesion: 0.17
Nodes (11): client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill(), test_send_guess_requires_confirmation_then_records() (+3 more)

### Community 21 - "notify.py"
Cohesion: 0.19
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 22 - "answers.py"
Cohesion: 0.15
Nodes (14): category(), common_questions(), match_option(), validate(), QuestionKind, q(), test_ashby_parser(), test_category() (+6 more)

### Community 23 - "test_outreach.py"
Cohesion: 0.22
Nodes (9): parse_round(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_parse_round(), test_regions_of() (+1 more)

### Community 25 - "test_notes.py"
Cohesion: 0.29
Nodes (6): posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns(), test_html_to_text_drops_scripts_and_tags()

### Community 26 - "test_leads.py"
Cohesion: 0.23
Nodes (15): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected() (+7 more)

### Community 27 - "Lead"
Cohesion: 0.21
Nodes (5): _email_line(), render_outreach(), EmailStatus, Lead, test_render_outreach_flags_unverified_emails_and_skips_undrafted()

### Community 28 - "find_startups"
Cohesion: 0.24
Nodes (7): search_startups(), Region, Segment, to_leads(), find_startups(), _log_xai(), test_to_leads_sets_region_and_drops_bad_handle()

### Community 29 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 30 - "AnswerBank"
Cohesion: 0.22
Nodes (4): AnswerBank, normalize(), prefill(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 32 - "note"
Cohesion: 0.20
Nodes (11): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Send email safeguards, index(), note(), NoteRequest, Dashboard page (index.html), Email section with two-click send (+3 more)

### Community 33 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 34 - "re"
Cohesion: 0.08
Nodes (23): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _clean(), _slug(), _ashby(), fetch_posting_text() (+15 more)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.17
Nodes (5): test_incompatible_eight_month_term_is_rejected(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_saving_answers_preserves_uncertain_submission(), test_scrape_stores_every_matching_non_workday_posting(), test_usage_log_contains_counts_without_prompt_content()

### Community 41 - "json"
Cohesion: 0.40
Nodes (6): FormQuestion, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request()

### Community 42 - "FitAssessment"
Cohesion: 0.22
Nodes (7): FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new()

### Community 43 - "pydantic"
Cohesion: 0.21
Nodes (9): apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules() (+1 more)

### Community 45 - "submit_application"
Cohesion: 0.28
Nodes (5): answer_bank(), _incompatible_term(), submit_application(), _use_gmail_for_applications(), test_application_email_uses_configured_gmail()

### Community 46 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 47 - "find_more_postings"
Cohesion: 0.29
Nodes (5): Big-company postings from the SimplifyJobs off-season list, set_status(), StatusUpdate, Lead detail panel: fit, links, contact, actions, find_more_postings()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 304 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `simplify.py`, `_view`, `workflows.py`, `leads/schemas.py`, `browser.py`, `ai.py`, `app.py`, `Settings`, `send_email`, `assess_fit`, `find-founders.md`, `leads/cli.py`, `startups.py`, `test_dashboard.py`, `notify.py`, `answers.py`, `test_outreach.py`, `test_notes.py`, `test_leads.py`, `find_startups`, `AnswerBank`, `test_daily_campaign.py`, `FitAssessment`, `pydantic`, `LeadStore`, `submit_application`, `find_more_postings`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `get_settings` be split into smaller, more focused modules?**
  _Cohesion score 0.13768115942028986 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `workflows.py`, `app.py`, `test_daily_campaign.py`, `client.py`, `internship_agent/cli.py`, `FitAssessment`, `config.py`, `local_only`, `send_email`, `submit_application`, `leads/cli.py`, `find_more_postings`, `answers.py`, `test_notes.py`, `find_startups`, `test_people.py`, `AnswerBank`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.060129509713228495 - nodes in this community are weakly interconnected._