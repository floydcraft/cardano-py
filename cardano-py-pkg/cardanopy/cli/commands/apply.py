import click

@click.command()
@click.argument('config', type=click.Path(exists=True))
def apply(config):
    """Apply command"""
    print (f"test apply {config}")