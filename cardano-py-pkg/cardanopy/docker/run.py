import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('--pull', 'pull', is_flag=True, help="pull the docker image. Instead of using local docker image cache")
@click.option('--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('--bash', 'bash', is_flag=True, help="connect to the container via bash")
@click.option('-d', '--daemon', 'daemon', is_flag=True, help="runs the container in the background")
@click.option('--config-filename', 'config_filename', default='cardanopy.yaml', type=str, help="defaults to 'cardanopy.yaml'")
@click.argument('target_dir', type=str)
@click.pass_context
def run(ctx, pull, dry_run, bash, target_dir, config_filename, daemon):
    """Docker Run helper command"""

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

    if pull:
        docker_pull_cmd = ["docker", "pull", config.docker.image]
        if dry_run:
            print(" ".join(docker_pull_cmd))
        else:
            try:
                subprocess.run(docker_pull_cmd)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
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

    if not container_running:
        try:
            result = subprocess.run(["docker",
                                     "ps",
                                     "-aq",
                                     "-f", f"name={config.name}"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8')
            container_exited = len(result) > 0
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1

        if container_exited:
            docker_container_rm_cmd = ["docker",
                                        "container",
                                        "rm", config.name]
            if dry_run:
                print(" ".join(docker_container_rm_cmd))
            else:
                try:
                    subprocess.run(docker_container_rm_cmd)
                except Exception as ex:
                    ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                    return 1

        docker_run_cmd = list(filter(None,["docker",
                            "run",
                            "--name", config.name,
                            "-d" if daemon else None,
                            "--env", f"CARDANO_NODE_SOCKET_PATH={config.socketPath}",
                            "-p", f"{config.port}:{config.port}",
                            "-it" if bash else None,
                            "--entrypoint" if bash else None,
                            "bin/bash" if bash else None,
                            config.docker.image]))
        if dry_run:
            print(" ".join(docker_run_cmd))
        else:
            try:
                subprocess.run(docker_run_cmd)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1
    else:
        ctx.fail(f"Docker container named '{config.name}' is currently running. Please stop/exit the container first.")
        return 1
