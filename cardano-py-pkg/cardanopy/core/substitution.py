from pathlib import Path
from .cardanopy_config import CardanoPyConfig
import json
import os


class Substitution(object):

    @staticmethod
    def generate(dry_run: bool, target_config_dir: Path, config: CardanoPyConfig, subs: tuple = tuple()):
        for dir_name, subdirList, fileList in os.walk(target_config_dir):
            dir_path = Path(dir_name)
            for file_name in fileList:
                file_path = dir_path.joinpath(file_name)
                if ".template" in file_name:
                    output_config_file = dir_path.joinpath(file_name.replace(".template", ""))
                    if dry_run:
                        print(f"generate config '{output_config_file}' from '{file_path}'")
                    else:
                        try:
                            with open(file_path, "r") as file:
                                config_data_str = file.read()
                        except Exception as ex:
                            raise ValueError(
                                f"Failed to load template. '{file_path}'. {type(ex).__name__} {ex.args}")

                        try:
                            config_data_resolved_str = config.substitute(config_data_str, subs)
                        except Exception as ex:
                            raise ValueError(
                                f"Failed to substitute template. '{file_path}'. {type(ex).__name__} {ex.args}")

                        try:
                            with open(output_config_file, "w") as file:
                                config_local = json.loads(config_data_resolved_str)
                                print(json.dumps(config_local, indent=4), file=file)
                        except Exception as ex:
                            raise ValueError(
                                f"Failed to save generated config. '{output_config_file}'. {type(ex).__name__} {ex.args}")

                        print(f"generated config '{output_config_file}'")
