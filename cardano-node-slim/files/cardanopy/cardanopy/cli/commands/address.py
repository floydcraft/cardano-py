import click
import subprocess

@click.group()
@click.pass_context
def address(ctx):
    """Payment address commands"""

@address.command("key-gen")
@click.option('--normal-key', 'key_type', flag_value='normal-key', default=True, help='Use a normal Shelley-era key (default).')
@click.option('--extended-key', 'key_type', flag_value='extended-key', help='Use an extended ed25519 Shelley-era key.')
@click.option('--byron-key', 'key_type', flag_value='byron-key', help='Use a Byron-era key.')
@click.option('--verification-key-file', 'verification_key_file', required=True, type=str, help='Output filepath of the verification key.')
@click.option('--signing-key-file', 'signing_key_file', required=True, type=str, help='Output filepath of the signing key.')
def key_gen(key_type, verification_key_file, signing_key_file):
    """Create an address key pair."""
    subprocess.run(["cardano-cli",
                    "address",
                    "key-gen",
                    f"--{key_type}",
                    "--verification-key-file", verification_key_file,
                    "--signing-key-file", signing_key_file
                    ])