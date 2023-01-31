# https://adventofcode.com/2017/day/7

import sys

programs, held = set(), set()
for line in sys.stdin:
    line = line.split()
    programs.add(line[0])
    if len(line) > 2:
        held |= {x.strip(',') for x in line[3:]}
print((programs - held).pop())
