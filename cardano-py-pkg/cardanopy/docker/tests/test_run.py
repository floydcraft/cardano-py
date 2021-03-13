import unittest
from click.testing import CliRunner
from ...create import create
from ..run import run
from pathlib import Path
import tempfile
import shutil
import os


class TestDockerRun(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        os.chdir(self.test_dir)
        # print(f"test_dir='{self.test_dir}'")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_basic_cmd(self):
        app_dir = str(self.test_dir.joinpath('test-app'))
        runner = CliRunner()
        create_result = runner.invoke(create, ['--template',
                                                    'basic',
                                                    '--network',
                                                    'testnet',
                                                    app_dir])
        assert create_result.exit_code == 0
        run_result = runner.invoke(run, ['--dry-run', app_dir])
        assert run_result.exit_code == 0
        assert "DRY RUN - no mutable changes will be made." in run_result.output
        assert "docker run --name basic -d --env CARDANO_NODE_SOCKET_PATH=/app/node.socket --env CARDANO_NETWORK=testnet -p 3001:3001" in run_result.output
        #  -v /private/var/folders/dj/qy6c5r217zxf4xf2rspds_km0000gn/T/tmpf9759ir0/test-app:/app
        assert "floydcraft/cardano-py-slim:latest run /app" in run_result.output
        assert "docker exec -it basic bin/bash" in run_result.output