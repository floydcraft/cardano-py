#!/bin/bash
#set -e
#set -u
#set -o pipefail

if [[ ("$1" == "slim") || ("$1" == "iohk") ]]; then
  CARDANO_NODE="$1"
else
  printf "please select an option (cardano node): slim, iohk-slim, or iohk"
  exit 1
fi

if [[ ("$2" == "mainnet") || ("$2" == "testnet") ]]; then
  CARDANO_NETWORK="$2"
else
  printf "please select an option (cardano network): mainnet or testnet "
  exit 1
fi

if [[ "$3" == "pull" ]]; then
  docker pull floydcraft/cardano-node-k8s:latest
fi

CARDANO_CONTAINER_ACTIVE="$( docker container inspect -f '{{.State.Running}}' "cardano-node-$CARDANO_NODE" )"

printf "CARDANO_NODE=$CARDANO_NODE\nCARDANO_NETWORK=$CARDANO_NETWORK\nCARDANO_CONTAINER_ACTIVE=$CARDANO_CONTAINER_ACTIVE\n"

if [[ "$CARDANO_CONTAINER_ACTIVE" == "true" ]]; then
  printf "active container found for: cardano_node_k8s\nattaching to the container\n"
  docker exec -it "cardano_node_$CARDANO_NODE" bash
else
  printf "no active container found for: cardano_node_k8s\ncleaning containers and creating new container via run\n"
  docker container rm "cardano_node_$CARDANO_NODE"
  docker run --name "cardano_node_$CARDANO_NODE" -it -v "$PWD/cardano-node-$CARDANO_NODE/storage:/storage" \
    --env "CARDANO_NETWORK=$CARDANO_NETWORK" --entrypoint bash "floydcraft/cardano-node-$CARDANO_NODE:latest"
fi




