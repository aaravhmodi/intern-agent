# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~87,800 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .example 1, .lock 1)

## Summary
- 888 nodes · 2590 edges · 39 communities (31 shown, 8 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 434 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `845a82c8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_outreach.py
- get_settings
- startups.py
- leads/schemas.py
- re
- LeadStatus
- simplify.py
- run_followups
- mailer.py
- Settings
- browser.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- workflows.py
- test_dashboard.py
- daily
- ai.py
- notify.py
- search_startups
- find-internships.md
- test_people.py
- leads/cli.py
- client.py
- assess_fit
- find-founders.md
- Lead
- rank
- followups.py
- FakeMailbox
- test_x_search.py
- people.py
- internship-agent
- Mailbox
- README.md
- AGENTS.md
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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (39 total, 8 thin omitted)

### Community 0 - "test_outreach.py"
Cohesion: 0.20
Nodes (11): mentions(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round() (+3 more)

### Community 1 - "get_settings"
Cohesion: 0.14
Nodes (10): get_settings(), apply_cmd(), browser_login(), daily_cmd(), export_drafts(), find_more(), find_startups_cmd(), followups_cmd() (+2 more)

### Community 2 - "startups.py"
Cohesion: 0.17
Nodes (7): Region, parse_round(), region_from_text(), regions_of(), _fold(), names(), to_leads()

### Community 3 - "leads/schemas.py"
Cohesion: 0.26
Nodes (5): EmailStatus, Round, Segment, Verdict, effective_segment()

### Community 4 - "re"
Cohesion: 0.06
Nodes (43): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+35 more)

### Community 5 - "LeadStatus"
Cohesion: 0.15
Nodes (16): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect, posting() (+8 more)

### Community 6 - "simplify.py"
Cohesion: 0.12
Nodes (10): Big-company postings from the SimplifyJobs off-season list, cap_per_company(), fetch(), is_software_role(), matching(), parse(), Posting, _TableParser (+2 more)

### Community 7 - "run_followups"
Cohesion: 0.13
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "Settings"
Cohesion: 0.20
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "browser.py"
Cohesion: 0.08
Nodes (17): _answer_for(), apply_to_posting(), _fill_form(), _normalize(), open_login_browser(), SubmissionResult, _supported_url(), FakeField (+9 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.14
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+4 more)

### Community 14 - "workflows.py"
Cohesion: 0.05
Nodes (62): Send email safeguards, AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest (+54 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "daily"
Cohesion: 0.27
Nodes (7): is_workday(), open_postings(), refill(), LeadKind, daily(), startup_postings(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 17 - "ai.py"
Cohesion: 0.17
Nodes (15): AnswerDraft, AnswerDrafts, CoverLetterDraft, format_preferences(), interpret_note(), _lead_context(), NoteResult, PeopleFindings (+7 more)

### Community 18 - "notify.py"
Cohesion: 0.21
Nodes (14): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+6 more)

### Community 19 - "search_startups"
Cohesion: 0.18
Nodes (3): search_startups(), search_x_raises(), _tool_usage()

### Community 20 - "find-internships.md"
Cohesion: 0.13
Nodes (9): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+1 more)

### Community 21 - "test_people.py"
Cohesion: 0.21
Nodes (8): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 22 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 23 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 24 - "assess_fit"
Cohesion: 0.21
Nodes (8): assess_fit(), draft_outreach(), FitAssessment, FitResult, OutreachDraft, OutreachDraftResult, test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 25 - "find-founders.md"
Cohesion: 0.29
Nodes (5): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, import_leads(), load_inbox()

### Community 26 - "Lead"
Cohesion: 0.07
Nodes (30): _email_line(), render_outreach(), Lead, _slug(), _identity(), LeadStore, merge(), normalize_url() (+22 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 34 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 36 - "people.py"
Cohesion: 0.25
Nodes (4): More people to connect with, chosen by company size, Person, _on_linkedin(), source_names()

### Community 40 - "README.md"
Cohesion: 0.06
Nodes (31): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules (+23 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 262 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_outreach.py`, `startups.py`, `leads/schemas.py`, `re`, `LeadStatus`, `simplify.py`, `run_followups`, `Settings`, `browser.py`, `workflows.py`, `test_dashboard.py`, `daily`, `ai.py`, `notify.py`, `find-internships.md`, `leads/cli.py`, `assess_fit`, `find-founders.md`, `rank`, `followups.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `get_settings` be split into smaller, more focused modules?**
  _Cohesion score 0.1422924901185771 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `re`, `LeadStatus`, `simplify.py`, `run_followups`, `internship_agent/cli.py`, `make_workflows.py`, `workflows.py`, `daily`, `test_people.py`, `leads/cli.py`, `client.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._