#!/bin/bash
set -e
set -u
set -o pipefail

pg_ctlcluster 13 main start
postgres createuser --createdb --superuser runner