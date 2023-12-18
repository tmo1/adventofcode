# https://adventofcode.com/2023/day/10#part2

field = []
for y, line in enumerate(open(0)):
    field.append(line)
    s_location = line.find('S')
    if s_location >= 0:
        x1, y1 = s_location, y
field_marked = [[False for i in range(len(field[0]))] for j in range(len(field))]
if y1 > 0 and field[y1 - 1][x1] in {'7', 'F', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = 0
        start_pipe = 'J'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = 0
        start_pipe = 'L'
if y1 < len(field) - 1 and field[y1 + 1][x1] in {'J', 'L', '|'}:
    if x1 > 0 and field[y1][x1 - 1] in {'F', 'L', '-'}:
        direction = 2
        start_pipe = '7'
    elif x1 < len(field[0]) - 1 and field[y1][x1 + 1] in {'J', '7', '-'}:
        direction = 2
        start_pipe = 'F'
if 0 < x1 < len(field[0]) - 1 and field[y1][x1 - 1] in {'F', 'L', '-'} and field[y1][x1 + 1] in {'7', 'J', '-'}:
    direction = 1
    start_pipe = '-'
if 0 < y1 < len(field) - 1 and field[y1 - 1][x1] in {'F', '7', '|'} and field[y1 + 1][x1] in {'L', 'J', '|'}:
    direction = 0
    start_pipe = '|'
field[y1] = field[y1][:x1] + start_pipe + field[y1][x1 + 1:]
x, y = x1, y1
while True:
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    match field[y][x]:
        case 'L':
            direction = 1 if direction == 2 else 0
        case 'J':
            direction = 3 if direction == 2 else 0
        case '7':
            direction = 2 if direction == 1 else 3
        case 'F':
            direction = 2 if direction == 3 else 1
    field_marked[y][x] = True
    if x1 == x and y1 == y:
        break
total = 0
for y, line in enumerate(field):
    for x, char in enumerate(line):
        if not field_marked[y][x]:
            n = 0
            for y1 in range(y + 1, len(field)):
                if field_marked[y1][x]:
                    if field[y1][x] == '-':
                        n += 1
                    elif field[y1][x] == '7' or field[y1][x] == 'F':
                        prev = field[y1][x]
                    elif (field[y1][x] == 'J' and prev == 'F') or (field[y1][x] == 'L' and prev == '7'):
                        n += 1
            if n % 2 == 1:
                total += 1
print(total)
