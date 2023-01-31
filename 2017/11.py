# https://adventofcode.com/2017/day/11
# this solution is based on: https://www.redblobgames.com/grids/hexagons/

import sys

q = r = s = 0
for direction in sys.stdin.readline().strip().split(','):
    match direction:
        case 'n':
            s += 1
            q -= 1
        case 's':
            s -= 1
            q += 1
        case 'ne':
            s += 1
            r -= 1
        case 'sw':
            s -= 1
            r += 1
        case 'nw':
            r += 1
            q -= 1
        case 'se':
            r -= 1
            q += 1
print(sum([abs(x) for x in [q, r, s]]) // 2)
