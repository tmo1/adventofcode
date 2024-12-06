# https://adventofcode.com/2024/day/6#part2

area, steps, total = open(0).readlines(), [(0, -1), (1, 0), (0, 1), (-1, 0)], 0
n = ''.join(area).find('^')
x_start, y_start = n % 131, n // 131
x, y, direction, locations = x_start, y_start, 0, set()
while True:
    locations.add((x, y))
    x1, y1 = x + steps[direction][0], y + steps[direction][1]
    if not (0 <= x1 < 130 and 0 <= y1 < 130):
        break
    if area[y1][x1] == '#':
        direction = (direction + 1) % 4
    x, y = x + steps[direction][0], y + steps[direction][1]
for location in locations:
    x, y, direction, visited = x_start, y_start, 0, set()
    while True:
        if (x, y, direction) in visited:
            total += 1
            break
        visited.add((x, y, direction))
        x1, y1 = x + steps[direction][0], y + steps[direction][1]
        if not (0 <= x1 < 130 and 0 <= y1 < 130):
            break
        if area[y1][x1] == '#' or (x1, y1) == location:
            direction = (direction + 1) % 4
        else:
            x, y = x + steps[direction][0], y + steps[direction][1]
print(total)
