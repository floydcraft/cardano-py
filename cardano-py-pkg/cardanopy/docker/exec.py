import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def exec(ctx, dry_run, target_config_dir):
    """Docker Exec helper command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_config_dir = Path(target_config_dir)

    if target_config_dir.is_dir():
        target_config = target_config_dir.joinpath("cardanopy.yaml")
    else:
        target_config = target_config_dir
        target_config_dir = target_config_dir.parent

    if not target_config_dir.exists():
        ctx.fail(f"Target directory '{target_config_dir}' does not exist.")
        return 1

    if not target_config.is_file():
        ctx.fail(
            f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")
        return 1

    if not target_config.exists():
        ctx.fail(f"Target file '{target_config}' does not exist.")
        return 1

    config = CardanoPyConfig()
    if not config.load(target_config):
        ctx.fail(f"Failed to load '{target_config}'")
        return 1

    try:
        result = subprocess.run(["docker",
                        "ps",
                        "-q",
                        "-f", f"name={config.name}"],
                        stdout=subprocess.PIPE).stdout.decode('utf-8')
        container_running = len(result) > 0
    except Exception as ex:
        ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
        return 1

    if container_running:
        docker_run_cmd = ["docker",
                          "exec",
                          "-it",
                          config.name,
                          "bin/bash"]
        if dry_run:
            print(" ".join(docker_run_cmd))
        else:
            try:
                subprocess.run(docker_run_cmd)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1
    else:
        ctx.fail(f"Docker container named '{config.name}' is NOT currently running. Please 'run' the container first.")
        return 1
