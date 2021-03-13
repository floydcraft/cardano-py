import unittest
from click.testing import CliRunner
from ...create import create
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
        create_result = runner.invoke(create, ['--template',
                                                    'basic',
                                                    '--network',
                                                    'testnet',
                                                    str(app_dir)])
        assert create_result.exit_code == 0

        cardanopy_config = CardanoPyConfig()
        cardanopy_config.load(app_dir)

        Substitution.generate(False, app_dir, cardanopy_config)