#!/bin/sh

set -e -u

output_filename="$1.png"
export GRIM_DEFAULT_DIR="$(pwd)"
sleep 1
grim -t png $output_filename
