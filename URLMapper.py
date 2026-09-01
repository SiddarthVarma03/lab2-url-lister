#!/usr/bin/env python3

import sys
import re

# Match the contents inside href="..."
url_pattern = re.compile(r'href="([^"]*)"')

for line in sys.stdin:
    urls = url_pattern.findall(line)

    for url in urls:
        print(f"{url}\t1")
