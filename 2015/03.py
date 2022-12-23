# https://adventofcode.com/2015/day/3

import sys

directions = sys.stdin.readline().strip()
position = (0, 0)
houses = set()
houses.add(position)
dirMap = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
for d in directions:
    position = (position[0] + dirMap[d][0], position[1] + dirMap[d][1])
    houses.add(position)
print(len(houses))
