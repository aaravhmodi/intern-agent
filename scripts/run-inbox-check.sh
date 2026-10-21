#!/usr/bin/env bash
# Every 30 minutes: record replies and bounces in both Gmail inboxes and push new replies
# to the outreach one. Sends nothing.
set -euo pipefail
cd /home/aaravmodi/projects/intern-agent
flock -w 120 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads followups --check-only
