#!/bin/bash
set -e
set -u
set -o pipefail

rm -rf dist build
python3 setup.py sdist
twine check dist/*
twine upload dist/* --skip-existing