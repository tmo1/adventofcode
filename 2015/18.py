# https://adventofcode.com/2015/day/18

import sys

grid = []
for line in sys.stdin:
    grid.append(line.strip())
for i in range(100):
    new_grid = [['.'] * len(grid[0]) for j in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            total = 0
            for j in range(max(0, y - 1), min(len(grid), y + 2)):
                for k in range(max(0, x - 1), min(len(grid[0]), x + 2)):
                    if (not j == y) or (not k == x):
                        if grid[j][k] == '#':
                            total += 1
            if (total == 3) or (total == 2 and grid[y][x] == '#'):
                new_grid[y][x] = '#'
    grid = new_grid
total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            total += 1
print(total)
