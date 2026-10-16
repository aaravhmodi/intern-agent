# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~87,518 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 886 nodes · 2570 edges · 47 communities (35 shown, 12 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 426 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d32eb6d9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_outreach.py
- leads/cli.py
- startups.py
- leads/schemas.py
- re
- LeadStatus
- Region
- run_followups
- send_email
- test_followups.py
- browser.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- workflows.py
- test_dashboard.py
- Dashboard page (index.html)
- ai.py
- README.md
- x_search.py
- test_ai.py
- EmailStatus
- get_settings
- client.py
- pathlib
- test_people.py
- Lead
- rank
- followups.py
- Winter 2027 Internship Agent
- BaseModel
- find-founders.md
- guess_email
- FakeMailbox
- test_x_search.py
- people.py
- internship-agent
- Mailbox
- candidate_context.md
- AGENTS.md
- _TableParser
- page_names
- local_only
- fit_to_limit

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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (47 total, 12 thin omitted)

### Community 0 - "test_outreach.py"
Cohesion: 0.26
Nodes (9): finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round(), test_regions_of(), test_to_leads_filters_age_stage_and_unverifiable_sources() (+1 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.24
Nodes (11): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+3 more)

### Community 2 - "startups.py"
Cohesion: 0.19
Nodes (5): parse_round(), _fold(), mentions(), names(), to_leads()

### Community 3 - "leads/schemas.py"
Cohesion: 0.29
Nodes (4): FindStartupsRequest, Round, Segment, Verdict

### Community 4 - "re"
Cohesion: 0.05
Nodes (54): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+46 more)

### Community 5 - "LeadStatus"
Cohesion: 0.15
Nodes (16): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 6 - "Region"
Cohesion: 0.16
Nodes (9): Region, region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+1 more)

### Community 7 - "run_followups"
Cohesion: 0.15
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "send_email"
Cohesion: 0.18
Nodes (6): build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "browser.py"
Cohesion: 0.09
Nodes (16): _answer_for(), apply_to_posting(), _fill_form(), _normalize(), open_login_browser(), SubmissionResult, _supported_url(), FakeField (+8 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "workflows.py"
Cohesion: 0.06
Nodes (63): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Big-company postings from the SimplifyJobs off-season list, Settings, AnswerEdit, daily_run(), delete_preference(), draft() (+55 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "Dashboard page (index.html)"
Cohesion: 0.24
Nodes (8): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Send email safeguards, index(), Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 17 - "ai.py"
Cohesion: 0.18
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 18 - "README.md"
Cohesion: 0.36
Nodes (9): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Fit score against the resume (0-100, reasons, talking points), Rules learned from notes (skip, downrank, boost), Application answers section (+1 more)

### Community 19 - "x_search.py"
Cohesion: 0.14
Nodes (7): search_startups(), StartupFinding, post_confirms(), post_id(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 20 - "test_ai.py"
Cohesion: 0.36
Nodes (5): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 21 - "EmailStatus"
Cohesion: 0.31
Nodes (5): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 22 - "get_settings"
Cohesion: 0.14
Nodes (10): get_settings(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd(), prepare_all_cmd() (+2 more)

### Community 23 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 25 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 26 - "Lead"
Cohesion: 0.07
Nodes (31): _email_line(), render_outreach(), Lead, _slug(), _identity(), LeadStore, load_inbox(), merge() (+23 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 29 - "Winter 2027 Internship Agent"
Cohesion: 0.25
Nodes (8): Current setup, Development, Founder leads (X.com), Other connectors, Outlook integration (MCP), Planned commands, What it does, Winter 2027 Internship Agent

### Community 30 - "BaseModel"
Cohesion: 0.29
Nodes (3): FitAssessment, OutreachDraft, OutreachDraftResult

### Community 31 - "find-founders.md"
Cohesion: 0.12
Nodes (11): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+3 more)

### Community 32 - "guess_email"
Cohesion: 0.32
Nodes (3): _clean(), guess_email(), test_guess_email()

### Community 34 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 36 - "people.py"
Cohesion: 0.23
Nodes (6): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, _on_linkedin(), source_names()

### Community 40 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 44 - "page_names"
Cohesion: 0.33
Nodes (4): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), page_names(), source_confirms()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 262 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_outreach.py`, `leads/cli.py`, `startups.py`, `leads/schemas.py`, `re`, `LeadStatus`, `Region`, `run_followups`, `send_email`, `test_followups.py`, `browser.py`, `workflows.py`, `test_dashboard.py`, `ai.py`, `EmailStatus`, `rank`, `followups.py`, `BaseModel`, `find-founders.md`, `people.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.050915211445402904 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `leads/cli.py`, `re`, `LeadStatus`, `run_followups`, `send_email`, `test_followups.py`, `internship_agent/cli.py`, `get_settings`, `client.py`, `pathlib`, `test_people.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `LeadStatus` be split into smaller, more focused modules?**
  _Cohesion score 0.14919354838709678 - nodes in this community are weakly interconnected._