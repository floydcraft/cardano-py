import click
from pathlib import Path
from .cardanopy_config import CardanoPyConfig


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('property', type=str, required=True)
@click.argument('value', type=str, required=True)
@click.argument('target_config_dir', type=str)
@click.pass_context
def config(ctx, dry_run, property, value, target_config_dir):
    """Config command"""
    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_config_dir = Path(target_config_dir)

    if target_config_dir.is_dir():
        target_config = target_config_dir.joinpath("cardanopy.yaml")
    else:
        target_config = target_config_dir
        target_config_dir = target_config_dir.parent

    if not target_config_dir.exists():
        ctx.fail(f"Target directory '{target_config_dir}' does not exist.")
        return 1

    if not target_config.is_file():
        ctx.fail(
            f"Target config '{target_config}' is not a file. e.g., 'cardanopy.yaml'")
        return 1

    if not target_config.exists():
        ctx.fail(f"Target file '{target_config}' does not exist.")
        return 1

    config = CardanoPyConfig()
    if not config.load(target_config):
        ctx.fail(f"Failed to load '{target_config}'")
        return 1

    config.set(property, value)

    if not config.save(target_config):
        ctx.fail(f"Failed to save '{target_config}'")
        return 1
