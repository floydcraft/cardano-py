#!/bin/bash
set -e
set -u
set -o pipefail

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-node  run --config "/config/mainnet-config.json" \
    --topology "/config/mainnet-topology.json" \
    --database-path "/storage/mainnet/db" \
    --socket-path "/storage/mainnet/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-node  run --config "/config/testnet-config.json" \
    --topology "/config/testnet-topology.json" \
    --database-path "/storage/testnet/db" \
    --socket-path "/storage/testnet/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
elif [[ "$CARDANO_NETWORK" == "staging" ]]; then
  cardano-node  run --config "/config/staging-config.json" \
    --topology "/config/staging-topology.json" \
    --database-path "/storage/staging/db" \
    --socket-path "/storage/staging/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
else
  echo "Please set a CARDANO_NETWORK environment variable to one of the following: mainnet, testnet, or staging"
fi