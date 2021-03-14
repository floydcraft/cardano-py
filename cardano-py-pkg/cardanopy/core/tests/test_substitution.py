import unittest
from click.testing import CliRunner
from ...create_cmd import create_cmd
from core.substitution import Substitution
from core.cardanopy_config import CardanoPyConfig
from pathlib import Path
import tempfile
import shutil
import os


class TestSubstitution(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        os.chdir(self.test_dir)
        # print(f"test_dir='{self.test_dir}'")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_substitution(self):
        app_dir = self.test_dir.joinpath('test-app')

        runner = CliRunner()
        create_result = runner.invoke(create_cmd, ['--template',
                                                    'basic',
                                                    '--network',
                                                    'testnet',
                                                    str(app_dir)])
        assert create_result.exit_code == 0

        target_config_dir = CardanoPyConfig.try_get_valid_config_dir(app_dir)
        target_config_file = CardanoPyConfig.try_get_valid_config_file(app_dir)

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(target_config_file, ("_NAME=test_app", "_TAG=test_tag"))

        Substitution.generate(False, target_config_dir, cardanopy_config)
