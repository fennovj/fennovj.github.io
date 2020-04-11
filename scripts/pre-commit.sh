#!/bin/sh

# Run this command in the root of the repo to install the hook:
# ln -s -f ../../scripts/pre-commit.sh .git/hooks/pre-commit
# This is my first pre-commit so not sure if I did everything correct.

# Run the python script that generates all the html
# Potentially rename this to 'python' based on environment?
python3 scripts/pre-commit.py

# Add the html directory (this directory should pretty much never be edited by hand)
git add html
