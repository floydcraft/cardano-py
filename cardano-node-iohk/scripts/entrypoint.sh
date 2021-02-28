#!/bin/bash
set -e
set -u
set -o pipefail

if [[ "$CARDANO_NODE_TYPE" == "producer" ]]; then
  TOPOLOGY_CONFIG="/config/$CARDANO_NETWORK/$CARDANO_NODE_TYPE-topology.json"
elif [[ "$1" == "relay" ]]; then
  TOPOLOGY_CONFIG="/config/$CARDANO_NETWORK/$CARDANO_NODE_TYPE-$TARGET_ROLE-topology.json"
else
  printf "please select an option (cardano node type): producer or relay"
  exit 1
fi

cardano-node run --config "/config/$CARDANO_NETWORK/config.json" \
  --topology $TOPOLOGY_CONFIG \
  --database-path "/storage/$CARDANO_NETWORK/db" \
  --host-addr "0.0.0.0" \
  --port 3001 \
  --socket-path "/storage/$CARDANO_NETWORK/node.socket"