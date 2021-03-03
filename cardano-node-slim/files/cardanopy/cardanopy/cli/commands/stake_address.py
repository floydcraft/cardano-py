import click
import subprocess

@click.group("stake-address")
@click.pass_context
def stake_address(ctx):
    """Stake address commands"""

@stake_address.command("key-gen")
@click.option('--verification-key-file', 'verification_key_file', required=True, type=str, help='Output filepath of the verification key.')
@click.option('--signing-key-file', 'signing_key_file', required=True, type=str, help='Output filepath of the signing key.')
def key_gen(verification_key_file, signing_key_file):
    """Create a stake address key pair"""
    subprocess.run(["cardano-cli",
                    "stake-address",
                    "key-gen",
                    "--verification-key-file", verification_key_file,
                    "--signing-key-file", signing_key_file
                    ])