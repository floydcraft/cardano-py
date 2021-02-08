#!/bin/sh
#set -e
#set -u
#set -o pipefail

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  /nix/store/1v1hfp0jn4w9yvhl27m4ghdn6k9v4wxm-cardano-node-exe-cardano-node-1.25.1/bin/cardano-node \
    run \
    --config "/config/mainnet/config.json" \
    --topology "/config/mainnet/topology.json" \
    --database-path "/storage/db" \
    --socket-path "/storage/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  /nix/store/1v1hfp0jn4w9yvhl27m4ghdn6k9v4wxm-cardano-node-exe-cardano-node-1.25.1/bin/cardano-node \
    run \
    --config "/config/mainnet/config.json" \
    --topology "/config/mainnet/topology.json" \
    --database-path "/storage/db" \
    --socket-path "/storage/sockets/nodes.socket" \
    --host-addr "0.0.0.0" \
    --port 3001
else
  echo "Please set a NETWORK environment variable to one of the following: mainnet / testnet"
fi

