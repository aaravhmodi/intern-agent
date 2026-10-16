# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 72 files · ~88,560 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 922 nodes · 2661 edges · 55 communities (41 shown, 14 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 449 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `687804a0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- leads/cli.py
- re
- startup_jobs.py
- answers.py
- LeadStatus
- workflows.py
- run_followups
- mailer.py
- Settings
- OutlookClient
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- _view
- test_dashboard.py
- test_application_browser.py
- Segment
- test_x_search.py
- x_search.py
- FormQuestion
- assess_fit
- notify.py
- app.py
- run-application-campaign-2026-10-16.sh
- browser.py
- test_leads.py
- README.md
- followups.py
- tracking.py
- startups.py
- ai.py
- client.py
- SentMessage
- test_refill.py
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- json
- Lead
- Region
- draft_outreach
- test_people.py
- people.py
- outlook
- fit_to_limit
- send_email
- AGENTS.md
- Person
- _TableParser
- ApplicationPrep
- test_interview_events

## God Nodes (most connected - your core abstractions)
1. `Lead` - 101 edges
2. `Settings` - 53 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 33 edges
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

## Communities (55 total, 14 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.25
Nodes (6): EmailStatus, LeadKind, Round, Verdict, parse_round(), test_parse_round()

### Community 1 - "leads/cli.py"
Cohesion: 0.06
Nodes (36): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+28 more)

### Community 2 - "re"
Cohesion: 0.26
Nodes (10): _slug(), _ashby(), fetch_posting_text(), _get(), _greenhouse(), html_to_text(), _json(), _lever() (+2 more)

### Community 3 - "startup_jobs.py"
Cohesion: 0.28
Nodes (9): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+1 more)

### Community 4 - "answers.py"
Cohesion: 0.13
Nodes (12): AnswerBank, category(), match_option(), normalize(), prefill(), validate(), q(), test_category() (+4 more)

### Community 5 - "LeadStatus"
Cohesion: 0.15
Nodes (15): apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting(), settings() (+7 more)

### Community 6 - "workflows.py"
Cohesion: 0.10
Nodes (18): More people to connect with, chosen by company size, search_people(), effective_segment(), load_resume_text(), to_people(), answer_bank(), find_people(), find_startups() (+10 more)

### Community 7 - "run_followups"
Cohesion: 0.11
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 8 - "mailer.py"
Cohesion: 0.21
Nodes (5): build_message(), MailError, send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "Settings"
Cohesion: 0.21
Nodes (17): Settings, emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing() (+9 more)

### Community 10 - "OutlookClient"
Cohesion: 0.15
Nodes (8): OutlookClient, OutlookError, ToolSession, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "mailbox.py"
Cohesion: 0.16
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "_view"
Cohesion: 0.11
Nodes (24): Screenshot: rules learned from notes, two skip and one boost, Rules learned from notes (skip, downrank, boost), daily_run(), draft(), find_more_startups(), FindStartupsRequest, followups(), KeyRequest (+16 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "test_application_browser.py"
Cohesion: 0.15
Nodes (9): FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_uses_prepared_answers_and_uploads_resume() (+1 more)

### Community 17 - "Segment"
Cohesion: 0.21
Nodes (11): Segment, to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+3 more)

### Community 18 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 19 - "x_search.py"
Cohesion: 0.17
Nodes (5): search_startups(), StartupFinding, post_confirms(), search_x_raises(), _tool_usage()

### Community 20 - "FormQuestion"
Cohesion: 0.27
Nodes (11): common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+3 more)

### Community 21 - "assess_fit"
Cohesion: 0.29
Nodes (6): assess_fit(), FitResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates()

### Community 22 - "notify.py"
Cohesion: 0.20
Nodes (15): PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 23 - "app.py"
Cohesion: 0.15
Nodes (18): AnswerEdit, delete_preference(), find_more(), FindMoreRequest, FollowupsRequest, _get(), index(), leads() (+10 more)

### Community 25 - "browser.py"
Cohesion: 0.12
Nodes (14): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), open_login_browser(), _posting_is_closed() (+6 more)

### Community 26 - "test_leads.py"
Cohesion: 0.11
Nodes (22): Output, Output, _clean(), guess_email(), LeadStore, fit(), lead(), posting() (+14 more)

### Community 27 - "README.md"
Cohesion: 0.09
Nodes (26): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules (+18 more)

### Community 28 - "followups.py"
Cohesion: 0.25
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), test_the_follow_up_names_them_the_company_and_the_first_email()

### Community 29 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 30 - "startups.py"
Cohesion: 0.22
Nodes (4): _fold(), mentions(), names(), source_confirms()

### Community 31 - "ai.py"
Cohesion: 0.20
Nodes (13): AnswerDraft, AnswerDrafts, CoverLetterDraft, format_preferences(), interpret_note(), _lead_context(), NoteResult, PeopleFindings (+5 more)

### Community 32 - "client.py"
Cohesion: 0.20
Nodes (8): CalendarEvent, DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 34 - "test_refill.py"
Cohesion: 0.16
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 41 - "Lead"
Cohesion: 0.14
Nodes (13): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, _identity(), merge(), daily() (+5 more)

### Community 42 - "Region"
Cohesion: 0.15
Nodes (10): Region, normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse() (+2 more)

### Community 43 - "draft_outreach"
Cohesion: 0.18
Nodes (5): draft_outreach(), FitAssessment, OutreachDraft, OutreachDraftResult, test_draft_prompt_leads_with_upside_impact()

### Community 44 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 45 - "people.py"
Cohesion: 0.32
Nodes (3): _on_linkedin(), source_names(), page_names()

### Community 46 - "outlook"
Cohesion: 0.50
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 49 - "send_email"
Cohesion: 0.19
Nodes (8): Send email safeguards, send(), SendRequest, Email section with two-click send, check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 53 - "ApplicationPrep"
Cohesion: 0.20
Nodes (7): ApplicationPrep, test_application_submission_is_disabled(), test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_pre_submit_block_can_be_retried_but_uncertain_cannot(), test_scrape_stores_every_matching_non_workday_posting()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 276 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `leads/cli.py`, `answers.py`, `LeadStatus`, `workflows.py`, `run_followups`, `Settings`, `_view`, `test_dashboard.py`, `test_application_browser.py`, `Segment`, `assess_fit`, `notify.py`, `app.py`, `browser.py`, `test_leads.py`, `followups.py`, `startups.py`, `ai.py`, `test_refill.py`, `json`, `Region`, `draft_outreach`, `send_email`, `ApplicationPrep`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/cli.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06479113384484228 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `client.py`, `leads/cli.py`, `answers.py`, `LeadStatus`, `workflows.py`, `run_followups`, `Lead`, `internship_agent/cli.py`, `test_people.py`, `make_workflows.py`, `_view`, `config.py`, `send_email`, `ApplicationPrep`, `app.py`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 44 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 44 INFERRED edges - model-reasoned connections that need verification._
- **Should `answers.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13227513227513227 - nodes in this community are weakly interconnected._