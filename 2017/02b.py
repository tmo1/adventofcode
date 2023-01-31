# https://adventofcode.com/2017/day/2#part2

import sys

s = 0
for line in sys.stdin:
    numbers = [int(x) for x in line.split()]
    for a in numbers:
        for b in numbers:
            if a != b and a % b == 0:
                s += a // b
                break
        else:
            continue
        break
print(s)
