# https://adventofcode.com/2016/day/1

import sys

x, y, d = 0, 0, 0
for i in sys.stdin.readline().split():
    if i[0] == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    n = int(i[1:].strip(','))
    match d:
        case 0:
            y += n
        case 1:
            x += n
        case 2:
            y -= n
        case 3:
            x -= n
print(abs(x) + abs(y))
