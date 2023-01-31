# https://adventofcode.com/2017/day/3#part2

import sys

n, x, y, direction, squares = int(sys.stdin.readline()), 0, 0, 0, {(0, 0): 1}


def set_value():
    s = 0
    for x1 in [x - 1, x, x + 1]:
        for y1 in [y - 1, y, y + 1]:
            if x1 != x or y1 != y:
                s += squares.get((x1, y1), 0)
    if s > n:
        print(s)
        quit()
    squares[(x, y)] = s


while True:
    match direction:
        case 0:
            x += 1
            set_value()
            if (x, y + 1) not in squares:
                direction = 1
        case 1:
            y += 1
            set_value()
            if (x - 1, y) not in squares:
                direction = 2
        case 2:
            x -= 1
            set_value()
            if (x, y - 1) not in squares:
                direction = 3
        case 3:
            y -= 1
            set_value()
            if (x + 1, y) not in squares:
                direction = 0
