import os
from pathlib import Path
from ..core.cardanopy_error import CardanoPyError


class CardanoNode(object):

    @staticmethod
    def validate_environment():
        cardano_node_socket_path = os.getenv('CARDANO_NODE_SOCKET_PATH')
        if not cardano_node_socket_path:
            raise CardanoPyError(f"Invalid CARDANO_NODE_SOCKET_PATH. Undefined.", 1)

        cardano_node_socket_path = Path(cardano_node_socket_path)
        if not cardano_node_socket_path.exists():
            raise CardanoPyError(f"Invalid CARDANO_NODE_SOCKET_PATH. '{cardano_node_socket_path}' does not exist.", 1)

        CardanoNode.get_network()

    @staticmethod
    def get_network():
        cardano_network = os.getenv('CARDANO_NETWORK')
        if not cardano_network:
            raise CardanoPyError(f"Invalid CARDANO_NETWORK. Undefined.", 1)

        return cardano_network