import click

from .run import run
from .exec import exec

@click.group()
@click.pass_context
def docker(ctx):
    """Docker helper command"""
    pass

# export
docker.add_command(run)
docker.add_command(exec)