#!/bin/bash
#set -e
#set -u
#set -o pipefail

if [[ ("$1" == "mainnet") || ("$1" == "testnet") ]]; then
  CARDANO_NETWORK="$1"
else
  echo "please select an option: mainnet, or testnet "
  exit 1
fi

if [[ "$2" == "pull" ]]; then
  docker pull floydcraft/cardano-node-k8s:latest
fi

if [ "$( docker container inspect -f '{{.State.Running}}' cardano_node_k8s )" == "true" ]; then
  printf "active container found for: cardano_node_k8s\nattaching to the container\n"
  docker exec -it cardano_node_k8s bash
else
  printf "no active container found for: cardano_node_k8s\ncleaning containers and creating new container via run\n"
  docker container prune -f
  docker run --name cardano_node_k8s -it -v $PWD/storage:/storage --env "CARDANO_NETWORK=$CARDANO_NETWORK" --entrypoint bash floydcraft/cardano-node-k8s:latest
fi




