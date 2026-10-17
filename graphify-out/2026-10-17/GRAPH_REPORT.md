# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~89,635 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 947 nodes · 2739 edges · 47 communities (33 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 473 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `710285d8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- run_followups
- leads/cli.py
- simplify.py
- startup_jobs.py
- answers.py
- LeadStatus
- workflows.py
- re
- followups.py
- test_followups.py
- tracking.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- ai.py
- SentMessage
- browser.py
- test_outreach.py
- candidate_context.md
- x_search.py
- test_dashboard.py
- leads/schemas.py
- OutlookClient
- Region
- run-application-campaign-2026-10-16.sh
- client.py
- Lead
- app.py
- AGENTS.md
- outlook/schemas.py
- startups.py
- _TableParser
- test_ai.py
- test_people.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- people.py
- Mailbox
- test_refill.py
- test_x_search.py
- fit_to_limit
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 107 edges
2. `Settings` - 55 edges
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
- `Rules learned from notes (skip, downrank, boost)` --references--> `interpret_note()`  [INFERRED]
  README.md → src/internship_agent/ai.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Automatic follow-ups on unanswered emails** — n8n_readme_followups_workflow, n8n_make_workflows_internship_followups, src_internship_agent_dashboard_app_followups, src_internship_agent_followup_run_run_followups [INFERRED 0.95]
- **Nothing is sent without the user's click** — agents_send_only_on_click, readme_send_email_safeguards, src_internship_agent_dashboard_index_email_section, src_internship_agent_dashboard_app_send, src_internship_agent_leads_sending_check_send [INFERRED 0.95]
- **Finding more people to connect with at a company** — readme_more_people, src_internship_agent_dashboard_index_people_section, src_internship_agent_dashboard_app_people, src_internship_agent_workflows_find_people, src_internship_agent_ai_search_people, src_internship_agent_sources_people_to_people [INFERRED 0.95]

## Communities (47 total, 14 thin omitted)

### Community 0 - "run_followups"
Cohesion: 0.17
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.05
Nodes (48): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+40 more)

### Community 2 - "simplify.py"
Cohesion: 0.14
Nodes (10): normalize_url(), cap_per_company(), fetch(), is_software_role(), matching(), parse(), Posting, to_lead() (+2 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "answers.py"
Cohesion: 0.06
Nodes (44): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), ApplicationPrep (+36 more)

### Community 5 - "LeadStatus"
Cohesion: 0.17
Nodes (14): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting() (+6 more)

### Community 6 - "workflows.py"
Cohesion: 0.13
Nodes (13): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), to_people(), DailyReport, find_people() (+5 more)

### Community 7 - "re"
Cohesion: 0.14
Nodes (15): Output, Output, _clean(), guess_email(), _slug(), _ashby(), fetch_posting_text(), _get() (+7 more)

### Community 8 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "ai.py"
Cohesion: 0.19
Nodes (14): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+6 more)

### Community 16 - "browser.py"
Cohesion: 0.06
Nodes (31): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+23 more)

### Community 17 - "test_outreach.py"
Cohesion: 0.23
Nodes (8): OutreachDraft, finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_regions_of(), test_to_leads_filters_age_stage_and_unverifiable_sources()

### Community 18 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 19 - "x_search.py"
Cohesion: 0.13
Nodes (9): search_startups(), StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage() (+1 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "leads/schemas.py"
Cohesion: 0.20
Nodes (6): LeadKind, Round, parse_round(), test_incompatible_eight_month_term_is_rejected(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_parse_round()

### Community 22 - "OutlookClient"
Cohesion: 0.20
Nodes (7): OutlookClient, OutlookError, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 23 - "Region"
Cohesion: 0.22
Nodes (8): Region, Segment, Verdict, region_from_text(), regions_of(), to_leads(), test_to_leads_sets_region_and_drops_bad_handle(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 25 - "client.py"
Cohesion: 0.15
Nodes (5): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), ToolSession

### Community 26 - "Lead"
Cohesion: 0.08
Nodes (25): _email_line(), render_outreach(), EmailStatus, Lead, _identity(), LeadStore, merge(), test_saving_answers_preserves_uncertain_submission() (+17 more)

### Community 27 - "app.py"
Cohesion: 0.05
Nodes (67): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder (+59 more)

### Community 29 - "outlook/schemas.py"
Cohesion: 0.26
Nodes (9): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient (+1 more)

### Community 30 - "startups.py"
Cohesion: 0.28
Nodes (3): _fold(), mentions(), names()

### Community 33 - "test_ai.py"
Cohesion: 0.27
Nodes (6): FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 34 - "test_people.py"
Cohesion: 0.27
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 40 - "people.py"
Cohesion: 0.24
Nodes (4): _on_linkedin(), source_names(), page_names(), source_confirms()

### Community 42 - "test_refill.py"
Cohesion: 0.17
Nodes (8): Big-company postings from the SimplifyJobs off-season list, refill(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 49 - "send_email"
Cohesion: 0.10
Nodes (11): Send email safeguards, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send(), send_email() (+3 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 290 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `run_followups`, `leads/cli.py`, `simplify.py`, `answers.py`, `LeadStatus`, `workflows.py`, `followups.py`, `test_followups.py`, `test_refill.py`, `ai.py`, `browser.py`, `send_email`, `test_outreach.py`, `test_dashboard.py`, `leads/schemas.py`, `Region`, `app.py`, `startups.py`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **Are the 76 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 76 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05030525030525031 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `leads/cli.py` to `run_followups`, `simplify.py`, `test_people.py`, `answers.py`, `LeadStatus`, `workflows.py`, `test_followups.py`, `internship_agent/cli.py`, `pathlib`, `send_email`, `client.py`, `Lead`, `app.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13852813852813853 - nodes in this community are weakly interconnected._