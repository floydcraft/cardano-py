#!/bin/bash
#set -e
#set -u
#set -o pipefail

IMAGE=cardano-py-slim

if [[ "$1" == "pull" ]]; then
  docker pull floydcraft/$IMAGE:latest
fi

printf "IMAGE=$IMAGE\n"

if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
  printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
  docker exec -it "$IMAGE" bash
else
  printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
  docker container rm "$IMAGE"
  docker run --name "$IMAGE" -it \
#    -v "$PWD/storage:/storage" \
    --env "CARDANO_NODE_SOCKET_PATH=/storage/node.socket" \
    --entrypoint bash "floydcraft/$IMAGE:latest"
fi




