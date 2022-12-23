# https://adventofcode.com/2015/day/18#part2

import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))
for i in range(100):
    grid[0][0] = grid[len(grid) - 1][0] = grid[0][len(grid[0]) - 1] = grid[len(grid) - 1][len(grid[0]) - 1] = '#'
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
grid[0][0] = grid[len(grid) - 1][0] = grid[0][len(grid[0]) - 1] = grid[len(grid) - 1][len(grid[0]) - 1] = '#'
total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '#':
            total += 1
print(total)
