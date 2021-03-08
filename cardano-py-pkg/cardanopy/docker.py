import click

@click.command()
@click.argument('config', type=click.Path(exists=True))
def docker(config):
    """Docker command"""
    print (f"test Docker {config}")