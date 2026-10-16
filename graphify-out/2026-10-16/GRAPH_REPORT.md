# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 69 files · ~88,544 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 901 nodes · 2623 edges · 43 communities (34 shown, 9 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 437 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d3c73cc3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Segment
- leads/cli.py
- Lead
- startup_jobs.py
- re
- leads/schemas.py
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
- find_startups
- ai.py
- test_outlook_client.py
- x_search.py
- AnswerBank
- outlook/schemas.py
- README.md
- tracking.py
- Mailbox
- browser.py
- test_leads.py
- test_refill.py
- followups.py
- Region
- startups.py
- candidate_context.md
- FakeMailbox
- run-application-campaign-2026-10-17.sh
- internship-agent
- simplify.py
- local_only
- AGENTS.md
- client.py
- send

## God Nodes (most connected - your core abstractions)
1. `Lead` - 98 edges
2. `Settings` - 49 edges
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

## Communities (43 total, 9 thin omitted)

### Community 0 - "Segment"
Cohesion: 0.16
Nodes (14): Round, Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment() (+6 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.05
Nodes (41): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+33 more)

### Community 2 - "Lead"
Cohesion: 0.20
Nodes (10): is_workday(), open_postings(), refill(), Lead, LeadKind, _identity(), merge(), daily() (+2 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "re"
Cohesion: 0.06
Nodes (47): category(), common_questions(), match_option(), normalize(), validate(), _clean(), FormQuestion, PreparedAnswer (+39 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.08
Nodes (25): NoteResult, PreferenceDraft, fit_to_limit(), apply_violations(), _normalize(), PreferenceStore, ApplicationPrep, FitAssessment (+17 more)

### Community 6 - "workflows.py"
Cohesion: 0.19
Nodes (14): Settings, answer_bank(), find_people(), handle_note(), lead_store(), NoteOutcome, _openai(), preference_store() (+6 more)

### Community 7 - "run_followups"
Cohesion: 0.15
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "send_email"
Cohesion: 0.18
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "OutlookClient"
Cohesion: 0.23
Nodes (4): OutlookClient, OutlookError, ToolSession, CalendarEvent

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
Cohesion: 0.11
Nodes (29): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest (+21 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "find_startups"
Cohesion: 0.15
Nodes (9): More people to connect with, chosen by company size, Person, effective_segment(), _on_linkedin(), source_names(), to_people(), find_startups(), people_at() (+1 more)

### Community 17 - "ai.py"
Cohesion: 0.19
Nodes (14): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+6 more)

### Community 18 - "test_outlook_client.py"
Cohesion: 0.31
Nodes (5): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 19 - "x_search.py"
Cohesion: 0.12
Nodes (9): StartupFindings, post_confirms(), post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder() (+1 more)

### Community 21 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 22 - "README.md"
Cohesion: 0.12
Nodes (26): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+18 more)

### Community 23 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 25 - "browser.py"
Cohesion: 0.07
Nodes (23): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed() (+15 more)

### Community 26 - "test_leads.py"
Cohesion: 0.09
Nodes (27): LeadStore, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_draft_prompt_leads_with_upside_impact(), fit(), lead(), posting() (+19 more)

### Community 27 - "test_refill.py"
Cohesion: 0.18
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "Region"
Cohesion: 0.43
Nodes (3): Region, region_from_text(), regions_of()

### Community 30 - "startups.py"
Cohesion: 0.16
Nodes (8): Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups(), StartupFinding, _fold(), mentions(), names(), page_names(), source_confirms()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 42 - "simplify.py"
Cohesion: 0.11
Nodes (12): Big-company postings from the SimplifyJobs off-season list, normalize_url(), cap_per_company(), fetch(), is_software_role(), matching(), parse(), Posting (+4 more)

### Community 43 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 48 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 49 - "send"
Cohesion: 0.19
Nodes (5): send(), SendRequest, check_outreach_text(), check_send(), SendBlocked

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 266 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `Segment`, `leads/cli.py`, `re`, `leads/schemas.py`, `workflows.py`, `run_followups`, `send_email`, `test_followups.py`, `app.py`, `test_dashboard.py`, `find_startups`, `ai.py`, `browser.py`, `test_leads.py`, `test_refill.py`, `followups.py`, `startups.py`, `simplify.py`, `send`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05443037974683544 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `leads/cli.py`, `Lead`, `re`, `leads/schemas.py`, `run_followups`, `send_email`, `test_followups.py`, `simplify.py`, `local_only`, `internship_agent/cli.py`, `client.py`, `find_startups`, `test_leads.py`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.05895061728395062 - nodes in this community are weakly interconnected._