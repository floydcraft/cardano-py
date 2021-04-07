from ..core.cli_base import CliBase
from .cardano_node import CardanoNode


class CardanoCli(object):

    @staticmethod
    def execute(cmd: list, dry_run: bool = False,
                include_network: bool = False, include_era: bool = False, encoding: str = "utf-8"):
        if not dry_run:
            CardanoNode.validate_environment()

        if include_network:
            cmd = cmd + CardanoCli.get_network_cli_args()

        if include_era:
            cmd = cmd + CardanoCli.get_era_cli_args()

        return CliBase.execute(cmd=cmd, dry_run=dry_run, encoding=encoding)

    @staticmethod
    def get_network_cli_args():
        # TODO:bfloyd change to use yaml config instead?
        # TODO:bfloyd allow for custom testnet magic?
        return ["--mainnet"] if CardanoNode.get_network() == "mainnet" else ["--testnet-magic", "1097911063"]

    @staticmethod
    def get_era_cli_args():
        # TODO:bfloyd implement
        return []




