#!/bin/bash
# ---
# environment:
#   - SSH_AGENT_PID
#   - SSH_AUTH_SOCK
# ---
set -eu

. venv/bin/activate

rm -rf dist
vg watch-templates build
cp -r images dist/
tailwindcss -i ./styles.css -o ./dist/styles.css --minify

ghp-import dist --branch=main --cname=3inc.mayortech.co.uk

git checkout main
git push origin main
git checkout develop
