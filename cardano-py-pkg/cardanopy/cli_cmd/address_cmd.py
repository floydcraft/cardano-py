import click
import subprocess
import os


@click.group("address")
@click.pass_context
def address_cmd(ctx):
    """Payment address commands"""


@address_cmd.command("key-gen")
@click.option('--normal-key', 'key_type', flag_value='normal-key', default=True, help='Use a normal Shelley-era key (default).')
@click.option('--extended-key', 'key_type', flag_value='extended-key', help='Use an extended ed25519 Shelley-era key.')
@click.option('--byron-key', 'key_type', flag_value='byron-key', help='Use a Byron-era key.')
@click.option('--verification-key-file', 'verification_key_file', required=True, type=str, help='Output filepath of the verification key.')
@click.option('--signing-key-file', 'signing_key_file', required=True, type=str, help='Output filepath of the signing key.')
@click.pass_context
def key_gen_cmd(ctx, key_type, verification_key_file, signing_key_file):
    """Create an address key pair."""

    try:
        subprocess.run(["cardano-cli",
                        "address",
                        "key-gen",
                        f"--{key_type}",
                        "--verification-key-file", verification_key_file,
                        "--signing-key-file", signing_key_file
                        ])
    except Exception as ex:
        ctx.fail(f"cli:address_cmd:key_gen_cmd(key_type={key_type}, "
                 f"verification_key_file={verification_key_file}, "
                 f"signing_key_file='{signing_key_file}') failed: {type(ex).__name__} {ex.args}")
        return 1


@address_cmd.command("build")
@click.pass_context
@click.option('--payment-verification-key-file', 'payment_verification_key_file', required=True, type=str, help='Output filepath of the verification key.')
@click.option('--stake-verification-key-file', 'stake_verification_key_file', required=True, type=str, help='Output filepath of the signing key.')
@click.option('--out-file', 'out_file', type=str, help='Optional output file. Default is to write to stdout')
@click.pass_context
def build_cmd(ctx, payment_verification_key_file, stake_verification_key_file, out_file):
    """Create an address key pair."""

    try:
        cardano_network = os.getenv('CARDANO_NETWORK')
        if cardano_network == "mainnet":
            cardano_network_params = ['--mainnet']
        elif cardano_network == "testnet":
            cardano_network_params = ['--testnet-magic', '1097911063']
        else:
            ctx.fail("missing or invalid param: mainnet or testnet")
            return

        subprocess.run(["cardano-cli",
                        "address",
                        "build",
                        "--payment-verification-key-file", payment_verification_key_file,
                        "--stake-verification-key-file", stake_verification_key_file]
                        + ([] if out_file is None else ['--out-file', out_file])
                        + cardano_network_params)
    except Exception as ex:
        ctx.fail(f"cli:address_cmd:build_cmd(payment_verification_key_file={payment_verification_key_file}, "
                 f"stake_verification_key_file={stake_verification_key_file}, "
                 f"out_file='{out_file}') failed: {type(ex).__name__} {ex.args}")
        return 1
