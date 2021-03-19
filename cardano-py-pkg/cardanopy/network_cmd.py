import click
from .core.cardano_node_helpers import CardanoNodeHelpers


@click.command("network")
@click.option('-p', '--param', 'param', is_flag=True, help="print the network param help for cardano-cli")
def network_cmd(param):
    """Get the cardano network"""

    if not param:
        print(CardanoNodeHelpers.get_cli_network())
    else:
        print(" ".join(CardanoNodeHelpers.get_cli_network_args()))