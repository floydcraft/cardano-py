#!/bin/bash
set -e
set -u
set -o pipefail

mkdir -p bin

#kubectl create secret generic -n cardano-mainnet \
#  block-producer-credentials \
#  --from-file files/bp/kes.skey \
#  --from-file files/bp/node.cert \
#  --from-file files/bp/vrf.skey
#kubectl create secret generic -n cardano-testnet \
#  block-producer-credentials \
#  --from-file files/bp/kes.skey \
#  --from-file files/bp/node.cert \
#  --from-file files/bp/vrf.skey