#!/bin/bash
set -e
set -u
set -o pipefail

if [[ ("$1" == "k8s") || ("$1" == "iohk") ]]; then
  CARDANO_NODE="$1"
else
  printf "please select an option (cardano node): k8s or iohk "
  exit 1
fi

docker build \
    --tag "floydcraft/cardano-node-$CARDANO_NODE:latest" .

