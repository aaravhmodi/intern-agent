#!/usr/bin/env bash
# Find more people to email, twice a day before the email batches: new raises (news, X,
# LinkedIn, funding feeds), then a recruiter and a senior engineer at startups with only one
# contact so far, then the addresses they publish. Each step's failure is logged, not fatal.
set -euo pipefail

cd /home/aaravmodi/projects/intern-agent
run() {
  flock -w 3600 /tmp/intern-agent-workflows.lock \
    docker compose exec -T dashboard /app/.venv/bin/internship-agent leads "$@"
}
run find-startups --stage early --stage mid || echo "Startup search failed" >&2
run funding-news --days 7 || echo "Funding news failed" >&2
# $1M+, not the $15M default: the bigger ones are all searched. 30 companies a run, up to
# 2 people each, so about 50 new people a run while unsearched companies last.
run team-contacts --min-usd 1000000 --limit 30 || echo "Team contacts failed" >&2
run site-emails || echo "Site email search failed" >&2
