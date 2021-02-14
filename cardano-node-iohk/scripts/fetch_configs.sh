#!/bin/sh
set -e
set -u
set -o pipefail

cd stage3-files/config

curl -L -O https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-byron-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-shelley-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-topology.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-db-sync-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-rest-config.json

curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-byron-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-shelley-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-topology.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-db-sync-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-rest-config.json

curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-byron-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-shelley-genesis.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-topology.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-db-sync-config.json
curl -L -O  https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/staging-rest-config.json