# https://adventofcode.com/2022/day/14

import sys
import re

points = set()
for line in sys.stdin:
    line = re.split('->|,', line)
    line = [int(x) for x in line]
    for i in range(2, len(line), 2):
        x1, y1, x2, y2 = line[i - 2], line[i - 1], line[i], line[i + 1]
        if x1 == x2:
            if y2 < y1:
                y2, y1 = y1, y2
            points |= {(x1, n) for n in range(y1, y2 + 1)}
        else:
            if x2 < x1:
                x2, x1 = x1, x2
            points |= {(n, y1) for n in range(x1, x2 + 1)}
i = 0
highest = max(point[1] for point in points)
while True:
    sand_x, sand_y = 500, 0
    while True:
        if sand_y >= highest:
            print(i)
            quit()
        sand_new_y = sand_y + 1
        if (sand_x, sand_new_y) not in points:
            sand_y = sand_new_y
        elif (sand_x - 1, sand_new_y) not in points:
            sand_x, sand_y = sand_x - 1, sand_new_y
        elif (sand_x + 1, sand_new_y) not in points:
            sand_x, sand_y = sand_x + 1, sand_new_y
        else:
            points.add((sand_x, sand_y))
            i += 1
            break
