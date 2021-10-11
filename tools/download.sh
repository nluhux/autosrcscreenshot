#!/bin/sh

while read line
do
    filename=`echo $line | sed -e 's/^http:\/\///'` || exit 1 # 删除 #http
    filedir=`dirname $filename` || exit 1
    mkdir -pv ./$filedir || exit 1
    axel --output=$filename $line &
done
