# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~162,869 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 968 nodes · 2813 edges · 42 communities (34 shown, 8 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 493 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8ee691b2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- leads/cli.py
- simplify.py
- _view
- prepare_application
- test_refill.py
- test_application_browser.py
- ai.py
- app.py
- Settings
- tracking.py
- internship_agent/cli.py
- Region
- make_workflows.py
- send_email
- test_ai.py
- client.py
- mailer.py
- workflows.py
- find_startups
- test_dashboard.py
- OutlookClient
- FormQuestion
- leads/schemas.py
- run-application-campaign-2026-10-16.sh
- test_notes.py
- Lead
- test_outlook_client.py
- outlook/schemas.py
- test_people.py
- AGENTS.md
- mailbox.py
- candidate_context.md
- re
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- LeadStatus
- _TableParser
- BaseModel

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

## Communities (42 total, 8 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.11
Nodes (27): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+19 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (38): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+30 more)

### Community 2 - "simplify.py"
Cohesion: 0.11
Nodes (14): Big-company postings from the SimplifyJobs off-season list, normalize_url(), region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+6 more)

### Community 3 - "_view"
Cohesion: 0.18
Nodes (18): daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, leads() (+10 more)

### Community 4 - "prepare_application"
Cohesion: 0.13
Nodes (15): answer_bank(), daily(), handle_note(), _incompatible_term(), lead_store(), _openai(), preference_store(), prepare_application() (+7 more)

### Community 5 - "test_refill.py"
Cohesion: 0.13
Nodes (9): is_workday(), refill(), merge(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped() (+1 more)

### Community 6 - "test_application_browser.py"
Cohesion: 0.06
Nodes (36): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+28 more)

### Community 7 - "ai.py"
Cohesion: 0.19
Nodes (13): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+5 more)

### Community 8 - "app.py"
Cohesion: 0.18
Nodes (12): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, NoteRequest, PreferenceDelete, SaveAnswersRequest (+4 more)

### Community 9 - "Settings"
Cohesion: 0.05
Nodes (37): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+29 more)

### Community 10 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "Region"
Cohesion: 0.12
Nodes (12): search_startups(), StartupFinding, Region, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "send_email"
Cohesion: 0.20
Nodes (6): Send email safeguards, send(), check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 15 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 16 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 17 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 18 - "workflows.py"
Cohesion: 0.13
Nodes (9): Search for recently funded startups (last 60 days; Canada, USA, Europe), _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms() (+1 more)

### Community 19 - "find_startups"
Cohesion: 0.16
Nodes (10): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, to_people(), find_people(), find_startups(), people_at() (+2 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 22 - "FormQuestion"
Cohesion: 0.07
Nodes (38): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+30 more)

### Community 23 - "leads/schemas.py"
Cohesion: 0.15
Nodes (15): LeadKind, Round, Segment, Verdict, effective_segment(), parse_round(), to_leads(), finding() (+7 more)

### Community 25 - "test_notes.py"
Cohesion: 0.26
Nodes (8): NoteResult, PreferenceDraft, posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns(), test_html_to_text_drops_scripts_and_tags()

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (37): _email_line(), render_outreach(), ApplicationPrep, EmailStatus, FitAssessment, Lead, _identity(), LeadStore (+29 more)

### Community 27 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 28 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 29 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 33 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 34 - "re"
Cohesion: 0.11
Nodes (21): _clean(), fit_to_limit(), _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text() (+13 more)

### Community 43 - "LeadStatus"
Cohesion: 0.21
Nodes (11): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, NoteOutcome (+3 more)

### Community 47 - "BaseModel"
Cohesion: 0.33
Nodes (3): FitResult, OutreachDraft, test_linkedin_note_never_exceeds_200_chars()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 298 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/cli.py`, `simplify.py`, `_view`, `prepare_application`, `test_refill.py`, `test_application_browser.py`, `ai.py`, `app.py`, `Settings`, `LeadStatus`, `send_email`, `BaseModel`, `workflows.py`, `find_startups`, `test_dashboard.py`, `FormQuestion`, `leads/schemas.py`, `test_notes.py`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.11375661375661375 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `simplify.py`, `prepare_application`, `internship_agent/cli.py`, `make_workflows.py`, `send_email`, `client.py`, `workflows.py`, `find_startups`, `FormQuestion`, `test_notes.py`, `Lead`, `test_people.py`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05649122807017544 - nodes in this community are weakly interconnected._