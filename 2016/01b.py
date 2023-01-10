# https://adventofcode.com/2016/day/1#part2

import sys

x, y, d, locations = 0, 0, 0, {(0, 0)}
for i in sys.stdin.readline().split():
    if i[0] == 'R':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    n = int(i[1:].strip(','))
    for j in range(n):
        match d:
            case 0:
                y += 1
            case 1:
                x += 1
            case 2:
                y -= 1
            case 3:
                x -= 1
        if (x, y) in locations:
            print(abs(x) + abs(y))
            quit()
        locations.add((x, y))
