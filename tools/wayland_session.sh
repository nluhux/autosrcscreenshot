#!/bin/sh

set -e
set -u

POS=$(dirname $(realpath $0))
export FILENAME=$1

# 这里的hikari必须魔改过，拥有 HIKARI_PID 环境变量
export PATH=$POS/bin:$PATH

hikari -a $POS/open_terminal.sh
