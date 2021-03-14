[![cardano-py Discord](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/FyDz4Xrt4x)

<img src="images/CardanoPyBlueSmall.png" alt="CardanoPy" width="150" height="150">

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
  7f1b51871e4f0be32e81c51d7e471a26ef282eb34bdb96295376421a14e6ad99
  root@7f1b51871e4f:/#
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

# CardanoPy Examples
  - [Cardano Node: Basic Example](https://github.com/floydcraft/cardano-py-examples/tree/master/basic-example)
  - (TODO) Cardano Pool: Docker Compose Example
  - (WIP) Cardano Pool: Kubernetes (k8s) Example

# Roadmap
- (WIP) Kubernetes definitions for different deployments (relay, producer, relays, db sync, ...) (see `cardano-node`)
- (TODO) cardanopy etl feature for db-sync providers

# Core Docker Images on [dockerhub](https://hub.docker.com/u/floydcraft)
## CardanoPy
- [cardano-py-slim](https://github.com/floydcraft/cardano-py/tree/master/cardano-py-slim) - Runtime slim build of CardanoPy Cardano node. Preinstalls latest cardanopy package.
## Cardano IOHK
- [cardano-node-iohk-dev](https://github.com/floydcraft/cardano-node-iohk/tree/master/dev) - developer image of [IOHK Cardano Node](https://github.com/input-output-hk/cardano-node) using [haskell](https://github.com/floydcraft/haskell) image. Includes Haskell and Cardano node source and binaries.
- [cardano-node-iohk-slim](https://github.com/floydcraft/cardano-node-iohk/tree/master/slim) - Runtime slim build of [cardano-node-iohk-dev](https://github.com/floydcraft/cardano-node-iohk/tree/master/dev).
- (DRAFT) [cardano-db-sync-iohk-dev](https://github.com/floydcraft/cardano-db-sync-iohk) - developer image of [IOHK Cardano DB Sync](https://github.com/input-output-hk/cardano-db-sync) using [haskell](https://github.com/floydcraft/haskell) image. Includes Haskell and Cardano DB Sync source and binaries.
- (TODO) `cardano-db-sync-iohk-slim` - Runtime slim build of [cardano-db-sync-iohk-dev](https://github.com/floydcraft/cardano-db-sync-iohk).
## Common
- [haskell](https://github.com/floydcraft/haskell) - base image to build Haskell projects like Cardano.
