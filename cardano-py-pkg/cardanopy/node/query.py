import click
from .cardano_cli import CardanoCli
from ..core.cardanopy_error import CardanoPyError


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
        print(query_tip(dry_run), end="")
    except CardanoPyError as cpe:
        ctx.fail(cpe.message)
        return cpe.return_code


def query_tip(dry_run) -> str:
    """Get the node's current tip (slot no, hash, block no)."""
    result = CardanoCli.execute(cmd=["cardano-cli", "query", "tip"], dry_run=dry_run, include_network=True)
    if result.stderr_str:
        raise CardanoPyError(result.stderr_str)
    elif not result.stdout_str:
        raise CardanoPyError("null result for query tip")
    else:
        return result.stdout_str


@query_cmd.command("utxo")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.pass_context
def utxo_cmd(ctx, dry_run):
    """Get the node's current UTxO with the option of filtering by address(es)"""

    try:
        CardanoCli.execute(cmd=["cardano-cli", "query", "utxo"], dry_run=dry_run, include_network=True)
    except CardanoPyError as cpe:
        ctx.fail(cpe.message)
        return cpe.return_code
