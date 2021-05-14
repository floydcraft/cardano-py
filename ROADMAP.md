# Roadmap for cardano-py
> See [README.md](README.md#how-to-upgrade) for how to upgrade
Prioritized, but open to feedback!

# Table of Contents
- [0.2.0](#020)
- [0.3.0](#030)
- [0.4.0](#040)
- [0.5.0](#050)
- [0.6.0](#060)
- [0.7.0](#070)
- [1.0.0](#100)

## 0.2.0
> ALMOST DONE - Kubernetes capabilities

- `cardanopy k8s apply/*` - full node pool capabilities for both local kubernetes and GCP / GKE kubernetes.
- [Cardano Node: Kubernetes Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube Overview + Examples

## 0.3.0
> 2 Months - Cardano CLI capabilities

- `cardanopy cli *` - more core cli capabilities
- `cardanopy cli native-tokens`
- [Cardano Node: Native Token Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Docker compose - Overview + Examples

## 0.4.0
> 1 Month - docker capabilities

- `cardanopy docker run/stop` - add additional support for python docker (instead of requiring external dependency of docker)
- `cardanopy docker-compose up/*`
- [Cardano Node: Docker compose Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Docker compose - Overview + Examples

## 0.5.0
> 1 Month - Wallet capabilities

- `cardanopy wallet *`
- [Cardano Node: Wallet Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Wallet - Overview + Examples

## 0.6.0
> 1 Month - db-sync capabilities (postgres)

- `cardanopy db-sync *`
- [Cardano Node: Postgres Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Postgres - Overview + Examples

## 0.7.0
> 2 Months - data exports to json delimited, csv, GCP PubSub, and BigQuery.

- `cardanopy data *` - export capabilities like db-sync. except to useful formats for python data engineering, data science, and data exploration/insights. Includes JSON delimited, CSV, PubSub, and BigQuery.
- [Cardano Node: Json / BigQuery Example](https://github.com/floydcraft/cardano-py-examples)
- YouTube: Json / BigQuery - Overview + Examples

## 1.0.0
> 1 Month - Official Release

- bug fixes and improvements to all features 0.1.x - 0.7.x and documentation
- YouTube Official Release

## Looking for Feedback / Additional Scope planning
- Audit for wallet features (at least)
- REST API's
- Plutus docker image and helpers for Smart Contracts
- Native Token Helpers
- Metadata Helpers
