__version__ = "0.1.8"
__license__ = "Apache-2.0 License"
__title__ = "cardanopy"

import click

from .run_cmd import run_cmd
from .create_cmd import create_cmd
from .node import node_cmd, cli_cmd
from .docker_cmd import docker_cmd
from .k8s_cmd import k8s_cmd
from .generate_cmd import generate_cmd
from .network_cmd import network_cmd
from .healthcheck_cmd import healthcheck_cmd

@click.group()
@click.version_option(version=__version__)
@click.pass_context
def main(ctx):
    pass


# export
main.add_command(run_cmd)
main.add_command(create_cmd)
main.add_command(node_cmd)
main.add_command(cli_cmd)
main.add_command(docker_cmd)
main.add_command(k8s_cmd)
main.add_command(generate_cmd)
main.add_command(network_cmd)
main.add_command(healthcheck_cmd)
# disable config cli for now (might remove)
# main.add_command(config)
