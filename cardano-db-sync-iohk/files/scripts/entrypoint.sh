#!/bin/bash
set -e
set -u
set -o pipefail

export PGPASSFILE="/config/$CARDANO_NETWORK/connection.pgpass"

pg_ctlcluster 11 main start
sudo -u postgres createuser --createdb --superuser root
/scripts/postgresql-setup.sh --createdb

cardano-db-sync  --config "/config/$CARDANO_NETWORK/db-sync-config.json" \
 --socket-path "/storage/$CARDANO_NETWORK/node.socket" \
 --state-dir "/storage/$CARDANO_NETWORK/db-sync-ledger-state" \
 --schema-dir "/schema"