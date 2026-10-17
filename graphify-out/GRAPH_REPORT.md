# Graph Report - winter-2027-internship-agent  (2026-10-17)

## Corpus Check
- 75 files · ~179,493 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 4, .service 3, .timer 3)

## Summary
- 993 nodes · 2884 edges · 45 communities (35 shown, 10 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 500 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ea3d6b48`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- README.md
- get_settings
- simplify.py
- app.py
- workflows.py
- leads/schemas.py
- browser.py
- Lead
- Settings
- run_followups
- client.py
- internship_agent/cli.py
- ai.py
- make_workflows.py
- verification_mail.py
- leads/cli.py
- mailbox.py
- followups.py
- startups.py
- find_startups
- test_dashboard.py
- notify.py
- re
- test_outreach.py
- run-application-campaign-2026-10-16.sh
- FakeMailbox
- test_leads.py
- find-founders.md
- test_x_search.py
- LeadKind
- store.py
- handle_note
- send_email
- load_resume_text
- typing
- run-daily-applications.sh
- internship-agent
- run-daily-job-scrape.sh
- test_daily_campaign.py
- rank
- LeadStatus
- OutreachDraft

## God Nodes (most connected - your core abstractions)
1. `Lead` - 109 edges
2. `Settings` - 61 edges
3. `get_settings()` - 43 edges
4. `run_followups()` - 38 edges
5. `LeadStatus` - 34 edges
6. `find_startups()` - 27 edges
7. `prepare_application()` - 27 edges
8. `Region` - 25 edges
9. `FormQuestion` - 25 edges
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

## Communities (45 total, 10 thin omitted)

### Community 0 - "README.md"
Cohesion: 0.06
Nodes (29): Internship agent coding instructions, Candidate and search preferences, CIBC — IT Project Coordinator Intern (Winter 2025), CIBC — Software Engineering Intern (Aug–Dec 2025 per resume), Enerzen — Founding Software Engineer (Aug 2026–present), Experience, Projects and public work, Upside Robotics — Software Engineering Intern (Jan–Aug 2026 per resume) (+21 more)

### Community 1 - "get_settings"
Cohesion: 0.14
Nodes (11): get_settings(), application_campaign(), apply_cmd(), browser_login(), daily_cmd(), find_more(), find_startups_cmd(), followups_cmd() (+3 more)

### Community 2 - "simplify.py"
Cohesion: 0.09
Nodes (11): normalize_url(), region_from_text(), regions_of(), cap_per_company(), is_software_role(), matching(), parse(), Posting (+3 more)

### Community 3 - "app.py"
Cohesion: 0.11
Nodes (31): AnswerEdit, daily_run(), delete_preference(), draft(), find_more(), find_more_startups(), FindMoreRequest, FindStartupsRequest (+23 more)

### Community 4 - "workflows.py"
Cohesion: 0.11
Nodes (16): answer_bank(), daily(), DailyReport, _incompatible_term(), lead_store(), prepare_application(), _record_openai_usage(), refresh_saved_application() (+8 more)

### Community 5 - "leads/schemas.py"
Cohesion: 0.15
Nodes (7): EmailStatus, OutreachDraftResult, Round, Segment, Verdict, parse_round(), test_parse_round()

### Community 6 - "browser.py"
Cohesion: 0.06
Nodes (36): _answer_for(), apply_to_posting(), _field_label(), _fill_form(), _normalize(), _numeric_answer(), _online_checks(), open_login_browser() (+28 more)

### Community 7 - "Lead"
Cohesion: 0.26
Nodes (7): assess_fit(), draft_outreach(), interpret_note(), _lead_context(), prepare_answers(), prepare_cover_letter(), Lead

### Community 8 - "Settings"
Cohesion: 0.22
Nodes (17): Settings, emailed(), outbox(), save(), settings(), test_a_bounced_address_gets_nothing(), test_a_dry_run_shows_what_would_go_and_changes_nothing(), test_a_due_follow_up_is_sent_as_a_reply_and_recorded() (+9 more)

### Community 9 - "run_followups"
Cohesion: 0.11
Nodes (11): FollowupReport, FollowupSent, _logged_subject(), _misaddressed(), _name(), run_followups(), _site(), company_domain() (+3 more)

### Community 10 - "client.py"
Cohesion: 0.06
Nodes (33): cmd, outlook, @softeria/ms-365-mcp-server, Outlook mail and calendar through the Softeria Microsoft 365 MCP server (read-only), OutlookClient, OutlookError, ToolSession, CalendarEvent (+25 more)

### Community 11 - "internship_agent/cli.py"
Cohesion: 0.13
Nodes (10): inbox(), run(), interviews(), run(), outlook_login(), outlook_status(), run(), _run() (+2 more)

### Community 12 - "ai.py"
Cohesion: 0.16
Nodes (12): AnswerDraft, AnswerDrafts, CoverLetterDraft, NoteResult, PeopleFindings, PersonFinding, search_startups(), StartupFinding (+4 more)

### Community 13 - "make_workflows.py"
Cohesion: 0.14
Nodes (12): compose.yaml: the dashboard on a home server, dashboard service, reachable only over Tailscale, install.sh script, _id(), internship_daily_prep(), internship_followups(), internship_replies(), Changing it (+4 more)

### Community 14 - "verification_mail.py"
Cohesion: 0.08
Nodes (13): _extract_code(), _message_text(), VerificationCode, wait_for_greenhouse_code(), build_message(), MailError, send(), test_build_message_requires_fields() (+5 more)

### Community 15 - "leads/cli.py"
Cohesion: 0.21
Nodes (12): Founder leads flow: /find-founders, import, score, list, draft, mark, _draft(), draft_all(), draft_lead(), _email_cell(), list_leads(), mark_lead(), _openai() (+4 more)

### Community 16 - "mailbox.py"
Cohesion: 0.21
Nodes (4): GmailMailbox, _imap_date(), MailboxError, _quoted()

### Community 17 - "followups.py"
Cohesion: 0.29
Nodes (4): first_name(), followup_body(), is_due(), last_contact()

### Community 18 - "startups.py"
Cohesion: 0.16
Nodes (7): _on_linkedin(), source_names(), _fold(), mentions(), names(), page_names(), source_confirms()

### Community 19 - "find_startups"
Cohesion: 0.15
Nodes (11): More people to connect with, chosen by company size, search_people(), Person, effective_segment(), to_people(), find_people(), find_startups(), people_at() (+3 more)

### Community 20 - "test_dashboard.py"
Cohesion: 0.15
Nodes (12): dashboard(), client(), test_cross_site_post_is_blocked(), test_finding_people_needs_an_openai_key(), test_foreign_host_is_blocked(), test_index_serves_html(), test_leads_includes_key_and_segment(), test_marking_applied_triggers_refill() (+4 more)

### Community 21 - "notify.py"
Cohesion: 0.20
Nodes (14): _clip(), _fit_bytes(), posting_push(), Push, send(), summary_push(), written_answers(), answer() (+6 more)

### Community 22 - "re"
Cohesion: 0.07
Nodes (34): AnswerBank, category(), common_questions(), match_option(), normalize(), prefill(), validate(), FormQuestion (+26 more)

### Community 23 - "test_outreach.py"
Cohesion: 0.24
Nodes (9): to_leads(), finding(), lead(), test_check_send_blocks_unconfirmed_guess_and_resends(), test_effective_segment(), test_linkedin_note_never_exceeds_200_chars(), test_mentions_requires_company_and_founder_ignoring_accents(), test_to_leads_filters_age_stage_and_unverifiable_sources() (+1 more)

### Community 26 - "test_leads.py"
Cohesion: 0.09
Nodes (24): Output, Output, _clean(), guess_email(), _email_line(), render_outreach(), LeadStore, fit() (+16 more)

### Community 27 - "find-founders.md"
Cohesion: 0.13
Nodes (10): Founder lead JSON written to data/leads-inbox.json, Rules, Where to look, Posting lead JSON appended to data/leads-inbox.json, Rules, Segment: early, mid or big, Where to look, export_drafts() (+2 more)

### Community 28 - "test_x_search.py"
Cohesion: 0.28
Nodes (5): post_id(), finding(), test_a_post_counts_when_it_exists_and_is_about_raising(), test_a_raise_announced_by_the_company_account_is_kept_without_a_founder(), test_only_a_link_to_a_post_has_a_post_id()

### Community 29 - "LeadKind"
Cohesion: 0.21
Nodes (9): Big-company postings from the SimplifyJobs off-season list, is_workday(), open_postings(), refill(), LeadKind, fetch(), find_more_postings(), scrape_jobs() (+1 more)

### Community 30 - "store.py"
Cohesion: 0.29
Nodes (3): _slug(), _identity(), merge()

### Community 31 - "handle_note"
Cohesion: 0.20
Nodes (10): Screenshot: rules learned from notes, two skip and one boost, Rules learned from notes (skip, downrank, boost), index(), Dashboard page (index.html), linkedinUrl(): profile URL, else a LinkedIn people search, Notes box that saves notes and learns rules, 'More people to connect with' section, handle_note() (+2 more)

### Community 32 - "send_email"
Cohesion: 0.22
Nodes (6): Send email safeguards, Email section with two-click send, check_outreach_text(), check_send(), SendBlocked, send_email()

### Community 34 - "typing"
Cohesion: 0.06
Nodes (27): FitResult, _ashby(), board_slugs(), find_intern_roles(), _greenhouse(), intern_roles(), _json(), _lever() (+19 more)

### Community 40 - "test_daily_campaign.py"
Cohesion: 0.11
Nodes (13): ApplicationPrep, FitAssessment, test_campaign_stops_after_target_confirmed_submissions(), load(), prepare(), test_daily_scores_only_new_leads_and_prepares_every_eligible_posting(), load(), score_new() (+5 more)

### Community 43 - "LeadStatus"
Cohesion: 0.14
Nodes (17): format_preferences(), PreferenceDraft, apply_violations(), _normalize(), PreferenceStore, LeadStatus, Note, Preference (+9 more)

### Community 49 - "OutreachDraft"
Cohesion: 0.18
Nodes (3): fit_to_limit(), OutreachDraft, test_fit_to_limit_prefers_sentence_then_word_boundary()

## Knowledge Gaps
- **3 isolated node(s):** `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 304 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lead` connect `Lead` to `simplify.py`, `app.py`, `workflows.py`, `leads/schemas.py`, `browser.py`, `Settings`, `run_followups`, `ai.py`, `leads/cli.py`, `followups.py`, `startups.py`, `find_startups`, `test_dashboard.py`, `notify.py`, `re`, `test_outreach.py`, `test_leads.py`, `find-founders.md`, `LeadKind`, `store.py`, `handle_note`, `send_email`, `typing`, `test_daily_campaign.py`, `rank`, `LeadStatus`, `OutreachDraft`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `Lead` (e.g. with `Posting lead JSON appended to data/leads-inbox.json` and `assess_fit()`) actually correct?**
  _`Lead` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `cmd`, `internship-agent`, `compose.yaml: the dashboard on a home server` to the rest of the system?**
  _3 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `README.md` be split into smaller, more focused modules?**
  _Cohesion score 0.056025369978858354 - nodes in this community are weakly interconnected._
- **Why does `Settings` connect `Settings` to `send_email`, `get_settings`, `typing`, `workflows.py`, `test_daily_campaign.py`, `run_followups`, `config.py`, `internship_agent/cli.py`, `client.py`, `make_workflows.py`, `LeadStatus`, `leads/cli.py`, `verification_mail.py`, `find_startups`, `re`, `LeadKind`, `handle_note`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Settings` (e.g. with `dashboard service, reachable only over Tailscale` and `_logged_subject()`) actually correct?**
  _`Settings` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Should `get_settings` be split into smaller, more focused modules?**
  _Cohesion score 0.13768115942028986 - nodes in this community are weakly interconnected._