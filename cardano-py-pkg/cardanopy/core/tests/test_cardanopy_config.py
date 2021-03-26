import unittest
from core.cardanopy_config import CardanoPyConfig
from core.cardanopy_common import CardanoPyCommon
from pathlib import Path
import tempfile
import shutil
import os
import yaml
import json
import jsonschema


class TestCardanoPyConfig(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        os.chdir(self.test_dir)
        # print(f"test_dir='{self.test_dir}'")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_basic_config_validation(self):
        config_file = Path(__file__).parent.joinpath("../../data/templates").absolute() / "testnet/basic/cardanopy.yaml"
        with open(config_file, "r") as file:
            config = yaml.full_load(file.read())

        api_version = config["apiVersion"]

        schema_file = Path(__file__).parent.joinpath("../../data/schemas").absolute() / f"{api_version}.json"
        with open(schema_file, "r") as file:
            schema = json.loads(file.read())

        jsonschema.validate(instance=config, schema=schema)

    def test_basic_config(self):
        file = Path(__file__).parent.joinpath("../../data/templates").absolute() / "testnet/basic/cardanopy.yaml"
        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(file)

        self.assertEqual(cardanopy_config.apiVersion, "cardanopy.node.config.v1")
        self.assertEqual(cardanopy_config.network, "testnet")
        self.assertEqual(cardanopy_config.configPath, "/home/ada/app/config.json")
        self.assertEqual(cardanopy_config.topologyPath, "/home/ada/app/topology.json")
        self.assertEqual(cardanopy_config.databasePath, "/home/ada/app/db")
        self.assertEqual(cardanopy_config.socketPath, "/home/ada/app/node.socket")
        self.assertEqual(cardanopy_config.hostAddr, "0.0.0.0")
        self.assertEqual(cardanopy_config.port, 3001)
        self.assertEqual(cardanopy_config.docker.name, "basic")
        self.assertEqual(cardanopy_config.docker.image, f"floydcraft/cardano-py-slim:{CardanoPyCommon.get_version()}")
        self.assertEqual(cardanopy_config.docker.rootVolume, "/home/ada/app")
        self.assertEqual(cardanopy_config.docker.mount, True)
        self.assertEqual(cardanopy_config.k8s.namespace, "cardano-testnet")

        file_save = self.test_dir / file.name
        cardanopy_config.save(file_save)

        cardanopy_config_v2 = CardanoPyConfig()
        cardanopy_config_v2.load(file_save)

        self.assertEqual(cardanopy_config_v2.apiVersion, cardanopy_config.apiVersion)
        self.assertEqual(cardanopy_config_v2.network, cardanopy_config.network)
        self.assertEqual(cardanopy_config_v2.configPath, cardanopy_config.configPath)
        self.assertEqual(cardanopy_config_v2.topologyPath, cardanopy_config.topologyPath)
        self.assertEqual(cardanopy_config_v2.databasePath, cardanopy_config.databasePath)
        self.assertEqual(cardanopy_config_v2.socketPath, cardanopy_config.socketPath)
        self.assertEqual(cardanopy_config_v2.hostAddr, cardanopy_config.hostAddr)
        self.assertEqual(cardanopy_config_v2.port, cardanopy_config.port)
        self.assertEqual(cardanopy_config_v2.docker.name, cardanopy_config.docker.name)
        self.assertEqual(cardanopy_config_v2.docker.image, cardanopy_config.docker.image)
        self.assertEqual(cardanopy_config_v2.docker.rootVolume, cardanopy_config.docker.rootVolume)
        self.assertEqual(cardanopy_config_v2.docker.mount, cardanopy_config.docker.mount)
        self.assertEqual(cardanopy_config_v2.k8s.namespace, cardanopy_config.k8s.namespace)

    def test_basic_config_subs(self):
        dir_path = Path(__file__).parent.joinpath("../../data/templates").absolute()
        for file in dir_path.glob("*/*.yaml"):
            cardanopy_config = CardanoPyConfig()
            cardanopy_config.load(file)

            self.assertEqual(cardanopy_config.apiVersion, "cardanopy.node.config.v1")
            self.assertIsInstance(cardanopy_config.network, str)
            self.assertEqual(cardanopy_config.configPath, "/home/ada/app/config.json")
            self.assertEqual(cardanopy_config.topologyPath, "/home/ada/app/topology.json")
            self.assertEqual(cardanopy_config.databasePath, "/home/ada/app/db")
            self.assertEqual(cardanopy_config.socketPath, "/home/ada/app/node.socket")
            self.assertEqual(cardanopy_config.hostAddr, "0.0.0.0")
            self.assertEqual(cardanopy_config.port, 3001)
            # self.assertEqual(cardanopy_config.shelleyKesKey, "/home/ada/app/bp/kes.skey")
            # self.assertEqual(cardanopy_config.shelleyVrfKey, "/home/ada/app/bp/vrf.skey")
            # self.assertEqual(cardanopy_config.shelleyOperationalCertificate, "/home/ada/app/bp/node.cert")
            self.assertIsInstance(cardanopy_config.docker.name, str)
            self.assertEqual(cardanopy_config.docker.image, f"floydcraft/cardano-py-slim:{CardanoPyCommon.get_version()}")
            self.assertEqual(cardanopy_config.docker.rootVolume, "/home/ada/app")
            self.assertEqual(cardanopy_config.docker.mount, True)
            self.assertIsInstance(cardanopy_config.k8s.namespace, str)
