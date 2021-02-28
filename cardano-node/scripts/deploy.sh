#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin/mainnet bin/testnet
COMMIT_SHA=$(git rev-parse HEAD)
BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

helm template --set namespace=cardano-mainnet \
  --set cardano.network=mainnet \
  --set git.commitSha=$COMMIT_SHA \
  --set git.branchName=$BRANCH_NAME \
  cardano-node/ > bin/mainnet.yaml
helm template --set namespace=cardano-testnet \
  --set cardano.network=testnet \
  --set git.commitSha=$COMMIT_SHA \
  --set git.branchName=$BRANCH_NAME \
  cardano-node/ > bin/testnet.yaml
#kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml