#!/bin/bash
set -e
set -u
set -o pipefail

IMAGE=cardano-py-slim

docker build \
    --tag "floydcraft/$IMAGE:latest" \
    "."

