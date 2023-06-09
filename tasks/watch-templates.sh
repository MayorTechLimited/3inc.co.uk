#!/bin/bash
set -eu

. venv/bin/activate
staticjinja watch --outpath dist
