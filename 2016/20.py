# https://adventofcode.com/2016/day/20

import sys

ranges = []
for line in sys.stdin:
    line = line.split('-')
    ranges.append([int(line[0]), int(line[1])])
i = 0
while True:
    for r in ranges:
        if r[0] <= i <= r[1]:
            i = r[1] + 1
            break
    else:
        break
print(i)
