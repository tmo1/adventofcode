# https://adventofcode.com/2015/day/6#part2

import sys
lights = [[0] * 1000 for i in range(1000)]
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
                lights[x][y] += 1
            if action == 'off':
                if lights[x][y] > 0:
                    lights[x][y] -= 1
            if action == 'toggle':
                lights[x][y] += 2
total = 0
for x in range(1000):
    for y in range(1000):
        total += lights[x][y]
print(total)
