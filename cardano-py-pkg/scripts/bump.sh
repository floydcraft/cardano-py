#!/bin/bash
set -e
set -u
set -o pipefail

# build or release
bump2version $1