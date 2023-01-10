# https://adventofcode.com/2016/day/3

import sys

possible = 0
for line in sys.stdin:
    sides = [int(x) for x in line.split()]
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
        possible += 1
print(possible)
