from typing import NamedTuple
from ..core.cardano_node_helpers import CardanoNodeHelpers
from ..core.base_cli import BaseCli, BaseCliError


class CardanoCliError(Exception):
    message: None
    return_code: 0

    def __init__(self, message: str, return_code: int = 0):
        self.message = message
        self.return_code = return_code


class CardanoCliResponse(NamedTuple):
    stdout: bytes
    stderr: bytes


class CardanoCli(NamedTuple):

    @staticmethod
    def run(cmd: list, dry_run: bool = False, include_network: bool = False, include_era: bool = False):
        try:
            CardanoNodeHelpers.validate_environment()

            if include_network:
                cmd = cmd + CardanoNodeHelpers.get_cli_network_args()

            BaseCli.run(cmd=cmd, dry_run=dry_run)
        except BaseCliError as bce:
            raise CardanoCliError(bce.message, bce.return_code)
        except ValueError as ve:
            raise CardanoCliError(ve, 1)


