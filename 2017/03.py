# https://adventofcode.com/2017/day/3

import sys

n = int(sys.stdin.readline())
sqrt = int(n ** .5)
if sqrt % 2 == 0:
    sqrt -= 1
square = sqrt * sqrt
if n == square:
    m = sqrt - 1
else:
    m = sqrt // 2 + 1
    if n < square + sqrt + 1:
        m += abs(n - (square + (sqrt // 2) + 1))
    elif n < square + 2 * (sqrt + 1):
        m += abs(n - (square + sqrt + 2 + (sqrt // 2)))
    elif n < square + 3 * (sqrt + 1):
        m += abs(n - (square + 2 * (sqrt + 1) + (sqrt // 2) + 1))
    else:
        m += abs(n - (square + 3 * (sqrt + 1) + (sqrt // 2) + 1))
print(m)
