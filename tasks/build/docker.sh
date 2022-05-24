#!/bin/bash
set -eu

docker build --tag 3inc "$VG_APP_DIR"
