import click

from .query import query
from .address import address
from .stake_address import stake_address

@click.group()
@click.pass_context
def cli(ctx):
    pass

# export
cli.add_command(query)
cli.add_command(address)
cli.add_command(stake_address)