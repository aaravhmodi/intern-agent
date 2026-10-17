# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~90,338 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 959 nodes · 2781 edges · 44 communities (33 shown, 11 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 486 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `677dfdf1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- leads/cli.py
- Region
- startup_jobs.py
- notify.py
- test_notes.py
- find_startups
- LeadStatus
- assess_fit
- run_followups
- client.py
- internship_agent/cli.py
- get_settings
- make_workflows.py
- ai.py
- workflows.py
- browser.py
- test_outreach.py
- candidate_context.md
- typing
- test_dashboard.py
- test_scrape_stores_every_matching_non_workday_posting
- find-founders.md
- test_people.py
- run-application-campaign-2026-10-16.sh
- test_followups.py
- test_leads.py
- AGENTS.md
- datetime
- _TableParser
- leads/schemas.py
- Lead
- mailbox.py
- answers.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- re
- json
- test_refill.py
- SentMessage
- store.py

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

## Communities (44 total, 11 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.05
Nodes (62): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+54 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.17
Nodes (13): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+5 more)

### Community 2 - "Region"
Cohesion: 0.14
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "notify.py"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 5 - "test_notes.py"
Cohesion: 0.18
Nodes (13): PreferenceDraft, _normalize(), PreferenceStore, Preference, PreferenceEffect, posting(), settings(), test_apply_violations_never_touches_applied_leads() (+5 more)

### Community 6 - "find_startups"
Cohesion: 0.12
Nodes (14): More people to connect with, chosen by company size, search_people(), Person, Segment, effective_segment(), to_people(), to_leads(), find_people() (+6 more)

### Community 7 - "LeadStatus"
Cohesion: 0.18
Nodes (7): first_name(), followup_body(), is_due(), last_contact(), apply_violations(), LeadStatus, Note

### Community 8 - "assess_fit"
Cohesion: 0.27
Nodes (7): assess_fit(), FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 9 - "run_followups"
Cohesion: 0.12
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

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
Cohesion: 0.19
Nodes (13): AnswerDraft, AnswerDrafts, CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context(), NoteResult (+5 more)

### Community 15 - "workflows.py"
Cohesion: 0.12
Nodes (21): Settings, answer_bank(), daily(), DailyReport, handle_note(), _incompatible_term(), lead_store(), NoteOutcome (+13 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (31): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+23 more)

### Community 17 - "test_outreach.py"
Cohesion: 0.07
Nodes (22): _email_line(), render_outreach(), EmailStatus, Round, Verdict, check_outreach_text(), check_send(), SendBlocked (+14 more)

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "typing"
Cohesion: 0.12
Nodes (10): search_startups(), StartupFinding, StartupFindings, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising() (+2 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 22 - "find-founders.md"
Cohesion: 0.11
Nodes (13): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+5 more)

### Community 23 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 25 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 26 - "test_leads.py"
Cohesion: 0.14
Nodes (19): _slug(), LeadStore, fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email() (+11 more)

### Community 30 - "leads/schemas.py"
Cohesion: 0.10
Nodes (15): ApplicationPrep, FitAssessment, OutreachDraft, OutreachDraftResult, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting() (+7 more)

### Community 31 - "Lead"
Cohesion: 0.24
Nodes (8): is_workday(), open_postings(), refill(), Lead, LeadKind, scrape_jobs(), startup_postings(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 34 - "answers.py"
Cohesion: 0.18
Nodes (6): AnswerBank, match_option(), normalize(), prefill(), validate(), test_yes_no_answer_matches_long_select_options()

### Community 40 - "re"
Cohesion: 0.07
Nodes (19): _clean(), fit_to_limit(), parse_round(), _on_linkedin(), source_names(), _ashby(), fetch_posting_text(), _get() (+11 more)

### Community 41 - "json"
Cohesion: 0.26
Nodes (11): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+3 more)

### Community 42 - "test_refill.py"
Cohesion: 0.12
Nodes (9): _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+1 more)

### Community 50 - "store.py"
Cohesion: 0.15
Nodes (5): q(), test_category(), test_prefill_uses_bank_and_flags_personal(), test_save_answers_remembers_personal_but_not_company_specific(), test_validate_by_kind()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 293 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `app.py`, `leads/cli.py`, `Region`, `notify.py`, `test_notes.py`, `find_startups`, `LeadStatus`, `assess_fit`, `run_followups`, `ai.py`, `workflows.py`, `browser.py`, `test_outreach.py`, `test_dashboard.py`, `test_scrape_stores_every_matching_non_workday_posting`, `find-founders.md`, `test_followups.py`, `test_leads.py`, `datetime`, `leads/schemas.py`, `re`, `test_refill.py`, `store.py`?**
  _High betweenness centrality (0.159) - this node is a cross-community bridge._
- **Are the 77 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 77 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05030643513789581 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `app.py`, `leads/cli.py`, `Region`, `test_notes.py`, `find_startups`, `run_followups`, `client.py`, `internship_agent/cli.py`, `get_settings`, `store.py`, `test_scrape_stores_every_matching_non_workday_posting`, `test_people.py`, `test_followups.py`, `leads/schemas.py`, `Lead`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14333333333333334 - nodes in this community are weakly interconnected._