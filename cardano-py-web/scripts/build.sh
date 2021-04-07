#!/bin/bash
set -e
set -u
set -o pipefail

docker build --tag "floydcraft/cardano-py-web:latest" .
