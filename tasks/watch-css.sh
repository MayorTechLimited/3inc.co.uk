#!/bin/bash
set -eu

tailwindcss -i "./${1:-styles}.css" -o "./dist/${1:-styles}.css" --watch
