import click
import subprocess
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def exec(ctx, dry_run, target_config_dir):
    """Docker Exec helper command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

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
                        "-f", f"name={cardanopy_config.name}"],
                        stdout=subprocess.PIPE).stdout.decode('utf-8')
        container_running = len(result) > 0
    except Exception as ex:
        ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
        return 1

    if container_running:
        docker_run_cmd = ["docker",
                          "exec",
                          "-it",
                          cardanopy_config.name,
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
        ctx.fail(f"Docker container named '{cardanopy_config.name}' is NOT currently running. Please 'run' the container first.")
        return 1
