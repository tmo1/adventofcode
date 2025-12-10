# https://adventofcode.com/2025/day/9

tiles = [[int(n) for n in line.split(',')] for line in open(0)]
print(max([(abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1) for tile1 in tiles for tile2 in tiles]))

