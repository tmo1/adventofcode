# https://adventofcode.com/2015/day/1

import sys

instructions = sys.stdin.readline().strip()
floor = 0
for i in instructions:
    if i == '(':
        floor += 1
    else:
        floor -= 1
print(floor)
