[![cardano-py Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/FyDz4Xrt4x)

[![dockeri.co](https://dockeri.co/image/floydcraft/cardano-py-slim)](https://hub.docker.com/r/floydcraft/cardano-py-slim)

[![GitHub issues](https://img.shields.io/github/issues/floydcraft/cardano-py/cardanopy.svg "GitHub issues")](https://github.com/floydcraft/cardano-py/issues)

<img src="images/CardanoPyBlueSmall.png" alt="CardanoPy" width="150" height="150">

## Table of Contents

- [Overview](#overview)
- [Problem](#problem)
- [Solution](#solution)
- [Quickstart](#quickstart)
  - [Use predefined docker image cardano-py-slim](#use-predefined-docker-image-cardano-py-slim)
- [Releases](#roadmap)
  - [0.1.x](#01x)
- [Roadmap](#roadmap)
  - [0.2.0](#020)
  - [0.3.0](#030)
  - [0.4.0](#040)
  - [0.5.0](#050)
  - [0.6.0](#060)
  - [0.7.0](#070)
  - [1.0.0](#100)
- [Resources](#resources)
  - [Core Docker Images](#core-docker-images)
    - [CardanoPy](#cardanopy)
    - [Cardano IOHK](#cardano-iohk)
    - [Common](#common)

> NOTE: THIS IS A PRE-RELEASE of cardanopy (until it reaches 1.0 in 2 months or so; currently 0.1.6 as of Pi Day (3/14/2021), but already with some cool features)

# Overview
> NOTE: Please visit the Cardano Idealscale link and provide this project Kudos and/or provide feedback!

[CardanoPy](https://github.com/floydcraft/cardano-py) is a simple and easy to use method to operate and extend Cardano Nodes (Relay and Producer) and DB Sync Nodes using a python CLI combined with docker. This project is a *Fund4* proposal for [Project Catalyst](https://cardano.ideascale.com/a/dtd/CardanoPy-5-min-extensible-node/341045-48088).

# Problem
Cardano nodes are complex and really should be SIMPLE to bootstrap / extend with your own features / projects using docker / python.

# Solution
See Quickstart.

# Quickstart
## Use predefined docker image cardano-py-slim
> See [Basic Example](https://github.com/floydcraft/cardano-py-examples/tree/master/basic-example) for custom docker image example.

- Install or upgrade cardanopy:

  `pip3 install --upgrade cardanopy`
- Create the basic config for testnet:

  `cardanopy create --template basic --network testnet files/app`

  ```bash
  Created cardano defaults from 'basic' template for network 'testnet': 'files/app'
  ```
- Start/run the node using that config:

  `cardanopy docker run files/app`

  ```bash
  ada@ce02f129e793:~$
  ```
- Once your logged into the node, run:

  `cardanopy cli query tip` as often as you like.

  > NOTE: might take a minute before the `files/app/node.socket` file to be created while cardano node is booting. It will take longer the larger the database `files/app/db`.

  ```json
  {
      "blockNo": 351325,
      "headerHash": "3649fcfed5be50be78036c900e98057917e89d8faa54b64499af0779e4232040",
      "slotNo": 352369
  }
  ```

# Releases
> NOTE: you can use these features already!

## 0.1.x
3/14/2021 - MVP key capabilities / developer workflow
- `cardanopy run` - executes cardano-node command using cardanopy.yaml config to generate *.template.json configs.
- `cardanopy create` - creates a cardanopy app from a template ('basic, producer-k8s, relay-k8s'). e.g., cardanopy.yaml, config.template.json, ...
- `cardanopy generate` - generates configs from cardanopy app using cardanopy.yaml
- `cardanopy docker run` - runs or attaches to docker container by name using cardanopy.yaml docker.* configs.
- `cardanopy docker stop` - stops docker container by name using cardanopy.yaml docker.name config.
- `cardanopy cli address` - same as cardano-cli except automaticaly provides cardano network param (testnet/mainnet)
- `cardanopy cli stake-address` - same as cardano-cli except automaticaly provides cardano network param (testnet/mainnet)
- `cardanopy cli query` - same as cardano-cli except automaticaly provides cardano network param (testnet/mainnet)
- `-d, --dry-run` - flag to print without mutation what would be executed. useful for most commands like docker and kubernetes.
- substitutions - core capability of cardanopy. cardanopy.yaml can both in memory and write to disk substitutions to configs before running a cardano-node. e.g., _BP_ENABLED=True or _BP_ENABLED=False to enable / disable a blocker producer.
- `-s KEY=VALUE, --sub KEY=VALUE` - optional override to substitutions defaults in cardanpy.yaml config.
- [Cardano Node: Basic Example](https://github.com/floydcraft/cardano-py-examples/tree/master/basic-example)
- YouTube: CardanoPy - Overview + Examples

# Roadmap
Prioritized, but open to feedback!

## 0.2.0
March - Kubernetes capabilities
> NOTE: WIP now. Already have testnet working. See [CardanoPy](https://github.com/floydcraft/cardano-py) GitHub

- `cardanopy k8s apply/*` - full node pool capabilities for both local kubernetes and GCP / GKE kubernetes.
- [Cardano Node: Kubernetes Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube Overview + Examples

## 0.3.0
April - Cardano CLI capabilities
- `cardanopy cli *` - more core cli capabilities
- `cardanopy cli native-tokens`
- [Cardano Node: Native Token Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Docker compose - Overview + Examples

## 0.4.0
April - docker capabilities
- `cardanopy docker run/stop` - add additional support for python docker (instead of requiring external dependency of docker)
- `cardanopy docker-compose up/*`
- [Cardano Node: Docker compose Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Docker compose - Overview + Examples

## 0.5.0
May - Wallet capabilities
- `cardanopy wallet *`
- [Cardano Node: Wallet Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Wallet - Overview + Examples

## 0.6.0
June - db-sync capabilities (postgres)
- `cardanopy db-sync *`
- [Cardano Node: Postgres Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Postgres - Overview + Examples

## 0.7.0
July through August - data exports to json delimited, csv, GCP PubSub, and BigQuery.
- `cardanopy data *` - export capabilities like db-sync. except to useful formats for python data engineering, data science, and data exploration/insights. Includes JSON delimited, CSV, PubSub, and BigQuery.
- [Cardano Node: Json / BigQuery Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Json / BigQuery - Overview + Examples

## 1.0.0
September - Official Release
- bug fixes and improvements to all features 0.1.x - 0.7.x and documentation
- YouTube Official Release

# Core Docker Images
Available on [floydcraft dockerhub](https://hub.docker.com/u/floydcraft)

## CardanoPy
- [cardano-py-slim](https://github.com/floydcraft/cardano-py/tree/master/cardano-py-slim) - Runtime slim build of CardanoPy Cardano node. Preinstalls latest cardanopy package.
## Cardano IOHK
- [cardano-node-iohk-dev](https://github.com/floydcraft/cardano-node-iohk/tree/master/dev) - developer image of [IOHK Cardano Node](https://github.com/input-output-hk/cardano-node) using [haskell](https://github.com/floydcraft/haskell) image. Includes Haskell and Cardano node source and binaries.
- [cardano-node-iohk-slim](https://github.com/floydcraft/cardano-node-iohk/tree/master/slim) - Runtime slim build of [cardano-node-iohk-dev](https://github.com/floydcraft/cardano-node-iohk/tree/master/dev).
- (DRAFT) [cardano-db-sync-iohk-dev](https://github.com/floydcraft/cardano-db-sync-iohk) - developer image of [IOHK Cardano DB Sync](https://github.com/input-output-hk/cardano-db-sync) using [haskell](https://github.com/floydcraft/haskell) image. Includes Haskell and Cardano DB Sync source and binaries.
- (TODO) `cardano-db-sync-iohk-slim` - Runtime slim build of [cardano-db-sync-iohk-dev](https://github.com/floydcraft/cardano-db-sync-iohk).
## Common
- [haskell](https://github.com/floydcraft/haskell) - base image to build Haskell projects like Cardano.
