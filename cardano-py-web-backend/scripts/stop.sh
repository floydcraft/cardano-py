#!/bin/bash
#set -e
#set -u
#set -o pipefail

docker stop "cardano-py-web-backend"
docker rm "cardano-py-web-backend"