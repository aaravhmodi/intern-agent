import os

import pytest

# Settings read the environment, so tests run where the app runs (the server's container)
# would otherwise reach the real database and Gmail. Only TEST_DATABASE_URL is kept.
_REAL = ("DATABASE_URL", "GMAIL_", "OUTREACH_GMAIL_", "OPENAI_", "XAI_", "NTFY_", "FOLLOWUPS_")


@pytest.fixture(autouse=True)
def no_real_services(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in list(os.environ):
        if name.upper().startswith(_REAL):
            monkeypatch.delenv(name)
