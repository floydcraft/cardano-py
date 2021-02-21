#!/bin/bash
set -e
set -u
set -o pipefail

cd storage

curl -L -o testnet/config/config.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-config.json
curl -L -o testnet/config/byron-genesis.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-byron-genesis.json
curl -L -o testnet/config/shelley-genesis.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-shelley-genesis.json
curl -L -o testnet/config/topology.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-topology.json
curl -L -o testnet/config/db-sync-config.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/testnet-db-sync-config.json

curl -L -o mainnet/config/config.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-config.json
curl -L -o mainnet/config/byron-genesis.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-byron-genesis.json
curl -L -o mainnet/config/shelley-genesis.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-shelley-genesis.json
curl -L -o mainnet/config/topology.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-topology.json
curl -L -o mainnet/config/db-sync-config.json https://hydra.iohk.io/job/Cardano/cardano-node/cardano-deployment/latest-finished/download/1/mainnet-db-sync-config.json