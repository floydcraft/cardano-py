import click
from ..core.cardanopy_config import CardanoPyConfig
from .docker_helper import DockerHelper


@click.command("run")
@click.option('-p', '--pull', 'pull', is_flag=True, help="pull the docker image. Instead of using local docker image cache")
@click.option('-s', '--stop', 'stop', is_flag=True, help="stop and remove the docker image before running")
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def run_cmd(ctx, pull, dry_run, target_config_dir_or_file):
    """Docker Run helper command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir_or_file)
    target_config_file = CardanoPyConfig.try_get_valid_config_file(target_config_dir_or_file)

    cardanopy_config = CardanoPyConfig()
    cardanopy_config.load(target_config_file)

    if pull:
        DockerHelper.pull(cardanopy_config.docker.image, dry_run)

    if DockerHelper.is_container_running(cardanopy_config.docker.name, dry_run):
        DockerHelper.exec_bash(cardanopy_config.docker.name, target_config_dir, dry_run)
    else:
        if DockerHelper.is_container_exited(cardanopy_config.docker.name, dry_run):
            DockerHelper.remove_container(cardanopy_config.docker.name, dry_run)

        DockerHelper.run_cardano_node(cardanopy_config.docker.name,
                                      target_config_dir,
                                      cardanopy_config.socketPath,
                                      cardanopy_config.network,
                                      cardanopy_config.port,
                                      cardanopy_config.docker.rootVolume,
                                      cardanopy_config.docker.image,
                                      dry_run)

        DockerHelper.exec_bash(cardanopy_config.docker.name, target_config_dir, dry_run)
