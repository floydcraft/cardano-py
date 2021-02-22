#!/bin/bash
set -e
set -u
set -o pipefail

cardano-node run --config "/config/config.json" \
  --topology "/config/topology.json" \
  --database-path "/storage/db" \
  --host-addr "0.0.0.0" \
  --port 3001 \
  --socket-path "/storage/node.socket"