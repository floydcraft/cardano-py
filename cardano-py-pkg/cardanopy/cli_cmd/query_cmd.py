import click
import subprocess
from pathlib import Path
import os
from ..core.cardano_node_helpers import CardanoNodeHelpers


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
        CardanoNodeHelpers.validate_environment()

        query_tip_cmd = ["cardano-cli", "query", "tip"] + CardanoNodeHelpers.get_cli_network_args()
        if dry_run:
            print(" ".join(query_tip_cmd))
        else:
            subprocess.run(query_tip_cmd)
    except Exception as ex:
        ctx.fail(f"cli:query_cmd:tip_cmd(dry_run={dry_run}) failed: {type(ex).__name__} {ex.args}")
        return 1



@query_cmd.command("utxo")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.pass_context
def utxo_cmd(ctx, dry_run):
    """Get the node's current UTxO with the option of filtering by address(es)"""

    try:
        CardanoNodeHelpers.validate_environment()

        query_tip_cmd = ["cardano-cli", "query", "utxo"] + CardanoNodeHelpers.get_cli_network_args()
        if dry_run:
            print(" ".join(query_tip_cmd))
        else:
            subprocess.run(query_tip_cmd)
    except Exception as ex:
        ctx.fail(f"cli:query_cmd:tip_cmd(dry_run={dry_run}) failed: {type(ex).__name__} {ex.args}")
        return 1

