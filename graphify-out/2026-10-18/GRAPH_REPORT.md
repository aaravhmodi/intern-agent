# Graph Report - winter-2027-internship-agent  (2026-10-18)

## Corpus Check
- 76 files · ~193,475 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1033 nodes · 2985 edges · 49 communities (39 shown, 10 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 526 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bdf40568`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_refill.py
- get_settings
- Region
- ai.py
- workflows.py
- test_people.py
- browser.py
- FakeToggle
- leads/cli.py
- test_followups.py
- test_dashboard.py
- internship_agent/cli.py
- re
- make_workflows.py
- test_leads.py
- FormQuestion
- app.py
- client.py
- mailbox.py
- scrape_jobs
- run_followups
- daily
- typing
- BaseModel
- run-application-campaign-2026-10-16.sh
- find-founders.md
- x_search.py
- Lead
- _TableParser
- PreparedAnswer
- store.py
- to_leads
- run-lowest-30-applications.sh
- find_startups
- load_resume_text
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- README.md
- leads/schemas.py
- test_outreach.py
- Bot Auto application preview
- followups.py
- EmailStatus
- SentMessage
- test_application_browser.py

## God Nodes (most connected - your core abstractions)
1. `Lead` - 111 edges
2. `Settings` - 62 edges
3. `get_settings()` - 45 edges
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

## Communities (49 total, 10 thin omitted)

### Community 0 - "test_refill.py"
Cohesion: 0.16
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_refill_noop_when_enough_open(), test_to_lead_normalizes_url()

### Community 1 - "get_settings"
Cohesion: 0.14
Nodes (11): get_settings(), application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd() (+3 more)

### Community 2 - "Region"
Cohesion: 0.14
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 3 - "ai.py"
Cohesion: 0.19
Nodes (15): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+7 more)

### Community 4 - "workflows.py"
Cohesion: 0.13
Nodes (19): Settings, normalize(), answer_bank(), handle_note(), lead_store(), _log_xai(), NoteOutcome, _openai() (+11 more)

### Community 5 - "test_people.py"
Cohesion: 0.19
Nodes (10): fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), person(), test_a_linkedin_source_passes_without_being_fetched(), test_find_people_stores_them_and_keeps_them_when_a_later_search_finds_nobody() (+2 more)

### Community 6 - "browser.py"
Cohesion: 0.14
Nodes (12): apply_to_posting(), _field_label(), _fill_form(), _normalize(), _online_checks(), open_login_browser(), _posting_is_closed(), _react_select_answer() (+4 more)

### Community 7 - "FakeToggle"
Cohesion: 0.09
Nodes (6): FakeLocator, FakeToggle, test_hidden_recaptcha_support_nodes_do_not_block(), locator(), test_three_live_checks_before_submit(), locator()

### Community 8 - "leads/cli.py"
Cohesion: 0.19
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 9 - "test_followups.py"
Cohesion: 0.21
Nodes (17): emailed(), FakeMailbox, outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 10 - "test_dashboard.py"
Cohesion: 0.14
Nodes (13): dashboard(), client(), test_auto_apply_prepares_then_submits(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment() (+5 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "re"
Cohesion: 0.06
Nodes (24): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), _clean(), fit_to_limit(), _slug(), _on_linkedin() (+16 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.15
Nodes (11): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+3 more)

### Community 14 - "test_leads.py"
Cohesion: 0.27
Nodes (14): fit(), lead(), posting(), test_email_needs_status_and_valid_format(), test_fit_assessment_bounds(), test_guess_email_rejects_bad_input(), test_invalid_x_handle_rejected(), test_key_is_stable_slug() (+6 more)

### Community 15 - "FormQuestion"
Cohesion: 0.24
Nodes (7): _answer_for(), AnswerBank, prefill(), FormQuestion, test_answer_mapping_uses_saved_answer_for_live_form_fields(), test_short_country_label_does_not_match_work_authorization_answer(), test_refresh_uses_saved_answer_without_regenerating_cover_letter()

### Community 16 - "app.py"
Cohesion: 0.05
Nodes (53): Send email safeguards, allow_retry(), AnswerEdit, auto_apply(), daily_run(), delete_preference(), draft(), find_more() (+45 more)

### Community 17 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 18 - "mailbox.py"
Cohesion: 0.21
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 19 - "scrape_jobs"
Cohesion: 0.29
Nodes (6): is_workday(), open_postings(), refill(), scrape_jobs(), startup_postings(), test_refill_tops_up_and_never_readds_applied_or_skipped()

### Community 20 - "run_followups"
Cohesion: 0.12
Nodes (9): Internship tracker: follow-ups (weekdays 9:30 AM), FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+1 more)

### Community 21 - "daily"
Cohesion: 0.22
Nodes (5): daily(), DailyReport, _incompatible_term(), _run_ai_cost(), submit_application()

### Community 22 - "typing"
Cohesion: 0.07
Nodes (33): category(), common_questions(), match_option(), validate(), QuestionKind, _clip(), _fit_bytes(), posting_push() (+25 more)

### Community 23 - "BaseModel"
Cohesion: 0.29
Nodes (3): FitResult, OutreachDraft, OutreachDraftResult

### Community 25 - "find-founders.md"
Cohesion: 0.09
Nodes (14): Founder lead JSON written to data/leads-inbox.json, Output, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Output, Rules, Segment: early, mid or big (+6 more)

### Community 26 - "x_search.py"
Cohesion: 0.14
Nodes (8): search_startups(), StartupFinding, post_confirms(), post_id(), post_text(), search_x_raises(), _tool_usage(), test_only_a_link_to_a_post_has_a_post_id()

### Community 27 - "Lead"
Cohesion: 0.23
Nodes (4): Lead, LeadStore, test_retry_reopens_only_uncertain_applications(), test_store_round_trip_and_upsert()

### Community 29 - "PreparedAnswer"
Cohesion: 0.19
Nodes (13): PreparedAnswer, FakeField, FakePage, posting(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+5 more)

### Community 30 - "store.py"
Cohesion: 0.47
Nodes (3): _identity(), merge(), normalize_url()

### Community 31 - "to_leads"
Cohesion: 0.28
Nodes (4): to_leads(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 33 - "find_startups"
Cohesion: 0.19
Nodes (11): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, Segment, effective_segment(), to_people(), find_people() (+3 more)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 41 - "README.md"
Cohesion: 0.06
Nodes (30): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+22 more)

### Community 43 - "leads/schemas.py"
Cohesion: 0.08
Nodes (18): apply_violations(), _normalize(), PreferenceStore, Note, Preference, PreferenceEffect, Verdict, posting() (+10 more)

### Community 48 - "test_outreach.py"
Cohesion: 0.13
Nodes (17): _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever(), OpenRole (+9 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 51 - "followups.py"
Cohesion: 0.20
Nodes (7): company_domain(), first_name(), followup_body(), is_due(), last_contact(), reply_subject(), test_a_reply_keeps_the_thread_subject_and_free_mail_is_not_a_company()

### Community 52 - "EmailStatus"
Cohesion: 0.21
Nodes (8): _email_line(), render_outreach(), EmailStatus, check_outreach_text(), check_send(), SendBlocked, test_render_outreach_flags_unverified_emails_and_skips_undrafted(), test_check_send_blocks_unconfirmed_guess_and_resends()

### Community 56 - "test_application_browser.py"
Cohesion: 0.12
Nodes (10): _numeric_answer(), _post_submit_outcome(), test_answer_mapping_requires_unambiguous_question_match(), test_bachelor_degree_maps_to_greenhouse_degree_choice(), test_closed_posting_text_is_detected(), test_field_label_does_not_expose_generated_lever_field_ids(), test_numeric_input_format_uses_saved_salary_and_study_values(), test_post_submit_invalid_and_challenge_states() (+2 more)

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 328 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_refill.py`, `Region`, `ai.py`, `workflows.py`, `browser.py`, `leads/cli.py`, `test_followups.py`, `test_dashboard.py`, `re`, `test_leads.py`, `FormQuestion`, `app.py`, `scrape_jobs`, `run_followups`, `daily`, `typing`, `BaseModel`, `find-founders.md`, `PreparedAnswer`, `store.py`, `to_leads`, `find_startups`, `test_daily_campaign.py`, `leads/schemas.py`, `test_outreach.py`, `followups.py`, `EmailStatus`?**
  _High betweenness centrality (0.147) - this node is a cross-community bridge._
- **Are the 80 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 80 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `get_settings` be split into smaller, more focused modules?**
  _Cohesion score 0.13768115942028986 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `workflows.py` to `get_settings`, `Region`, `find_startups`, `test_people.py`, `leads/cli.py`, `test_daily_campaign.py`, `test_followups.py`, `internship_agent/cli.py`, `leads/schemas.py`, `make_workflows.py`, `FormQuestion`, `app.py`, `client.py`, `scrape_jobs`, `run_followups`, `daily`, `typing`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14333333333333334 - nodes in this community are weakly interconnected._