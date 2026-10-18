# Graph Report - winter-2027-internship-agent  (2026-10-18)

## Corpus Check
- 76 files · ~193,974 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1043 nodes · 3018 edges · 51 communities (37 shown, 14 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 531 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2ffc94db`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- typing
- get_settings
- Region
- ai.py
- workflows.py
- app.py
- browser.py
- FakeToggle
- leads/cli.py
- Settings
- test_leads.py
- internship_agent/cli.py
- re
- make_workflows.py
- PreparedAnswer
- FormQuestion
- _view
- client.py
- mailbox.py
- daily
- run_followups
- mailer.py
- answers.py
- startups.py
- run-application-campaign-2026-10-16.sh
- find-founders.md
- x_search.py
- Lead
- _TableParser
- test_application_browser.py
- followups_cmd
- candidate_context.md
- run-lowest-30-applications.sh
- leads/schemas.py
- fit_to_limit
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- README.md
- test_hidden_recaptcha_support_nodes_do_not_block
- LeadStatus
- test_outreach.py
- Bot Auto application preview
- followups.py
- send_email
- FakeMailbox
- _field_label

## God Nodes (most connected - your core abstractions)
1. `Lead` - 113 edges
2. `Settings` - 62 edges
3. `get_settings()` - 47 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `prepare_application()` - 29 edges
7. `FormQuestion` - 27 edges
8. `find_startups()` - 27 edges
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

## Communities (51 total, 14 thin omitted)

### Community 0 - "typing"
Cohesion: 0.14
Nodes (6): merge(), posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 1 - "get_settings"
Cohesion: 0.15
Nodes (9): open_login_browser(), get_settings(), browser_login(), daily_cmd(), find_more(), mark_lead(), prepare_cmd(), scrape_jobs_cmd() (+1 more)

### Community 2 - "Region"
Cohesion: 0.13
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 3 - "ai.py"
Cohesion: 0.05
Nodes (37): Internship agent coding instructions, More people to connect with, chosen by company size, AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences() (+29 more)

### Community 4 - "workflows.py"
Cohesion: 0.07
Nodes (20): load_resume_text(), answer_bank(), find_people(), find_startups(), _incompatible_term(), _log_xai(), _openai(), prepare_application() (+12 more)

### Community 5 - "app.py"
Cohesion: 0.11
Nodes (17): AnswerEdit, application_proof(), delete_preference(), FindMoreRequest, FindStartupsRequest, followups(), FollowupsRequest, note() (+9 more)

### Community 6 - "browser.py"
Cohesion: 0.12
Nodes (16): apply_to_posting(), _confirmation_quote(), _confirmed(), _normalize(), _online_checks(), _post_submit_outcome(), _posting_is_closed(), _react_select_answer() (+8 more)

### Community 8 - "leads/cli.py"
Cohesion: 0.21
Nodes (11): _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), _openai(), prepare_all_cmd(), _resume() (+3 more)

### Community 9 - "Settings"
Cohesion: 0.21
Nodes (16): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+8 more)

### Community 10 - "test_leads.py"
Cohesion: 0.06
Nodes (40): Output, Output, dashboard(), _clean(), guess_email(), _email_line(), render_outreach(), EmailStatus (+32 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "re"
Cohesion: 0.11
Nodes (25): _slug(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _ashby(), fetch_posting_text() (+17 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "PreparedAnswer"
Cohesion: 0.18
Nodes (16): category(), PreparedAnswer, _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push() (+8 more)

### Community 15 - "FormQuestion"
Cohesion: 0.24
Nodes (7): _answer_for(), AnswerBank, prefill(), FormQuestion, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 16 - "_view"
Cohesion: 0.19
Nodes (18): allow_retry(), auto_apply(), daily_run(), draft(), find_more(), find_more_startups(), _get(), KeyRequest (+10 more)

### Community 17 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 18 - "mailbox.py"
Cohesion: 0.07
Nodes (12): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), GmailMailbox, _imap_date(), MailboxError, _quoted() (+4 more)

### Community 19 - "daily"
Cohesion: 0.21
Nodes (8): is_workday(), open_postings(), refill(), daily(), DailyReport, scrape_jobs(), startup_postings(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 20 - "run_followups"
Cohesion: 0.11
Nodes (12): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+4 more)

### Community 21 - "mailer.py"
Cohesion: 0.21
Nodes (4): build_message(), send(), test_build_message_requires_fields(), test_build_message_with_attachment()

### Community 22 - "answers.py"
Cohesion: 0.16
Nodes (14): common_questions(), match_option(), normalize(), validate(), QuestionKind, q(), test_ashby_parser(), test_category() (+6 more)

### Community 23 - "startups.py"
Cohesion: 0.23
Nodes (5): _fold(), mentions(), names(), page_names(), source_confirms()

### Community 25 - "find-founders.md"
Cohesion: 0.12
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+4 more)

### Community 26 - "x_search.py"
Cohesion: 0.15
Nodes (8): StartupFinding, post_id(), search_x_raises(), _tool_usage(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 27 - "Lead"
Cohesion: 0.17
Nodes (5): Lead, _identity(), normalize_url(), test_post_submit_state_is_persisted_for_tracker(), test_normalize_url_keeps_meaningful_query()

### Community 29 - "test_application_browser.py"
Cohesion: 0.10
Nodes (21): _fill_form(), _numeric_answer(), FakeField, FakeLocator, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_closed_posting_text_is_detected() (+13 more)

### Community 30 - "followups_cmd"
Cohesion: 0.27
Nodes (4): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd()

### Community 31 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 33 - "leads/schemas.py"
Cohesion: 0.27
Nodes (6): LeadKind, Round, Segment, Verdict, effective_segment(), test_effective_segment()

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 41 - "README.md"
Cohesion: 0.11
Nodes (29): Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Screenshot: startups listed by fit score, round, amount, date and founder, Application answers prepared from the resume, Current setup (+21 more)

### Community 43 - "LeadStatus"
Cohesion: 0.16
Nodes (14): PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, posting() (+6 more)

### Community 48 - "test_outreach.py"
Cohesion: 0.18
Nodes (11): parse_round(), to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round() (+3 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 51 - "followups.py"
Cohesion: 0.25
Nodes (5): first_name(), followup_body(), is_due(), last_contact(), test_nobody_gets_a_third_or_one_after_replying_or_being_skipped()

### Community 52 - "send_email"
Cohesion: 0.17
Nodes (7): send(), SendRequest, check_outreach_text(), check_send(), SendBlocked, MailError, send_email()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 332 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `typing`, `Region`, `ai.py`, `workflows.py`, `app.py`, `browser.py`, `leads/cli.py`, `Settings`, `test_leads.py`, `PreparedAnswer`, `FormQuestion`, `_view`, `daily`, `run_followups`, `answers.py`, `startups.py`, `find-founders.md`, `test_application_browser.py`, `leads/schemas.py`, `test_daily_campaign.py`, `LeadStatus`, `test_outreach.py`, `followups.py`, `send_email`?**
  _High betweenness centrality (0.178) - this node is a cross-community bridge._
- **Are the 82 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 82 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.14166666666666666 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `Region`, `ai.py`, `workflows.py`, `app.py`, `leads/cli.py`, `internship_agent/cli.py`, `make_workflows.py`, `FormQuestion`, `_view`, `client.py`, `daily`, `run_followups`, `answers.py`, `Lead`, `test_daily_campaign.py`, `LeadStatus`, `config.py`, `send_email`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.1282051282051282 - nodes in this community are weakly interconnected._