import click

from .query_cmd import query_cmd
from .address_cmd import address_cmd
from .stake_address_cmd import stake_address_cmd


@click.group("cli")
def cli_cmd():
    """Cardano CLI command"""
    pass

# export
cli_cmd.add_command(query_cmd)
cli_cmd.add_command(address_cmd)
cli_cmd.add_command(stake_address_cmd)
