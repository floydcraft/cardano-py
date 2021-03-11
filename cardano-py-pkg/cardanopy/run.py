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

    if not generate(dry_run, target_config_dir, config):
        ctx.fail(f"Failed to generate '{target_config_dir}'")
        return 1

    cardano_node_cmd = ["cardano-node",
                        "run",
                        "--config", config.config,
                        "--topology", config.topologyPath,
                        "--database-path", config.databasePath,
                        "--host-addr", config.hostAddr,
                        "--port", f"{config.port}",
                        "--socket-path", config.socketPath]
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
