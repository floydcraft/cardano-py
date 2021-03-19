import click
from ..core.cardano_node_helpers import CardanoNodeHelpers


@click.group("network")
def network_cmd():
    """Node network commands. Helpers."""


@network_cmd.command("option")
def option_cmd():
    """Get the command line option for the Cardano network. Useful helper"""

    print(CardanoNodeHelpers.get_cli_network_args())