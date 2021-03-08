import click

@click.command()
@click.argument('config', type=click.Path(exists=True))
def k8s(config):
    """Kubernetes command"""
    print (f"test Kubernetes {config}")