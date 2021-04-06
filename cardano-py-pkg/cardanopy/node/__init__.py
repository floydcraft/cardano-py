import click

from .query import query_cmd
from .address_cmd import address_cmd
from .stake_address_cmd import stake_address_cmd


@click.group("node")
def node_cmd():
    """Cardano Node CLI command"""
    pass


# TODO:bfloyd remove later before 1.0
@click.command("cli")
@click.pass_context
def cli_cmd(ctx):
    ctx.fail("cli command group is obsolete. please use `node` instead for the same features. e.g., `cardanopy node query tip`")


# export
node_cmd.add_command(query_cmd)
node_cmd.add_command(address_cmd)
node_cmd.add_command(stake_address_cmd)
