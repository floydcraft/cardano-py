import unittest
from click.testing import CliRunner
from ..cardanopy_config import CardanoPyConfig
from pathlib import Path
import tempfile
import shutil
import os


class TestCreate(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        os.chdir(self.test_dir)
        # print(f"test_dir='{self.test_dir}'")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_basic_config(self):
        file = Path(__file__).parent.joinpath("../data/templates").absolute() / "testnet/basic.yaml"
        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(file)

        self.assertEqual(cardanopy_config.apiVersion, "cardanopy.node.config/v1")
        self.assertEqual(cardanopy_config.name, "basic")
        self.assertEqual(cardanopy_config.network, "testnet")
        self.assertEqual(cardanopy_config.root, "/app")
        self.assertEqual(cardanopy_config.config, "/app/config/config.json")
        self.assertEqual(cardanopy_config.topologyPath, "/app/config/topology.json")
        self.assertEqual(cardanopy_config.databasePath, "/app/db")
        self.assertEqual(cardanopy_config.socketPath, "/app/node.socket")
        self.assertEqual(cardanopy_config.hostAddr, "0.0.0.0")
        self.assertEqual(cardanopy_config.port, 3001)
        self.assertEqual(cardanopy_config.docker.image, "floydcraft/cardano-py-slim:latest")
        self.assertEqual(cardanopy_config.kubernetes.namespace, "cardano-testnet")

        file_save = self.test_dir / (file.name)
        cardanopy_config.save(file_save)

        cardanopy_config_v2 = CardanoPyConfig()
        cardanopy_config_v2.load(file_save)

        self.assertEqual(cardanopy_config_v2.apiVersion, cardanopy_config.apiVersion)
        self.assertEqual(cardanopy_config_v2.name, cardanopy_config.name)
        self.assertEqual(cardanopy_config_v2.network, cardanopy_config.network)
        self.assertEqual(cardanopy_config_v2.root, cardanopy_config.root)
        self.assertEqual(cardanopy_config_v2.config, cardanopy_config.config)
        self.assertEqual(cardanopy_config_v2.topologyPath, cardanopy_config.topologyPath)
        self.assertEqual(cardanopy_config_v2.databasePath, cardanopy_config.databasePath)
        self.assertEqual(cardanopy_config_v2.socketPath, cardanopy_config.socketPath)
        self.assertEqual(cardanopy_config_v2.hostAddr, cardanopy_config.hostAddr)
        self.assertEqual(cardanopy_config_v2.port, cardanopy_config.port)
        self.assertEqual(cardanopy_config_v2.docker.image, cardanopy_config.docker.image)
        self.assertEqual(cardanopy_config_v2.kubernetes.namespace, cardanopy_config.kubernetes.namespace)

    def test_basic_config_subs(self):
        file = Path(__file__).parent.joinpath("../data/templates").absolute() / "testnet/basic.yaml"
        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(file)

        self.assertEqual(cardanopy_config.name, "basic")