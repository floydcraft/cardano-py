import click
import subprocess
from pathlib import Path
from ..core.cardanopy_config import CardanoPyConfig
from .docker_helper import DockerHelper


@click.command("stop")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-s', '--sub', 'subs', multiple=True, type=str, default=tuple(), help="Substitutions for configs")
@click.argument('target_config_dir_or_file', type=str)
@click.pass_context
def stop_cmd(ctx, dry_run, subs, target_config_dir_or_file):
    """Docker Stop helper command"""

    try:
        target_config_file = CardanoPyConfig.try_get_valid_config_file(target_config_dir_or_file)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, subs)

        if DockerHelper.is_container_running(cardanopy_config.docker.name, dry_run):
            DockerHelper.stop_container(cardanopy_config.docker.name, dry_run)

        if DockerHelper.is_container_exited(cardanopy_config.docker.name, dry_run):
            DockerHelper.remove_container(cardanopy_config.docker.name, dry_run)
    except Exception as ex:
        ctx.fail(f"docker_cmd:stop_cmd(dry_run={dry_run}, target_config_dir_or_file='{target_config_dir_or_file}') failed: {type(ex).__name__} {ex.args}")
        return 1
