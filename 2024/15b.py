# https://adventofcode.com/2024/day/15#part2

warehouse, moves = open(0).read().split('\n\n')
warehouse, robot = [[('[' if i % 2 == 0 else ']') if line[i // 2] == 'O' else line[i // 2] for i in range(len(line) * 2)] for line in warehouse.split()], warehouse.index('@')
x, y, directions = robot % (len(warehouse[0]) // 2), robot // (len(warehouse[0]) // 2), {'>': 1, '<': -1, '^': -1, 'v': 1}
warehouse[y][x], warehouse[y][x + 1] = '.', '.'
for move in ''.join(moves.split()):
    if move in ['>', '<']:
        x1 = x + (directions[move])
        while warehouse[y][x1] in ['[', ']']: x1 += directions[move]
        if warehouse[y][x1] == '.':
            for x2 in range(x1, x, -directions[move]): warehouse[y][x2] = warehouse[y][x2 - directions[move]]
            x += directions[move]
    else:
        boxes = [{(x, y)}]
        while boxes[-1]:
            boxes.append(set())
            for box in boxes[-2]:
                if warehouse[box[1] + directions[move]][box[0]] == '#': break
                if warehouse[box[1] + directions[move]][box[0]] == '[': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] + 1, box[1] + directions[move])}
                elif warehouse[box[1] + directions[move]][box[0]] == ']': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] - 1, box[1] + directions[move])}
            else: continue
            break
        else:
            for row in list(reversed(boxes)):
                for box in row: warehouse[box[1] + directions[move]][box[0]], warehouse[box[1]][box[0]] = warehouse[box[1]][box[0]], '.'
            y += directions[move]
print(sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == '[']))
