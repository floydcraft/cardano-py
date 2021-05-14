#!/bin/bash
set -e
set -u
set -o pipefail

gcloud config configurations activate cardano-etl
gcloud container clusters get-credentials cardanopy --zone us-central1-c