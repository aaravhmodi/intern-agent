# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 75 files · ~191,905 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1014 nodes · 2924 edges · 47 communities (39 shown, 8 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 512 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5827cf6b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _view
- get_settings
- Region
- README.md
- workflows.py
- datetime
- re
- Lead
- store.py
- Settings
- tracking.py
- internship_agent/cli.py
- typing
- make_workflows.py
- posting_text.py
- leads/cli.py
- app.py
- OutlookClient
- startups.py
- find_startups
- test_dashboard.py
- find-founders.md
- json
- Segment
- run-application-campaign-2026-10-16.sh
- sending.py
- test_leads.py
- find-internships.md
- startup_jobs.py
- find_more_postings
- outlook/schemas.py
- _TableParser
- leads/schemas.py
- client.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- ranking.py
- ai.py
- export_drafts
- send_email
- candidate_context.md
- search_startups
- Bot Auto application preview

## God Nodes (most connected - your core abstractions)
1. `Lead` - 110 edges
2. `Settings` - 62 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 27 edges
8. `FormQuestion` - 26 edges
9. `Region` - 25 edges
10. `Segment` - 24 edges

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

## Communities (47 total, 8 thin omitted)

### Community 0 - "_view"
Cohesion: 0.18
Nodes (17): daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), _get(), KeyRequest, leads() (+9 more)

### Community 1 - "get_settings"
Cohesion: 0.16
Nodes (9): get_settings(), browser_login(), daily_cmd(), find_more(), mark_lead(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd() (+1 more)

### Community 2 - "Region"
Cohesion: 0.15
Nodes (11): Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching(), parse() (+3 more)

### Community 3 - "README.md"
Cohesion: 0.10
Nodes (28): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+20 more)

### Community 4 - "workflows.py"
Cohesion: 0.09
Nodes (22): answer_bank(), daily(), DailyReport, find_people(), handle_note(), _incompatible_term(), lead_store(), NoteOutcome (+14 more)

### Community 5 - "datetime"
Cohesion: 0.31
Nodes (3): FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first()

### Community 6 - "re"
Cohesion: 0.05
Nodes (43): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+35 more)

### Community 7 - "Lead"
Cohesion: 0.27
Nodes (3): Lead, LeadStore, test_store_round_trip_and_upsert()

### Community 8 - "store.py"
Cohesion: 0.12
Nodes (11): _identity(), merge(), normalize_url(), test_merge_keeps_existing_and_dedupes_incoming(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query() (+3 more)

### Community 9 - "Settings"
Cohesion: 0.05
Nodes (38): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+30 more)

### Community 10 - "tracking.py"
Cohesion: 0.17
Nodes (13): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+3 more)

### Community 12 - "typing"
Cohesion: 0.13
Nodes (10): StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising() (+2 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "posting_text.py"
Cohesion: 0.08
Nodes (16): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _ashby(), fetch_posting_text(), _get(), _greenhouse() (+8 more)

### Community 15 - "leads/cli.py"
Cohesion: 0.23
Nodes (7): _draft(), draft_all(), draft_lead(), _openai(), _resume(), _store(), load_resume_text()

### Community 16 - "app.py"
Cohesion: 0.18
Nodes (12): AnswerEdit, FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, NoteRequest, PreferenceDelete, SaveAnswersRequest (+4 more)

### Community 17 - "OutlookClient"
Cohesion: 0.21
Nodes (6): OutlookClient, OutlookError, ToolSession, CalendarEvent, test_tool_error_raises(), test_write_tools_are_blocked()

### Community 18 - "startups.py"
Cohesion: 0.19
Nodes (6): Search for recently funded startups (last 60 days; Canada, USA, Europe), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 19 - "find_startups"
Cohesion: 0.23
Nodes (7): LeadKind, effective_segment(), to_people(), find_startups(), people_at(), _log_xai(), startup_postings()

### Community 20 - "test_dashboard.py"
Cohesion: 0.17
Nodes (11): client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill(), test_send_guess_requires_confirmation_then_records() (+3 more)

### Community 21 - "find-founders.md"
Cohesion: 0.19
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), score_leads(), load_inbox()

### Community 22 - "json"
Cohesion: 0.07
Nodes (38): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+30 more)

### Community 23 - "Segment"
Cohesion: 0.16
Nodes (13): Round, Segment, parse_round(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+5 more)

### Community 25 - "sending.py"
Cohesion: 0.31
Nodes (4): check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 26 - "test_leads.py"
Cohesion: 0.29
Nodes (13): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+5 more)

### Community 27 - "find-internships.md"
Cohesion: 0.13
Nodes (9): Output, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big, Where to look, _clean(), guess_email() (+1 more)

### Community 28 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 29 - "find_more_postings"
Cohesion: 0.40
Nodes (4): Big-company postings from the SimplifyJobs off-season list, open_postings(), refill(), find_more_postings()

### Community 30 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 32 - "leads/schemas.py"
Cohesion: 0.18
Nodes (8): _email_line(), render_outreach(), fit_to_limit(), EmailStatus, OutreachDraft, Verdict, test_render_outreach_flags_unverified_emails_and_skips_undrafted(), test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 33 - "client.py"
Cohesion: 0.16
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (15): ApplicationPrep, FitAssessment, _slug(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load() (+7 more)

### Community 41 - "ranking.py"
Cohesion: 0.28
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 43 - "ai.py"
Cohesion: 0.05
Nodes (48): More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note() (+40 more)

### Community 45 - "export_drafts"
Cohesion: 0.21
Nodes (5): application_campaign(), apply_cmd(), export_drafts(), find_startups_cmd(), followups_cmd()

### Community 47 - "send_email"
Cohesion: 0.09
Nodes (8): Internship agent coding instructions, Send email safeguards, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 48 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 317 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `_view`, `Region`, `workflows.py`, `re`, `store.py`, `Settings`, `leads/cli.py`, `app.py`, `startups.py`, `find_startups`, `test_dashboard.py`, `find-founders.md`, `json`, `Segment`, `sending.py`, `test_leads.py`, `find-internships.md`, `find_more_postings`, `leads/schemas.py`, `test_daily_campaign.py`, `ranking.py`, `ai.py`, `send_email`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14855072463768115 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `client.py`, `get_settings`, `Region`, `workflows.py`, `test_daily_campaign.py`, `internship_agent/cli.py`, `ai.py`, `make_workflows.py`, `send_email`, `leads/cli.py`, `find_startups`, `json`, `find_more_postings`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.10344827586206896 - nodes in this community are weakly interconnected._