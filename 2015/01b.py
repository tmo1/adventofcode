# https://adventofcode.com/2015/day/1#part2

import sys

instructions = sys.stdin.readline().strip()
floor = 0
pos = 1
for i in instructions:
    if i == '(':
        floor += 1
    else:
        floor -= 1
        if floor == -1:
            print(pos)
    pos += 1
