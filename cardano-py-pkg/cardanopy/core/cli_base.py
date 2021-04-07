import subprocess
from typing import NamedTuple
from .cardanopy_error import CardanoPyError


class CliResult(NamedTuple):
    stdout: bytes
    stderr: bytes
    encoding: str = "utf-8"

    def get_stdout_str(self):
        return self.stdout.decode(self.encoding) if self.stdout else None

    stdout_str = property(get_stdout_str)

    def get_stderr_str(self):
        return self.stderr.decode(self.encoding) if self.stdout else None

    stderr_str = property(get_stderr_str)


class CliBase(NamedTuple):

    @staticmethod
    def execute(cmd: list, dry_run: bool = False, encoding: str = "utf-8"):
        try:
            if dry_run:
                print(" ".join(cmd))
                stdout, stderr = b""
            else:
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = p.communicate()

                if p.returncode != 0:
                    raise CardanoPyError(f" {stderr.decode(encoding)}", p.returncode)

        except subprocess.CalledProcessError as cpe:
            raise CardanoPyError(f"{' '.join(cmd)} failed: {cpe.returncode} {cpe.output}", cpe.returncode)
        except Exception as ex:
            raise CardanoPyError(f"{' '.join(cmd)} failed: {type(ex).__name__} {ex.args}", 1)

        return CliResult(stdout=stdout, stderr=stderr, encoding=encoding)

