#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

helm template --set namespace=cardano-mainnet \
  --set cardano.network=mainnet \
  cardano-py-k8s/ > bin/mainnet.yaml
helm template --set namespace=cardano-testnet \
  --set cardano.network=testnet \
  cardano-py-k8s/ > bin/testnet.yaml
#kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml