__version__ = "0.1.2-dev12"
__license__ = "Apache-2.0 License"
__title__ = "cardanopy"

import click

from .apply import apply
from .run import run
from .cli import cli

@click.group()
@click.version_option(version=__version__)
@click.pass_context
def main(ctx):
    pass

# export
main.add_command(apply)
main.add_command(run)
main.add_command(cli)