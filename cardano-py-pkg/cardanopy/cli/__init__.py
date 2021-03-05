import click

from .commands.apply import apply
from .commands.run import run
from .commands.query import query
from .commands.address import address
from .commands.stake_address import stake_address

@click.group()
@click.version_option(version='0.1.0')
@click.pass_context
def cli(ctx):
    pass

# export
cli.add_command(apply)
cli.add_command(run)
cli.add_command(query)
cli.add_command(address)
cli.add_command(stake_address)