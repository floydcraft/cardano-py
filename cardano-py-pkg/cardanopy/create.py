import click
import string
from pathlib import Path
import os
import shutil
import json
from .cardanopy_config import CardanoPyConfig

_TEMPLATES_DIR = Path(__file__).parent.joinpath("templates").absolute()


def try_create_template(ctx, network: str, template: str, out_dir: str):
    out_dir = Path(out_dir)
    network = network.lower()
    network_dir = _TEMPLATES_DIR.joinpath(network)

    if out_dir.exists():
        ctx.fail(f"Failed to create. Directory '{out_dir}' already exists.")
        return 1

    if network_dir.is_dir() and network_dir.exists():
        config_dir = network_dir.joinpath("config")
        storage_dir = network_dir.joinpath("storage")
        template_yaml = network_dir.joinpath(f"{template}.yaml")

        if not config_dir.is_dir() or not config_dir.exists():
            ctx.fail(f"Failed to create. Unable to locate template '{network}/config'.")
            return 1

        if not storage_dir.is_dir() or not storage_dir.exists():
            ctx.fail(f"Failed to create. Unable to locate template '{network}/storage'.")
            return 1

        if not template_yaml.is_file() or not template_yaml.exists():
            ctx.fail(f"Failed to create. Unable to locate template '{network}/{template}.yaml'.")
            return 1

        try:
            shutil.copytree(config_dir, out_dir.joinpath("config"))
        except Exception as ex:
            ctx.fail(f"Failed to create. Unable to copy config to '{out_dir}'. {type(ex).__name__} {ex.args}")
            return 1

        try:
            shutil.copytree(storage_dir, out_dir.joinpath("storage"))
        except Exception as ex:
            ctx.fail(f"Failed to create. Unable to copy storage to '{out_dir}'. {type(ex).__name__} {ex.args}")
            return 1

        try:
            shutil.copyfile(template_yaml, out_dir.joinpath('cardanopy.yaml'))
        except Exception as ex:
            ctx.fail(f"Failed to create. Unable to locate '{template}.yaml' to '{out_dir}'. {type(ex).__name__} {ex.args}")
            return 1

        out_cardanopy_config_file = out_dir.joinpath('cardanopy.yaml')

        config = CardanoPyConfig()
        if not config.load(out_cardanopy_config_file):
            ctx.fail(f"Failed to load '{out_cardanopy_config_file}'")
            return 1

        with open(out_dir.joinpath(config.topologyPath), "w") as file:
            print(json.dumps(config.topology, sort_keys=True, indent=4), file=file)

        print(f"Created template '{template}' for network '{network}': '{out_dir}'")
    else:
        ctx.fail(f"Failed to create. Unable to locate template '{template}' for network '{network}'.")
        return 1


@click.command()
@click.option('-t', '--template', 'template', required=True, type=str, help='template type to create.')
@click.option('-n', '--network', 'network', default="testnet",
              type=click.Choice(['testnet', 'mainnet'], case_sensitive=False), help='network type to create.')
@click.argument('out_dir', type=click.Path(file_okay=False, dir_okay=True, exists=False))
@click.pass_context
def create(ctx, template, network, out_dir):
    """Create command"""
    try_create_template(ctx, network, template, out_dir)