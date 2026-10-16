# Graph Report - winter-2027-internship-agent  (2026-10-16)

## Corpus Check
- 68 files · ~87,588 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 94 file(s) not represented in the graph (top: (none) 78, .log 5, .old 5)

## Summary
- 887 nodes · 2588 edges · 42 communities (33 shown, 9 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 434 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1c7805e4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Segment
- workflows.py
- startups.py
- leads/schemas.py
- re
- ai.py
- Region
- run_followups
- send_email
- test_followups.py
- test_application_browser.py
- internship_agent/cli.py
- mailbox.py
- make_workflows.py
- app.py
- test_dashboard.py
- Lead
- store.py
- OutlookClient
- x_search.py
- outlook/schemas.py
- EmailStatus
- leads/cli.py
- tracking.py
- client.py
- ToolSession
- test_leads.py
- test_interview_events
- followups.py
- FakeMailbox
- test_x_search.py
- find_startups
- internship-agent
- Mailbox
- candidate_context.md
- startup_jobs.py
- _TableParser
- search_startups
- OutreachDraft

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

## Communities (42 total, 9 thin omitted)

### Community 0 - "Segment"
Cohesion: 0.30
Nodes (8): Segment, to_leads(), finding(), lead(), test_effective_segment(), test_mentions_requires_company_and_founder_ignoring_accents(), test_to_leads_filters_age_stage_and_unverifiable_sources(), test_to_leads_sets_region_and_drops_bad_handle()

### Community 1 - "workflows.py"
Cohesion: 0.16
Nodes (15): Settings, common_questions(), answer_bank(), handle_note(), lead_store(), _log_xai(), NoteOutcome, _openai() (+7 more)

### Community 2 - "startups.py"
Cohesion: 0.22
Nodes (5): _fold(), mentions(), names(), page_names(), source_confirms()

### Community 3 - "leads/schemas.py"
Cohesion: 0.13
Nodes (10): ApplicationPrep, FitAssessment, FitResult, OutreachDraftResult, Round, Verdict, parse_round(), test_assess_fit_sends_resume_and_lead_and_validates() (+2 more)

### Community 4 - "re"
Cohesion: 0.06
Nodes (47): _answer_for(), _fill_form(), _normalize(), SubmissionResult, AnswerBank, category(), match_option(), normalize() (+39 more)

### Community 5 - "ai.py"
Cohesion: 0.09
Nodes (31): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+23 more)

### Community 6 - "Region"
Cohesion: 0.14
Nodes (11): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+3 more)

### Community 7 - "run_followups"
Cohesion: 0.15
Nodes (10): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+2 more)

### Community 8 - "send_email"
Cohesion: 0.16
Nodes (7): Send email safeguards, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 9 - "test_followups.py"
Cohesion: 0.22
Nodes (16): emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded(), test_a_follow_up_is_due_five_days_after_the_last_email() (+8 more)

### Community 10 - "test_application_browser.py"
Cohesion: 0.14
Nodes (11): _supported_url(), FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_fill_form_blocks_unanswered_required_questions() (+3 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.12
Nodes (11): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+3 more)

### Community 12 - "mailbox.py"
Cohesion: 0.20
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "app.py"
Cohesion: 0.06
Nodes (60): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume (+52 more)

### Community 15 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 16 - "Lead"
Cohesion: 0.19
Nodes (11): apply_to_posting(), is_workday(), open_postings(), refill(), Lead, LeadKind, to_lead(), daily() (+3 more)

### Community 17 - "store.py"
Cohesion: 0.13
Nodes (9): _identity(), merge(), normalize_url(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open() (+1 more)

### Community 18 - "OutlookClient"
Cohesion: 0.20
Nodes (8): OutlookClient, OutlookError, CalendarEvent, FakeSession, test_calendar_view_parses_events(), test_search_messages_quotes_query_and_sorts_newest_first(), test_tool_error_raises(), test_write_tools_are_blocked()

### Community 19 - "x_search.py"
Cohesion: 0.15
Nodes (8): StartupFinding, _slug(), post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 20 - "outlook/schemas.py"
Cohesion: 0.39
Nodes (7): DateTimeTimeZone, EmailAddress, GraphEventPage, GraphMessagePage, _GraphModel, Location, Recipient

### Community 21 - "EmailStatus"
Cohesion: 0.31
Nodes (5): EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 22 - "leads/cli.py"
Cohesion: 0.05
Nodes (35): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+27 more)

### Community 23 - "tracking.py"
Cohesion: 0.20
Nodes (12): MailMessage, application_updates(), ApplicationUpdate, classify_text(), guess_company(), Stage, to_update(), message() (+4 more)

### Community 24 - "client.py"
Cohesion: 0.15
Nodes (4): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only)

### Community 26 - "test_leads.py"
Cohesion: 0.07
Nodes (31): Output, Output, _clean(), guess_email(), LeadStore, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing() (+23 more)

### Community 28 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 34 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 36 - "find_startups"
Cohesion: 0.22
Nodes (8): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups(), people_at()

### Community 40 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 41 - "startup_jobs.py"
Cohesion: 0.10
Nodes (12): Internship agent coding instructions, _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles() (+4 more)

### Community 44 - "search_startups"
Cohesion: 0.33
Nodes (3): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups()

### Community 46 - "OutreachDraft"
Cohesion: 0.17
Nodes (4): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary(), test_linkedin_note_never_exceeds_200_chars()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 262 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `Segment`, `workflows.py`, `startups.py`, `leads/schemas.py`, `re`, `ai.py`, `Region`, `run_followups`, `send_email`, `test_followups.py`, `test_application_browser.py`, `app.py`, `test_dashboard.py`, `store.py`, `x_search.py`, `EmailStatus`, `leads/cli.py`, `test_leads.py`, `followups.py`, `find_startups`, `OutreachDraft`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/schemas.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13043478260869565 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `find_startups`, `re`, `Region`, `run_followups`, `send_email`, `test_followups.py`, `ai.py`, `internship_agent/cli.py`, `app.py`, `Lead`, `leads/cli.py`, `client.py`, `test_leads.py`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `re` be split into smaller, more focused modules?**
  _Cohesion score 0.058823529411764705 - nodes in this community are weakly interconnected._