"""Deterministic handling of application questions: categories, saved answers, validation."""

import difflib
import json
import re
from pathlib import Path

from internship_agent.leads.schemas import FormQuestion, PreparedAnswer, QuestionKind

# Questions only the candidate can answer. Never guessed by AI.
_PERSONAL = re.compile(
    r"authori[sz]ed|legally|entitled to work|sponsor|visa|citizen|background check|"
    r"compensation|salary|pay expectation|hourly|relocat|willing to (come|work)|office|"
    r"based in|current(ly)? located|current location|city|how did you hear|where did you hear|"
    r"referr|previously employed|former|co-?op requirement|part of your co-?op|consent|"
    r"phone|email|legal name|first name|last name|preferred name|full name|address",
    re.I,
)
# Optional self-identification questions. Always left to the candidate.
_DEMOGRAPHIC = re.compile(
    r"gender|pronoun|race|racial|ethnic|indigenous|aboriginal|disabilit|veteran|"
    r"sexual orientation|lgbt|self-identify|transgender",
    re.I,
)


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def category(question: FormQuestion) -> str:
    """'file', 'demographic', 'personal', or 'ai' (answerable from resume and posting)."""
    if question.kind is QuestionKind.FILE:
        return "file"
    if _DEMOGRAPHIC.search(question.label):
        return "demographic"
    if _PERSONAL.search(question.label):
        return "personal"
    return "ai"


def match_option(answer: str, options: list[str]) -> str | None:
    """Map an answer onto one of a select's options, or None if nothing fits."""
    if not options:
        return answer
    by_norm = {normalize(o): o for o in options}
    if normalize(answer) in by_norm:
        return by_norm[normalize(answer)]
    close = difflib.get_close_matches(normalize(answer), list(by_norm), n=1, cutoff=0.8)
    return by_norm[close[0]] if close else None


def validate(question: FormQuestion, answer: str) -> str | None:
    """Return a cleaned answer that fits the question type, or None if it does not fit."""
    answer = answer.strip()
    if question.kind is QuestionKind.SINGLE_SELECT:
        return match_option(answer, question.options) if answer else None
    if question.kind is QuestionKind.MULTI_SELECT:
        picks = [match_option(part, question.options) for part in answer.split(";") if part.strip()]
        if not picks or any(p is None for p in picks):
            return None
        return "; ".join(p for p in picks if p)
    if question.kind is QuestionKind.YES_NO:
        lowered = answer.lower()
        return "Yes" if lowered.startswith("y") else "No" if lowered.startswith("n") else None
    return answer or None


class AnswerBank:
    """Answers the candidate typed for personal questions, reused across applications."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> dict[str, str]:
        if not self.path.exists():
            return {}
        data: dict[str, str] = json.loads(self.path.read_text(encoding="utf-8"))
        return data

    def remember(self, question: str, answer: str) -> None:
        bank = self.load()
        bank[normalize(question)] = answer.strip()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(bank, indent=2, ensure_ascii=False), encoding="utf-8")

    def lookup(self, question: FormQuestion) -> str | None:
        bank = self.load()
        key = normalize(question.label)
        hit = bank.get(key)
        if hit is None:
            close = difflib.get_close_matches(key, list(bank), n=1, cutoff=0.9)
            hit = bank[close[0]] if close else None
        return validate(question, hit) if hit else None


def prefill(questions: list[FormQuestion], bank: AnswerBank) -> list[PreparedAnswer]:
    """Fill everything that does not need AI: files, demographics, and saved personal answers."""
    prepared: list[PreparedAnswer] = []
    for q in questions:
        kind = category(q)
        saved = bank.lookup(q)
        if kind == "file":
            note = "Upload your resume PDF." if "resume" in q.label.lower() else "Optional upload."
            prepared.append(PreparedAnswer(question=q, note=note))
        elif kind == "demographic":
            prepared.append(
                PreparedAnswer(question=q, needs_user_input=True, note="Optional; your choice.")
            )
        elif saved is not None:
            prepared.append(
                PreparedAnswer(question=q, answer=saved, note="From your saved answers.")
            )
        elif kind == "personal":
            prepared.append(
                PreparedAnswer(question=q, needs_user_input=True, note="Only you can answer this.")
            )
        else:
            prepared.append(PreparedAnswer(question=q, needs_user_input=True, note="ai"))
    return prepared


def common_questions(company: str) -> list[FormQuestion]:
    """Typical questions for boards that do not publish their form (Workday, iCIMS)."""
    return [
        FormQuestion(label=f"Why are you interested in {company}?", kind=QuestionKind.LONG_TEXT),
        FormQuestion(label="Why are you a good fit for this role?", kind=QuestionKind.LONG_TEXT),
        FormQuestion(
            label="Tell us about a project you are proud of and its impact.",
            kind=QuestionKind.LONG_TEXT,
        ),
        FormQuestion(
            label="Are you available for a 4-month Winter 2027 (January-April) term?",
            kind=QuestionKind.YES_NO,
        ),
    ]
