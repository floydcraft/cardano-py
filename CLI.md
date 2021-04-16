# CLI for cardano-py
> NOTE: requires python3 to be installed to use.

> NOTE: Docker is OPTIONAL if you want to run locally. You can run the docker container on remote machines as well.

## CLI
- `--help` - show help messages (on all commands)
  

- `-d, --dry-run` - print the mutable commands (on most commands)

  
- `-s, --sub {{KEY=VALUE}}` - optional override to substitutions defaults in cardanpy.yaml config (on some commands)


- `cardanopy create {{TARGET_DIR}}` - Create command
    - `-t, --template [basic|bp-k8s|relay-k8s]` - template type to create *[required]*
    - `-n, --network [testnet|mainnet]` - network type to create
    - `-q, --quite` - do not report warnings


- `cardanopy docker run {{TARGET_CONFIG_DIR_OR_FILE}}` - Docker Run helper command
    - `-p, --pull` - pull the docker image. Instead of using local docker image cache
    - `-s, --stop` - stop and remove the docker image before running
    - `-b, --bash` - override docker image entrypoint with /bin/bash
    - `-d, --dry-run` - print the mutable commands
    - `-s, --sub {{TEXT}}` - Substitutions for configs


- `cardanopy docker stop {{TARGET_CONFIG_DIR_OR_FILE}}` - Docker Stop helper command
    - `-d, --dry-run` - print the mutable commands
    - `-s, --sub {{TEXT}}` - Substitutions for configs


- `cardanopy node query tip` - Get the node's current tip (slot no, hash, block no).
    - `-d, --dry-run` - print the mutable commands


- `cardanopy run {{TARGET_CONFIG_DIR_OR_FILE}}` - Run command
    - `-b, --block-producer` - enable block producer mode
    - `-d, --dry-run` - print the mutable commands
    - `-s, --sub {{TEXT}}` - Substitutions for configs
    

- `cardanopy generate {{TARGET_CONFIG_DIR_OR_FILE}}` - Generate command
    - `-d, --dry-run` - print the mutable commands
    - `-s, --sub {{TEXT}}` - Substitutions for configs


- `cardanopy healthcheck` - Check if the cardano node is healthy
    - `-t, --timeout {{INTEGER}}` - timeout for healthcheck second check
    - `-d, --dry-run` - print the mutable commands


- `cardanopy k8s *` - In Active Development for 0.2.0
    - `-d, --dry-run` - print the mutable commands
    - `-q, --quite` - do not report warnings
    

- `cardanopy cli *` - Obsolete in 0.1.7! Moved to `cardanopy node *`
    

## Simple Example
- Install or upgrade cardanopy:
  
  `pip3 install --upgrade cardanopy`

- Create a new cardanopy project in the folder `app`:

  `cardanopy create --template basic --network testnet app`

  ```bash
  Created cardano defaults from 'basic' template for network 'testnet': 'app'
  ```
- Start docker container for the CardanoPy project `app`:

  `cardanopy docker run app`

  ```bash
  root@ce02f129e793:~$
  ```
- Start docker container for the CardanoPy project `app` once logged into the Docker container:

  `cardanopy node query tip`

  ```json
  {
  "epoch": 126,
  "hash": "bafe78f11866e3b77a254f55c46bd44335b367197db74fb95620237f43fe583d",
  "slot": 24098404,
  "block": 2494291
  }
  ```
