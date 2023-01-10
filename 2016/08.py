# https://adventofcode.com/2016/day/8

import sys

screen = [[0 for i in range(50)] for j in range(6)]
for line in sys.stdin:
    line = line.split()
    if line[0] == 'rect':
        x, y = line[1].split('x')
        x, y = int(x), int(y)
        for i in range(x):
            for j in range(y):
                screen[j][i] = 1
    else:
        n, shift = int(line[2][2:]), int(line[4])
        for i in range(shift):
            if line[1] == 'row':
                last = screen[n][49]
                for x in range(48, -1, -1):
                    screen[n][x + 1] = screen[n][x]
                screen[n][0] = last
            else:
                last = screen[5][n]
                for y in range(4, -1, -1):
                    screen[y + 1][n] = screen[y][n]
                screen[0][n] = last
print(sum([sum([screen[y][x] for x in range(50)]) for y in range(6)]))
