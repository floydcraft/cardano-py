import click
import subprocess
import yaml
from pathlib import Path
from .cardanopy_config import CardanoPyConfig


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

    try:
        subprocess.run(["cardano-node",
                        "run",
                        "--config", config.config,
                        "--topology", config.topology,
                        "--database-path", config.databasePath,
                        "--host-addr", config.hostAddr,
                        "--port", config.port,
                        "--socket-path", config.socketPath])
    except Exception as ex:
        ctx.fail(f"TODODO'. {type(ex).__name__} {ex.args}")
        return 1