#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

helm template --set namespace="cardano-mainnet" \
  --set cardanoNode.relayIpv4="35.184.53.16" \
  --set cardanoNode.memoryRequest="7Gi" \
  --set cardanoNode.storageRequest="50Gi" \
  --set cardanoNode.relayDns="mainnet-relays.cardanopy.com" \
  --set cardanoNode.network="mainnet" . > bin/mainnet.yaml
helm template --set namespace="cardano-testnet" \
  --set cardanoNode.relayIpv4="34.68.36.180" \
  --set cardanoNode.memoryRequest="2Gi" \
  --set cardanoNode.storageRequest="10Gi" \
  --set cardanoNode.relayDns="testnet-relays.cardanopy.com" \
  --set cardanoNode.network="testnet" . > bin/testnet.yaml
#kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml
