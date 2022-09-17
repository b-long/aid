#!/bin/bash

set -eu
ROOT="$(git rev-parse --show-toplevel)"
cd "${ROOT}/"

poetry run python aid/prefect/basic_prefect.py

# poetry run python aid/prefect/basic_prefect_with_pandas.py