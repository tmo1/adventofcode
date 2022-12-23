# https://adventofcode.com/2015/day/2#part2

import sys

total = 0

for line in sys.stdin:
    x, y, z = line.split('x')
    x, y, z = int(x), int(y), int(z)
    total += min([2 * (x + y), 2 * (x + z), 2 * (y + z)]) + (x * y * z)
print(total)
