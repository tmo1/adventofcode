# https://adventofcode.com/2015/day/6

import sys
lights = [[False] * 1000 for i in range(1000)]
for line in sys.stdin:
    words = line.split()
    if words[0] == 'turn':
        action = words.pop(1)
    else:
        action = words[0]
    x1, y1 = words[1].split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = words[3].split(',')
    x2, y2 = int(x2), int(y2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == 'on':
                lights[x][y] = True
            if action == 'off':
                lights[x][y] = False
            if action == 'toggle':
                lights[x][y] = not lights[x][y]
total = 0
for x in range(1000):
    for y in range(1000):
        if lights[x][y]:
            total += 1
print(total)
