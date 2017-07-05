import json
import os
import subprocess

def read(filename):
    result = []
    with open(filename) as f:
        for line in f:
            item = json.loads(line)
            result.append(item)
    return result

def download(items, dirname):
    pids = set()
    for item in items:
        id = item['id']
        path = '{}/{}.jpg'.format(dirname, id)
        if os.path.exists(path):
            continue
        url = item['url']
        p = subprocess.Popen(['curl', '-s', url, '-o', path])
        pids.add(p.pid)
    while pids:
        pid, _ = os.wait()
        pids.remove(pid)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

items = read(args.input)
download(items, args.output)
