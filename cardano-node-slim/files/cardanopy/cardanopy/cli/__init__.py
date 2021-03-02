import click

from .commands.query import query
from .commands.address import address
from .commands.stake_address import stake_address

@click.group()
@click.version_option(version='0.1.0')
@click.pass_context
def cli(ctx):
    pass

# export
cli.add_command(query)
cli.add_command(address)
cli.add_command(stake_address)