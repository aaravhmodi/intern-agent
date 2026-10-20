#!/usr/bin/env bash
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
run() {
  flock -w 3600 /tmp/intern-agent-workflows.lock \
    docker compose exec -T dashboard /app/.venv/bin/internship-agent leads "$@"
}
run scrape-jobs
# New US startups from SEC Form D filings; a failure here must not hide the scrape's result.
run form-d || echo "Form D search failed" >&2
# Opportunity agent: hackathon, conference and research-deadline feeds daily (no AI); the
# networking-event web search on Mondays. Pushes new finds and deadlines due this week.
events=""
[ "$(date +%u)" = 1 ] && events="--events"
docker compose exec -T dashboard /app/.venv/bin/internship-agent opportunities refresh $events \
  || echo "Opportunity refresh failed" >&2
