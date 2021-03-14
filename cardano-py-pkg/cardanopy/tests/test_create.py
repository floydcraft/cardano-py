import unittest
from click.testing import CliRunner
from ..create_cmd import create_cmd
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

    def test_basic_cmd(self):
        runner = CliRunner()
        result = runner.invoke(create_cmd, ['--template',
                                                    'basic',
                                                    '--network',
                                                    'testnet',
                                                    'test-app'])
        assert result.exit_code == 0
        # assert result.output == "Created cardano defaults from 'basic' template for network 'testnet': 'test-app'\n"

        # # Create a file in the temporary directory
        # f = open(path.join(self.test_dir, 'test.txt'), 'w')
        # # Write something to it
        # f.write('The owls are not what they seem')
        # # Reopen the file and check if what we read back is the same
        # f = open(path.join(self.test_dir, 'test.txt'))
        # self.assertEqual(f.read(), 'The owls are not what they seem')