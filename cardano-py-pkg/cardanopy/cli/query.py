import click
import subprocess
from pathlib import Path
import os


@click.group()
@click.pass_context
def query(ctx):
    """Node query commands. Will query the local node"""


@query.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.pass_context
def tip(ctx, dry_run):
    """Get the node's current tip (slot no, hash, block no)."""

    cardano_node_socket_path = os.getenv('CARDANO_NODE_SOCKET_PATH')
    if not cardano_node_socket_path:
        ctx.fail(f"Invalid CARDANO_NODE_SOCKET_PATH. Undefined.")
        return 1

    cardano_node_socket_path = Path(cardano_node_socket_path)
    if not cardano_node_socket_path.exists():
        ctx.fail(f"Invalid CARDANO_NODE_SOCKET_PATH. '{cardano_node_socket_path}' does not exist.")
        return 1

    cardano_network = os.getenv('CARDANO_NETWORK')
    if not cardano_network:
        cardano_network = "testnet"

    cardano_network_cmd = ["--mainnet"] if cardano_network == "mainnet" else ["--testnet-magic", "1097911063"]

    query_tip_cmd = ["cardano-cli", "query", "tip"] + cardano_network_cmd
    if dry_run:
        print(" ".join(query_tip_cmd))
    else:
        try:
            subprocess.run(query_tip_cmd)
        except Exception as ex:
            ctx.fail(f"Unknown exception: {type(ex).__name__} {ex.args}")
            return 1

