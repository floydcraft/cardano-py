import click
from pathlib import Path
import shutil


def get_template_dir(network: str, template: str):
    return Path(__file__).parent.joinpath("data/templates").joinpath(network).joinpath(template)


@click.command("create")
@click.option('-t', '--template', 'template', required=True,
              type=click.Choice(['basic', 'bp-k8s', 'relay-k8s'], case_sensitive=False),
              help='template type to create.')
@click.option('-n', '--network', 'network', default="testnet",
              type=click.Choice(['testnet', 'mainnet'], case_sensitive=False), help='network type to create.')
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-q', '--quite', 'quite', is_flag=True, help="do not report warnings")
@click.argument('target_dir', type=str)
@click.pass_context
def create_cmd(ctx, template, network, dry_run, quite, target_dir):
    """Create command"""

    try:
        target_dir = Path(target_dir)
        network = network.lower()
        template = template.lower()
        template_dir = get_template_dir(network, template)

        if target_dir.exists():
            if not quite:
                ctx.fail(f"Failed to create. Directory '{target_dir}' already exists.")
                return 1
            else:
                return 0

        if not template_dir.is_dir() or not template_dir.exists():
            ctx.fail(f"Failed to create. Unable to locate template '{template}' for network '{network}'.")
            return 1

        if dry_run:
            print(f"copy 'template' directory from '{template_dir}' to '{target_dir}'")
        else:
            shutil.copytree(template_dir, target_dir)

        if not dry_run:
            print(f"Created cardano defaults from '{template}' template for network '{network}': '{target_dir}'")
    except Exception as ex:
        ctx.fail(f"create_cmd(template={template}, network={network}, dry_run={dry_run}, target_dir='{target_dir}') failed: {type(ex).__name__} {ex.args}")
        return 1
