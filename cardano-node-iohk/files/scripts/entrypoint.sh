#!/bin/bash
set -e
set -u
set -o pipefail

export POD_INDEX=${HOSTNAME##*-}
if [[ "$CARDANO_NODE_TYPE" == "producer" ]]; then
  TOPOLOGY_CONFIG="/config/$CARDANO_NETWORK/$CARDANO_NODE_TYPE-$TARGET_ROLE-topology.json"
elif [[ "$CARDANO_NODE_TYPE" == "relay" ]]; then
  TOPOLOGY_CONFIG="/config/$CARDANO_NETWORK/$CARDANO_NODE_TYPE-$TARGET_ROLE-$POD_INDEX-topology.json"
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