import click
from ..core.cardanopy_config import CardanoPyConfig
from .docker_helper import DockerHelper


@click.command("run")
@click.option('-p', '--pull', 'pull', is_flag=True, help="pull the docker image. Instead of using local docker image cache")
@click.option('-s', '--stop', 'stop', is_flag=True, help="stop and remove the docker image before running")
@click.option('-b', '--bash', 'bash', is_flag=True, help="override docker image entrypoint with /bin/bash")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-s', '--subs', 'subs', multiple=True, type=str, default=tuple(), help="Substitutions for configs")
@click.argument('target_config_dir_or_file', type=str)
@click.pass_context
def run_cmd(ctx, pull, stop, bash, dry_run, subs, target_config_dir_or_file):
    """Docker Run helper command"""

    try:
        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir_or_file)
        target_config_file = CardanoPyConfig.try_get_valid_config_file(target_config_dir_or_file)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, subs)

        if pull:
            DockerHelper.pull_container(cardanopy_config.docker.image, dry_run)

        is_container_running = DockerHelper.is_container_running(cardanopy_config.docker.name, dry_run)

        if is_container_running:
            if stop:
                DockerHelper.stop_container(cardanopy_config.docker.name, dry_run)
            else:
                DockerHelper.exec_bash(cardanopy_config.docker.name, target_config_dir, dry_run)
                return 0

        if DockerHelper.is_container_exited(cardanopy_config.docker.name, dry_run):
            DockerHelper.remove_container(cardanopy_config.docker.name, dry_run)

        DockerHelper.run_cardano_node(cardanopy_config.docker.name,
                                      target_config_dir,
                                      cardanopy_config.socketPath,
                                      cardanopy_config.network,
                                      cardanopy_config.port,
                                      cardanopy_config.docker.rootVolume,
                                      cardanopy_config.docker.image,
                                      bash,
                                      dry_run)

        if not bash:
            DockerHelper.exec_bash(cardanopy_config.docker.name, target_config_dir, dry_run)
    except Exception as ex:
        ctx.fail(f"docker:run_cmd(pull={pull}, "
                 f"dry_run={dry_run}, "
                 f"target_config_dir_or_file='{target_config_dir_or_file}') failed: {type(ex).__name__} {ex.args}")
        return 1
