#!/bin/bash
#set -e
#set -u
#set -o pipefail

IMAGE=cardano-py-slim
IMAGE_TAG=0.1.9-dev1

if [[ "$1" == "pull" ]]; then
  docker pull "floydcraft/$IMAGE:$IMAGE_TAG"
fi

printf "IMAGE=$IMAGE\n"

if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
  printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
  docker exec -it "$IMAGE" bash
else
  printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
  docker rm "$IMAGE"
  docker run --name "$IMAGE" -d \
    --env "CARDANO_NODE_SOCKET_PATH=/storage/node.socket" \
    "floydcraft/$IMAGE:$IMAGE_TAG"
  docker exec -it "$IMAGE" bash
fi


#    -v "$PWD/storage:/storage" \


