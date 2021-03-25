#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

helm template --set namespace="cardano-mainnet" \
  --set cardanoNode.relayIpv4="34.107.174.232" \
  --set cardanoNode.relayIpv6="2600:1901:0:1ac5::" \
  --set cardanoNode.network="mainnet" . > bin/mainnet.yaml
helm template --set namespace="cardano-testnet" \
  --set cardanoNode.relayIpv4="34.120.114.40" \
  --set cardanoNode.relayIpv6="2600:1901:0:686c::" \
  --set cardanoNode.network="testnet" . > bin/testnet.yaml
kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
kubectl apply -n cardano-testnet -f bin/testnet.yaml
