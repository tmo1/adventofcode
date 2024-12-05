# https://adventofcode.com/2024/day/4

grid, total = [line.strip() for line in open(0)], 0
for y in range(len(grid)):
    for x in range(len(grid)):
        if grid[y][x] == 'X':
            for i in range(-1 if y > 2 else 0, 2 if y < len(grid) - 3 else 1):
                for j in range(-1 if x > 2 else 0, 2 if x < len(grid) - 3 else 1):
                    if grid[y + i][x + j] == 'M' and grid[y + 2 * i][x + 2 * j] == 'A' and grid[y + 3 * i][x + 3 * j] == 'S':
                        total += 1
print(total)
