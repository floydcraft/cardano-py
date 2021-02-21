#!/bin/bash
set -e
set -u
set -o pipefail

export PGPASSFILE="/storage/$CARDANO_NETWORK/config/connection.pgpass"

pg_ctlcluster 11 main start
sudo -u postgres createuser --createdb --superuser root
/scripts/postgresql-setup.sh --createdb

if [[ "$CARDANO_NETWORK" == "mainnet" ]]; then
  cardano-db-sync \
   --config "/storage/mainnet/config/db-sync-config.json" \
   --socket-path "/storage/mainnet/node.socket" \
   --state-dir "/storage/mainnet/db-sync-ledger-state" \
   --schema-dir "schema"
elif [[ "$CARDANO_NETWORK" == "testnet" ]]; then
  cardano-db-sync \
   --config "/storage/testnet/config/db-sync-config.json" \
   --socket-path "/storage/testnet/node.socket" \
   --state-dir "/storage/testnet/db-sync-ledger-state" \
   --schema-dir "schema"
else
  echo "Please set a CARDANO_NETWORK environment variable to one of the following: mainnet or testnet"
fi