# https://adventofcode.com/2023/day/18

dug, x, y = {(0, 0)}, 0, 0
directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
for line in open(0):
    line = line.split()
    for i in range(int(line[1])):
        x, y = x + directions[line[0]][0], y + directions[line[0]][1]
        dug.add((x, y))
min_x, min_y, max_x, max_y = min({tile[0] for tile in dug}), min({tile[1] for tile in dug}), max({tile[0] for tile in dug}), max({tile[1] for tile in dug})
old_tiles, new_tiles = set(), {(x, y) for y in range(min_y, max_y + 1) for x in [min_x, max_x] if (x, y) not in dug} | {(x, y) for x in range(min_x, max_x + 1) for y in [min_y, max_y] if (x, y) not in dug}
while new_tiles:
    new_new_tiles = {(tile[0] + direction[0], tile[1] + direction[1]) for tile in new_tiles for direction in directions.values() if min_x <= tile[0] + direction[0] <= max_x and min_y <= tile[1] + direction[1] <= max_y and (tile[0] + direction[0], tile[1] + direction[1]) not in dug and (tile[0] + direction[0], tile[1] + direction[1]) not in old_tiles and (tile[0] + direction[0], tile[1] + direction[1]) not in new_tiles}
    old_tiles, new_tiles = old_tiles | new_tiles, new_new_tiles
print((max_x - min_x + 1) * (max_y - min_y + 1) - len(old_tiles))
