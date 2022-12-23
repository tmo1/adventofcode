# https://adventofcode.com/2015/day/12

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
        for x in j.values():
            acc(x)


acc(doc)
print(total)
