"""Read an application form's questions from public job-board endpoints (read-only)."""

import html
import json
import re
import urllib.request
from typing import Any
from urllib.parse import urlsplit

from internship_agent.leads.schemas import FormQuestion, QuestionKind


def _request(url: str, body: dict[str, Any] | None = None) -> bytes:
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "*/*"}
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(request, timeout=25) as response:
        raw: bytes = response.read()
    return raw


_GREENHOUSE_KIND = {
    "input_text": QuestionKind.TEXT,
    "textarea": QuestionKind.LONG_TEXT,
    "multi_value_single_select": QuestionKind.SINGLE_SELECT,
    "multi_value_multi_select": QuestionKind.MULTI_SELECT,
    "input_file": QuestionKind.FILE,
    "input_hidden": QuestionKind.OTHER,
}


def greenhouse_questions(data: dict[str, Any]) -> list[FormQuestion]:
    questions: list[FormQuestion] = []
    for q in data.get("questions", []):
        fields = q.get("fields", [])
        kinds = [_GREENHOUSE_KIND.get(f.get("type", ""), QuestionKind.OTHER) for f in fields]
        kind = (
            QuestionKind.FILE
            if QuestionKind.FILE in kinds
            else (kinds[0] if kinds else QuestionKind.OTHER)
        )
        options = [str(v.get("label")) for f in fields for v in f.get("values", []) or []]
        questions.append(
            FormQuestion(
                label=str(q.get("label", "")).strip(),
                required=bool(q.get("required")),
                kind=kind,
                options=options,
            )
        )
    return questions


_ASHBY_KIND = {
    "String": QuestionKind.TEXT,
    "Email": QuestionKind.TEXT,
    "Phone": QuestionKind.TEXT,
    "LongText": QuestionKind.LONG_TEXT,
    "ValueSelect": QuestionKind.SINGLE_SELECT,
    "MultiValueSelect": QuestionKind.MULTI_SELECT,
    "Boolean": QuestionKind.YES_NO,
    "Date": QuestionKind.DATE,
    "File": QuestionKind.FILE,
    "Location": QuestionKind.TEXT,
}

_ASHBY_QUERY = (
    "query ApiJobPosting($organizationHostedJobsPageName: String!, $jobPostingId: String!) "
    "{ jobPosting(organizationHostedJobsPageName: $organizationHostedJobsPageName, "
    "jobPostingId: $jobPostingId) { applicationForm { sections { fieldEntries "
    "{ ... on FormFieldEntry { field isRequired } } } } } }"
)


def ashby_questions(data: dict[str, Any]) -> list[FormQuestion]:
    posting = (data.get("data") or {}).get("jobPosting") or {}
    sections = (posting.get("applicationForm") or {}).get("sections") or []
    questions: list[FormQuestion] = []
    for section in sections:
        for entry in section.get("fieldEntries", []):
            field = entry.get("field") or {}
            kind = _ASHBY_KIND.get(field.get("type", ""), QuestionKind.OTHER)
            options = [str(o.get("label")) for o in field.get("selectableValues") or []]
            questions.append(
                FormQuestion(
                    label=str(field.get("title", "")).strip(),
                    required=bool(entry.get("isRequired")),
                    kind=kind,
                    options=options,
                )
            )
    return questions


def lever_questions(page: str) -> list[FormQuestion]:
    questions: list[FormQuestion] = []
    for raw in re.findall(r'class="application-label[^"]*"[^>]*>(.*?)</div>', page, re.S):
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw))).strip()
        required = "✱" in text
        label = text.replace("✱", "").strip()
        if not label:
            continue
        kind = QuestionKind.FILE if label.lower().startswith("resume") else QuestionKind.TEXT
        questions.append(FormQuestion(label=label, required=required, kind=kind))
    return questions


def fetch_questions(url: str) -> list[FormQuestion]:
    """Questions for a posting, or [] when the board does not publish its form."""
    parts = urlsplit(url)
    host = parts.netloc.lower()
    try:
        if "greenhouse.io" in host or "gh_jid=" in url:
            match = re.search(r"/([^/]+)/jobs/(\d+)", parts.path)
            if match:
                board, job_id = match.group(1), match.group(2)
            else:
                gh = re.search(r"gh_jid=(\d+)", parts.query)
                if gh is None:
                    return []
                board, job_id = host.split(".")[-2], gh.group(1)
            api = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs/{job_id}?questions=true"
            return greenhouse_questions(json.loads(_request(api)))
        if host == "jobs.ashbyhq.com":
            _, org, job_id = parts.path.split("/")[:3]
            body = {
                "operationName": "ApiJobPosting",
                "variables": {"organizationHostedJobsPageName": org, "jobPostingId": job_id},
                "query": _ASHBY_QUERY,
            }
            api = "https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobPosting"
            return ashby_questions(json.loads(_request(api, body)))
        if host == "jobs.lever.co":
            _, company, job_id = parts.path.split("/")[:3]
            page = _request(f"https://jobs.lever.co/{company}/{job_id}/apply")
            return lever_questions(page.decode("utf-8", "ignore"))
    except Exception:
        return []
    return []
