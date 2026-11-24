#!/usr/bin/env bash
set -euo pipefail
repo_dir="$(dirname "$(dirname "$(realpath "$0")")")"
exec python "$repo_dir/scripts/qa_dashboard.py" \
  "${1:-https://esaonc-ai.github.io/it-leadership-dashboard/}" \
  --workbook "$repo_dir/Weekly_Leadership_Source_Workbook.xlsx" \
  --source-name 'IT & Technology Project_Portfolios_2026_v1.0 (Week of 15Nov2026 PST).xlsx' \
  --report-date 2026-11-15 \
  --audit "$repo_dir/reports/15nov-2026/workbook-audit.json" \
  --output "${2:-/tmp/github-pages-15nov-live-qa}"
