# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 70 files · ~88,722 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 907 nodes · 2638 edges · 37 communities (32 shown, 5 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 444 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cd4060f7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- leads/cli.py
- re
- startup_jobs.py
- json
- ai.py
- workflows.py
- run_followups
- mailer.py
- Settings
- OutlookClient
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- find_startups
- test_outreach.py
- test_x_search.py
- x_search.py
- Dashboard page (index.html)
- client.py
- README.md
- tracking.py
- browser.py
- Lead
- followups.py
- page_names
- candidate_context.md
- SentMessage
- run-application-campaign-2026-10-17.sh
- internship-agent
- simplify.py
- outlook
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 99 edges
2. `Settings` - 50 edges
3. `get_settings()` - 42 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `daily()` - 26 edges
8. `Region` - 25 edges
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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (37 total, 5 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.17
Nodes (9): LeadKind, Region, Round, Segment, Verdict, parse_round(), to_leads(), test_to_leads_filters_age_stage_and_unverifiable_sources() (+1 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (37): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+29 more)

### Community 2 - "re"
Cohesion: 0.20
Nodes (12): fit_to_limit(), _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json() (+4 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.10
Nodes (12): Internship agent coding instructions, _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles() (+4 more)

### Community 4 - "json"
Cohesion: 0.06
Nodes (42): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), ApplicationPrep (+34 more)

### Community 5 - "ai.py"
Cohesion: 0.06
Nodes (40): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+32 more)

### Community 6 - "workflows.py"
Cohesion: 0.14
Nodes (13): answer_bank(), daily(), DailyReport, handle_note(), lead_store(), NoteOutcome, prepare_application(), rescore_open() (+5 more)

### Community 7 - "run_followups"
Cohesion: 0.12
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "Settings"
Cohesion: 0.21
Nodes (17): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 10 - "OutlookClient"
Cohesion: 0.15
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.11
Nodes (11): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+3 more)

### Community 12 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "app.py"
Cohesion: 0.11
Nodes (32): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest (+24 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "find_startups"
Cohesion: 0.17
Nodes (11): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups() (+3 more)

### Community 17 - "test_outreach.py"
Cohesion: 0.22
Nodes (9): mentions(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round() (+1 more)

### Community 18 - "test_x_search.py"
Cohesion: 0.32
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 19 - "x_search.py"
Cohesion: 0.13
Nodes (9): search_startups(), StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+1 more)

### Community 20 - "Dashboard page (index.html)"
Cohesion: 0.38
Nodes (7): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, index(), Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 21 - "client.py"
Cohesion: 0.16
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 22 - "README.md"
Cohesion: 0.16
Nodes (19): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Dashboard (+11 more)

### Community 23 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 25 - "browser.py"
Cohesion: 0.07
Nodes (24): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed() (+16 more)

### Community 26 - "Lead"
Cohesion: 0.06
Nodes (34): _email_line(), render_outreach(), refill(), EmailStatus, Lead, _identity(), LeadStore, load_inbox() (+26 more)

### Community 28 - "followups.py"
Cohesion: 0.25
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 30 - "page_names"
Cohesion: 0.20
Nodes (5): _clean(), _fold(), names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 42 - "simplify.py"
Cohesion: 0.10
Nodes (12): Big-company postings from the SimplifyJobs off-season list, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+4 more)

### Community 48 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 49 - "send_email"
Cohesion: 0.18
Nodes (7): Send email safeguards, send(), SendRequest, check_outreach_text(), check_send(), SendBlocked, send_email()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 268 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `leads/cli.py`, `json`, `ai.py`, `workflows.py`, `run_followups`, `Settings`, `simplify.py`, `app.py`, `test_dashboard.py`, `find_startups`, `send_email`, `test_outreach.py`, `browser.py`, `followups.py`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 68 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 68 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0593607305936073 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `json`, `ai.py`, `workflows.py`, `run_followups`, `simplify.py`, `internship_agent/cli.py`, `make_workflows.py`, `app.py`, `find_startups`, `send_email`, `client.py`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 41 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 41 INFERRED edges - model-reasoned connections that need verification._
- **Should `startup_jobs.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10344827586206896 - nodes in this community are weakly interconnected._