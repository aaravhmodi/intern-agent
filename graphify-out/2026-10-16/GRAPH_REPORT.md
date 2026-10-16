# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~88,120 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 894 nodes · 2603 edges · 51 communities (41 shown, 10 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 436 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7a4b515e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Segment
- leads/cli.py
- startups.py
- startup_jobs.py
- json
- preferences.py
- Settings
- run_followups
- mailer.py
- test_followups.py
- pathlib
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- workflows.py
- ai.py
- notify.py
- x_search.py
- answers.py
- find-internships.md
- EmailStatus
- tracking.py
- re
- browser.py
- Lead
- OutlookClient
- followups.py
- client.py
- people.py
- candidate_context.md
- test_notes.py
- FakeMailbox
- test_ai.py
- outlook/schemas.py
- internship-agent
- export_drafts
- BaseModel
- test_people.py
- Mailbox
- test_answers.py
- AGENTS.md
- leads/schemas.py
- find-founders.md
- load_resume_text
- ToolSession
- test_interview_events

## God Nodes (most connected - your core abstractions)
1. `Lead` - 98 edges
2. `Settings` - 49 edges
3. `get_settings()` - 41 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `daily()` - 25 edges
9. `Segment` - 24 edges
10. `prepare_application()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `Segment: early, mid or big` --references--> `Segment`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Posting lead JSON appended to data/leads-inbox.json` --references--> `Lead`  [INFERRED]
  .claude/commands/find-internships.md → src/internship_agent/leads/schemas.py
- `Fit score against the resume (0-100, reasons, talking points)` --references--> `assess_fit()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Application answers prepared from the resume` --references--> `prepare_answers()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (51 total, 10 thin omitted)

### Community 0 - "Segment"
Cohesion: 0.18
Nodes (12): Segment, parse_round(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+4 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.12
Nodes (18): Founder leads flow: /find-founders, import, score, list, draft, mark, browser_login(), daily_cmd(), _draft(), draft_all(), draft_lead(), _email_cell(), find_more() (+10 more)

### Community 2 - "startups.py"
Cohesion: 0.20
Nodes (6): Region, region_from_text(), regions_of(), _fold(), mentions(), names()

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "json"
Cohesion: 0.20
Nodes (12): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+4 more)

### Community 5 - "preferences.py"
Cohesion: 0.20
Nodes (10): apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, NoteOutcome, posting(), test_apply_violations_never_touches_applied_leads() (+2 more)

### Community 6 - "Settings"
Cohesion: 0.07
Nodes (25): Big-company postings from the SimplifyJobs off-season list, Settings, normalize_url(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+17 more)

### Community 7 - "run_followups"
Cohesion: 0.15
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "pathlib"
Cohesion: 0.13
Nodes (10): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_field_label_does_not_expose_generated_lever_field_ids(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+2 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "app.py"
Cohesion: 0.06
Nodes (64): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+56 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "workflows.py"
Cohesion: 0.14
Nodes (12): More people to connect with, chosen by company size, PersonFinding, search_people(), LeadKind, Person, effective_segment(), to_people(), find_people() (+4 more)

### Community 17 - "ai.py"
Cohesion: 0.19
Nodes (13): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+5 more)

### Community 18 - "notify.py"
Cohesion: 0.21
Nodes (14): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+6 more)

### Community 19 - "x_search.py"
Cohesion: 0.14
Nodes (9): StartupFinding, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 20 - "answers.py"
Cohesion: 0.16
Nodes (8): _answer_for(), AnswerBank, category(), match_option(), normalize(), prefill(), validate(), test_answer_mapping_uses_saved_answer_for_live_form_fields()

### Community 21 - "find-internships.md"
Cohesion: 0.13
Nodes (9): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+1 more)

### Community 22 - "EmailStatus"
Cohesion: 0.22
Nodes (7): _email_line(), render_outreach(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 23 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 24 - "re"
Cohesion: 0.34
Nodes (9): _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+1 more)

### Community 25 - "browser.py"
Cohesion: 0.15
Nodes (9): apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), SubmissionResult, _supported_url() (+1 more)

### Community 26 - "Lead"
Cohesion: 0.07
Nodes (30): is_workday(), open_postings(), refill(), Lead, _identity(), LeadStore, load_inbox(), merge() (+22 more)

### Community 27 - "OutlookClient"
Cohesion: 0.19
Nodes (8): OutlookClient, OutlookError, CalendarEvent, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "client.py"
Cohesion: 0.14
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 30 - "people.py"
Cohesion: 0.15
Nodes (6): Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups(), _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 32 - "test_notes.py"
Cohesion: 0.31
Nodes (7): NoteResult, PreferenceDraft, settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns(), test_html_to_text_drops_scripts_and_tags()

### Community 34 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 36 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 39 - "export_drafts"
Cohesion: 0.28
Nodes (3): apply_cmd(), export_drafts(), find_startups_cmd()

### Community 40 - "BaseModel"
Cohesion: 0.22
Nodes (5): ApplicationPrep, FitAssessment, FitResult, Note, OutreachDraftResult

### Community 41 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 44 - "test_answers.py"
Cohesion: 0.43
Nodes (5): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind()

### Community 46 - "leads/schemas.py"
Cohesion: 0.18
Nodes (7): fit_to_limit(), is_open(), rank(), LeadStatus, Round, Verdict, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 47 - "find-founders.md"
Cohesion: 0.33
Nodes (4): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, import_leads()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 263 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `Segment`, `leads/cli.py`, `startups.py`, `preferences.py`, `Settings`, `run_followups`, `test_followups.py`, `pathlib`, `app.py`, `test_dashboard.py`, `workflows.py`, `ai.py`, `notify.py`, `answers.py`, `find-internships.md`, `EmailStatus`, `browser.py`, `followups.py`, `BaseModel`, `test_answers.py`, `leads/schemas.py`, `find-founders.md`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12121212121212122 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `test_notes.py`, `leads/cli.py`, `run_followups`, `test_followups.py`, `test_people.py`, `internship_agent/cli.py`, `test_answers.py`, `app.py`, `workflows.py`, `client.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `Settings` be split into smaller, more focused modules?**
  _Cohesion score 0.07142857142857142 - nodes in this community are weakly interconnected._