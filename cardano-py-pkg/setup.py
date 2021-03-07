#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='cardanopy',
      version='0.1.3',
      description='Cardano CLI tools for python3',
      author='Bourke Floyd',
      author_email='chbfiv@floydcraft.com',
      url='https://github.com/floydcraft/cardano-py',
      packages=find_packages(),
      keywords='cardano,ada,cli',
      python_requires='>=3.5.3,<4',
      install_requires=[
        'click==7.0'
      ],
      entry_points={
          'console_scripts': [
              'cardanopy=cardanopy:main',
          ],
      },
      project_urls={
          'Bug Reports': 'https://github.com/floydcraft/cardano-py/issues',
          'Chat': 'https://discord.gg/FyDz4Xrt4x',
          'Source': 'https://github.com/floydcraft/cardano-py',
      }
)