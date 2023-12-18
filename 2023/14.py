# https://adventofcode.com/2023/day/14

platform = [list(line.strip()) for line in open(0)]
weight = 0
for y, row in enumerate(platform):
    for x, char in enumerate(row):
        if char == 'O':
            platform[y][x] = '.'
            i = y - 1
            while i >= 0 and platform[i][x] == '.':
                i -= 1
            platform[i + 1][x] = 'O'
            weight += len(platform) - i - 1
print(weight)
