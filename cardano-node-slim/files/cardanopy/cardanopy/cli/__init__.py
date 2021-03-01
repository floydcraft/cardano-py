import click

from .commands.query import query

@click.group()
@click.version_option(version='0.1.0')
@click.pass_context
def cli(ctx):
    pass

# export
cli.add_command(query)