# https://adventofcode.com/2022/day/10

import sys

x = 1
cycle = 1
total = 0
for line in sys.stdin:
    if (cycle - 20) % 40 == 0 and cycle <= 220:
        total += x * cycle
    line = line.split()
    if line[0] == 'addx':
        cycle += 1
        if (cycle - 20) % 40 == 0:
            total += x * cycle
        x += int(line[1])
    cycle += 1
print(total)
