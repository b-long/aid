#!/bin/bash

set -eu
ROOT="$(git rev-parse --show-toplevel)"
cd "${ROOT}/"

poetry run prefect server create-tenant --name "aid-tenant" 2>&1 > /dev/null \
    || echo "Warning: the 'create-tenant' step will fail if the tenant already exists."

poetry run prefect create project 'aid-tenant'

export PREFECT__CLOUD__API='http://apollo:4200'
poetry run prefect agent docker start --network prefect-server
