#!/bin/sh
set -e
set -u
set -o pipefail

PARAM=$1

if [[ "$PARAM" == "mainnet" ]]; then
  docker run -it -v $PWD/storage:/storage --env CARDANO_NETWORK=mainnet -p 3001:3001 floydcraft/cardano-node:latest
elif [[ "$PARAM" == "testnet" ]]; then
  docker run -it -v $PWD/storage:/storage --env CARDANO_NETWORK=testnet -p 3001:3001 floydcraft/cardano-node:latest
elif [[ "$PARAM" == "mainbash" ]]; then
  docker run -it -v $PWD/storage:/storage --env CARDANO_NETWORK=mainnet -p 3001:3001 --entrypoint bash floydcraft/cardano-node:latest
elif [[ "$PARAM" == "testbash" ]]; then
  docker run -it -v $PWD/storage:/storage --env CARDANO_NETWORK=testnet -p 3001:3001 --entrypoint bash floydcraft/cardano-node:latest
else
  echo "please select a config to run: mainnet / testnet / mainbash / testbash"
fi
