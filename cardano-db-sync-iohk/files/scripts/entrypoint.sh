#!/bin/bash
set -e
set -u
set -o pipefail

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-node  run --config "/config/mainnet-config.json" \
    --topology "/config/mainnet-topology.json" \
    --database-path "/storage/mainnet/db" \
    --host-addr "0.0.0.0" \
    --port 3001 \
    --socket-path "/storage/mainnet/nodes.socket"
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-node  run --config "/config/testnet-config.json" \
    --topology "/config/testnet-topology.json" \
    --database-path "/storage/testnet/db" \
    --host-addr "0.0.0.0" \
    --port 3001 \
    --socket-path "/storage/testnet/nodes.socket"
else
  echo "Please set a CARDANO_NETWORK environment variable to one of the following: mainnet, testnet, or staging"
fi