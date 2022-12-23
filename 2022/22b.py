# https://adventofcode.com/2022/day/22#part2

# this solution utilizes hand-crafted wrap rules based on my particular puzzle input (with the aid of a foldable model
# constructed with paper, pen, and scissors), and will probably not work without adjustment for other inputs)

import sys
import re

grid = []
for line in sys.stdin:
    if len(line) == 1:
        break
    line = line.rstrip()
    grid.append(line)
wrap_rules = {}
for i in range(50):
    wrap_rules[(100 + i, 49, 1)] = (99, 50 + i, 2)
    wrap_rules[(99, 50 + i, 0)] = (100 + i, 49, 3)
    wrap_rules[(149, 49 - i, 0)] = (99, 100 + i, 2)
    wrap_rules[(99, 100 + i, 0)] = (149, 49 - i, 2)
    wrap_rules[(50 + i, 149, 1)] = (49, 150 + i, 2)
    wrap_rules[(49, 150 + i, 0)] = (50 + i, 149, 3)
    wrap_rules[(50, i, 2)] = (0, 149 - i, 0)
    wrap_rules[(0, 149 - i, 2)] = (50, i, 0)
    wrap_rules[(50, 50 + i, 2)] = (i, 100, 1)
    wrap_rules[(i, 100, 3)] = (50, 50 + i, 0)
    wrap_rules[(100 + i, 0, 3)] = (i, 199, 3)
    wrap_rules[(i, 199, 1)] = (100 + i, 0, 1)
    wrap_rules[(50 + i, 0, 3)] = (0, 150 + i, 0)
    wrap_rules[(0, 150 + i, 2)] = (50 + i, 0, 1)
path = sys.stdin.readline().strip()
x, y, d, index = re.search('[.#]', grid[0]).start(), 0, 0, 0
while index < len(path):
    if path[index].isdigit():
        new_x, new_y, new_d, next_index = x, y, d, index
        while next_index < len(path) and path[next_index].isdigit():
            next_index += 1
        n = int(path[index:next_index])
        index = next_index
        for i in range(n):
            if (x, y, d) in wrap_rules:
                new_x, new_y, new_d = wrap_rules[(x, y, d)]
            else:
                match d:
                    case 0:
                        new_x = new_x + 1
                    case 1:
                        new_y = new_y + 1
                    case 2:
                        new_x = new_x - 1
                    case 3:
                        new_y = new_y - 1
            if grid[new_y][new_x] == '#':
                break
            x, y, d = new_x, new_y, new_d
    else:
        if path[index] == 'R':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        index += 1
print((y + 1) * 1000 + (x + 1) * 4 + d)
