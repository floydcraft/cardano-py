import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.argument('target_config', type=str)
@click.pass_context
def run(ctx, target_config):
    """Docker Run command"""

    target_config = Path(target_config)

    if not target_config.is_file():
        ctx.fail(f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")
        return 1

    if not target_config.exists():
        ctx.fail(f"Target config '{target_config}' does not exist.")
        return 1

    config = CardanoPyConfig()
    if not config.load(target_config):
        ctx.fail(f"Failed to load '{target_config}'")
        return 1

    try:
        subprocess.run(["docker",
                        "container",
                        "rm", f"'{config.name}'"])
        subprocess.run(["docker",
                        "run",
                        "--name", f"'{config.name}'",
                        "-it",
                        "--entrypoint", "'/bin/bash'",
                        f"'{config.docker.image}'"])
    except Exception as ex:
        ctx.fail(f"TODODO'. {type(ex).__name__} {ex.args}")
        return 1





# if [[ "$2" == "pull" ]]; then
#   docker pull floydcraft/$IMAGE:latest
# fi
#
# printf "IMAGE=$IMAGE\nCARDANO_NETWORK=$CARDANO_NETWORK\n"
#
# if [[ "$( docker container inspect -f '{{.State.Running}}' "$IMAGE" )" == "true" ]]; then
#   printf "ACTIVE CONTAINER found for: $IMAGE\nattaching to the container\n"
#   docker exec -it "$IMAGE" bash
# else
#   printf "NO ACTIVE CONTAINER found for: $IMAGE\ncleaning containers and creating new container via run\n"
#   docker container rm "$IMAGE"
#   docker run --name "$IMAGE" -it \
#     -v "$PWD/storage/$CARDANO_NETWORK:/storage" \
#     --env "CARDANO_NETWORK=$CARDANO_NETWORK" \
#     --env "CARDANO_NODE_SOCKET_PATH=/storage/$CARDANO_NETWORK/node.socket" \
#     --entrypoint bash "floydcraft/$IMAGE:latest"
# fi
