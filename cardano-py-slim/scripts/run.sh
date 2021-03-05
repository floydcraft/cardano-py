#!/bin/bash
#set -e
#set -u
#set -o pipefail

IMAGE=cardano-py-slim

if [[ ("$1" == "mainnet") || ("$1" == "testnet") ]]; then
  CARDANO_NETWORK="$1"
else
  printf "please select an option (cardano network): mainnet or testnet "
  exit 1
fi

if [[ "$2" == "pull" ]]; then
  docker pull floydcraft/$IMAGE:latest
fi

printf "IMAGE=$IMAGE\nCARDANO_NETWORK=$CARDANO_NETWORK\n"

if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
  printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
  docker exec -it "$IMAGE" bash
else
  printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
  docker container rm "$IMAGE"
  docker run --name "$IMAGE" -it \
    -v "$PWD/storage/$CARDANO_NETWORK:/storage" \
    --env "CARDANO_NETWORK=$CARDANO_NETWORK" \
    --env "CARDANO_NODE_SOCKET_PATH=/storage/$CARDANO_NETWORK/node.socket" \
    --entrypoint bash "floydcraft/$IMAGE:latest"
fi




