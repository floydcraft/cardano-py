import click
import subprocess
from pathlib import Path
from .cardanopy_config import CardanoPyConfig

@click.command()
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config', type=str)
@click.pass_context
def run(ctx, dry_run, target_config):
    """Run command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

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

    cardano_node_cmd = ["cardano-node",
                            "run",
                            "--config", config.config,
                            "--topology", config.topologyPath,
                            "--database-path", config.databasePath,
                            "--host-addr", config.hostAddr,
                            "--port", f"{config.port}",
                            "--socket-path", config.socketPath]
    if dry_run:
        print(" ".join(cardano_node_cmd))
    else:
        try:
            subprocess.run(cardano_node_cmd)
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1
