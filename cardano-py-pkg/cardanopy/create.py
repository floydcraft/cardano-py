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
        return Path(__file__).parent.joinpath("data/templates").absolute()

    @staticmethod
    def __get_template_dir(network: str, template: str):
        return CreateCommand.__get_templates_dir().joinpath(network).joinpath(template)

    @staticmethod
    def exec(ctx, template, network, dry_run, out_dir):
        out_dir = Path(out_dir)
        network = network.lower()
        template = template.lower()
        template_dir = CreateCommand.__get_template_dir(network, template)

        if dry_run:
            print("#### DRY RUN - no mutable changes will be made. ####")

        if out_dir.exists():
            ctx.fail(f"Failed to create. Directory '{out_dir}' already exists.")
            return 1

        if template_dir.is_dir() and template_dir.exists():
            try:
                if dry_run:
                    print(f"copy 'template' directory from '{template_dir}' to '{out_dir}'")
                else:
                    shutil.copytree(template_dir, out_dir)
            except Exception as ex:
                ctx.fail(f"Failed to create. Unable to copy config to '{out_dir}'. {type(ex).__name__} {ex.args}")
                return 1

            if not dry_run:
                print(f"Created cardano defaults from '{template}' template for network '{network}': '{out_dir}'")
        else:
            ctx.fail(f"Failed to create. Unable to locate template '{template}' for network '{network}'.")
            return 1
