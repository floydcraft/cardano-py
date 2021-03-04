import click
import subprocess

@click.group()
@click.pass_context
def query(ctx):
    """Node query commands. Will query the local node"""

@query.command()
def tip():
    """Get the node's current tip (slot no, hash, block no)."""
    subprocess.run(["cardano-cli","query","tip","--testnet-magic", "1097911063"])

