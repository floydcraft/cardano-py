import click

from .apply import apply
from .run import run
from .cli import cli

@click.group()
@click.version_option(version='0.1.0')
@click.pass_context
def main(ctx):
    pass

# export
main.add_command(apply)
main.add_command(run)
main.add_command(cli)