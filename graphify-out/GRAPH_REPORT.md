# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~90,680 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 964 nodes · 2804 edges · 42 communities (31 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 492 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `676b9e68`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- command
- simplify.py
- test_refill.py
- notify.py
- LeadStatus
- leads/schemas.py
- followups.py
- find-founders.md
- run_followups
- client.py
- internship_agent/cli.py
- get_settings
- make_workflows.py
- followups_cmd
- workflows.py
- browser.py
- mailer.py
- startups.py
- find_startups
- test_dashboard.py
- README.md
- leads/cli.py
- send_email
- run-application-campaign-2026-10-16.sh
- Settings
- Lead
- test_x_search.py
- rank
- mailbox.py
- re
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- fit_to_limit
- handle_note
- ai.py
- SentMessage
- test_outreach.py

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

## Communities (42 total, 11 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.11
Nodes (32): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, followups() (+24 more)

### Community 1 - "command"
Cohesion: 0.17
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), list_leads(), mark_lead(), _openai(), prepare_all_cmd() (+4 more)

### Community 2 - "simplify.py"
Cohesion: 0.07
Nodes (22): Big-company postings from the SimplifyJobs off-season list, normalize_url(), region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+14 more)

### Community 3 - "test_refill.py"
Cohesion: 0.18
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 4 - "notify.py"
Cohesion: 0.20
Nodes (14): _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers(), answer() (+6 more)

### Community 5 - "LeadStatus"
Cohesion: 0.15
Nodes (15): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting(), settings() (+7 more)

### Community 6 - "leads/schemas.py"
Cohesion: 0.26
Nodes (4): Round, Verdict, parse_round(), test_parse_round()

### Community 7 - "followups.py"
Cohesion: 0.18
Nodes (8): Internship tracker: follow-ups (weekdays 9:30 AM), company_domain(), first_name(), followup_body(), is_due(), last_contact(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 8 - "find-founders.md"
Cohesion: 0.11
Nodes (11): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, export_drafts() (+3 more)

### Community 9 - "run_followups"
Cohesion: 0.12
Nodes (9): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), Note (+1 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (36): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), run(), connect(), OutlookClient, OutlookError (+28 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.16
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "get_settings"
Cohesion: 0.18
Nodes (6): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_cmd(), scrape_jobs_cmd()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+4 more)

### Community 14 - "followups_cmd"
Cohesion: 0.27
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 15 - "workflows.py"
Cohesion: 0.09
Nodes (22): is_workday(), open_postings(), refill(), LeadKind, answer_bank(), daily(), DailyReport, find_more_postings() (+14 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (35): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+27 more)

### Community 17 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 18 - "startups.py"
Cohesion: 0.24
Nodes (3): _fold(), mentions(), names()

### Community 19 - "find_startups"
Cohesion: 0.10
Nodes (21): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups(), StartupFinding, FindStartupsRequest, Region, Segment, effective_segment() (+13 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "README.md"
Cohesion: 0.08
Nodes (33): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules (+25 more)

### Community 22 - "leads/cli.py"
Cohesion: 0.26
Nodes (5): _email_cell(), _email_line(), render_outreach(), EmailStatus, load_resume_text()

### Community 23 - "send_email"
Cohesion: 0.21
Nodes (4): check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 25 - "Settings"
Cohesion: 0.21
Nodes (18): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+10 more)

### Community 26 - "Lead"
Cohesion: 0.05
Nodes (37): Output, Output, _clean(), guess_email(), ApplicationPrep, FitAssessment, Lead, _identity() (+29 more)

### Community 27 - "test_x_search.py"
Cohesion: 0.29
Nodes (4): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_only_a_link_to_a_post_has_a_post_id()

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 34 - "re"
Cohesion: 0.07
Nodes (34): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+26 more)

### Community 43 - "ai.py"
Cohesion: 0.05
Nodes (36): Internship agent coding instructions, More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences() (+28 more)

### Community 47 - "test_outreach.py"
Cohesion: 0.29
Nodes (7): finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_regions_of(), test_to_leads_filters_age_stage_and_unverifiable_sources()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 295 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `app.py`, `command`, `simplify.py`, `test_refill.py`, `notify.py`, `LeadStatus`, `leads/schemas.py`, `followups.py`, `find-founders.md`, `run_followups`, `workflows.py`, `browser.py`, `startups.py`, `find_startups`, `test_dashboard.py`, `leads/cli.py`, `send_email`, `Settings`, `rank`, `re`, `handle_note`, `ai.py`, `test_outreach.py`, `store.py`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11081560283687943 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `app.py`, `command`, `re`, `LeadStatus`, `run_followups`, `client.py`, `handle_note`, `get_settings`, `make_workflows.py`, `ai.py`, `workflows.py`, `find_startups`, `store.py`, `leads/cli.py`, `send_email`, `Lead`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0696969696969697 - nodes in this community are weakly interconnected._