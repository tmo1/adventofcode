# https://adventofcode.com/2024/day/6

area, direction, steps, locations = open(0).readlines(), 0, [(0, -1), (1, 0), (0, 1), (-1, 0)], set()
n = ''.join(area).find('^')
x, y = n % 131, n // 131
while True:
    locations.add((x, y))
    x1, y1 = x + steps[direction][0], y + steps[direction][1]
    if not (0 <= x1 < 130 and 0 <= y1 < 130):
        print(len(locations))
        quit()
    if area[y1][x1] == '#':
        direction = (direction + 1) % 4
    x, y = x + steps[direction][0], y + steps[direction][1]
