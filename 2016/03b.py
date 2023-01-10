# https://adventofcode.com/2016/day/3#part2

import sys

possible, sides = 0, []
for line in sys.stdin:
    sides.append([int(x) for x in line.split()])
    if len(sides) == 3:
        for i in range(3):
            if sides[0][i] + sides[1][i] > sides[2][i] and sides[0][i] + sides[2][i] > sides[1][i] and sides[1][i] + \
                    sides[2][i] > sides[0][i]:
                possible += 1
        sides = []
print(possible)
