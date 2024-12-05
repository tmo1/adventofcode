# https://adventofcode.com/2024/day/4#part2

grid = [line.strip() for line in open(0)]
print(sum([1 for y in range(1, len(grid) - 1) for x in range(1, len(grid) - 1) if grid[y][x] == 'A' and {grid[y - 1][x - 1], grid[y + 1][x + 1]} == {'M', 'S'} and {grid[y + 1][x - 1], grid[y - 1][x + 1]} == {'M', 'S'}]))
