#!/usr/bin/env python3

import os
import sys

def dec_file_type(filename):
    suffix = filename.split('.')[-1]
    if suffix == 'rar' or suffix == 'RAR' or\
       suffix == 'Rar' or suffix == 'RAr' or\
       suffix == 'rAr' or suffix == 'rAR':
        return 'rar'
    if suffix == 'zip' or suffix == 'ZIP' or\
       suffix == 'Zip' or suffix == 'ZIp' or\
       suffix == 'zIp' or suffix == 'zIP':
        return 'zip'
    if  suffix == 'gz' or suffix == 'tgz':
        return 'tar'

    
    return None

def view_archive(filename,filetype):
    if filetype == None:
        return 1
    
    if filetype == 'rar':
        cmd = "unrar v " + filename
        ret_val = os.system(cmd)

    if filetype == 'zip':
        cmd = "unzip -l " + filename
        ret_val = os.system(cmd)

    if filetype == 'tar':
        cmd = "tar -tvf " + filename
        ret_val = os.system(cmd)

    if ret_val == 0:
        return 0
    else:
        return 1

def main():
    filename = sys.argv[1]
    filetype = dec_file_type(filename)
    exit(view_archive(filename,filetype))
    
main()
