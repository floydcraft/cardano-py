import click
import subprocess
from .core.cardanopy_config import CardanoPyConfig
from .core.substitution import Substitution


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def run(ctx, dry_run, target_config_dir):
    """Run command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    cardanopy_config = CardanoPyConfig()
    try:
        cardanopy_config.load(target_config_dir)
    except ValueError as e:
        ctx.fail(e.args)
        return 1

    try:
        Substitution.generate(dry_run, target_config_dir, cardanopy_config)
    except Exception as ex:
        ctx.fail(f"Failed to generate '{target_config_dir}': {ex} {type(ex).__name__} {ex.args}")
        return 1

    cardano_node_cmd = ["cardano-node",
                        "run",
                        "--config", cardanopy_config.configPath,
                        "--topology", cardanopy_config.topologyPath,
                        "--database-path", cardanopy_config.databasePath,
                        "--host-addr", cardanopy_config.hostAddr,
                        "--port", f"{cardanopy_config.port}",
                        "--socket-path", cardanopy_config.socketPath]
    if dry_run:
        print(" ".join(cardano_node_cmd))
    else:
        try:
            subprocess.run(cardano_node_cmd, cwd=target_config_dir)
        except Exception as ex:
            ctx.fail(f"Unknown exception: {ex} {type(ex).__name__} {ex.args}")
            return 1