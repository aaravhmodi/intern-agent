# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~89,472 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 944 nodes · 2729 edges · 41 communities (30 shown, 11 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 470 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `33adf342`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_followups
- leads/cli.py
- leads/schemas.py
- posting_text.py
- answers.py
- ai.py
- workflows.py
- json
- followups.py
- test_followups.py
- pydantic
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- lead_store
- SentMessage
- browser.py
- re
- candidate_context.md
- x_search.py
- test_dashboard.py
- local_only
- OutlookClient
- app.py
- run-application-campaign-2026-10-16.sh
- client.py
- Lead
- README.md
- AGENTS.md
- outlook/schemas.py
- page_names
- _TableParser
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- handle_note
- store.py
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 107 edges
2. `Settings` - 55 edges
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
- `Fit score against the resume (0-100, reasons, talking points)` --references--> `assess_fit()`  [INFERRED]
  README.md → src/internship_agent/ai.py
- `Search for recently funded startups (last 60 days; Canada, USA, Europe)` --references--> `search_startups()`  [INFERRED]
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

## Communities (41 total, 11 thin omitted)

### Community 0 - "run_followups"
Cohesion: 0.12
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (44): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, get_settings(), Settings, application_campaign(), apply_cmd() (+36 more)

### Community 2 - "leads/schemas.py"
Cohesion: 0.11
Nodes (15): Big-company postings from the SimplifyJobs off-season list, LeadKind, Region, Verdict, region_from_text(), regions_of(), cap_per_company(), fetch() (+7 more)

### Community 3 - "posting_text.py"
Cohesion: 0.14
Nodes (18): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+10 more)

### Community 4 - "answers.py"
Cohesion: 0.06
Nodes (34): AnswerBank, category(), match_option(), normalize(), prefill(), validate(), ApplicationPrep, FitAssessment (+26 more)

### Community 5 - "ai.py"
Cohesion: 0.06
Nodes (42): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+34 more)

### Community 6 - "workflows.py"
Cohesion: 0.11
Nodes (11): More people to connect with, chosen by company size, Person, effective_segment(), check_outreach_text(), _on_linkedin(), source_names(), to_people(), find_startups() (+3 more)

### Community 7 - "json"
Cohesion: 0.21
Nodes (14): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+6 more)

### Community 8 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "pydantic"
Cohesion: 0.16
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+3 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "lead_store"
Cohesion: 0.15
Nodes (20): daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, leads() (+12 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (29): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+21 more)

### Community 17 - "re"
Cohesion: 0.11
Nodes (18): fit_to_limit(), Round, Segment, _slug(), parse_round(), to_leads(), finding(), lead() (+10 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.11
Nodes (10): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+2 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.17
Nodes (11): client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill(), test_send_guess_requires_confirmation_then_records() (+3 more)

### Community 21 - "local_only"
Cohesion: 0.29
Nodes (3): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, local_only()

### Community 22 - "OutlookClient"
Cohesion: 0.20
Nodes (8): OutlookClient, OutlookError, CalendarEvent, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 23 - "app.py"
Cohesion: 0.17
Nodes (11): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, NoteRequest, PreferenceDelete, SaveAnswersRequest (+3 more)

### Community 25 - "client.py"
Cohesion: 0.14
Nodes (5): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), ToolSession

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (32): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+24 more)

### Community 27 - "README.md"
Cohesion: 0.10
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+21 more)

### Community 29 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 30 - "page_names"
Cohesion: 0.22
Nodes (5): _fold(), mentions(), names(), page_names(), source_confirms()

### Community 42 - "store.py"
Cohesion: 0.11
Nodes (13): is_workday(), open_postings(), refill(), _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe() (+5 more)

### Community 49 - "send_email"
Cohesion: 0.11
Nodes (11): Send email safeguards, send(), SendRequest, check_send(), SendBlocked, build_message(), MailError, send() (+3 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 288 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `run_followups`, `leads/cli.py`, `leads/schemas.py`, `answers.py`, `ai.py`, `workflows.py`, `followups.py`, `test_followups.py`, `store.py`, `lead_store`, `browser.py`, `re`, `send_email`, `test_dashboard.py`, `app.py`, `README.md`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Are the 76 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 76 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run_followups` be split into smaller, more focused modules?**
  _Cohesion score 0.1164021164021164 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `leads/cli.py` to `run_followups`, `leads/schemas.py`, `answers.py`, `ai.py`, `workflows.py`, `handle_note`, `test_followups.py`, `internship_agent/cli.py`, `lead_store`, `send_email`, `local_only`, `client.py`, `README.md`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05554035567715458 - nodes in this community are weakly interconnected._