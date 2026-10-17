# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~90,267 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 958 nodes · 2773 edges · 52 communities (41 shown, 11 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 483 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3d22abfe`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- leads/cli.py
- Region
- startup_jobs.py
- notify.py
- LeadStatus
- find_startups
- app.py
- local_only
- run_followups
- client.py
- internship_agent/cli.py
- get_settings
- make_workflows.py
- ai.py
- Settings
- browser.py
- leads/schemas.py
- candidate_context.md
- typing
- test_dashboard.py
- test_daily_campaign.py
- find-founders.md
- sending.py
- run-application-campaign-2026-10-16.sh
- test_followups.py
- test_leads.py
- _view
- ranking.py
- load_resume_text
- ApplicationPrep
- Lead
- mailbox.py
- workflows.py
- answers.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- startups.py
- json
- store.py
- re
- fit_to_limit
- followups
- FakeMailbox
- Dashboard page (index.html)
- Mailbox
- mailer.py
- test_answers.py
- EmailStatus

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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (52 total, 11 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.14
Nodes (20): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup, Development (+12 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.21
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 2 - "Region"
Cohesion: 0.12
Nodes (9): Region, region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+1 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "notify.py"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 5 - "LeadStatus"
Cohesion: 0.14
Nodes (14): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting() (+6 more)

### Community 6 - "find_startups"
Cohesion: 0.28
Nodes (5): effective_segment(), to_people(), find_startups(), people_at(), _log_xai()

### Community 7 - "app.py"
Cohesion: 0.15
Nodes (13): delete_preference(), _get(), index(), leads(), note(), NoteRequest, PreferenceDelete, send() (+5 more)

### Community 8 - "local_only"
Cohesion: 0.25
Nodes (4): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Dashboard, local_only()

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
Cohesion: 0.14
Nodes (11): get_settings(), application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd() (+3 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "ai.py"
Cohesion: 0.06
Nodes (35): Internship agent coding instructions, More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences() (+27 more)

### Community 15 - "Settings"
Cohesion: 0.15
Nodes (14): Settings, answer_bank(), find_people(), lead_store(), _openai(), prepare_application(), _record_openai_usage(), refresh_saved_application() (+6 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (30): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+22 more)

### Community 17 - "leads/schemas.py"
Cohesion: 0.14
Nodes (16): Round, Segment, Verdict, parse_round(), mentions(), to_leads(), finding(), lead() (+8 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "typing"
Cohesion: 0.11
Nodes (11): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding() (+3 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "test_daily_campaign.py"
Cohesion: 0.12
Nodes (7): _slug(), test_incompatible_eight_month_term_is_rejected(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_refresh_uses_saved_answer_without_regenerating_cover_letter(), test_saving_answers_preserves_uncertain_submission(), test_scrape_stores_every_matching_non_workday_posting(), test_usage_log_contains_counts_without_prompt_content()

### Community 22 - "find-founders.md"
Cohesion: 0.11
Nodes (13): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+5 more)

### Community 23 - "sending.py"
Cohesion: 0.25
Nodes (3): Send email safeguards, check_outreach_text(), check_send()

### Community 25 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 26 - "test_leads.py"
Cohesion: 0.15
Nodes (18): LeadStore, fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email(), test_guess_email_rejects_bad_input() (+10 more)

### Community 27 - "_view"
Cohesion: 0.16
Nodes (14): daily_run(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest, KeyRequest, people() (+6 more)

### Community 30 - "ApplicationPrep"
Cohesion: 0.22
Nodes (8): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new()

### Community 31 - "Lead"
Cohesion: 0.16
Nodes (11): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, LeadKind, fetch(), to_lead() (+3 more)

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 33 - "workflows.py"
Cohesion: 0.15
Nodes (7): common_questions(), daily(), DailyReport, _incompatible_term(), NoteOutcome, _run_ai_cost(), submit_application()

### Community 34 - "answers.py"
Cohesion: 0.18
Nodes (6): AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options()

### Community 40 - "startups.py"
Cohesion: 0.18
Nodes (4): _clean(), _fold(), names(), source_confirms()

### Community 41 - "json"
Cohesion: 0.30
Nodes (10): FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), test_ashby_parser() (+2 more)

### Community 42 - "store.py"
Cohesion: 0.14
Nodes (10): _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+2 more)

### Community 43 - "re"
Cohesion: 0.34
Nodes (9): _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever(), _workday() (+1 more)

### Community 45 - "followups"
Cohesion: 0.20
Nodes (7): AnswerEdit, followups(), FollowupsRequest, save(), SaveAnswersRequest, submit(), SubmitApplicationRequest

### Community 47 - "Dashboard page (index.html)"
Cohesion: 0.32
Nodes (6): Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, LinkedIn connection note is pasted and sent by hand, Dashboard page (index.html), Email section with two-click send, linkedinUrl(): profile URL, else a LinkedIn people search, 'More people to connect with' section

### Community 49 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 50 - "test_answers.py"
Cohesion: 0.43
Nodes (5): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind()

### Community 51 - "EmailStatus"
Cohesion: 0.60
Nodes (3): _email_line(), render_outreach(), EmailStatus

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 293 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/cli.py`, `Region`, `notify.py`, `LeadStatus`, `find_startups`, `app.py`, `run_followups`, `ai.py`, `Settings`, `browser.py`, `leads/schemas.py`, `test_dashboard.py`, `test_daily_campaign.py`, `find-founders.md`, `sending.py`, `test_followups.py`, `test_leads.py`, `_view`, `ranking.py`, `ApplicationPrep`, `workflows.py`, `startups.py`, `store.py`, `test_answers.py`, `EmailStatus`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **Are the 77 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 77 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.13852813852813853 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `leads/cli.py`, `workflows.py`, `LeadStatus`, `find_startups`, `app.py`, `local_only`, `run_followups`, `client.py`, `internship_agent/cli.py`, `get_settings`, `ai.py`, `test_answers.py`, `test_daily_campaign.py`, `test_followups.py`, `ApplicationPrep`, `Lead`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.11692307692307692 - nodes in this community are weakly interconnected._