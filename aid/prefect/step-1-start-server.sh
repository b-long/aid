#!/bin/bash

set -eu
ROOT="$(git rev-parse --show-toplevel)"

rm -rf ~/.prefect/
mkdir -p ~/.prefect
cd "${ROOT}/"

# shellcheck disable=SC2034
# ENVIRONMENT="local"
# source "${ROOT}/ansible/scripts/multiplatform/utils/env-no-git-clone-in-root.sh"
# ENVIRONMENT="docker-compose"
# cp "${ROOT}/ansible/templates/config-${ENVIRONMENT}.toml" ~/.prefect/config.toml

poetry run prefect backend server
poetry run prefect server start

