#!/bin/sh
set -e
set -u
set -o pipefail

VERSION="1.25.1"
docker build \
    --build-arg VERSION=${VERSION} \
    --tag floydcraft/cardano-node:${VERSION} \
    --tag floydcraft/cardano-node:latest .
