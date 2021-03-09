import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('--config-filename', 'config_filename', default='cardanopy.yaml', type=str, help="defaults to 'cardanopy.yaml'")
@click.argument('target_dir', type=str)
@click.pass_context
def exec(ctx, dry_run, target_dir, config_filename):
    """Docker Exec helper command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_dir = Path(target_dir)

    if not target_dir.is_dir():
        ctx.fail(f"Target directory '{target_dir}' is not a directory. e.g., the directory that contains 'cardanopy.yaml'")
        return 1

    if not target_dir.exists():
        ctx.fail(f"Target directory '{target_dir}' does not exist.")
        return 1

    target_config = target_dir.joinpath(config_filename)

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
