#!/bin/bash
#set -e
#set -u
#set -o pipefail

OPTION1=$1
OPTION2=$2
OPTION3=$3

if [[ "$OPTION1" == "mainnet" ]]; then
  echo "CARDANO_NETWORK=$OPTION1"
elif [[ "$OPTION1" == "testnet" ]]; then
  echo "CARDANO_NETWORK=$OPTION1"
elif [[ "$OPTION1" == "staging" ]]; then
  echo "CARDANO_NETWORK=$OPTION1"
else
  echo "please select an option: mainnet / testnet / staging"
fi

if [[ "$OPTION2" == "pull" ]]; then
  docker pull floydcraft/cardano-node-iohk:latest
elif [[ "$OPTION2" == "bash" ]]; then
  docker run -it -v $PWD/storage:/storage --env "CARDANO_NETWORK=$OPTION1" --entrypoint bash floydcraft/cardano-node-iohk:latest
else
  docker run -it -v $PWD/storage:/storage --env "CARDANO_NETWORK=$OPTION1" floydcraft/cardano-node-iohk:latest
fi

if [[ "$OPTION3" == "bash" ]]; then
  docker run -it -v $PWD/storage:/storage --env "CARDANO_NETWORK=$OPTION1" --entrypoint bash floydcraft/cardano-node-iohk:latest
else
  docker run -it -v $PWD/storage:/storage --env "CARDANO_NETWORK=$OPTION1" floydcraft/cardano-node-iohk:latest
fi






