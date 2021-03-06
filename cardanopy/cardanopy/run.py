import click

@click.command()
@click.option('-n', '--node', 'node', required=True, type=str, help='Node to run from config')
@click.argument('config', type=click.Path(exists=True))
def run(node, config):
    """Run command"""
    print (f"test run node={node} config={config}")