import click

from .run import run

@click.group()
@click.pass_context
def docker(ctx):
    pass

# export
docker.add_command(run)