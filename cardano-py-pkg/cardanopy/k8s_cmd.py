import click


@click.command("k8s")
@click.argument('config', type=click.Path(exists=True))
def k8s_cmd(config):
    """Kubernetes command (PRE-ALPHA)"""
    print(f"test Kubernetes {config}")