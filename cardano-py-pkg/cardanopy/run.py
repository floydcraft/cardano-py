import click

@click.command()
@click.option('-n', '--node', 'node', required=True, type=str, help='Node to run from config')
@click.argument('config', type=click.Path(exists=True))
def run(node, config):
    """Run command"""
    print (f"test run node={node} config={config}")






# cardanopy run /config/testnet/cardanopy-basic.yaml


# cd network/testnet




# cardanopy k8s generate


    # -g, --generate-name                generate the name (and omit the NAME parameter)

##### V2 RUN ######

## ----- LOCAL ----- ##
# cardanopy create --template basic --network testnet basic-testnet
# cd basic
# cardanopy run

# config/**
# storage/**
## cardanopy.yaml

## cardanopy run --config cardanopy-featurex.yaml


# cardanopy create --template basic --network mainnet basic-mainnet
# cd basic-mainnet
# cardanopy run

## ----- DOCKER ----- ##

# cardanopy docker run
# cardanopy docker exec -it - bash
# cardanopy docker exec - ls

## ----- k8s ----- ##

# cardanopy k8s apply
# cardanopy k8s delete




##### V2 Docker ######





# cardanopy docker run --set _BLOCK_PRODUCER_ENABLED=True k8s-producer.yaml .
# cardanopy docker run --set _POD_ORDINAL=0 k8s-relay.yaml .






##### RUN #####

# cardanopy run basic.yaml .
# cardanopy run --set _BLOCK_PRODUCER_ENABLED=False k8s-producer.yaml .
# cardanopy run --set _BLOCK_PRODUCER_ENABLED=True k8s-producer.yaml .
# cardanopy run --set _POD_ORDINAL=0 k8s-relay.yaml .
# cardanopy run --set _POD_ORDINAL=1 k8s-relay.yaml .

# https://docs.cardano.org/projects/cardano-node/en/latest/stake-pool-operations/start_your_nodes.html
# cardano-node run --config "/config/$CARDANO_NETWORK/config.json" \
#   --topology $TOPOLOGY_CONFIG \
#   --database-path "/storage/$CARDANO_NETWORK/db" \
#   --host-addr "0.0.0.0" \
#   --port 3001 \
#   --socket-path "/storage/$CARDANO_NETWORK/node.socket"

# --shelley-kes-key kes.skey \
# --shelley-vrf-key vrf.skey \
# --shelley-operational-certificate node.cert

##### DOCKER #####
# ./scripts/run.sh testnet pull
# ./scripts/run.sh mainnet pull

# cardanopy run docker basic.yaml .
# cardanopy run docker --set _BLOCK_PRODUCER_ENABLED=False k8s-producer.yaml .
# cardanopy run docker --set _BLOCK_PRODUCER_ENABLED=True k8s-producer.yaml .
# cardanopy run docker --set _POD_ORDINAL=0 k8s-relay.yaml .
# cardanopy run docker --set _POD_ORDINAL=1 k8s-relay.yaml .

# fails / prompts for docker install / setup

# if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
#     printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
#     docker exec -it "$IMAGE" bash
# else
#     printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
#     docker container rm "$IMAGE"
#     docker run --name "$IMAGE" -it \
#     -v "$PWD/storage/$CARDANO_NETWORK:/storage" \
#     --env "CARDANO_NETWORK=$CARDANO_NETWORK" \
#     --env "CARDANO_NODE_SOCKET_PATH=/storage/$CARDANO_NETWORK/node.socket" \
#     --entrypoint bash "floydcraft/$IMAGE:latest"
# fi

##### K8S ######
# ./scripts/deploy.sh testnet

# helm template --set namespace=cardano-mainnet --set cardanoNetwork=mainnet . > bin/mainnet.yaml
# helm template --set namespace=cardano-testnet --set cardanoNetwork=testnet . > bin/testnet.yaml
# #kubectl apply -n cardano-mainnet -f bin/mainnet.yaml
# kubectl apply -n cardano-testnet -f bin/testnet.yaml


# cardanopy run k8s basic.yaml .
# cardanopy run k8s --set _BLOCK_PRODUCER_ENABLED=False k8s-producer.yaml .
# cardanopy run k8s --set _BLOCK_PRODUCER_ENABLED=True k8s-producer.yaml .
# cardanopy run k8s --set _POD_ORDINAL=0 k8s-relay.yaml .
# cardanopy run k8s --set _POD_ORDINAL=1 k8s-relay.yaml .
