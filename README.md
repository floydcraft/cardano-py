[![cardano-py Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/FyDz4Xrt4x)

<img src="images/CardanoPyBlueSmall.png" alt="CardanoPy" width="150" height="150">

## Overview
[CardanoPy](https://github.com/floydcraft/cardano-py) is a simple and easy to use method to operate and extend Cardano Nodes (Relay and Producer) and DB Sync Nodes using a python CLI combined with docker. This project is a *Fund4* proposal for [Project Catalyst](https://cardano.ideascale.com/a/dtd/CardanoPy-5-min-extensible-node/341045-48088).

## Problem
Cardano nodes are complex and really should be SIMPLE to bootstrap / extend with your own features / projects using docker / python.

## Solution
*CardanoPy: 5 min extensible Cardano Nodes*
- (4 mins) `pip3 install cardanopy`
- (1 min) `cardanopy run cardano-node-slim:latest --network testnet pynode`
- (0 secs) `cardanopy exec pynode query tip`

## Roadmap
- (WIP) Core Docker Images (Dev + Slim) with CI/CD
- (WIP) Kubernetes definitions for different deployments (relay, producer, relays, db sync, ...) (see `cardano-node`)
- (WIP) cardanopy python CLI approach
- (TODO) move 'run.sh' features into python CLI
- (TODO) cardanopy wrapper for cardano-cli w/ easy of use improvements
- (TODO) cardanopy etl feature for db-sync providers

## Core Docker Images on [dockerhub](https://hub.docker.com/u/floydcraft)
- (MVP) `haskell` "haskell" - base image to build Haskell projects like Cardano.
- (MVP) `cardano-node-iohk` "iohk" - build of [IOHK Cardano Node](https://github.com/input-output-hk/cardano-node) using `haskell` image.
- (MVP) `cardano-node-iohk-slim` "iohk-slim" - slim build of `cardano-node-iohk` (only runtime)
- (MVP) `cardano-node-slim` "slim" - slim build of custom node planning to use for `cardano-etl`
- (WIP) `cardano-db-sync-iohk` "db-sync-iohk" - build of [IOHK Cardano DB Sync](https://github.com/input-output-hk/cardano-db-sync) using `haskell` image.
- (WIP) `cardano-db-sync-iohk-slim` "db-sync-iohk-slim" - slim build of `cardano-db-sync-iohk` (only runtime)


## Quickstarts (DRAFT Proposal)
> NOTE: All of these are WIP. See "Quickstarts (working pre-alpha)" for working examples.

### Prerequisites
- python3 is required.

### Install CardanoPy
- `pip3 install cardanopy`

### Run - Cardano Node
- Complete "Install CardanoPy" OR "Install CardanoPy via Source" step.
- `cardanopy run cardano-node-slim:latest --network testnet pynode`
- `cardanopy exec pynode query tip`
```json
{
    "blockNo": 351325,
    "headerHash": "3649fcfed5be50be78036c900e98057917e89d8faa54b64499af0779e4232040",
    "slotNo": 352369
}
```

### (OPTIONAL) Install CardanoPy via Source
- `git clone git@github.com:floydcraft/cardano-py.git`
- `cd cardano-py`
- `python3 setup.py install`

### (OPTIONAL) Build - Cardano Node
- Complete "Install CardanoPy via Source" step.
- `cardanopy build --tag cardano-node-slim:latest --dir cardano-node-slim`
- Complete "Run - Cardano Node" step.


## Quickstarts (working pre-alpha)

### Passive Cardano Stakepool
> NOTE: this section is works atm, but is still under development
> Requires docker. Works on OSX and likely linux distributions

1. Clone this repo and open terminal at the project root of `cardano-node-k8s`
2. `chmod +x scripts/run.sh`
3. `./scripts/run.sh slim testnet relay blue pull`
- "slim" is my custom Cardano container I'm building for cardano-etl. See above for the different options
- "testnet" is the devnet for Cardano. Can also use "mainnet"
- "relay" a simple type of cardano node
- "blue" type of deployment for kubernetes (will be optional later)
- "pull" will force a pull from docker hub "latest" tag. If you omit it will use a local image.

4. Once in the container run `./scripts/entrypoint.sh`
5. Congratulations! You should now see the Passive Cardano Node booting.

### Cardano DB Sync
> NOTE: This section is broken atm and is still WIP.

1. Clone this repo and open terminal at the project root of `cardano-node-k8s`
2. `chmod +x scripts/run.sh`
3. `./scripts/run.sh slim testnet relay blue pull`
4. Once in the container run `./scripts/entrypoint.sh`   
5. Open an additional terminal at the project root of `cardano-py`
6. `./scripts/run.sh db-sync-iohk testnet pull` (broken atm)
7. Once in the container run `./scripts/entrypoint.sh`
8. Congratulations! You should now see the Passive Cardano Node booting and have access to the Postgres SQL db syncing.
