import click
from .node.cardano_cli import CardanoCli
from .node.cardano_node import CardanoNode


@click.command("network")
@click.option('-p', '--param', 'param', is_flag=True, help="print the network param help for cardano-cli")
def network_cmd(param):
    """Get the cardano network"""

    if not param:
        print(CardanoNode.get_cli_network())
    else:
        print(" ".join(CardanoCli.get_network_cli_args()))