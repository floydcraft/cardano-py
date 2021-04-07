import subprocess
from pathlib import Path
from ..core.cardanopy_config import CardanoPyConfig


class DockerHelper(object):

    @staticmethod
    def is_container_running(container_name: str, dry_run=False):
        docker_cmd = ["docker",
                     "ps",
                     "-q",
                     "-f", f"name=^/{container_name}$"]
        if dry_run:
            print(" ".join(docker_cmd))

        try:
            result = subprocess.run(docker_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
            return len(result) > 0
        except Exception as ex:
            raise ValueError(f"DockerHelper:is_container_running('{container_name}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def is_container_exited(container_name: str, dry_run=False):
        docker_cmd = ["docker",
                     "ps",
                     "-aq",
                     "-f", f"name=^/{container_name}$"]
        if dry_run:
            print(" ".join(docker_cmd))

        try:
            result = subprocess.run(docker_cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
            return len(result) > 0
        except Exception as ex:
            raise ValueError(f"DockerHelper:is_container_exited('{container_name}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def remove_container(container_name: str, dry_run=False):
        docker_cmd = ["docker",
                       "rm",
                       container_name]
        if dry_run:
            print(" ".join(docker_cmd))
        else:
            try:
                subprocess.run(docker_cmd)
            except Exception as ex:
                raise ValueError(f"DockerHelper:remove_container('{container_name}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def stop_container(container_name: str, dry_run=False):
        docker_cmd = ["docker",
                      "stop",
                      container_name]
        if dry_run:
            print(" ".join(docker_cmd))
        else:
            try:
                subprocess.run(docker_cmd)
            except Exception as ex:
                raise ValueError(
                    f"DockerHelper:stop_container('{container_name}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def pull_container(docker_image: str, dry_run=False):
        docker_cmd = ["docker",
                      "pull",
                      docker_image]
        if dry_run:
            print(" ".join(docker_cmd))
        else:
            try:
                subprocess.run(docker_cmd)
            except Exception as ex:
                raise ValueError(
                    f"DockerHelper:pull('{docker_image}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def exec_bash(container_name: str, target_config_dir: Path, dry_run=False):

        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir)

        docker_cmd = ["docker",
                      "exec",
                      "-it",
                      container_name,
                      "/bin/bash"]
        if dry_run:
            print(" ".join(docker_cmd))
        else:
            try:
                subprocess.run(docker_cmd, cwd=target_config_dir)
            except Exception as ex:
                raise ValueError(f"DockerHelper:exec_bash('{container_name}') failed. {type(ex).__name__} {ex.args}")

    @staticmethod
    def run_cardano_node(container_name: str,
                         target_config_dir: Path,
                         socket_path: str,
                         network: str,
                         port: int,
                         docker_root_volume: str,
                         docker_image: str,
                         docker_mount: bool = False,
                         bash=False,
                         dry_run=False):

        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir)

        docker_cmd = list(filter(None,
                                ["docker",
                                "run",
                                "--name", container_name,
                                "-d" if not bash else None,
                                "--env", f"CARDANO_NODE_SOCKET_PATH={socket_path}",
                                "--env", f"CARDANO_NETWORK={network}",
                                "-p", f"{port}:{port}",
                                "-v" if docker_mount else None,
                                f"{target_config_dir.absolute()}:{docker_root_volume}" if docker_mount else None,
                                "-it" if bash else None,
                                "--entrypoint",
                                "/bin/bash" if bash else "cardanopy",
                                docker_image,
                                "run" if not bash else None,
                                docker_root_volume if not bash else None]))

        if dry_run:
            print(" ".join(docker_cmd))
        else:
            try:
                subprocess.run(docker_cmd, cwd=target_config_dir)
            except Exception as ex:
                raise ValueError(f"DockerHelper:run_cardano_node('{container_name}', '{target_config_dir}') failed. {type(ex).__name__} {ex.args}")