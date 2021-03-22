import click
import time
import subprocess
from .core.cardano_node_helpers import CardanoNodeHelpers
from .core.cardanopy_config import CardanoPyConfig


@click.command("healthcheck")
@click.option('-s', '--sub', 'subs', multiple=True, type=str, default=tuple(), help="Substitutions for configs")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-t', '--timeout', 'timeout', default=60, type=int, help="timeout for healthcheck second check")
@click.argument('target_dir', type=str)
@click.pass_context
def healthcheck_cmd(ctx, dry_run, subs, timeout, target_dir):
    """Check if the cardano network is healthy"""

    try:
        target_config_file = CardanoPyConfig.try_get_valid_config_file(target_dir)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, subs)

        query_tip_cmd = ["cardano-cli", "query", "tip"] + CardanoNodeHelpers.get_cli_network_args()
        if dry_run:
            print(" ".join(query_tip_cmd))
        else:
            result = subprocess.run(query_tip_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
            if len(result) > 0 and "blockNo" in result:
                return 0

        time.sleep(timeout)

        if dry_run:
            print(" ".join(query_tip_cmd))
        else:
            result = subprocess.run(query_tip_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
            if len(result) > 0 and "blockNo" in result:
                return 0

    except Exception as ex:
        ctx.fail(f"healthcheck_cmd(dry_run={dry_run}, timeout={timeout}, target_dir='{target_dir}') failed: {type(ex).__name__} {ex.args}")
        return 1

    print("unable to query tip for healthcheck")
    return 1
