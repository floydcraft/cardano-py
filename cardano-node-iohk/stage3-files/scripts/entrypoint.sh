#!/bin/sh
set -e
set -u
set -o pipefail

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-node  run --config "/config/mainnet/config.json" \
    --topology "/config/mainnet/topology.json" \
    --database-path "/storage/db" \
    --socket-path "/storage/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-node  run --config "/config/mainnet/config.json" \
    --topology "/config/mainnet/topology.json" \
    --database-path "/storage/db" \
    --socket-path "/storage/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
else
  echo "Please set a NETWORK environment variable to one of the following: mainnet / testnet"
fi