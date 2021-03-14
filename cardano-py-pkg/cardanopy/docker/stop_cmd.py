import click
import subprocess
from pathlib import Path
from ..core.cardanopy_config import CardanoPyConfig


@click.command("stop")
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def stop_cmd(ctx, dry_run, target_config_dir):
    """Docker Bash helper command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_config_dir = Path(target_config_dir)

    cardanopy_config = CardanoPyConfig()
    try:
        cardanopy_config.load(target_config_dir)
    except ValueError as e:
        ctx.fail(e.args)
        return 1

    try:
        result = subprocess.run(["docker",
                        "ps",
                        "-q",
                        "-f", f"name={cardanopy_config.docker.name}"],
                        stdout=subprocess.PIPE).stdout.decode('utf-8')
        container_running = len(result) > 0
    except Exception as ex:
        ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
        return 1

    if container_running:
        docker_stop_cmd = ["docker",
                           "stop",
                           cardanopy_config.docker.name]
        if dry_run:
            print(" ".join(docker_stop_cmd))
        else:
            try:
                subprocess.run(docker_stop_cmd)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1

    try:
        result = subprocess.run(["docker",
                                 "ps",
                                 "-aq",
                                 "-f", f"name={cardanopy_config.docker.name}"],
                                stdout=subprocess.PIPE).stdout.decode('utf-8')
        container_exited = len(result) > 0
    except Exception as ex:
        ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
        return 1

    if container_exited:
        docker_container_rm_cmd = ["docker",
                                    "container",
                                    "rm", cardanopy_config.docker.name]
        if dry_run:
            print(" ".join(docker_container_rm_cmd))
        else:
            try:
                subprocess.run(docker_container_rm_cmd)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1

