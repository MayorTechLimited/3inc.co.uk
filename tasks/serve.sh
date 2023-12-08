#!/bin/bash
set -eu

. venv/bin/activate
cd dist
python -m http.server 8002
