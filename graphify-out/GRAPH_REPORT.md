# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~88,181 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 896 nodes · 2607 edges · 50 communities (41 shown, 9 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 437 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8aaa1a5e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- leads/cli.py
- Lead
- startup_jobs.py
- json
- test_notes.py
- Settings
- run_followups
- mailer.py
- test_followups.py
- test_application_browser.py
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
- README.md
- client.py
- re
- browser.py
- test_leads.py
- store.py
- followups.py
- Dashboard page (index.html)
- people.py
- candidate_context.md
- get_settings
- SentMessage
- test_ai.py
- assess_fit
- internship-agent
- export_drafts
- BaseModel
- test_people.py
- _TableParser
- local_only
- LeadStatus
- AGENTS.md
- rank
- find-founders.md
- pathlib

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

## Communities (50 total, 9 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.06
Nodes (33): FindStartupsRequest, fit_to_limit(), EmailStatus, Region, Round, Segment, Verdict, parse_round() (+25 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.31
Nodes (8): _draft(), draft_all(), draft_lead(), _openai(), _resume(), score_leads(), show_lead(), _store()

### Community 2 - "Lead"
Cohesion: 0.13
Nodes (16): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, LeadKind, merge(), fetch() (+8 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "json"
Cohesion: 0.20
Nodes (15): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q() (+7 more)

### Community 5 - "test_notes.py"
Cohesion: 0.15
Nodes (14): apply_violations(), _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads() (+6 more)

### Community 6 - "Settings"
Cohesion: 0.14
Nodes (14): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Settings, draft(), common_questions(), ApplicationPrep, answer_bank(), lead_store() (+6 more)

### Community 7 - "run_followups"
Cohesion: 0.11
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "test_application_browser.py"
Cohesion: 0.15
Nodes (9): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+1 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "app.py"
Cohesion: 0.11
Nodes (28): AnswerEdit, daily_run(), delete_preference(), find_more(), find_more_startups(), FindMoreRequest, followups(), FollowupsRequest (+20 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "workflows.py"
Cohesion: 0.12
Nodes (12): search_people(), effective_segment(), check_outreach_text(), to_people(), find_people(), find_startups(), people_at(), handle_note() (+4 more)

### Community 17 - "ai.py"
Cohesion: 0.27
Nodes (8): AnswerDraft, AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PersonFinding, PreferenceDraft, prepare_answers()

### Community 18 - "notify.py"
Cohesion: 0.19
Nodes (15): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+7 more)

### Community 19 - "x_search.py"
Cohesion: 0.15
Nodes (7): search_startups(), StartupFinding, StartupFindings, post_id(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 20 - "answers.py"
Cohesion: 0.19
Nodes (5): AnswerBank, match_option(), normalize(), prefill(), validate()

### Community 21 - "find-internships.md"
Cohesion: 0.29
Nodes (4): Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look

### Community 22 - "README.md"
Cohesion: 0.14
Nodes (21): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Dashboard (+13 more)

### Community 23 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 24 - "re"
Cohesion: 0.29
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 25 - "browser.py"
Cohesion: 0.13
Nodes (14): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed() (+6 more)

### Community 26 - "test_leads.py"
Cohesion: 0.09
Nodes (24): Output, Output, _clean(), guess_email(), _email_line(), render_outreach(), LeadStore, fit() (+16 more)

### Community 27 - "store.py"
Cohesion: 0.12
Nodes (9): _slug(), _identity(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+1 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "Dashboard page (index.html)"
Cohesion: 0.24
Nodes (8): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Send email safeguards, index(), Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 30 - "people.py"
Cohesion: 0.18
Nodes (6): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 32 - "get_settings"
Cohesion: 0.23
Nodes (6): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd()

### Community 34 - "test_ai.py"
Cohesion: 0.39
Nodes (4): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_draft_prompt_leads_with_upside_impact()

### Community 36 - "assess_fit"
Cohesion: 0.27
Nodes (8): assess_fit(), draft_outreach(), format_preferences(), interpret_note(), _lead_context(), prepare_cover_letter(), FitResult, test_assess_fit_sends_resume_and_lead_and_validates()

### Community 39 - "export_drafts"
Cohesion: 0.21
Nodes (4): apply_cmd(), export_drafts(), find_startups_cmd(), followups_cmd()

### Community 40 - "BaseModel"
Cohesion: 0.18
Nodes (3): FitAssessment, OutreachDraft, OutreachDraftResult

### Community 41 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 44 - "LeadStatus"
Cohesion: 0.67
Nodes (3): set_status(), StatusUpdate, LeadStatus

### Community 46 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 47 - "find-founders.md"
Cohesion: 0.22
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), mark_lead(), load_inbox()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 263 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `leads/cli.py`, `json`, `test_notes.py`, `Settings`, `run_followups`, `test_followups.py`, `test_application_browser.py`, `app.py`, `test_dashboard.py`, `workflows.py`, `ai.py`, `notify.py`, `find-internships.md`, `browser.py`, `test_leads.py`, `store.py`, `followups.py`, `assess_fit`, `BaseModel`, `LeadStatus`, `rank`, `find-founders.md`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/schemas.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05754527162977867 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `leads/cli.py`, `Lead`, `json`, `test_notes.py`, `run_followups`, `test_followups.py`, `test_people.py`, `internship_agent/cli.py`, `app.py`, `pathlib`, `workflows.py`, `client.py`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `Lead` be split into smaller, more focused modules?**
  _Cohesion score 0.13054187192118227 - nodes in this community are weakly interconnected._