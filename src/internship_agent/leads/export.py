"""Render drafted outreach as a Markdown file for review before sending."""

from internship_agent.leads.schemas import EmailStatus, Lead


def _email_line(lead: Lead) -> str:
    if not lead.email:
        return "**Email:** not found"
    if lead.email_status is EmailStatus.PATTERN:
        return f"**Email:** {lead.email} (UNVERIFIED guess from company format)"
    return f"**Email:** {lead.email} (published: {lead.email_source or 'source not recorded'})"


def render_outreach(leads: list[Lead]) -> str:
    sections = [
        "# Outreach drafts\n\nNothing here has been sent. Review and edit before sending.\n"
    ]
    for lead in leads:
        if lead.draft is None:
            continue
        who = lead.contact_name or "Unknown contact"
        role = f", {lead.contact_role}" if lead.contact_role else ""
        fit = f"{lead.fit.score} ({lead.fit.verdict.value})" if lead.fit else "not scored"
        lines = [
            f"## {lead.company}: {who}{role}",
            f"`{lead.key}` · {lead.kind.value} · fit {fit}",
            "",
            _email_line(lead),
        ]
        if lead.x_url:
            lines.append(f"**X:** {lead.x_url}")
        if lead.linkedin_url:
            lines.append(f"**LinkedIn:** {lead.linkedin_url}")
        if lead.posting_url:
            lines.append(f"**Posting:** {lead.posting_title or 'link'} ({lead.posting_url})")
        lines.append(f"**Source:** {lead.source_url}")
        if lead.fit and lead.fit.concerns:
            lines.append(f"**Concerns:** {'; '.join(lead.fit.concerns)}")
        lines += [
            "",
            f"**Subject:** {lead.draft.email_subject}",
            "",
            lead.draft.email_body,
            "",
            "**X DM:**",
            "",
            lead.draft.x_dm,
            "",
        ]
        sections.append("\n".join(lines))
    return "\n".join(sections)
