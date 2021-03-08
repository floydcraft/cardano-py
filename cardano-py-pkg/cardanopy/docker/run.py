import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('--pull', is_flag=True)
@click.argument('target_config', type=str)
@click.pass_context
def run(ctx, pull, target_config):
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

    if pull:
        try:
            subprocess.run(["docker", "pull", config.name])
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1

    try:
        result = subprocess.run(["docker",
                        "ps",
                        "-q",
                        "-f", f"name={config.name}"],
                        stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(f"container_running={result}")
        container_running = len(result) > 0
    except Exception as ex:
        ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
        return 1

    if not container_running:
        try:
            result = subprocess.run(["docker",
                                     "ps",
                                     "-aq",
                                     "-f", f"name={config.name}"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8')
            print(f"container_exited={result}")
            container_exited = len(result) > 0
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1

        if container_exited:
            try:
                subprocess.run(["docker",
                                "container",
                                "rm", config.name])
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1

        try:
            subprocess.run(["docker",
                            "run",
                            "--name", config.name,
                            "-it",
                            "--env", f"CARDANO_NODE_SOCKET_PATH={config.socketPath}",
                            "--entrypoint", "/bin/bash",
                            config.docker.image])
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1
    else:
        ctx.fail(f"Docker container named '{config.name}' is currently running. Please stop/exit the container first.")
        return 1
