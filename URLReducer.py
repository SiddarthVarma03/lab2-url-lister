#!/usr/bin/env python3

import sys

current_url = None
current_count = 0

for line in sys.stdin:
    line = line.strip()

    try:
        url, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_url == url:
        current_count += count
    else:
        if current_url is not None and current_count > 5:
            print(f"{current_url}\t{current_count}")

        current_url = url
        current_count = count

# Output the final URL
if current_url is not None and current_count > 5:
    print(f"{current_url}\t{current_count}")
