#!/usr/bin/env python3

import os
import sys
import os.path
import requests
import urllib
import json
from time import sleep

# 脚本存放位置
POS=os.path.dirname(os.path.realpath(sys.argv[0]))

def get_domain_by_urllib(u):
    return urllib.parse.urlparse(u).netloc

def get_url_data(url):
    data = requests.get("https://api.vvhan.com/api/icp?url="+url)
    return data.text

def json_convert_to_dict(json_data):
    return json.loads(json_data)

def get_url_beian_name(dict_data):
    return dict_data['info']['name']

def take_img(url):
    url = url.strip('\n')
    domain = get_domain_by_urllib(url)
    filename = domain + '/' + url.split('/')[-1]
    cmd = POS + '/' + "wayland_session.sh" + " " + filename
    ret_val = os.system(cmd)
    img_filename = filename + '.png'
    return img_filename

def run(url):
    sleep(2)
    url = url.strip('\n')
    json_data = get_url_data(url)
    dict_data = json_convert_to_dict(json_data)
    beian_name = get_url_beian_name(dict_data)
    domain = get_domain_by_urllib(url)
    bug_url = url
    img_path = take_img(url)

    output = beian_name + ',' + domain + ',' + bug_url + ',' + img_path + '\n'
    return output 

    

def main():
    url_list=sys.argv[1]
    infile = open(url_list, 'r')
    outfile = open('output.csv', 'a')
    for url in infile.readlines():
        outfile.write(run(url))


main()
