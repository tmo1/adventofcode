# https://adventofcode.com/2022/day/24
# this works, but 24a.py is a much more efficient solution

import sys

blizzards = set()
for i, line in enumerate(sys.stdin):
    if i == 0:
        x_max = len(line) - 3
        continue
    blizzards |= set((count, i, char) for count, char in enumerate(line) if char in ['^', 'v', '>', '<'])
y_max = i - 1
positions = {(1, 0)}
i = 0
while True:
    i += 1
    new_blizzards = set()
    for blizzard in blizzards:
        new_blizzard = list(blizzard)
        match blizzard[2]:
            case '^':
                new_blizzard[1] = y_max if blizzard[1] == 1 else blizzard[1] - 1
            case 'v':
                new_blizzard[1] = 1 if blizzard[1] == y_max else blizzard[1] + 1
            case '<':
                new_blizzard[0] = x_max if blizzard[0] == 1 else blizzard[0] - 1
            case '>':
                new_blizzard[0] = 1 if blizzard[0] == x_max else blizzard[0] + 1
        new_blizzards.add(tuple(new_blizzard))
        blizzards = new_blizzards
        blizzard_locations = {(blizzard[0], blizzard[1]) for blizzard in blizzards}
    new_positions = set()
    for position in positions:
        for new_position in [(position[0], position[1]), (position[0] + 1, position[1]), (position[0] - 1, position[1]),
                             (position[0], position[1] + 1), (position[0], position[1] - 1)]:
            if new_position not in blizzard_locations and (new_position[1] > 0 or new_position[0] == 1) and new_position[1] <= y_max and 0 < \
                    new_position[0] <= x_max:
                if new_position == (x_max, y_max):
                    print(i + 1)
                    quit()
                new_positions.add(new_position)
    positions = new_positions
