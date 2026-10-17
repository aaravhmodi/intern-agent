# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~90,587 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 961 nodes · 2795 edges · 47 communities (36 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 490 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1796af02`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- leads/cli.py
- Region
- typing
- json
- LeadStatus
- leads/schemas.py
- posting_text.py
- find-founders.md
- run_followups
- client.py
- internship_agent/cli.py
- get_settings
- make_workflows.py
- find_startups
- Settings
- browser.py
- mailer.py
- candidate_context.md
- x_search.py
- test_dashboard.py
- README.md
- find-internships.md
- send_email
- run-application-campaign-2026-10-16.sh
- test_followups.py
- test_leads.py
- Mailbox
- rank
- _TableParser
- test_daily_campaign.py
- mailbox.py
- answers.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- re
- FormQuestion
- Lead
- ai.py
- FakeMailbox
- test_outreach.py
- local_only
- test_answers.py
- pathlib

## God Nodes (most connected - your core abstractions)
1. `Lead` - 108 edges
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
- `More people to connect with, chosen by company size` --references--> `search_people()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (47 total, 11 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.12
Nodes (28): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest (+20 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.21
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 2 - "Region"
Cohesion: 0.13
Nodes (13): Big-company postings from the SimplifyJobs off-season list, Region, normalize_url(), region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role() (+5 more)

### Community 3 - "typing"
Cohesion: 0.11
Nodes (15): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+7 more)

### Community 4 - "json"
Cohesion: 0.19
Nodes (14): _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers(), answer() (+6 more)

### Community 5 - "LeadStatus"
Cohesion: 0.17
Nodes (14): apply_violations(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads() (+6 more)

### Community 6 - "leads/schemas.py"
Cohesion: 0.13
Nodes (11): LeadKind, Round, Segment, Verdict, parse_round(), _fold(), mentions(), names() (+3 more)

### Community 7 - "posting_text.py"
Cohesion: 0.35
Nodes (8): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday()

### Community 8 - "find-founders.md"
Cohesion: 0.22
Nodes (6): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, export_drafts(), import_leads(), load_inbox()

### Community 9 - "run_followups"
Cohesion: 0.12
Nodes (15): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+7 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "get_settings"
Cohesion: 0.13
Nodes (11): get_settings(), application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "find_startups"
Cohesion: 0.24
Nodes (6): search_people(), effective_segment(), to_people(), find_startups(), people_at(), _log_xai()

### Community 15 - "Settings"
Cohesion: 0.12
Nodes (18): Settings, answer_bank(), daily(), find_people(), handle_note(), lead_store(), _openai(), preference_store() (+10 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (34): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+26 more)

### Community 17 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.10
Nodes (11): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "README.md"
Cohesion: 0.11
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+21 more)

### Community 22 - "find-internships.md"
Cohesion: 0.14
Nodes (11): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, guess_email(), _email_line() (+3 more)

### Community 23 - "send_email"
Cohesion: 0.29
Nodes (3): send(), SendRequest, send_email()

### Community 25 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 26 - "test_leads.py"
Cohesion: 0.16
Nodes (17): LeadStore, fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input() (+9 more)

### Community 30 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 34 - "answers.py"
Cohesion: 0.16
Nodes (7): AnswerBank, category(), match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options()

### Community 40 - "re"
Cohesion: 0.14
Nodes (5): _clean(), fit_to_limit(), _normalize(), _slug(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 41 - "FormQuestion"
Cohesion: 0.27
Nodes (11): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+3 more)

### Community 42 - "Lead"
Cohesion: 0.16
Nodes (12): is_workday(), open_postings(), refill(), Lead, _identity(), merge(), DailyReport, _incompatible_term() (+4 more)

### Community 43 - "ai.py"
Cohesion: 0.05
Nodes (35): Internship agent coding instructions, More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences() (+27 more)

### Community 47 - "test_outreach.py"
Cohesion: 0.16
Nodes (11): check_outreach_text(), check_send(), SendBlocked, finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_mentions_requires_company_and_founder_ignoring_accents() (+3 more)

### Community 49 - "local_only"
Cohesion: 0.29
Nodes (3): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, local_only()

### Community 50 - "test_answers.py"
Cohesion: 0.43
Nodes (5): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 293 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `app.py`, `leads/cli.py`, `Region`, `typing`, `json`, `LeadStatus`, `leads/schemas.py`, `find-founders.md`, `run_followups`, `find_startups`, `Settings`, `browser.py`, `test_dashboard.py`, `find-internships.md`, `send_email`, `test_followups.py`, `test_leads.py`, `rank`, `test_daily_campaign.py`, `re`, `ai.py`, `test_outreach.py`, `test_answers.py`?**
  _High betweenness centrality (0.160) - this node is a cross-community bridge._
- **Are the 77 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 77 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11515151515151516 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `Region`, `LeadStatus`, `run_followups`, `client.py`, `internship_agent/cli.py`, `get_settings`, `Lead`, `find_startups`, `ai.py`, `local_only`, `test_answers.py`, `pathlib`, `send_email`, `test_followups.py`, `test_daily_campaign.py`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.13105413105413105 - nodes in this community are weakly interconnected._