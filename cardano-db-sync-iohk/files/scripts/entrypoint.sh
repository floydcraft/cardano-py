#!/bin/bash
set -e
set -u
set -o pipefail

export PGPASSFILE="/config/connection.pgpass"

pg_ctlcluster 11 main start
sudo -u postgres createuser --createdb --superuser root
/scripts/postgresql-setup.sh --createdb

cardano-db-sync  --config "/config/db-sync-config.json" \
 --socket-path "/storage/node.socket" \
 --state-dir "/storage/db-sync-ledger-state" \
 --schema-dir "/schema"