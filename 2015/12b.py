# https://adventofcode.com/2015/day/12#part2

import sys
import json

doc = sys.stdin.readline()
doc = json.loads(doc)
total = 0


def acc(j):
    global total
    if isinstance(j, int):
        total += j
    elif isinstance(j, list):
        for x in j:
            acc(x)
    elif isinstance(j, dict):
        if 'red' not in j.values():
            for x in j.values():
                acc(x)


acc(doc)
print(total)
