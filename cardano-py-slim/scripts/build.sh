#!/bin/bash
set -e
set -u
set -o pipefail

docker build --tag "floydcraft/cardano-py-slim:0.1.10-dev1" .
