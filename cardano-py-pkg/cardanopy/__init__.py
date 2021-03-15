__version__ = "0.1.7-dev6"
__license__ = "Apache-2.0 License"
__title__ = "cardanopy"

import click

from .run_cmd import run_cmd
from .create_cmd import create_cmd
from .cli_cmd import cli_cmd
from .docker_cmd import docker_cmd
from .k8s_cmd import k8s_cmd
from .generate_cmd import generate_cmd
# from .config import config

@click.group()
@click.version_option(version=__version__)
@click.pass_context
def main(ctx):
    pass


# export
main.add_command(run_cmd)
main.add_command(create_cmd)
main.add_command(cli_cmd)
main.add_command(docker_cmd)
main.add_command(k8s_cmd)
main.add_command(generate_cmd)
# disable config cli for now (might remove)
# main.add_command(config)
