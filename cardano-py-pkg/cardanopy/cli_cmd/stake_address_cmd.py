import click
import subprocess


@click.group("stake-address")
@click.pass_context
def stake_address_cmd(ctx):
    """Stake address commands"""


@stake_address_cmd.command("key-gen")
@click.option('--verification-key-file', 'verification_key_file', required=True, type=str, help='Output filepath of the verification key.')
@click.option('--signing-key-file', 'signing_key_file', required=True, type=str, help='Output filepath of the signing key.')
@click.pass_context
def key_gen_cmd(ctx, verification_key_file, signing_key_file):
    """Create a stake address key pair"""

    try:
        subprocess.run(["cardano-cli",
                        "stake-address",
                        "key-gen",
                        "--verification-key-file", verification_key_file,
                        "--signing-key-file", signing_key_file
                        ])
    except Exception as ex:
        ctx.fail(f"cli:stake_address_cmd:key_gen_cmd(verification_key_file={verification_key_file}, "
                 f"signing_key_file={signing_key_file}) failed: {type(ex).__name__} {ex.args}")
        return 1
