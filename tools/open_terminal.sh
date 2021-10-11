#!/bin/sh

set -e
set -u

POS=$(dirname $(realpath $0))

cleanup() {
    sleep 1
    kill -9 $HIKARI_PID
    exit 1
}

trap cleanup EXIT


foot -f Unifont-16 -w 1280x720 -- $POS/view_and_screenshot.sh

