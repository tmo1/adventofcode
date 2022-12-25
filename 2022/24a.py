# https://adventofcode.com/2022/day/24

import sys

blizzards = []
for i, line in enumerate(sys.stdin):
    if i == 0:
        x_max = len(line) - 3
    blizzards.append([[char] if char in ['^', 'v', '>', '<'] else [] for char in line])
y_max = i - 1
positions = {(1, 0)}
i = 0
while True:
    i += 1
    new_blizzards = [[[] for x in range(x_max + 1)] for y in range(y_max + 1)]
    for y in range(1, y_max + 1):
        for x in range(1, x_max + 1):
            for blizzard in blizzards[y][x]:
                new_x, new_y = x, y
                match blizzard:
                    case '^':
                        new_y = y_max if y == 1 else y - 1
                    case 'v':
                        new_y = 1 if y == y_max else y + 1
                    case '<':
                        new_x = x_max if x == 1 else x - 1
                    case '>':
                        new_x = 1 if x == x_max else x + 1
                new_blizzards[new_y][new_x].append(blizzard)
    blizzards = new_blizzards
    new_positions = set()
    for position in positions:
        for new_position in [(position[0], position[1]), (position[0] + 1, position[1]), (position[0] - 1, position[1]),
                             (position[0], position[1] + 1), (position[0], position[1] - 1)]:
            if new_position == (1, 0) or new_position == (x_max, y_max + 1) or (
                    y_max >= new_position[1] > 0 and 0 < new_position[0] <= x_max and len(
                    blizzards[new_position[1]][new_position[0]]) == 0):
                if new_position == (x_max, y_max):
                    print(i + 1)
                    quit()
                new_positions.add(new_position)
    positions = new_positions
