import click
from pathlib import Path
from .cardanopy_config import CardanoPyConfig


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('--config-filename', 'config_filename', default='cardanopy.yaml', type=str, help="defaults to 'cardanopy.yaml'")
@click.argument('property', type=str, required=True)
@click.argument('value', type=str, required=True)
@click.argument('target_dir', type=str)
@click.pass_context
def config(ctx, dry_run, property, value, target_dir, config_filename):
    """Config command"""
    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    target_dir = Path(target_dir)

    if not target_dir.is_dir():
        ctx.fail(f"Target directory '{target_dir}' is not a directory. e.g., the directory that contains 'cardanopy.yaml'")
        return 1

    if not target_dir.exists():
        ctx.fail(f"Target directory '{target_dir}' does not exist.")
        return 1

    target_config = target_dir.joinpath(config_filename)

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
