# https://adventofcode.com/2022/day/3

import sys

priorities = 0
for line in sys.stdin:
    line.strip()
    items = len(line) // 2
    item = ord(({*line[:items]} & {*line[items:]}).pop()) - 38
    if item > 52:
        item -= 58
    priorities += item
print(priorities)
