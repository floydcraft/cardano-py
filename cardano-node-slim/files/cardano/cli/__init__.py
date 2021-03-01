import click

from cardano.cli.query_tip import query_tip

@click.group()
@click.version_option(version='1.6.1')
@click.pass_context
def cli(ctx):
    pass

# export
cli.add_command(query_tip, "query_tip")