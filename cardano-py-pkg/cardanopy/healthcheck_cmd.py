import click
import time
from .node.query import query_tip
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

        tip = query_tip(dry_run)
        if len(tip) > 0 and "blockNo" in tip:
            return 0

        time.sleep(timeout)

        tip = query_tip(dry_run)
        if len(tip) > 0 and "blockNo" in tip:
            return 0

    except Exception as ex:
        ctx.fail(f"healthcheck_cmd(dry_run={dry_run}, timeout={timeout}, target_dir='{target_dir}') failed: {type(ex).__name__} {ex.args}")
        return 1

    print("unable to query tip for healthcheck")
    return 1
