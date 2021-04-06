from ..core.cli_base import CliBase


class CardanoCli(object):

    @staticmethod
    def execute(cmd: list, dry_run: bool = False, include_network: bool = False, include_era: bool = False):
        CardanoCli.validate_environment()

        if include_network:
            cmd = cmd + CardanoCli.get_network_cli_args()

        if include_era:
            cmd = cmd + CardanoCli.get_era_cli_args()

        return CliBase.execute(cmd=cmd, dry_run=dry_run)

    @staticmethod
    def get_network_cli_args():
        # TODO:bfloyd change to use yaml config instead?
        # TODO:bfloyd allow for custom testnet magic?
        return ["--mainnet"] if CardanoCli.get_network() == "mainnet" else ["--testnet-magic", "1097911063"]

    @staticmethod
    def get_era_cli_args():
        # TODO:bfloyd implement
        return []




