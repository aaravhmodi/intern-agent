# Graph Report - winter-2027-internship-agent  (2026-10-19)

## Corpus Check
- 78 files · ~195,785 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1079 nodes · 3128 edges · 46 communities (37 shown, 9 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 541 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `854f5c40`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_refill.py
- get_settings
- simplify.py
- ai.py
- prepare_application
- app.py
- browser.py
- FakeField
- leads/cli.py
- form_d.py
- test_leads.py
- internship_agent/cli.py
- re
- make_workflows.py
- notify.py
- FormQuestion
- _view
- client.py
- verification_mail.py
- Lead
- Settings
- EmailStatus
- find-founders.md
- find_startups
- run-application-campaign-2026-10-16.sh
- find-internships.md
- test_x_search.py
- rank
- test_form_d.py
- test_application_browser.py
- followups_cmd
- _post_submit_outcome
- run-lowest-30-applications.sh
- leads/schemas.py
- OutreachDraft
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- README.md
- test_hidden_recaptcha_support_nodes_do_not_block
- Segment
- Bot Auto application preview
- send_email

## God Nodes (most connected - your core abstractions)
1. `Lead` - 116 edges
2. `Settings` - 63 edges
3. `get_settings()` - 48 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `prepare_application()` - 29 edges
7. `Segment` - 27 edges
8. `Region` - 27 edges
9. `FormQuestion` - 27 edges
10. `find_startups()` - 27 edges

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

## Communities (46 total, 9 thin omitted)

### Community 0 - "test_refill.py"
Cohesion: 0.18
Nodes (6): posting(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_refill_noop_when_enough_open(), test_refill_tops_up_and_never_readds_applied_or_skipped(), test_to_lead_normalizes_url()

### Community 1 - "get_settings"
Cohesion: 0.20
Nodes (7): get_settings(), browser_login(), daily_cmd(), find_more(), prepare_all_cmd(), prepare_cmd(), scrape_jobs_cmd()

### Community 2 - "simplify.py"
Cohesion: 0.09
Nodes (11): normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+3 more)

### Community 3 - "ai.py"
Cohesion: 0.05
Nodes (43): AnswerDraft, AnswerDrafts, assess_fit(), CompanySite, CoverLetterDraft, draft_outreach(), find_company_site(), format_preferences() (+35 more)

### Community 4 - "prepare_application"
Cohesion: 0.10
Nodes (15): common_questions(), answer_bank(), handle_note(), lead_store(), _openai(), prepare_application(), _record_openai_usage(), refresh_saved_application() (+7 more)

### Community 5 - "app.py"
Cohesion: 0.13
Nodes (14): AnswerEdit, application_proof(), delete_preference(), FindMoreRequest, followups(), FollowupsRequest, leads(), NoteRequest (+6 more)

### Community 6 - "browser.py"
Cohesion: 0.11
Nodes (18): apply_to_posting(), _confirmation_quote(), _confirmed(), _field_label(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+10 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 8 - "leads/cli.py"
Cohesion: 0.20
Nodes (9): _draft(), draft_all(), draft_lead(), _openai(), _resume(), score_leads(), show_lead(), _store() (+1 more)

### Community 9 - "form_d.py"
Cohesion: 0.17
Nodes (9): company_name(), Filing, filings(), form_d_paths(), _get(), index_url(), parse_filing(), _person() (+1 more)

### Community 10 - "test_leads.py"
Cohesion: 0.08
Nodes (33): dashboard(), LeadStore, client(), test_auto_apply_prepares_then_submits(), test_confirmation_screenshot_is_served_as_proof(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked() (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "re"
Cohesion: 0.08
Nodes (36): QuestionKind, _slug(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request(), _ashby() (+28 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.11
Nodes (13): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+5 more)

### Community 14 - "notify.py"
Cohesion: 0.18
Nodes (15): category(), _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers() (+7 more)

### Community 15 - "FormQuestion"
Cohesion: 0.15
Nodes (11): _answer_for(), AnswerBank, match_option(), normalize(), prefill(), validate(), FormQuestion, test_yes_no_answer_matches_long_select_options() (+3 more)

### Community 16 - "_view"
Cohesion: 0.14
Nodes (20): allow_retry(), auto_apply(), daily_run(), draft(), find_more(), find_more_startups(), _get(), KeyRequest (+12 more)

### Community 17 - "client.py"
Cohesion: 0.06
Nodes (36): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), run(), connect(), OutlookClient, OutlookError (+28 more)

### Community 18 - "verification_mail.py"
Cohesion: 0.10
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 19 - "Lead"
Cohesion: 0.12
Nodes (18): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), Lead, _identity(), merge(), fetch() (+10 more)

### Community 20 - "Settings"
Cohesion: 0.05
Nodes (38): Settings, FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site() (+30 more)

### Community 21 - "EmailStatus"
Cohesion: 0.18
Nodes (7): Output, Output, _clean(), guess_email(), EmailStatus, founder_email(), page_text()

### Community 22 - "find-founders.md"
Cohesion: 0.22
Nodes (7): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark, import_leads(), mark_lead(), load_inbox()

### Community 23 - "find_startups"
Cohesion: 0.09
Nodes (19): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, effective_segment(), _on_linkedin(), source_names(), to_people() (+11 more)

### Community 25 - "find-internships.md"
Cohesion: 0.15
Nodes (7): Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, export_drafts(), _email_line(), render_outreach()

### Community 26 - "test_x_search.py"
Cohesion: 0.47
Nodes (3): finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 27 - "rank"
Cohesion: 0.33
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 29 - "test_application_browser.py"
Cohesion: 0.20
Nodes (17): _fill_form(), PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_bachelor_degree_maps_to_greenhouse_degree_choice(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required() (+9 more)

### Community 30 - "followups_cmd"
Cohesion: 0.22
Nodes (5): application_campaign(), apply_cmd(), find_startups_cmd(), followups_cmd(), form_d_cmd()

### Community 31 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

### Community 33 - "leads/schemas.py"
Cohesion: 0.16
Nodes (10): FindStartupsRequest, LeadKind, Region, Round, Verdict, parse_round(), _fold(), mentions() (+2 more)

### Community 34 - "OutreachDraft"
Cohesion: 0.18
Nodes (3): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary()

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.10
Nodes (14): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+6 more)

### Community 41 - "README.md"
Cohesion: 0.06
Nodes (37): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+29 more)

### Community 48 - "Segment"
Cohesion: 0.18
Nodes (12): Segment, to_leads(), finding(), lead(), test_build_message_with_attachment(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars() (+4 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

### Community 52 - "send_email"
Cohesion: 0.14
Nodes (8): check_outreach_text(), check_send(), SendBlocked, build_message(), MailError, send(), send_email(), test_build_message_requires_fields()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 343 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `test_refill.py`, `simplify.py`, `ai.py`, `prepare_application`, `app.py`, `browser.py`, `leads/cli.py`, `form_d.py`, `test_leads.py`, `re`, `notify.py`, `FormQuestion`, `_view`, `Settings`, `find-founders.md`, `find_startups`, `find-internships.md`, `rank`, `test_application_browser.py`, `leads/schemas.py`, `OutreachDraft`, `test_daily_campaign.py`, `Segment`, `send_email`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Are the 83 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 83 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `simplify.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09425287356321839 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `get_settings`, `ai.py`, `prepare_application`, `app.py`, `leads/cli.py`, `test_daily_campaign.py`, `internship_agent/cli.py`, `re`, `make_workflows.py`, `FormQuestion`, `client.py`, `Lead`, `send_email`, `find_startups`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `ai.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05417236662106703 - nodes in this community are weakly interconnected._