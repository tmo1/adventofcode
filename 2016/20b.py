# https://adventofcode.com/2016/day/20#part2

import sys

ranges = []
for line in sys.stdin:
    line = line.split('-')
    ranges.append([int(line[0]), int(line[1])])
i, unblocked, total = 0, False, 0
while i < 4294967296:
    while True:
        for r in ranges:
            if r[0] <= i <= r[1]:
                i = r[1] + 1
                break
        else:
            break
    j = min({r[0] for r in ranges if r[0] > i} | {4294967296})
    total += j - i
    i = j
print(total)
