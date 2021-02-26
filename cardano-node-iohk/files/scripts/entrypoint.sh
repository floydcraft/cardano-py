#!/bin/bash
set -e
set -u
set -o pipefail

cardano-node run --config "/config/$CARDANO_NETWORK/config.json" \
  --topology "/config/$CARDANO_NETWORK/topology.json" \
  --database-path "/storage/$CARDANO_NETWORK/db" \
  --host-addr "0.0.0.0" \
  --port 3001 \
  --socket-path "/storage/$CARDANO_NETWORK/node.socket"