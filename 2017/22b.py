# https://adventofcode.com/2017/day/22#part2

from collections import defaultdict

nodes, d, total, changes = defaultdict(lambda: 'c'), 3, 0, {'c': 'w', 'w': 'i', 'i': 'f', 'f': 'c'}
for i, line in enumerate(open(0)):
    for j, char in enumerate(line):
        if char == '#':
            nodes[(j, i)] = 'i'
x = y = i // 2
for i in range(10000000):
    state = nodes[(x, y)]
    if state == 'w':
        total += 1
    match state:
        case 'c':
            d = (d - 1) % 4
        case 'i':
            d = (d + 1) % 4
        case 'f':
            d = (d + 2) % 4
    nodes[(x, y)] = changes[state]
    match d:
        case 0:
            x += 1
        case 1:
            y += 1
        case 2:
            x -= 1
        case 3:
            y -= 1
print(total)
