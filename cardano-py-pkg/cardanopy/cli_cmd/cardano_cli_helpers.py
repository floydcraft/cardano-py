from pathlib import Path
import json
import os
import subprocess
from ..core.cardano_node_helpers import CardanoNodeHelpers


class CardanoCliHelpers(object):

    @staticmethod
    def query_tip(dry_run):
        CardanoNodeHelpers.validate_environment()

        query_tip_cmd = ["cardano-cli", "query", "tip"] + CardanoNodeHelpers.get_cli_network_args()
        if dry_run:
            print(" ".join(query_tip_cmd))
        else:
            subprocess.run(query_tip_cmd)

    @staticmethod
    def get_cli_network_args():
        return ["--mainnet"] if CardanoNodeHelpers.get_cli_network() == "mainnet" else ["--testnet-magic", "1097911063"]

    @staticmethod
    def get_cli_network():
        cardano_network = os.getenv('CARDANO_NETWORK')
        if not cardano_network:
            cardano_network = "testnet"
        return cardano_network
