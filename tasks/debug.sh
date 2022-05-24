#!/bin/sh
# ---
# help-text: Run a local debug server
# image:
#   tag: python:3.10
#   publish:
#     - 8000:8000
#   volume:
#     - $VG_APP_DIR/public:/public
# ---
python -m http.server --bind 0.0.0.0 --directory /public
