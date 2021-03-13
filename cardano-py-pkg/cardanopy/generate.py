import click
from .core.cardanopy_config import CardanoPyConfig
from .core.substitution import Substitution


@click.command("generate")
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def generate_cmd(ctx, dry_run, target_config_dir):
    """Generate command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    cardanopy_config = CardanoPyConfig()
    try:
        cardanopy_config.load(target_config_dir)
    except ValueError as e:
        ctx.fail(e.args)
        return 1

    try:
        Substitution.generate(dry_run, target_config_dir, cardanopy_config)
    except Exception as ex:
        ctx.fail(f"Failed to generate '{target_config_dir}': {ex} {type(ex).__name__} {ex.args}")
        return 1