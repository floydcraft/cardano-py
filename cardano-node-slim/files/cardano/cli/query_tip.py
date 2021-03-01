import click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
def query_tip():
    """Query tip."""
    print("Query TIP!")