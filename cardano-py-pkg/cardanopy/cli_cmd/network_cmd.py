import click
from ..core.cardano_node_helpers import CardanoNodeHelpers


@click.group("network")
def network_cmd():
    """Node network commands. Helpers."""


@network_cmd.command("param")
def param_cmd():
    """Get the command line param for the Cardano network CLI. Useful helper"""

    print(" ".join(CardanoNodeHelpers.get_cli_network_args()))
