# https://adventofcode.com/2017/day/2

import sys

s = 0
for line in sys.stdin:
    numbers = [int(x) for x in line.split()]
    s += max(numbers) - min(numbers)
print(s)
