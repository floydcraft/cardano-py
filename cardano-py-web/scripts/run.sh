#!/bin/bash
#set -e
#set -u
#set -o pipefail

IMAGE="cardano-py-web"
CONTAINER_NAME="cpy-web"

if [[ ! -z $( docker ps -q -f "name=^/$CONTAINER_NAME$" ) ]]; then
  printf "Active container  found for: $IMAGE\nattaching to the container '$CONTAINER_NAME'\n"
  docker exec -it $CONTAINER_NAME /bin/sh
  exit 0
fi

if [[ ! -z $( docker ps -aq -f "name=^/$CONTAINER_NAME$" ) ]]; then
  printf "Inactive container found for: $IMAGE\nstarting the container '$CONTAINER_NAME'\n"
  docker start $CONTAINER_NAME
  docker exec -it $CONTAINER_NAME /bin/sh
else
  printf "No active container found for: $IMAGE\nrunning a new container '$CONTAINER_NAME'\n"
  docker run --name $CONTAINER_NAME \
    -d \
    -p 8080:8080 \
    "floydcraft/$IMAGE:latest"
  docker exec -it $CONTAINER_NAME /bin/sh
fi
