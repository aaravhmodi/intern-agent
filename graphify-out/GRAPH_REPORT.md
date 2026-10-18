# Graph Report - winter-2027-internship-agent  (2026-10-18)

## Corpus Check
- 76 files · ~193,047 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 1039 nodes · 2996 edges · 52 communities (36 shown, 16 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 522 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `71403c54`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- leads/schemas.py
- command
- Region
- candidate_context.md
- workflows.py
- test_daily_campaign.py
- browser.py
- FakeField
- startups.py
- Settings
- fit_to_limit
- internship_agent/cli.py
- startup_jobs.py
- make_workflows.py
- verification_mail.py
- leads/cli.py
- app.py
- client.py
- notify.py
- Lead
- LeadStatus
- x_search.py
- FormQuestion
- test_outreach.py
- run-application-campaign-2026-10-16.sh
- run_followups
- re
- find-founders.md
- mailbox.py
- test_application_browser.py
- test_notes.py
- followups.py
- run-lowest-30-applications.sh
- FakeMailbox
- _TableParser
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_leads.py
- ranking.py
- _post_submit_outcome
- ai.py
- _use_gmail_for_applications
- test_hidden_recaptcha_support_nodes_do_not_block
- send_email
- open_login_browser
- export.py
- Bot Auto application preview
- _run_ai_cost

## God Nodes (most connected - your core abstractions)
1. `Lead` - 110 edges
2. `Settings` - 62 edges
3. `get_settings()` - 46 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `prepare_application()` - 28 edges
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

## Communities (52 total, 16 thin omitted)

### Community 0 - "leads/schemas.py"
Cohesion: 0.14
Nodes (8): LeadKind, Verdict, merge(), normalize_url(), test_matching_by_region_includes_us_and_europe(), test_merge_dedupes_same_posting_with_different_key(), test_normalize_url_keeps_meaningful_query(), test_to_lead_normalizes_url()

### Community 1 - "command"
Cohesion: 0.16
Nodes (7): application_campaign(), apply_cmd(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd(), scrape_jobs_cmd()

### Community 2 - "Region"
Cohesion: 0.14
Nodes (12): Big-company postings from the SimplifyJobs off-season list, Region, region_from_text(), regions_of(), cap_per_company(), fetch(), is_software_role(), matching() (+4 more)

### Community 3 - "candidate_context.md"
Cohesion: 0.22
Nodes (8): Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume), Writing and answering rules

### Community 4 - "workflows.py"
Cohesion: 0.12
Nodes (17): More people to connect with, chosen by company size, PersonFinding, search_people(), Person, Segment, effective_segment(), to_people(), find_people() (+9 more)

### Community 5 - "test_daily_campaign.py"
Cohesion: 0.06
Nodes (23): ApplicationPrep, FitAssessment, fake_client(), FakeResponses, test_assess_fit_raises_when_model_returns_nothing(), test_assess_fit_sends_resume_and_lead_and_validates(), test_draft_prompt_leads_with_upside_impact(), test_campaign_stops_after_target_confirmed_submissions() (+15 more)

### Community 6 - "browser.py"
Cohesion: 0.12
Nodes (17): apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), _posting_is_closed(), _react_select_answer() (+9 more)

### Community 7 - "FakeField"
Cohesion: 0.09
Nodes (5): FakeField, FakeLocator, FakeToggle, test_three_live_checks_before_submit(), locator()

### Community 8 - "startups.py"
Cohesion: 0.17
Nodes (6): _fold(), mentions(), names(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder()

### Community 9 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.16
Nodes (7): inbox(), run(), interviews(), outlook_login(), outlook_status(), run(), _run()

### Community 12 - "startup_jobs.py"
Cohesion: 0.12
Nodes (15): Screenshot: startups listed by fit score, round, amount, date and founder, Search for recently funded startups (last 60 days; Canada, USA, Europe), _on_linkedin(), source_names(), _ashby(), board_slugs(), find_intern_roles(), _greenhouse() (+7 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.16
Nodes (10): install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it, Changing a workflow: edit make_workflows.py, regenerate, push, run install.sh, Internship tracker: follow-ups (weekdays 9:30 AM) (+2 more)

### Community 14 - "verification_mail.py"
Cohesion: 0.10
Nodes (8): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), message(), test_extracts_greenhouse_mail_code_after_application_label(), test_extracts_only_fresh_greenhouse_code_for_the_application_inbox(), test_mail_poll_refreshes_inbox_until_new_code_arrives()

### Community 15 - "leads/cli.py"
Cohesion: 0.17
Nodes (10): _draft(), draft_all(), draft_lead(), mark_lead(), _openai(), prepare_all_cmd(), _resume(), show_lead() (+2 more)

### Community 16 - "app.py"
Cohesion: 0.05
Nodes (73): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, Screenshot: prepared application answers, one marked 'Needs you', Demo recording: a startup's fit and draft, a posting's answers, the learned rules, Screenshot: an email draft and a LinkedIn connection note (175/200) for a founder, Screenshot: a startup's fit score (91, strong), reasons and talking points, Screenshot: rules learned from notes, two skip and one boost, Application answers prepared from the resume (+65 more)

### Community 17 - "client.py"
Cohesion: 0.06
Nodes (36): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), run(), connect(), OutlookClient, OutlookError (+28 more)

