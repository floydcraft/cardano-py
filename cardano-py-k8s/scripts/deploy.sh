#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

helm template --set namespace="cardano-mainnet" \
  --set cardanoNode.relayIpv4="cardanopy-relay-mainnet-ipv4" \
  --set cardanoNode.relayIpv6="cardanopy-relay-mainnet-ipv6" \
  --set cardanoNode.network="mainnet" . > bin/mainnet.yaml
helm template --set namespace="cardano-testnet" \
  --set cardanoNode.relayIpv4="cardanopy-relay-testnet-ipv4" \
  --set cardanoNode.relayIpv6="cardanopy-relay-testnet-ipv6" \
  --set cardanoNode.network="testnet" . > bin/testnet.yaml
kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml
