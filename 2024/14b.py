# https://adventofcode.com/2024/day/14#part2
# Hacky solution that just looks for a row containing a bunch of consecutive locations containing robots

import re

robots = [[int(n) for n in re.findall(r"[-\d]+", line)] for line in open(0)]
for i in range(1000000):
    for j in range(103):
        row, n = sorted({robot[0] for robot in robots if robot[1] == j}), 0
        for k in range(len(row) - 1):
            n = n + 1 if row[k + 1] == row[k] + 1 else 0
            if n > 10:
                print(i)
                quit()
    for robot in robots: robot[0], robot[1] = (robot[0] + robot[2]) % 101, (robot[1] + robot[3]) % 103
