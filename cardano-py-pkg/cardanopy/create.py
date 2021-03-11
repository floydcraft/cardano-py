import click
from pathlib import Path
import shutil


@click.command()
@click.option('-t', '--template', 'template', required=True,
              type=click.Choice(['basic', 'bp-k8s', 'relay-k8s'], case_sensitive=False),
              help='template type to create.')
@click.option('-n', '--network', 'network', default="testnet",
              type=click.Choice(['testnet', 'mainnet'], case_sensitive=False), help='network type to create.')
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('out_dir', type=str)
@click.pass_context
def create(ctx, template, network, dry_run, out_dir):
    """Create command"""
    CreateCommand.exec(ctx, template, network, dry_run, out_dir)


class CreateCommand(object):

    @staticmethod
    def __get_templates_dir():
        return Path(__file__).parent.joinpath("templates").absolute()

    @staticmethod
    def __get_network_dir(network: str):
        return CreateCommand.__get_templates_dir().joinpath(network)

    @staticmethod
    def exec(ctx, template, network, dry_run, out_dir):
        out_dir = Path(out_dir)
        network = network.lower()
        network_dir = CreateCommand.__get_network_dir(network)

        if dry_run:
            print("#### DRY RUN - no mutable changes will be made. ####")

        if out_dir.exists():
            ctx.fail(f"Failed to create. Directory '{out_dir}' already exists.")
            return 1

        if network_dir.is_dir() and network_dir.exists():
            config_dir = network_dir.joinpath("config")
            template_yaml = network_dir.joinpath(f"{template}.yaml")

            if not config_dir.is_dir() or not config_dir.exists():
                ctx.fail(f"Failed to create. Unable to locate template '{network}/config'.")
                return 1

            if not template_yaml.is_file() or not template_yaml.exists():
                ctx.fail(f"Failed to create. Unable to locate template '{network}/{template}.yaml'.")
                return 1

            try:
                output_config_dir = out_dir.joinpath("config")
                if dry_run:
                    print(f"copy 'config' directory from '{config_dir}' to '{output_config_dir}'")
                else:
                    shutil.copytree(config_dir, output_config_dir)
            except Exception as ex:
                ctx.fail(f"Failed to create. Unable to copy config to '{out_dir}'. {type(ex).__name__} {ex.args}")
                return 1

            try:
                output_template_yaml = out_dir.joinpath('cardanopy.yaml')
                if dry_run:
                    print(f"copy 'cardanopy.yaml' file from '{template_yaml}' to '{output_template_yaml}'")
                else:
                    shutil.copyfile(template_yaml, output_template_yaml)
            except Exception as ex:
                ctx.fail(f"Failed to create. Unable to locate '{template}.yaml' to '{out_dir}'. {type(ex).__name__} {ex.args}")
                return 1

            if not dry_run:
                print(f"Created cardano defaults from '{template}' template for network '{network}': '{out_dir}'")
        else:
            ctx.fail(f"Failed to create. Unable to locate template '{template}' for network '{network}'.")
            return 1