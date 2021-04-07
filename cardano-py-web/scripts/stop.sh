#!/bin/bash
#set -e
#set -u
#set -o pipefail

docker stop "cardano-py-web"
docker rm "cardano-py-web"
