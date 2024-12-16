# https://adventofcode.com/2024/day/14

import re

quadrants = [0 for i in range(4)]
for line in open(0):
    robot = [int(n) for n in re.findall(r"[-\d]+", line)]
    x, y = (robot[0] + (100 * robot[2])) % 101, (robot[1] + (100 * robot[3])) % 103
    if x < 50 and y < 51: quadrants[0] += 1
    elif x > 50 and y < 51: quadrants[1] += 1
    elif x < 50 and y > 51: quadrants[2] += 1
    elif x > 50 and y > 51: quadrants[3] += 1
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
