# Changelog for cardano-py
> See [README.md](README.md#how-to-upgrade) for how to upgrade

# Table of Contents
- [0.1.9](#019)
- [0.1.7](#017)
- [0.1.6](#016)

## 0.1.9
> 4/18/2021
This point release is a recommended upgrade for all stake pool operators. It is not required for relays or other passive nodes. It ensures that block producing nodes do not unnecessarily re-evaluate the stake distribution at the epoch boundary.

### Cardano Node
- Upgrade to [1.26.2](https://github.com/input-output-hk/cardano-node/releases/tag/1.26.2)

## 0.1.7 
> 4/15/2021

MVP kubernetes implementation. Still needs to be added to the CLI (0.2.0), but is being used in production for APy🥧 Cardano Node.

### Cardano Node
- Upgrade to [1.26.1](https://github.com/input-output-hk/cardano-node/releases/tag/1.26.1)

### CLI
- `create --quite` - new flag to suppress error prompt when the director exists
- `network --param` - new command to get the network w/ or w/o the param for cardano-cli. e.g., --mainnet or --testnet magic_id
- `healthcheck --timeout` - new command useful for doing a healthcheck on the cardano node operations w/ timeout. 
- moved `cli` to `node` in prep for additional commands `wallet`, `db-sync`, ...

### Docker
- cardano-py-slim - added optional ada user

### Config
- updated cardanopy.yaml defaults

### Kubernetes
- MVP k8s implementation. Still not part of the CLI, but WIP. 

### Web
- MVP Website for CardanoPy landing page w/ HTTPS support. New kubernetes pod. 
- Nodejs backend for metadata and serving static frontend
- Static Angularjs frontend for landing page.

### Learn
- Moved CHANGELOG and ROADMAP to respective *.md files

### Bugs
- fixed /bin/bash path bug that was occuring in some cases

## 0.1.6
> 3/14/2021

MVP key capabilities / developer workflow

### CLI 
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
  
### Learn
- [Cardano Node: Basic Example](https://github.com/floydcraft/cardano-py-examples/tree/master/basic-example)
- YouTube: CardanoPy - Overview + Examples