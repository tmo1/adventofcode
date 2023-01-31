# https://adventofcode.com/2017/day/19

diagram, y, direction, letters = [line[:-1] for line in open(0)], 0, 1, []
for i, char in enumerate(diagram[0]):
    if char == '|':
        x = i
        break
while True:
    current = diagram[y][x]
    if current == '+':
        if direction == 0 or direction == 2:
            if y > 0 and diagram[y - 1][x] != ' ':
                direction, y = 3, y - 1
            else:
                direction, y = 1, y + 1
        else:
            if x > 0 and diagram[y][x - 1] != ' ':
                direction, x = 2, x - 1
            else:
                direction, x = 0, x + 1
    elif current == ' ':
        print(''.join(letters))
        quit()
    else:
        if current.isalpha():
            letters.append(diagram[y][x])
        match direction:
            case 0:
                x += 1
            case 1:
                y += 1
            case 2:
                x -= 1
            case 3:
                y -= 1
