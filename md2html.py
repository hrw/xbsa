#!/usr/bin/python3

import markdown
import sys

from string import Template

filename = 'bsa-sbsa.md'

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    text = f.read()

xbsa_table = markdown.markdown(text, extensions=['extra'])

with open("template.html") as html_file:
    html = Template(html_file.read())

    print(html.substitute(xbsa_table=xbsa_table))
