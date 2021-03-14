import click

from .run_cmd import run_cmd
from .bash_cmd import bash_cmd
from .stop_cmd import stop_cmd

@click.group()
@click.pass_context
def docker(ctx):
    """Docker helper command"""
    pass

# export
docker.add_command(run_cmd)
docker.add_command(bash_cmd)
docker.add_command(stop_cmd)