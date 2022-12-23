# https://adventofcode.com/2022/day/10#part2

import sys

x = 1
cycle = 0
for line in sys.stdin:
    print('#' if x - 1 <= (cycle % 40) <= x + 1 else '.', end='')
    line = line.split()
    if line[0] == 'addx':
        cycle += 1
        if cycle % 40 == 0:
            print()
        print('#' if x - 1 <= (cycle % 40) <= x + 1 else '.', end='')
        x += int(line[1])
    cycle += 1
    if cycle % 40 == 0:
        print()
