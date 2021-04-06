import subprocess
from typing import NamedTuple
from .cardanopy_error import CardanoPyError


class CliResult(NamedTuple):
    stdout: bytes
    stderr: bytes


class CliBase(NamedTuple):

    @staticmethod
    def execute(cmd: list, dry_run: bool = False):
        try:
            if dry_run:
                print(" ".join(cmd))
            else:
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()

                if p.returncode != 0:
                    raise CardanoPyError(f" {stderr.decode()}", p.returncode)

        except subprocess.CalledProcessError as cpe:
            raise CardanoPyError(f"{' '.join(cmd)} failed: {cpe.returncode} {cpe.output}", cpe.returncode)
        except Exception as ex:
            raise CardanoPyError(f"{' '.join(cmd)} failed: {type(ex).__name__} {ex.args}", 1)

        return CliResult(stdout or b"", stderr or b"")

