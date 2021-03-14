import click

from .run_cmd import run_cmd
from .bash_cmd import bash_cmd
from .stop_cmd import stop_cmd


@click.group()
@click.pass_context
def docker_cmd(ctx):
    """Docker helper command"""
    pass

# export
docker_cmd.add_command(run_cmd)
docker_cmd.add_command(bash_cmd)
docker_cmd.add_command(stop_cmd)