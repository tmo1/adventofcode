# https://adventofcode.com/2022/day/22

import sys
import re

rows = []
columns = []
grid = []
longest = 0
for line in sys.stdin:
    if len(line) == 1:
        break
    line = line.rstrip()
    longest = max(longest, len(line))
    grid.append(line)
    rows.append({'first': re.search('[.#]', line).start(), 'last': len(line) - 1})
for i in range(longest):
    first = None
    for j, row in enumerate(rows):
        between = row['first'] <= i <= row['last']
        if first is not None:
            if not between:
                j -= 1
                break
        elif between:
            first = j
    columns.append({'first': first, 'last': j})
x, y, d = rows[0]['first'], 0, 0
path = sys.stdin.readline().strip()
index = 0
while index < len(path):
    if path[index].isdigit():
        new_x, new_y = x, y
        next_index = index
        while next_index < len(path) and path[next_index].isdigit():
            next_index += 1
        n = int(path[index:next_index])
        index = next_index
        for i in range(n):
            match d:
                case 0:
                    new_x = new_x + 1 if x < rows[y]['last'] else rows[y]['first']
                case 1:
                    new_y = new_y + 1 if y < columns[x]['last'] else columns[x]['first']
                case 2:
                    new_x = new_x - 1 if x > rows[y]['first'] else rows[y]['last']
                case 3:
                    new_y = new_y - 1 if y > columns[x]['first'] else columns[x]['last']
            if grid[new_y][new_x] == '#':
                break
            x, y = new_x, new_y
    else:
        if path[index] == 'R':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        index += 1
print((y + 1) * 1000 + (x + 1) * 4 + d)
