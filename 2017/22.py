# https://adventofcode.com/2017/day/22

nodes, d, total = set(), 3, 0
for i, line in enumerate(open(0)):
    for j, char in enumerate(line):
        if char == '#':
            nodes.add((j, i))
x = y = i // 2
for i in range(10000):
    if (x, y) in nodes:
        d = (d + 1) % 4
        nodes.remove((x, y))
    else:
        d = (d - 1) % 4
        nodes.add((x, y))
        total += 1
    match d:
        case 0:
            x += 1
        case 1:
            y += 1
        case 2:
            x -= 1
        case 3:
            y -= 1
print(total)
