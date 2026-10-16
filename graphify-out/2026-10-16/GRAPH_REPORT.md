# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~89,062 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 933 nodes · 2690 edges · 38 communities (30 shown, 8 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 453 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6d47ddcf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_followups
- leads/cli.py
- leads/schemas.py
- re
- json
- ai.py
- workflows.py
- LeadStatus
- followups.py
- Settings
- client.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- _view
- FakeMailbox
- browser.py
- Segment
- candidate_context.md
- x_search.py
- Region
- local_only
- test_x_search.py
- app.py
- run-application-campaign-2026-10-16.sh
- send
- Lead
- README.md
- startups.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- prepare_application
- simplify.py
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 102 edges
2. `Settings` - 52 edges
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

## Communities (38 total, 8 thin omitted)

### Community 0 - "run_followups"
Cohesion: 0.12
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (35): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+27 more)

### Community 2 - "leads/schemas.py"
Cohesion: 0.18
Nodes (8): ApplicationPrep, LeadKind, Round, Verdict, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_pre_submit_block_can_be_retried_but_uncertain_cannot()

### Community 3 - "re"
Cohesion: 0.12
Nodes (20): fit_to_limit(), _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json() (+12 more)

### Community 4 - "json"
Cohesion: 0.07
Nodes (38): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+30 more)

### Community 5 - "ai.py"
Cohesion: 0.06
Nodes (32): Internship agent coding instructions, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note() (+24 more)

### Community 6 - "workflows.py"
Cohesion: 0.13
Nodes (10): More people to connect with, chosen by company size, Person, effective_segment(), check_outreach_text(), to_people(), find_startups(), people_at(), _log_xai() (+2 more)

### Community 7 - "LeadStatus"
Cohesion: 0.15
Nodes (16): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, NoteOutcome, posting() (+8 more)

### Community 8 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 9 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.07
Nodes (22): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+14 more)

### Community 12 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "_view"
Cohesion: 0.22
Nodes (15): daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, leads() (+7 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (29): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+21 more)

### Community 17 - "Segment"
Cohesion: 0.19
Nodes (12): Segment, parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_mentions_requires_company_and_founder_ignoring_accents() (+4 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.16
Nodes (7): StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 20 - "Region"
Cohesion: 0.25
Nodes (3): search_startups(), Region, region_from_text()

### Community 21 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

### Community 22 - "test_x_search.py"
Cohesion: 0.32
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 23 - "app.py"
Cohesion: 0.15
Nodes (13): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, note(), NoteRequest, PreferenceDelete (+5 more)

### Community 25 - "send"
Cohesion: 0.29
Nodes (3): send(), SendRequest, SendBlocked

### Community 26 - "Lead"
Cohesion: 0.07
Nodes (31): Output, Output, _clean(), guess_email(), _email_line(), render_outreach(), EmailStatus, Lead (+23 more)

### Community 27 - "README.md"
Cohesion: 0.12
Nodes (26): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+18 more)

### Community 30 - "startups.py"
Cohesion: 0.14
Nodes (8): Search for recently funded startups (last 60 days; Canada, USA, Europe), _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 41 - "prepare_application"
Cohesion: 0.15
Nodes (13): answer_bank(), daily(), find_people(), handle_note(), lead_store(), _openai(), preference_store(), prepare_application() (+5 more)

### Community 42 - "simplify.py"
Cohesion: 0.06
Nodes (23): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), normalize_url(), regions_of(), cap_per_company(), fetch() (+15 more)

### Community 49 - "send_email"
Cohesion: 0.15
Nodes (8): Send email safeguards, check_send(), build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 282 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `run_followups`, `leads/cli.py`, `leads/schemas.py`, `json`, `ai.py`, `workflows.py`, `LeadStatus`, `followups.py`, `prepare_application`, `simplify.py`, `internship_agent/cli.py`, `Settings`, `_view`, `browser.py`, `send_email`, `Segment`, `app.py`, `startups.py`?**
  _High betweenness centrality (0.152) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 71 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `run_followups` be split into smaller, more focused modules?**
  _Cohesion score 0.1164021164021164 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `run_followups`, `leads/cli.py`, `leads/schemas.py`, `json`, `ai.py`, `workflows.py`, `LeadStatus`, `prepare_application`, `client.py`, `internship_agent/cli.py`, `simplify.py`, `send_email`, `local_only`, `Lead`, `pathlib`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.061569416498993966 - nodes in this community are weakly interconnected._