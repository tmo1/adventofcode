# https://adventofcode.com/2015/day/2

import sys

total = 0

for line in sys.stdin:
    x, y, z = line.split('x')
    x, y, z = int(x), int(y), int(z)
    total += 2 * ((x * y) + (x * z) + (y * z)) + min([(x * y), (x * z), (y * z)])
print(total)
