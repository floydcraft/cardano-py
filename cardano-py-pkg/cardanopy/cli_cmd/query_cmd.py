import click
from .cardano_cli import CardanoCli, CardanoCliError


@click.group("query")
@click.pass_context
def query_cmd(ctx):
    """Node query commands. Will query the local node"""


@query_cmd.command("tip")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.pass_context
def tip_cmd(ctx, dry_run):
    """Get the node's current tip (slot no, hash, block no)."""

    try:
        CardanoCli.run(cmd=["cardano-cli", "query", "tip"], dry_run=dry_run, include_network=True)
    except CardanoCliError as cce:
        ctx.fail(cce.message)
        return cce.return_code


@query_cmd.command("utxo")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.pass_context
def utxo_cmd(ctx, dry_run):
    """Get the node's current UTxO with the option of filtering by address(es)"""

    try:
        CardanoCli.run(cmd=["cardano-cli", "query", "utxo"], dry_run=dry_run, include_network=True)
    except CardanoCliError as cce:
        ctx.fail(cce.message)
        return cce.return_code

