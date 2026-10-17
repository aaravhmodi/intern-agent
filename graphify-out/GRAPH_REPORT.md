# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 72 files · ~123,788 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 967 nodes · 2812 edges · 48 communities (37 shown, 11 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 493 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fb174e45`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- leads/cli.py
- Region
- test_daily_campaign.py
- notify.py
- workflows.py
- test_application_browser.py
- ai.py
- FakeLocator
- Settings
- client.py
- internship_agent/cli.py
- x_search.py
- make_workflows.py
- answers.py
- test_ai.py
- browser.py
- send_email
- startups.py
- find_startups
- test_dashboard.py
- search_startups
- FormQuestion
- leads/schemas.py
- run-application-campaign-2026-10-16.sh
- find-founders.md
- Lead
- test_x_search.py
- followups_cmd
- test_people.py
- find-internships.md
- AGENTS.md
- mailbox.py
- candidate_context.md
- re
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- rank
- load_resume_text
- fit_to_limit
- LeadStatus
- test_regions_of
- _TableParser
- Segment
- _numeric_answer

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

## Communities (48 total, 11 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.05
Nodes (73): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume, Big-company postings from the SimplifyJobs off-season list, Current setup (+65 more)

### Community 1 - "leads/cli.py"
Cohesion: 0.16
Nodes (13): browser_login(), daily_cmd(), _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), prepare_all_cmd() (+5 more)

### Community 2 - "Region"
Cohesion: 0.16
Nodes (9): Region, normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), to_lead() (+1 more)

### Community 3 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 4 - "notify.py"
Cohesion: 0.18
Nodes (15): application_campaign(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 5 - "workflows.py"
Cohesion: 0.06
Nodes (29): is_workday(), open_postings(), refill(), merge(), fetch(), _ashby(), board_slugs(), find_intern_roles() (+21 more)

### Community 6 - "test_application_browser.py"
Cohesion: 0.17
Nodes (14): _fill_form(), PreparedAnswer, FakeField, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_defers_react_select_input_to_combobox_pass() (+6 more)

### Community 7 - "ai.py"
Cohesion: 0.22
Nodes (12): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+4 more)

### Community 8 - "FakeLocator"
Cohesion: 0.14
Nodes (5): FakeLocator, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 9 - "Settings"
Cohesion: 0.05
Nodes (37): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+29 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (34): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+26 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): dashboard(), inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run() (+2 more)

### Community 12 - "x_search.py"
Cohesion: 0.16
Nodes (8): StartupFinding, StartupFindings, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "answers.py"
Cohesion: 0.14
Nodes (8): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 15 - "test_ai.py"
Cohesion: 0.18
Nodes (8): FitResult, OutreachDraft, OutreachDraftResult, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact()

### Community 16 - "browser.py"
Cohesion: 0.14
Nodes (13): apply_to_posting(), _field_label(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _save_submission_diagnostic(), SubmissionResult (+5 more)

### Community 17 - "send_email"
Cohesion: 0.16
Nodes (7): Send email safeguards, build_message(), MailError, send(), send_email(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 18 - "startups.py"
Cohesion: 0.28
Nodes (3): _fold(), mentions(), names()

### Community 19 - "find_startups"
Cohesion: 0.14
Nodes (11): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, _on_linkedin(), source_names(), to_people(), page_names() (+3 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.17
Nodes (11): client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill(), test_send_guess_requires_confirmation_then_records() (+3 more)

### Community 21 - "search_startups"
Cohesion: 0.40
Nodes (3): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), search_startups()

### Community 22 - "FormQuestion"
Cohesion: 0.16
Nodes (18): category(), common_questions(), FormQuestion, QuestionKind, ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions() (+10 more)

### Community 23 - "leads/schemas.py"
Cohesion: 0.27
Nodes (5): LeadKind, Round, Verdict, parse_round(), test_parse_round()

### Community 25 - "find-founders.md"
Cohesion: 0.24
Nodes (6): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, export_drafts(), import_leads()

### Community 26 - "Lead"
Cohesion: 0.08
Nodes (26): _email_line(), render_outreach(), EmailStatus, Lead, check_outreach_text(), check_send(), SendBlocked, _identity() (+18 more)

### Community 27 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 28 - "followups_cmd"
Cohesion: 0.28
Nodes (3): apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 29 - "test_people.py"
Cohesion: 0.36
Nodes (5): person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody(), test_search_people_asks_for_roles_that_suit_the_company_size(), test_to_people_keeps_distinct_sourced_people_other_than_the_main_contact()

### Community 30 - "find-internships.md"
Cohesion: 0.29
Nodes (4): Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look

### Community 32 - "mailbox.py"
Cohesion: 0.17
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 33 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 34 - "re"
Cohesion: 0.14
Nodes (15): Output, Output, _clean(), guess_email(), _slug(), _ashby(), fetch_posting_text(), _get() (+7 more)

### Community 40 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 43 - "LeadStatus"
Cohesion: 0.15
Nodes (16): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference, PreferenceEffect (+8 more)

### Community 45 - "_TableParser"
Cohesion: 0.18
Nodes (3): parse(), Posting, _TableParser

### Community 47 - "Segment"
Cohesion: 0.23
Nodes (10): Segment, effective_segment(), to_leads(), finding(), lead(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents() (+2 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 297 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `app.py`, `leads/cli.py`, `Region`, `test_daily_campaign.py`, `notify.py`, `workflows.py`, `test_application_browser.py`, `ai.py`, `Settings`, `answers.py`, `test_ai.py`, `browser.py`, `send_email`, `startups.py`, `find_startups`, `test_dashboard.py`, `FormQuestion`, `leads/schemas.py`, `find-founders.md`, `find-internships.md`, `rank`, `LeadStatus`, `Segment`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `app.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05086390992040381 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `app.py`, `leads/cli.py`, `test_daily_campaign.py`, `workflows.py`, `client.py`, `internship_agent/cli.py`, `LeadStatus`, `make_workflows.py`, `answers.py`, `send_email`, `find_startups`, `FormQuestion`, `test_people.py`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_daily_campaign.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11462450592885376 - nodes in this community are weakly interconnected._