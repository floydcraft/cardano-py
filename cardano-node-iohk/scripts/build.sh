#!/bin/bash
set -e
set -u
set -o pipefail

_VERSION="1.25.1"
docker build \
    --memory=4g \
    --build-arg "_VERSION=$_VERSION" \
    --tag "floydcraft/cardano-node-iohk:$_VERSION" \
    --tag "floydcraft/cardano-node-iohk:latest" .

