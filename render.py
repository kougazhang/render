#!/usr/bin/python

import argparse
import json

from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument("--tpl", help="the template path")
parser.add_argument("--cfg", help="the config path")
parser.add_argument("--dest", help="the render output path")
args = parser.parse_args()

with open(args.tpl) as f:
    template = Template(f.read())
    with open(args.cfg) as fc:
        cfg = fc.read()
        render = template.render(json.loads(cfg))
        with open(args.dest, mode="w") as fd:
            fd.write(render)
