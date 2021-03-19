from pathlib import Path
from .cardanopy_config import CardanoPyConfig
import json
import os


class CardanoNodeHelpers(object):

    @staticmethod
    def validate_environment():
        cardano_node_socket_path = os.getenv('CARDANO_NODE_SOCKET_PATH')
        if not cardano_node_socket_path:
            raise ValueError(f"Invalid CARDANO_NODE_SOCKET_PATH. Undefined.")

        cardano_node_socket_path = Path(cardano_node_socket_path)
        if not cardano_node_socket_path.exists():
            raise ValueError(f"Invalid CARDANO_NODE_SOCKET_PATH. '{cardano_node_socket_path}' does not exist.")

        cardano_network = os.getenv('CARDANO_NETWORK')
        if not cardano_network:
            raise ValueError(f"Invalid CARDANO_NETWORK. Undefined.")

    @staticmethod
    def get_cli_network_args():
        return ["--mainnet"] if CardanoNodeHelpers.get_cli_network() == "mainnet" else ["--testnet-magic", "1097911063"]

    @staticmethod
    def get_cli_network():
        cardano_network = os.getenv('CARDANO_NETWORK')
        if not cardano_network:
            cardano_network = "testnet"
        return cardano_network
