#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

# helm template . > bin/mainnet.yaml
helm template . > bin/testnet.yaml
#kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml
