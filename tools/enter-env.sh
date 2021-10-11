#!/bin/sh

POS=$(dirname $(realpath $0))

guix environment \
     --ad-hoc busybox \
     --ad-hoc python python-requests \
     --ad-hoc grim foot \
     --ad-hoc vim \
     --ad-hoc wget curl axel \
     $@
