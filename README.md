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
- [Resources](#resources)
  - [Core Docker Images](#core-docker-images)
    - [CardanoPy](#cardanopy)
    - [Cardano IOHK](#cardano-iohk)
    - [Common](#common)

> WARNING: THIS IS A PRE-RELEASE of cardanopy (until it reaches [1.0.0](ROADMAP.md#100); currently [0.1.7](CHANGELOG.md#017))
> 
> Things will:
> - Break
> - Lack documentation
> - Differ greatly between iterations
> - Disorient, overload and inspire

# Overview
> NOTE: Please visit the Cardano Idealscale link and provide this project Kudos and/or provide feedback!

[CardanoPy](https://github.com/floydcraft/cardano-py) is a simple and easy to use method to operate and extend Cardano Nodes (Relay and Producer) and DB Sync Nodes using a python CLI combined with docker. It's intended for dApp development and data infrastricture by providing python access to cardano node and onchain data / apis. 

Checkout the [Project Catalyst - Fund 4 Proposal](https://cardano.ideascale.com/a/dtd/CardanoPy-5-min-extensible-node/341045-48088) and [Project Catalyst - Fund 5 Proposal](https://cardano.ideascale.com/a/dtd/CardanoPy-python-dApp-passive-node/351323-48088). 

Also see [ROADMAP.md](ROADMAP.md#100) and [CHANGELOG.md](CHANGELOG.md#017).

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

  `cardanopy node query tip` as often as you like.

  > NOTE: might take a minute before the `files/app/node.socket` file to be created while cardano node is booting. It will take longer the larger the database `files/app/db`.

  ```json
  {
  "epoch": 126,
  "hash": "bafe78f11866e3b77a254f55c46bd44335b367197db74fb95620237f43fe583d",
  "slot": 24098404,
  "block": 2494291
  }
  ```

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
