# https://adventofcode.com/2015/day/3#part2

import sys

directions = sys.stdin.readline().strip()
position1 = position2 = (0, 0)
houses = set()
houses.add(position1)
dirMap = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
f = True
for d in directions:
    # print(houses)
    if f:
        position1 = (position1[0] + dirMap[d][0], position1[1] + dirMap[d][1])
        houses.add(position1)
        f = False
    else:
        position2 = (position2[0] + dirMap[d][0], position2[1] + dirMap[d][1])
        houses.add(position2)
        f = True
print(len(houses))
