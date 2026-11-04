"""Guards for the scripts and systemd units that run the scheduled jobs on the server."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = sorted((ROOT / "scripts").glob("*.sh"))
SERVICES = sorted(
    p for p in (ROOT / "systemd").glob("*.service") if not p.name.startswith("internship-failure@")
)


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_scripts_dont_open_stdio_by_path(script: Path) -> None:
    # Under systemd, stdout and stderr are the journal's socket: opening /dev/stderr fails,
    # and with pipefail that stopped every outreach batch before its top-up step.
    text = script.read_text(encoding="utf-8")
    assert not re.search(r"/dev/std(err|out)", text), "write to >&2 or >&1 instead"


@pytest.mark.parametrize("unit", SERVICES, ids=lambda p: p.name)
def test_every_scheduled_job_alerts_when_it_fails(unit: Path) -> None:
    text = unit.read_text(encoding="utf-8")
    assert "OnFailure=internship-failure@%n.service" in text
