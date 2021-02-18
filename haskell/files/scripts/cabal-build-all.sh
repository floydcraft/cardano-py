#!/bin/bash
set -e
set -u
set -o pipefail

# executes cabal build all
# parses executables created from compiler output and copies it to ~./cabal/bin folder.

echo "Running cabal update to ensure you're on latest dependencies.."
cabal update 2>&1 | tee /tmp/cabal-build.log
echo "Building.."
cabal build all 2>&1 | tee /tmp/build.log

grep "^Linking" /tmp/build.log | grep -Ev 'test|golden|demo' | while read -r line ; do
    act_bin_path=$(echo "$line" | awk '{print $2}')
    act_bin=$(echo "$act_bin_path" | awk -F "/" '{print $NF}')
    echo "Copying $act_bin to $HOME/.cabal/bin/"
    cp -f "$act_bin_path" "$HOME/.cabal/bin/"
done
