# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~87,953 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 891 nodes · 2597 edges · 44 communities (37 shown, 7 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 435 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `56724402`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Segment
- leads/cli.py
- startups.py
- typing
- json
- LeadStatus
- Region
- run_followups
- mailer.py
- test_followups.py
- test_application_browser.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- get_settings
- test_dashboard.py
- workflows.py
- ai.py
- notify.py
- x_search.py
- answers.py
- app.py
- send_email
- tracking.py
- re
- browser.py
- Lead
- OutlookClient
- followups.py
- client.py
- test_outlook_client.py
- candidate_context.md
- note
- FakeMailbox
- test_x_search.py
- outlook/schemas.py
- internship-agent
- local_only
- README.md
- _TableParser
- leads/schemas.py

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
- `Fit score against the resume (0-100, reasons, talking points)` --references--> `assess_fit()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Search for recently funded startups (last 60 days; Canada, USA, Europe)` --references--> `search_startups()`  [INFERRED]
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

## Communities (44 total, 7 thin omitted)

### Community 0 - "Segment"
Cohesion: 0.14
Nodes (17): LeadKind, Round, Segment, Verdict, effective_segment(), parse_round(), to_leads(), finding() (+9 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.05
Nodes (43): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, Settings, apply_cmd(), browser_login(), daily_cmd() (+35 more)

### Community 2 - "startups.py"
Cohesion: 0.19
Nodes (7): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 3 - "typing"
Cohesion: 0.11
Nodes (14): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+6 more)

### Community 4 - "json"
Cohesion: 0.15
Nodes (15): QuestionKind, load_inbox(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q() (+7 more)

### Community 5 - "LeadStatus"
Cohesion: 0.15
Nodes (16): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 6 - "Region"
Cohesion: 0.13
Nodes (11): Region, normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse() (+3 more)

### Community 7 - "run_followups"
Cohesion: 0.12
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "test_application_browser.py"
Cohesion: 0.14
Nodes (10): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+2 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "get_settings"
Cohesion: 0.23
Nodes (16): get_settings(), daily_run(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, leads() (+8 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "workflows.py"
Cohesion: 0.18
Nodes (7): is_workday(), open_postings(), refill(), ApplicationPrep, merge(), _log_xai(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 17 - "ai.py"
Cohesion: 0.05
Nodes (37): Internship agent coding instructions, More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences() (+29 more)

### Community 18 - "notify.py"
Cohesion: 0.21
Nodes (14): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+6 more)

### Community 19 - "x_search.py"
Cohesion: 0.17
Nodes (5): search_startups(), StartupFinding, post_confirms(), search_x_raises(), _tool_usage()

### Community 20 - "answers.py"
Cohesion: 0.16
Nodes (8): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion

### Community 21 - "app.py"
Cohesion: 0.16
Nodes (12): AnswerEdit, delete_preference(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, PreferenceDelete, SaveAnswersRequest (+4 more)

### Community 22 - "send_email"
Cohesion: 0.16
Nodes (8): Send email safeguards, send(), SendRequest, Email section with two-click send, check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 23 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 24 - "re"
Cohesion: 0.26
Nodes (10): _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+2 more)

### Community 25 - "browser.py"
Cohesion: 0.19
Nodes (9): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), open_login_browser(), SubmissionResult, _supported_url() (+1 more)

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (35): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+27 more)

### Community 27 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 30 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 32 - "note"
Cohesion: 0.25
Nodes (8): index(), note(), NoteRequest, Dashboard page (index.html), Lead detail panel: fit, links, contact, actions, linkedinUrl(): profile URL, else a LinkedIn people search, Notes box that saves notes and learns rules, 'More people to connect with' section

### Community 34 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 36 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 39 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 40 - "README.md"
Cohesion: 0.15
Nodes (19): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Big-company postings from the SimplifyJobs off-season list, Current setup (+11 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 262 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `Segment`, `leads/cli.py`, `startups.py`, `typing`, `json`, `LeadStatus`, `Region`, `run_followups`, `test_followups.py`, `test_application_browser.py`, `get_settings`, `test_dashboard.py`, `workflows.py`, `ai.py`, `notify.py`, `app.py`, `send_email`, `browser.py`, `followups.py`, `leads/schemas.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Segment` be split into smaller, more focused modules?**
  _Cohesion score 0.1396011396011396 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `leads/cli.py` to `json`, `LeadStatus`, `local_only`, `run_followups`, `test_followups.py`, `internship_agent/cli.py`, `get_settings`, `workflows.py`, `ai.py`, `app.py`, `send_email`, `client.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0531883632089333 - nodes in this community are weakly interconnected._