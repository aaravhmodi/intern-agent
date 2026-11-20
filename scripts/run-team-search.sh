#!/usr/bin/env bash
# Weekly: find engineers on backend, infrastructure and data teams at big tech, drafting each a
# coffee-chat note. Drafts only; nothing is sent here. One web search per company.
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
flock -w 3600 /tmp/intern-agent-workflows.lock \
  docker compose exec -T dashboard /app/.venv/bin/internship-agent leads big-tech-teams
