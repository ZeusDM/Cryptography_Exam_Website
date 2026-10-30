#!/usr/bin/env bash
set -e
exec python3 "$(dirname "$0")/scripts/dev.py" "$@"
