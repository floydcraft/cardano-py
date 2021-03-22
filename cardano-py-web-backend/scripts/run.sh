#!/bin/bash
#set -e
#set -u
#set -o pipefail

IMAGE=cardano-py-web-backend

if [[ "$1" == "pull" ]]; then
  docker pull floydcraft/$IMAGE:latest
fi

printf "IMAGE=$IMAGE\n"

if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
  printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
  docker exec -it "$IMAGE" /bin/sh
else
  printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
  docker rm "$IMAGE"
  docker run --name "$IMAGE" -d \
    -p "8080:8080" "floydcraft/$IMAGE:latest"
  docker exec -it "$IMAGE" /bin/sh
fi


