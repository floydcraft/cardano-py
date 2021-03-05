#!/bin/bash
set -e
set -u
set -o pipefail

rm -rf dist
python setup.py bdist_wheel --universal
twine check dist/*
twine upload dist/* --skip-existing