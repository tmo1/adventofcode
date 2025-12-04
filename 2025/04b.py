# https://adventofcode.com/2025/day/4#part2

grid = [list(line.strip()) for line in open(0)]
rolls, done = 0, False
while not done:
    done = True
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@' and sum([1 for y_ in range(max(y - 1, 0), min(y + 1, len(grid) - 1) + 1) for x_ in range(max(x - 1, 0), min(x + 1, len(grid[0]) - 1) + 1) if (x_ != x or y_ != y) and grid[y_][x_] == '@']) < 4:
                rolls, done, grid[y][x] = rolls + 1, False, '.'
print(rolls)