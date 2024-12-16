# https://adventofcode.com/2024/day/15

warehouse, moves = open(0).read().split('\n\n')
warehouse, robot = [list(line) for line in warehouse.split()], warehouse.index('@')
x, y, directions = robot % (len(warehouse[0]) + 1), robot // (len(warehouse[0]) + 1), {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
warehouse[y][x] = '.'
for move in ''.join(moves.split()):
    x1, y1 = x + directions[move][0], y + directions[move][1]
    while warehouse[y1][x1] == 'O': x1, y1 = x1 + directions[move][0], y1 + directions[move][1]
    if warehouse[y1][x1] == '.':
        if abs(y1 - y + x1 - x) > 1: warehouse[y1][x1], warehouse[y + directions[move][1]][x + directions[move][0]] = 'O', '.'
        x, y = x + directions[move][0], y + directions[move][1]
print(sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == 'O']))