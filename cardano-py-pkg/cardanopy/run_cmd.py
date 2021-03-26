import click
import subprocess
from .core.cardanopy_config import CardanoPyConfig
from .core.substitution import Substitution


@click.command("run")
@click.option('-d', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.option('-b', '--block-producer', 'block_producer', is_flag=True, help="enable block producer mode")
@click.option('-s', '--sub', 'subs', multiple=True, type=str, default=tuple(), help="Substitutions for configs")
@click.argument('target_config_dir_or_file', type=str)
@click.pass_context
def run_cmd(ctx, dry_run, block_producer, subs, target_config_dir_or_file):
    """Run command"""

    try:
        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(target_config_dir_or_file)
        target_config_file = CardanoPyConfig.try_get_valid_config_file(target_config_dir_or_file)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, subs)

        Substitution.generate(dry_run, target_config_dir, cardanopy_config, subs)

        cardano_node_cmd = ["cardano-node",
                            "run",
                            "--config", cardanopy_config.configPath,
                            "--topology", cardanopy_config.topologyPath,
                            "--database-path", cardanopy_config.databasePath,
                            "--host-addr", cardanopy_config.hostAddr,
                            "--port", f"{cardanopy_config.port}",
                            "--socket-path", cardanopy_config.socketPath]

        if block_producer:
            cardano_node_cmd = cardano_node_cmd + ["--shelley-kes-key", cardanopy_config.shelleyKesKey,
                                                   "--shelley-vrf-key", cardanopy_config.shelleyVrfKey,
                                                   "--shelley-operational-certificate", cardanopy_config.shelleyOperationalCertificate]

        if dry_run:
            print(" ".join(cardano_node_cmd))
        else:
            subprocess.run(cardano_node_cmd, cwd=target_config_dir)
    except Exception as ex:
        ctx.fail(f"run_cmd(dry_run={dry_run}, target_config_dir_or_file='{target_config_dir_or_file}') failed: {type(ex).__name__} {ex.args}")
        return 1

