# https://adventofcode.com/2022/day/9

import sys

hx = tx = hy = ty = 0
visited = {(0, 0)}
for line in sys.stdin:
    line = line.split()
    for i in range(int(line[1])):
        match line[0]:
            case 'U':
                hy -= 1
            case 'D':
                hy += 1
            case 'R':
                hx += 1
            case 'L':
                hx -= 1
        if abs(hx - tx) == 2:
            tx += (hx - tx) // 2
            ty = hy
        if abs(hy - ty) == 2:
            ty += (hy - ty) // 2
            tx = hx
        visited.add((tx, ty))
print(len(visited))
