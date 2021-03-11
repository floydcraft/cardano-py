import click
import subprocess
from pathlib import Path
from .cardanopy_config import CardanoPyConfig
import json
import os
import shutil


@click.command()
@click.option('-r', '--dry-run', 'dry_run', is_flag=True, help="print the mutable commands")
@click.argument('target_config_dir', type=str)
@click.pass_context
def run(ctx, dry_run, target_config_dir):
    """Run command"""

    if dry_run:
        print("#### DRY RUN - no mutable changes will be made. ####")

    cardanopy_config = CardanoPyConfig()
    try:
        cardanopy_config.load(target_config_dir)
    except ValueError as e:
        ctx.fail(e.args)
        return 1

    if not generate(dry_run, target_config_dir, cardanopy_config):
        ctx.fail(f"Failed to generate '{target_config_dir}'")
        return 1

    cardano_node_cmd = ["cardano-node",
                        "run",
                        "--config", cardanopy_config.config,
                        "--topology", cardanopy_config.topologyPath,
                        "--database-path", cardanopy_config.databasePath,
                        "--host-addr", cardanopy_config.hostAddr,
                        "--port", f"{cardanopy_config.port}",
                        "--socket-path", cardanopy_config.socketPath]
    if dry_run:
        print(" ".join(cardano_node_cmd))
    else:
        try:
            subprocess.run(cardano_node_cmd, cwd=target_config_dir)
        except Exception as ex:
            ctx.fail(f"Unknown exception: {ex} {type(ex).__name__} {ex.args}")
            return 1


def generate(dry_run: bool, target_config_dir: Path, config: CardanoPyConfig):
    if dry_run:
        print(f"generate 'topology.json' file config.topologyPath to `{config.topologyPath}'")
    else:
        with open(target_config_dir.joinpath(config.topologyPath), "w") as file:
            print(json.dumps(config.topology, sort_keys=True, indent=4), file=file)

        for dir_name, subdirList, fileList in os.walk(target_config_dir):
            dir_path = Path(dir_name)
            for file_name in fileList:
                file_path = dir_path.joinpath(file_name)
                if ".template" in file_name:
                    try:
                        output_template_yaml = dir_path.joinpath(file_name.replace(".template", ""))
                        if dry_run:
                            print(f"copy file from '{file_path}' to '{output_template_yaml}'")
                        else:
                            shutil.copyfile(file_path, output_template_yaml)
                    except Exception as ex:
                        print(f"Unknown exception: {ex} {type(ex).__name__} {ex.args}")
                        return False

    return True
