#!/bin/bash
set -e
set -u
set -o pipefail

if [[ ("$1" == "slim") || ("$1" == "iohk") || ("$1" == "iohk-slim") ]]; then
  CARDANO_NODE="$1"
else
  printf "please select an option (cardano node): slim, iohk-slim, or iohk"
  exit 1
fi

docker build \
    --tag "floydcraft/cardano-node-$CARDANO_NODE:latest" \
    "cardano-node-$CARDANO_NODE"

