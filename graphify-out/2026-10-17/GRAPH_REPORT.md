# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 75 files · ~191,676 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1010 nodes · 2910 edges · 53 communities (40 shown, 13 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 506 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1ab0d0f9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_followups.py
- get_settings
- simplify.py
- app.py
- Settings
- leads/schemas.py
- browser.py
- Lead
- GmailMailbox
- run_followups
- client.py
- internship_agent/cli.py
- Region
- make_workflows.py
- mailer.py
- leads/cli.py
- test_application_browser.py
- FakeField
- startups.py
- find_startups
- test_dashboard.py
- mailbox.py
- re
- test_outreach.py
- run-application-campaign-2026-10-16.sh
- AnswerBank
- test_leads.py
- find-founders.md
- startup_jobs.py
- find_more_postings
- followups.py
- workflows.py
- fit_to_limit
- pathlib
- test_ai.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- rank
- test_people.py
- test_notes.py
- SentMessage
- followups_cmd
- daily
- AGENTS.md
- candidate_context.md
- ai.py
- Bot Auto application preview
- test_hidden_recaptcha_support_nodes_do_not_block
- _numeric_answer

## God Nodes (most connected - your core abstractions)
1. `Lead` - 110 edges
2. `Settings` - 62 edges
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

## Communities (53 total, 13 thin omitted)

### Community 0 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 1 - "get_settings"
Cohesion: 0.20
Nodes (7): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd(), show_lead()

### Community 2 - "simplify.py"
Cohesion: 0.06
Nodes (16): normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+8 more)

### Community 3 - "app.py"
Cohesion: 0.05
Nodes (63): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+55 more)

### Community 4 - "Settings"
Cohesion: 0.14
Nodes (14): Settings, common_questions(), answer_bank(), lead_store(), prepare_application(), _record_openai_usage(), refresh_saved_application(), resume_text() (+6 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.24
Nodes (5): LeadKind, Round, Verdict, parse_round(), test_parse_round()

### Community 6 - "browser.py"
Cohesion: 0.11
Nodes (16): apply_to_posting(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _post_submit_outcome(), _posting_is_closed(), _save_submission_diagnostic() (+8 more)

### Community 7 - "Lead"
Cohesion: 0.27
Nodes (7): assess_fit(), format_preferences(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter(), Lead

### Community 8 - "GmailMailbox"
Cohesion: 0.22
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 9 - "run_followups"
Cohesion: 0.10
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "Region"
Cohesion: 0.13
Nodes (9): Region, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "mailer.py"
Cohesion: 0.10
Nodes (9): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox() (+1 more)

### Community 15 - "leads/cli.py"
Cohesion: 0.19
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.25
Nodes (12): _fill_form(), FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability(), test_fill_form_selects_saved_year_from_lever_radio_group() (+4 more)

### Community 17 - "FakeField"
Cohesion: 0.12
Nodes (4): FakeField, FakeLocator, test_three_live_checks_before_submit(), locator()

### Community 18 - "startups.py"
Cohesion: 0.15
Nodes (7): _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 19 - "find_startups"
Cohesion: 0.19
Nodes (9): More people to connect with, chosen by company size, search_people(), Person, Segment, effective_segment(), to_people(), find_startups(), people_at() (+1 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "mailbox.py"
Cohesion: 0.20
Nodes (4): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code()

### Community 22 - "re"
Cohesion: 0.06
Nodes (45): category(), match_option(), normalize(), validate(), _clean(), FormQuestion, PreparedAnswer, QuestionKind (+37 more)

### Community 23 - "test_outreach.py"
Cohesion: 0.21
Nodes (9): to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_regions_of(), test_to_leads_filters_age_stage_and_unverifiable_sources() (+1 more)

### Community 25 - "AnswerBank"
Cohesion: 0.22
Nodes (5): _answer_for(), AnswerBank, prefill(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 26 - "test_leads.py"
Cohesion: 0.10
Nodes (24): _email_line(), render_outreach(), _slug(), _identity(), LeadStore, merge(), test_post_submit_state_is_persisted_for_tracker(), fit() (+16 more)

### Community 27 - "find-founders.md"
Cohesion: 0.11
Nodes (13): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+5 more)

### Community 28 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 29 - "find_more_postings"
Cohesion: 0.19
Nodes (9): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), fetch(), find_more_postings(), scrape_jobs(), startup_postings() (+1 more)

### Community 30 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 31 - "workflows.py"
Cohesion: 0.17
Nodes (12): Rules learned from notes (skip, downrank, boost), apply_violations(), LeadStatus, Note, Preference, find_people(), handle_note(), NoteOutcome (+4 more)

### Community 34 - "test_ai.py"
Cohesion: 0.27
Nodes (6): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 42 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 43 - "test_notes.py"
Cohesion: 0.17
Nodes (14): NoteResult, PreferenceDraft, _normalize(), PreferenceStore, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads() (+6 more)

### Community 45 - "followups_cmd"
Cohesion: 0.25
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 46 - "daily"
Cohesion: 0.25
Nodes (4): daily(), DailyReport, _incompatible_term(), _run_ai_cost()

### Community 48 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 49 - "ai.py"
Cohesion: 0.17
Nodes (11): AnswerDraft, AnswerDrafts, CoverLetterDraft, draft_outreach(), PeopleFindings, PersonFinding, search_startups(), StartupFinding (+3 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 316 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_followups.py`, `simplify.py`, `app.py`, `Settings`, `leads/schemas.py`, `browser.py`, `run_followups`, `leads/cli.py`, `test_application_browser.py`, `startups.py`, `find_startups`, `test_dashboard.py`, `re`, `test_outreach.py`, `AnswerBank`, `test_leads.py`, `find-founders.md`, `find_more_postings`, `followups.py`, `workflows.py`, `fit_to_limit`, `test_daily_campaign.py`, `rank`, `test_notes.py`, `daily`, `ai.py`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06387921022067364 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_followups.py`, `pathlib`, `get_settings`, `test_daily_campaign.py`, `run_followups`, `client.py`, `internship_agent/cli.py`, `test_notes.py`, `make_workflows.py`, `daily`, `leads/cli.py`, `test_people.py`, `find_startups`, `re`, `AnswerBank`, `test_leads.py`, `find_more_postings`, `workflows.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0522466039707419 - nodes in this community are weakly interconnected._