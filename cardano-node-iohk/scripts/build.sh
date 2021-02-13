#!/bin/sh
set -e
set -u
set -o pipefail

COMMIT_SHA=$(git rev-parse HEAD)
VERSION="1.25.1"
docker build \
    --memory=8g \
    --build-arg VERSION=${VERSION} \
    --tag floydcraft-local/cardano-node-iohk:${COMMIT_SHA} \
    --tag floydcraft-local/cardano-node-iohk:${VERSION} \
    --tag floydcraft-local/cardano-node-iohk:latest .

