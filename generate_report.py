#!/usr/bin/env python3

import json
import re

from string import Template

# TODO: Find a feed to setup links to the font samples

nope = Template('<li><strike>$family</strike></li>')

with open('font-report.json') as _in:
    data = json.load(_in)
    with open('font-report.html', 'w') as _out:
        for font in data:
            if font['status'] == 200:
                _out.write(f"<li>{font['family']}</li>\n")
            else:
                _out.write(f"<li><strike>{font['family']}</strike></li>\n")
