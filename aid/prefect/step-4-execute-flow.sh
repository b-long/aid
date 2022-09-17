#!/bin/bash

set -eu
ROOT="$(git rev-parse --show-toplevel)"
cd "${ROOT}/"

poetry run python summrizr/onboarding/basic_prefect_cli_flow_run.py