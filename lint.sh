#!/usr/bin/env bash
set -euo pipefail
python -m ruff check synoptiko tests setup.py
