# Internship agent coding instructions

- Prefer simple implementations and small, focused modules.
- Use type hints throughout the Python codebase.
- Use Pydantic at AI and browser-output boundaries; validate all model output.
- Never expose credentials, cookies, auth headers, or tokens in logs.
- Outlook and calendar access is read-only. Browser automation may submit job applications only when the user has explicitly authorized the campaign and the application is complete with verified candidate facts. Skip Workday applications; never bypass CAPTCHAs, access controls, or missing required answers. Never automate LinkedIn/X actions (invitations, DMs, follows).
- Agents may email prospective leads when the user has explicitly authorized outreach. Use sending checks, send only to an address on the lead or one entered by the user, require explicit verification before sending to a recorded guessed address, prevent duplicate sends, and log the send. Never mention visas, J-1, sponsorship, or work authorization in lead emails or outreach drafts.
- Keep AI and browser orchestration separate from deterministic business logic.
- Write tests for deterministic logic and use mock browser fixtures for application development.
- Do not introduce infrastructure unless it is necessary for the local-first workflow.
- Consult current official documentation before integrating unstable APIs.
