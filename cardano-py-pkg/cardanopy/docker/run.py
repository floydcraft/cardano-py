import click
import subprocess
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

    cardanopy_config = CardanoPyConfig()
    try:
        cardanopy_config.load(target_config_dir)
    except ValueError as e:
        ctx.fail(e.args)
        return 1

    if pull:
        docker_pull_cmd = ["docker", "pull", cardanopy_config.docker.image]
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
                        "-f", f"name={cardanopy_config.name}"],
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
                                     "-f", f"name={cardanopy_config.name}"],
                                    stdout=subprocess.PIPE).stdout.decode('utf-8')
            container_exited = len(result) > 0
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1

        if container_exited:
            docker_container_rm_cmd = ["docker",
                                        "container",
                                        "rm", cardanopy_config.name]
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
                            "--name", cardanopy_config.name,
                            "-d",
                            "--env", f"CARDANO_NODE_SOCKET_PATH={cardanopy_config.socketPath}",
                            "--env", f"CARDANO_NETWORK={cardanopy_config.network}",
                            "-p", f"{cardanopy_config.port}:{cardanopy_config.port}",
                            "-v", f"{target_config_dir.absolute()}:{cardanopy_config.root}",
                            cardanopy_config.docker.image,
                            "run",
                            "/app"]))

        docker_exec_cmd = ["docker",
                          "exec",
                          "-it",
                          cardanopy_config.name,
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
