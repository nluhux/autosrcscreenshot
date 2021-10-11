#!/bin/sh

set -e
set -u

POS=$(dirname $(realpath $0))

$POS/view_archive.py $FILENAME
echo 压缩文件: $FILENAME
$POS/make_screenshot.sh $FILENAME
