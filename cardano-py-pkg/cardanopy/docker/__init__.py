import click

from .run import run

@click.group()
@click.pass_context
def docker(ctx):
    """Docker helper command"""
    pass

# export
docker.add_command(run)