### Community 18 - "notify.py"
Cohesion: 0.13
Nodes (17): category(), _clip(), _fit_bytes(), history(), posting_push(), Push, send(), summary_push() (+9 more)

### Community 19 - "Lead"
Cohesion: 0.11
Nodes (14): is_workday(), open_postings(), refill(), Lead, _identity(), daily(), DailyReport, _incompatible_term() (+6 more)

### Community 20 - "LeadStatus"
Cohesion: 0.25
Nodes (8): apply_violations(), PreferenceStore, LeadStatus, Preference, PreferenceEffect, test_apply_violations_never_touches_applied_leads(), test_apply_violations_skips_only_for_skip_rules(), test_preference_store_dedupes_and_removes()

### Community 21 - "x_search.py"
Cohesion: 0.18
Nodes (6): search_startups(), StartupFinding, StartupFindings, post_confirms(), search_x_raises(), _tool_usage()

### Community 22 - "FormQuestion"
Cohesion: 0.14
Nodes (12): _answer_for(), AnswerBank, common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+4 more)

### Community 23 - "test_outreach.py"
Cohesion: 0.17
Nodes (11): Round, parse_round(), to_leads(), finding(), lead(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_parse_round() (+3 more)

### Community 25 - "run_followups"
Cohesion: 0.11
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), reply_subject() (+3 more)

### Community 26 - "re"
Cohesion: 0.10
Nodes (28): _normalize(), QuestionKind, _slug(), ashby_questions(), fetch_questions(), greenhouse_questions(), lever_questions(), _request() (+20 more)

### Community 27 - "find-founders.md"
Cohesion: 0.12
Nodes (12): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, Founder leads flow: /find-founders, import, score, list, draft, mark (+4 more)

### Community 28 - "mailbox.py"
Cohesion: 0.19
Nodes (5): company_domain(), GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 29 - "test_application_browser.py"
Cohesion: 0.26
Nodes (13): PreparedAnswer, FakePage, posting(), test_answer_mapping_requires_unambiguous_question_match(), test_fill_form_blocks_unanswered_required_questions(), test_fill_form_clicks_ashby_yes_no_and_blocks_unknown_required(), test_fill_form_defers_react_select_input_to_combobox_pass(), test_fill_form_selects_only_four_month_availability() (+5 more)

### Community 30 - "test_notes.py"
Cohesion: 0.31
Nodes (6): PreferenceDraft, posting(), settings(), test_format_preferences(), test_general_note_without_lead_only_learns(), test_handle_note_saves_note_status_and_learns()

### Community 31 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 40 - "test_leads.py"
Cohesion: 0.07
Nodes (36): Output, Output, dashboard(), _clean(), guess_email(), LeadStore, client(), test_auto_apply_prepares_then_submits() (+28 more)

### Community 41 - "ranking.py"
Cohesion: 0.28
Nodes (4): _email_cell(), list_leads(), is_open(), rank()

### Community 42 - "_post_submit_outcome"
Cohesion: 0.40
Nodes (3): _post_submit_outcome(), test_post_submit_invalid_and_challenge_states(), test_post_submit_outcomes_across_ats_pages()

### Community 43 - "ai.py"
Cohesion: 0.15
Nodes (16): AnswerDraft, AnswerDrafts, assess_fit(), CoverLetterDraft, draft_outreach(), format_preferences(), interpret_note(), _lead_context() (+8 more)

### Community 47 - "send_email"
Cohesion: 0.08
Nodes (13): Internship agent coding instructions, Send email safeguards, EmailStatus, check_outreach_text(), check_send(), SendBlocked, build_message(), MailError (+5 more)

### Community 50 - "Bot Auto application preview"
Cohesion: 0.50
Nodes (3): Bot Auto application preview, Drafted cover letter, Values filled on the live form

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 331 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `leads/schemas.py`, `Region`, `workflows.py`, `test_daily_campaign.py`, `browser.py`, `startups.py`, `Settings`, `leads/cli.py`, `app.py`, `notify.py`, `LeadStatus`, `FormQuestion`, `test_outreach.py`, `run_followups`, `re`, `find-founders.md`, `test_application_browser.py`, `test_notes.py`, `followups.py`, `test_leads.py`, `ranking.py`, `ai.py`, `send_email`, `export.py`?**
  _High betweenness centrality (0.148) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `leads/schemas.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1380952380952381 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `Region`, `workflows.py`, `test_daily_campaign.py`, `_use_gmail_for_applications`, `pathlib`, `leads/cli.py`, `app.py`, `client.py`, `send_email`, `Lead`, `_run_ai_cost`, `FormQuestion`, `run_followups`, `re`, `test_notes.py`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `Region` be split into smaller, more focused modules?**
  _Cohesion score 0.14333333333333334 - nodes in this community are weakly interconnected._