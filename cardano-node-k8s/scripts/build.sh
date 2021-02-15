#!/bin/bash
set -e
set -u
set -o pipefail

docker build \
    --no-cache \
    --tag "floydcraft/cardano-node-k8s:latest" .

