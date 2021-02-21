[![cardano-node-k8s Telegram](https://img.shields.io/badge/telegram-join%20chat-blue.svg)](http://bit.ly/cardano-node-k8s-telegram)

## Overview
[Cardano Node k8s (Kubernetes)](https://github.com/floydcraft/cardano-node-k8s) is a simple and easy to use method to operate and extend Cardano Stakepools + DB Sync. Provides the foundation for [Cardano ETL](https://github.com/floydcraft/cardano-etl) which is a proposal for [Project Catalyst Fund3](https://cardano.ideascale.com/a/dtd/Cardano-ETL-Public-BigQuery-Data/334530-48088).

## Problem
Cardano Stakepools are complex and difficult to get started for many reasons. The primary issue is productivity and lack of standardization.

## Solution
This repo provides and alternative which anyone can try in a few mins have a stakepool running passively. It will also have a GCP / AWS deployable kuberentes setup w/ privisioning steps.

## Roadmap
- (WIP) Core Docker Images (Dev + Slim) with CI/CD
- (Local) Kubernetes Definition for different deployments (passive, active/producer, relays, db sync, ...)

## Core Docker Images on [dockerhub](https://hub.docker.com/u/floydcraft)
- (MVP) `haskell` "haskell" - base image to build Haskell projects like Cardano.
- (MVP) `cardano-node-iohk` "iohk" - build of [IOHK Cardano Node](https://github.com/input-output-hk/cardano-node) using `haskell` image.
- (MVP) `cardano-node-iohk-slim` "iohk-slim" - slim build of `cardano-node-iohk` (only runtime)
- (MVP) `cardano-node-slim` "slim" - slim build of custom node planning to use for `cardano-etl`
- (WIP) `cardano-db-sync-iohk` "db-sync-iohk" - build of [IOHK Cardano DB Sync](https://github.com/input-output-hk/cardano-db-sync) using `haskell` image.
- (WIP) `cardano-db-sync-iohk-slim` "db-sync-iohk-slim" - slim build of `cardano-db-sync-iohk` (only runtime)

## Quickstarts
### Passive Cardano Stakepool
> NOTE: this section is works atm, but is still under development
> Requires docker. Works on OSX and likely linux distributions

1. Clone this repo and open terminal at the project root of `cardano-node-k8s`
2. `chmod +x scripts/run.sh`
3. `./scripts/run.sh slim testnet pull`
- "slim" is my custom Cardano container I'm building for cardano-etl. See above for the different options
- "testnet" is the devnet for Cardano. Can also use "mainnet"
- "pull" will force a pull from docker hub "latest" tag. If you opmit it will use a local image.
4. Once in the container run `./scripts/entrypoint.sh`
5. Congratulations! You should now see the Passive Cardano Node booting.

### Cardano DB Sync
> NOTE: This section is WIP. Might not work without some minor fixes.
> Requires docker. Works on OSX and likely linux distributions

1. Clone this repo and open terminal at the project root of `cardano-node-k8s`
2. `chmod +x scripts/run.sh`
3. `./scripts/run.sh slim testnet pull`
4. Once in the container run `./scripts/entrypoint.sh`   
5. Open an additional terminal at the project root of `cardano-node-k8s`
6. `./scripts/run.sh db-sync-iohk testnet pull`
7. Once in the container run `./scripts/entrypoint.sh`
8. Congratulations! You should now see the Passive Cardano Node booting and have access to the Postgres SQL db syncing.

