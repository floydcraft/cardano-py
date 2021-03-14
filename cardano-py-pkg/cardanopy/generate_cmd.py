import click
from .core.cardanopy_config import CardanoPyConfig
from .core.substitution import Substitution


@click.command("generate")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-s', '--sub', 'subs', multiple=True, type=str, default=tuple(), help="Substitutions for configs")
@click.argument('target_config_dir_or_file', type=str)
@click.pass_context
def generate_cmd(ctx, dry_run, subs, target_config_dir_or_file):
    """Generate command"""

    try:
        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir_or_file)
        target_config_file = CardanoPyConfig.try_get_valid_config_file(target_config_dir_or_file)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, subs)

        Substitution.generate(dry_run, target_config_dir, cardanopy_config, subs)
    except Exception as ex:
        ctx.fail(f"generate_cmd(dry_run={dry_run}, target_config_dir_or_file='{target_config_dir_or_file}') failed: {type(ex).__name__} {ex.args}")
        return 1
