import subprocess
from typing import NamedTuple


class BaseCliError(Exception):
    message: None
    return_code: 0

    def __init__(self, message: str, return_code: int = 0):
        self.message = message
        self.return_code = return_code


class BaseCliResponse(NamedTuple):
    stdout: bytes
    stderr: bytes


class BaseCli(NamedTuple):

    @staticmethod
    def run(dry_run: bool, cmd: list):
        try:
            if dry_run:
                print(" ".join(cmd))
            else:
                subprocess.run(cmd)
        except subprocess.CalledProcessError as cpe:
            raise BaseCliError(f"{' '.join(cmd)} failed: {cpe.returncode} {cpe.output}", cpe.returncode)
        except Exception as ex:
            raise BaseCliError(f"{' '.join(cmd)} failed: {type(ex).__name__} {ex.args}", 1)

