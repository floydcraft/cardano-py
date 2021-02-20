#!/bin/bash
set -e
set -u
set -o pipefail

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-node  run --config "/storage/config/mainnet-config.json" \
    --topology "/storage/config/mainnet-topology.json" \
    --database-path "/storage/mainnet/db" \
    --host-addr "0.0.0.0" \
    --port 3001 \
    --socket-path "/storage/mainnet/node.socket"
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-node  run --config "/storage/config/testnet-config.json" \
    --topology "/storage/config/testnet-topology.json" \
    --database-path "/storage/testnet/db" \
    --host-addr "0.0.0.0" \
    --port 3001 \
    --socket-path "/storage/testnet/node.socket"
else
  echo "Please set a CARDANO_NETWORK environment variable to one of the following: mainnet or testnet"
fi