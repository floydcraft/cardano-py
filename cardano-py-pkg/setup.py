#!/usr/bin/env python

from setuptools import setup, find_packages
from pathlib import Path

datadir = Path(__file__).parent / 'cardanopy' / 'data'
files = ['data/' + str(p.relative_to(datadir)) for p in datadir.rglob('*')]

setup(name='cardanopy',
      version='0.1.9-dev3',
      description='Cardano CLI tools for python3',
      author='Bourke Floyd',
      author_email='chbfiv@floydcraft.com',
      url='https://github.com/floydcraft/cardano-py',
      # package_dir={'cardanopy': '.'},
      package_data={'cardanopy': files},
      packages=find_packages(exclude=['tests']),
      keywords='cardano,ada,cli',
      python_requires='>=3.5.3,<4',
      install_requires=[
        'click~=7.1.2',
        'pyyaml~=5.4.1',
        'jsonschema~=3.2.0'
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
