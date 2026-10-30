#!/usr/bin/env bash
set -euo pipefail
python -m pytest --cov=synoptiko --cov-report=term-missing "$@"
