#!/bin/sh
# ---
# help-text: Bootstrap this project
# ---
set -eu

python3.10 -m venv venv
. ./venv/bin/activate
pip install -U pip
pip install -r requirements.txt
