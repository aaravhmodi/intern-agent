# Internship agent coding instructions

- Prefer simple implementations and small, focused modules.
- Use type hints throughout the Python codebase.
- Use Pydantic at AI and browser-output boundaries; validate all model output.
- Never expose credentials, cookies, auth headers, or tokens in logs.
- Outlook and calendar access is read-only. Browser automation may submit job applications only when the user has explicitly authorized the campaign and the application is complete with verified candidate facts. Skip Workday applications; never bypass CAPTCHAs, access controls, or missing required answers. Never automate LinkedIn/X actions (invitations, DMs, follows).
- Use `candidate_context.md`, the configured resume, and the candidate's public website/GitHub as sources for experience and project answers. You may synthesize concise, role-specific wording and derive ordinary details when they follow clearly from candidate-provided facts or a timeline; do not ask again for facts the sources already establish. Never fabricate personal facts, dates, qualifications, employment, outcomes, metrics, or authorization. If a required answer cannot be established from those sources or the saved answer bank, leave it unanswered and do not submit.
- Candidate-confirmed application defaults: legal/full name Aarav Modi; preferred name Aarav; pronouns he/him only when required; location-only fields use Toronto, Ontario, Canada; address fields use 191 Erb Street West, Waterloo, Ontario, Canada. Do not expose the street address in fields that only ask for city/location.
- Candidate confirms Canadian citizenship and authorization to work in Canada without sponsorship. For U.S. applications, use the candidate's confirmed answers: currently legally authorized to work in the United States; will require employer sponsorship. Do not infer any other country's work authorization.
- Candidate is in third year of study, enrolled in a co-op program, and accepts only a four-month term from January through April 2027. Do not apply if the posting requires another term length or a transcript. Candidate consents to interview recording/data processing and background checks; no active offers and no referral. Salary expectation is CAD 30/hour or higher where a required salary answer is needed. Current employer/role: Enerzen, Founding Software Engineer.
- Keep optional demographic, GPA, test score, and other unanswered personal questions blank. Do not apply automatically when a transcript is required.
- Agents may email prospective leads when the user has explicitly authorized outreach. Use sending checks, send only to an address on the lead or one entered by the user, require explicit verification before sending to a recorded guessed address, prevent duplicate sends, and log the send. Never mention visas, J-1, sponsorship, or work authorization in lead emails or outreach drafts.
- Keep AI and browser orchestration separate from deterministic business logic.
- Write tests for deterministic logic and use mock browser fixtures for application development.
- Do not introduce infrastructure unless it is necessary for the local-first workflow.
- Consult current official documentation before integrating unstable APIs.
