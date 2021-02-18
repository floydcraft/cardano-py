#!/bin/bash
set -e
set -u
set -o pipefail

if [[ ("$1" == "slim") || ("$1" == "iohk") || ("$1" == "iohk-slim") ]]; then
  IMAGE="cardano-node-$1"
elif [[ "$1" == "db-sync" ]]; then
  IMAGE="cardano-$1"
elif [[ "$1" == "haskell" ]]; then
  IMAGE="$1"
else
  printf "please select an option (cardano node): haskell, iohk, iohk-slim, db-sync, or slim"
  exit 1
fi

docker build \
    --tag "floydcraft/$IMAGE:latest" \
    "$IMAGE"

