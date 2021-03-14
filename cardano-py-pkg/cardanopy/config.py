# import click
# from .core.cardanopy_config import CardanoPyConfig
#
#
# @click.command()
# @click.argument('property_name', type=str, required=True)
# @click.argument('property_value', type=str)
# @click.argument('target_config_dir', type=str)
# @click.pass_context
# def config(ctx, property_name, property_value, target_config_dir):
#     """Config command"""
#
#     cardanopy_config = CardanoPyConfig()
#     try:
#         cardanopy_config.load(target_config_dir)
#     except ValueError as e:
#         ctx.fail(e.args)
#         return 1
#
#     if not property_value:
#         print(cardanopy_config.get(property_name))
#     else:
#         cardanopy_config.set(property_name, property_value)
#
#         try:
#             cardanopy_config.save(target_config_dir)
#         except ValueError as e:
#             ctx.fail(e.args)
#             return 1
