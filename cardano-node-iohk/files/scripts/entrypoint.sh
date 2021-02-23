#!/bin/bash
set -e
set -u
set -o pipefail

if [[ -f "/config/config.tar.gz" ]]; then
  tar -xzvf /config/config.tar.gz -C /config
fi

cardano-node run --config "/config/config.json" \
  --topology "/config/topology.json" \
  --database-path "/storage/db" \
  --host-addr "0.0.0.0" \
  --port 3001 \
  --socket-path "/storage/node.socket"