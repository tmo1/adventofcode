# https://adventofcode.com/2023/day/14#part2

platform = [list(line.strip()) for line in open(0)]
direction, cycles, states = 0, 0, {}
while True:
    if direction in {0, 2}:
        if direction == 2:
            platform.reverse()
        else:
            if states is not None:
                new_state = tuple([(x, y) for y, row in enumerate(platform) for x, char in enumerate(row) if platform[y][x] == 'O'])
                if new_state in states:
                    cycles = 1000000000 - (1000000000 - cycles) % (cycles - states[new_state])
                    states = None
                else:
                    states[new_state] = cycles
        for y, row in enumerate(platform):
            for x, char in enumerate(row):
                if char == 'O':
                    platform[y][x] = '.'
                    i = y - 1
                    while i >= 0 and platform[i][x] == '.':
                        i -= 1
                    platform[i + 1][x] = 'O'
        if direction == 2:
            platform.reverse()
    elif direction == 1:
        for x in range(len(platform[0])):
            for y in range(len(platform)):
                if platform[y][x] == 'O':
                    platform[y][x] = '.'
                    i = x - 1
                    while i >= 0 and platform[y][i] == '.':
                        i -= 1
                    platform[y][i + 1] = 'O'
    else:
        for x in range(len(platform[0]) - 1, -1, -1):
            for y in range(len(platform)):
                if platform[y][x] == 'O':
                    platform[y][x] = '.'
                    i = x + 1
                    while i < len(platform[0]) and platform[y][i] == '.':
                        i += 1
                    platform[y][i - 1] = 'O'
        cycles += 1
        if cycles == 1000000000:
            print(sum([len(platform) - y for y, row in enumerate(platform) for x, char in enumerate(row) if char == 'O']))
            quit()
    direction = (direction + 1) % 4
