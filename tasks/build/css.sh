#!/bin/bash
set -eu

tailwindcss -i ./styles.css -o ./public/styles.css --minify
