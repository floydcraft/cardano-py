import click
import subprocess
from pathlib import Path
from cardanopy.cardanopy_config import CardanoPyConfig


@click.command()
@click.option('-p', '--pull', 'pull', is_flag=True, help="pull the docker image. Instead of using local docker image cache")
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def run(ctx, pull, dry_run, target_config_dir):
    """Docker Run helper command"""

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
                            "-d",
                            "--env", f"CARDANO_NODE_SOCKET_PATH={config.socketPath}",
                            "--env", f"CARDANO_NETWORK={config.network}",
                            "-p", f"{config.port}:{config.port}",
                            "-v", f"{target_config_dir.absolute()}:{config.root}",
                            config.docker.image,
                            "run",
                            "/app"]))

        docker_exec_cmd = ["docker",
                          "exec",
                          "-it",
                          config.name,
                          "bin/bash"]
        if dry_run:
            print(" ".join(docker_run_cmd))
            print(" ".join(docker_exec_cmd))
        else:
            try:
                subprocess.run(docker_run_cmd, cwd=target_config_dir)
                subprocess.run(docker_exec_cmd, cwd=target_config_dir)
            except Exception as ex:
                ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
                return 1
    else:
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
