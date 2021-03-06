#!/bin/bash
set -e
set -u
set -o pipefail

rm -rf dist build
python setup.py bdist
twine check dist/*
twine upload dist/* --skip-existing