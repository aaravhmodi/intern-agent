#!/usr/bin/env bash
# Every 30 minutes: record replies and bounces in both Gmail inboxes and push new replies
# to the outreach one. Sends nothing.
set -euo pipefail
cd /home/aaravmodi/projects/intern-agent
check() {
  flock -w 120 -E 75 /tmp/intern-agent-workflows.lock \
    docker compose exec -T dashboard /app/.venv/bin/internship-agent leads followups --check-only
}
status=0
check || status=$?
# Gmail sometimes times out once. Try again a minute later, so only a failure that repeats
# reaches your phone.
if [ "$status" -ne 0 ] && [ "$status" -ne 75 ]; then
  echo "Check failed (exit $status); trying once more in a minute."
  sleep 60
  status=0
  check || status=$?
fi
# A batch or the application run can hold the lock for minutes. That's not a failure:
# skip this round (75 = lock still busy after 2 minutes) and check again in 30 minutes.
if [ "$status" -eq 75 ]; then
  echo "Another job is running; skipping this check."
  exit 0
fi
exit "$status"
