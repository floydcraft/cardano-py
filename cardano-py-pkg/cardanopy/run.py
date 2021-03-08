import click
import subprocess
from pathlib import Path
from .cardanopy_config import CardanoPyConfig
import os

@click.command()
@click.argument('target_config', type=str)
@click.pass_context
def run(ctx, target_config):
    """Run command"""
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

    os.putenv("CARDANO_NODE_SOCKET_PATH", config.socketPath)

    try:
        command = ["cardano-node",
                        "run",
                        "--config", config.config,
                        "--topology", config.topologyPath,
                        "--database-path", config.databasePath,
                        "--host-addr", config.hostAddr,
                        "--port", f"{config.port}",
                        "--socket-path", config.socketPath]
        print(command)
        subprocess.run(command)
    except Exception as ex:
        ctx.fail(f"TODODO'. {type(ex).__name__} {ex.args}")
        return 1