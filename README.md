[![cardano-py Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/FyDz4Xrt4x)

<img src="images/CardanoPyBlueSmall.png" alt="CardanoPy" width="150" height="150">

## Overview
[CardanoPy](https://github.com/floydcraft/cardano-py) is a simple and easy to use method to operate and extend Cardano Nodes (Relay and Producer) and DB Sync Nodes using a python CLI combined with docker. This project is a *Fund4* proposal for [Project Catalyst](https://cardano.ideascale.com/a/dtd/CardanoPy-5-min-extensible-node/341045-48088).

## Problem
Cardano nodes are complex and really should be SIMPLE to bootstrap / extend with your own features / projects using docker / python.

## Solution
*CardanoPy: 5 min extensible Cardano Nodes*
- `pip3 install cardanopy`
- `cardanopy create --template basic --network testnet bin/testnet-basic`
- `cardanopy docker run bin/testnet-basic`
- `cardanopy cli query tip`

## Roadmap
- (WIP) Kubernetes definitions for different deployments (relay, producer, relays, db sync, ...) (see `cardano-node`)
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


### Create - CardanoPy Config from templates (basic, bp-k8s, relay-k8s, ...)
> NOTE: using testnet for example
- `cardanopy create --template basic --network testnet bin/testnet-basic`

### Run - Cardano Node
- `cardanopy docker run bin/testnet-basic`
- `cardanopy cli query tip`
```json
{
    "blockNo": 351325,
    "headerHash": "3649fcfed5be50be78036c900e98057917e89d8faa54b64499af0779e4232040",
    "slotNo": 352369
}
```
