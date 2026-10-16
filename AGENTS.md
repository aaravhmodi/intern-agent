# Internship agent coding instructions

- Prefer simple implementations and small, focused modules.
- Use type hints throughout the Python codebase.
- Use Pydantic at AI and browser-output boundaries; validate all model output.
- Never expose credentials, cookies, auth headers, or tokens in logs.
- Outlook and browser access is read-only. Never modify calendar events, submit applications, or automate LinkedIn/X actions (invitations, DMs, follows).
- Email is sent only by the dashboard's Send button: one message per explicit user click, after `leads/sending.py` checks. Agents never send email themselves.
- Keep AI and browser orchestration separate from deterministic business logic.
- Write tests for deterministic logic and use mock browser fixtures for application development.
- Do not introduce infrastructure unless it is necessary for the local-first workflow.
- Consult current official documentation before integrating unstable APIs.
