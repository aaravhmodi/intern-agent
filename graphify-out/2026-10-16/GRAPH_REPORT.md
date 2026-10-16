# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~88,943 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 918 nodes · 2658 edges · 43 communities (32 shown, 11 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 448 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `89b5f101`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- leads/cli.py
- re
- startup_jobs.py
- answers.py
- ai.py
- workflows.py
- run_followups
- send_email
- test_followups.py
- OutlookClient
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- test_application_browser.py
- Segment
- test_x_search.py
- x_search.py
- json
- outlook/schemas.py
- notify.py
- tracking.py
- run-application-campaign-2026-10-16.sh
- browser.py
- Lead
- Mailbox
- followups.py
- datetime
- startups.py
- candidate_context.md
- fit_to_limit
- FakeMailbox
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- Region
- client.py
- sending.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 101 edges
2. `Settings` - 52 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `Region` - 25 edges
8. `Segment` - 24 edges
9. `prepare_application()` - 24 edges
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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (43 total, 11 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.20
Nodes (7): EmailStatus, LeadKind, Round, Verdict, parse_round(), test_parse_round(), test_regions_of()

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (37): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+29 more)

### Community 2 - "re"
Cohesion: 0.24
Nodes (11): _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+3 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.17
Nodes (11): _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json() (+3 more)

### Community 4 - "answers.py"
Cohesion: 0.15
Nodes (9): _answer_for(), AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate() (+1 more)

### Community 5 - "ai.py"
Cohesion: 0.06
Nodes (45): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+37 more)

### Community 6 - "workflows.py"
Cohesion: 0.08
Nodes (28): More people to connect with, chosen by company size, Settings, ApplicationPrep, Person, effective_segment(), load_resume_text(), to_people(), answer_bank() (+20 more)

### Community 7 - "run_followups"
Cohesion: 0.15
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "send_email"
Cohesion: 0.09
Nodes (8): Internship agent coding instructions, Send email safeguards, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "OutlookClient"
Cohesion: 0.15
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

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
Nodes (61): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+53 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.15
Nodes (9): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+1 more)

### Community 17 - "Segment"
Cohesion: 0.25
Nodes (10): Segment, to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+2 more)

### Community 18 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 19 - "x_search.py"
Cohesion: 0.17
Nodes (5): search_startups(), StartupFinding, post_confirms(), search_x_raises(), _tool_usage()

### Community 20 - "json"
Cohesion: 0.20
Nodes (14): QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), q(), test_ashby_parser() (+6 more)

### Community 21 - "outlook/schemas.py"
Cohesion: 0.33
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 22 - "notify.py"
Cohesion: 0.19
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 23 - "tracking.py"
Cohesion: 0.18
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 25 - "browser.py"
Cohesion: 0.13
Nodes (13): apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed(), SubmissionResult (+5 more)

### Community 26 - "Lead"
Cohesion: 0.10
Nodes (24): _email_line(), render_outreach(), Lead, _identity(), LeadStore, load_inbox(), merge(), fit() (+16 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 30 - "startups.py"
Cohesion: 0.17
Nodes (6): _clean(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 42 - "Region"
Cohesion: 0.06
Nodes (26): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Region, normalize_url(), region_from_text(), regions_of() (+18 more)

### Community 48 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 49 - "sending.py"
Cohesion: 0.32
Nodes (3): check_outreach_text(), check_send(), SendBlocked

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 276 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `leads/cli.py`, `answers.py`, `ai.py`, `workflows.py`, `run_followups`, `send_email`, `test_followups.py`, `app.py`, `test_dashboard.py`, `test_application_browser.py`, `Segment`, `json`, `notify.py`, `browser.py`, `followups.py`, `datetime`, `startups.py`, `Region`, `sending.py`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.061971830985915494 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `leads/cli.py`, `ai.py`, `run_followups`, `send_email`, `test_followups.py`, `Region`, `internship_agent/cli.py`, `app.py`, `client.py`, `json`, `datetime`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `ai.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05721168322794339 - nodes in this community are weakly interconnected._