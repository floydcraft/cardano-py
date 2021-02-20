#!/bin/bash
set -e
set -u
set -o pipefail

export PGPASSFILE="/storage/$CARDANO_NETWORK.pgpass"

pg_ctlcluster 11 main restart

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-db-sync \
    --config "/storage/config/mainnet-db-sync-config.json" \
    --socket-path "/storage/node.socket" \
    --state-dir "/storage/db-sync-node/ledger-state/mainnet" \
    --schema-dir "schema/"
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-db-sync \
    --config "/storage/config/mainnet-db-sync-config.json" \
    --socket-path "/storage/node.socket" \
    --state-dir "/storage/db-sync-node/ledger-state/testnet" \
    --schema-dir "schema/"
else
  echo "Please set a CARDANO_NETWORK environment variable to one of the following: mainnet or testnet"
fi