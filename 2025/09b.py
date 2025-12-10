# https://adventofcode.com/2025/day/9

tiles = [[int(n) for n in line.split(',')] for line in open(0)]
tiles.append(tiles[0])
verticals = sorted([(tiles[i][0], min(tiles[i][1], tiles[i + 1][1]), max(tiles[i][1], tiles[i + 1][1])) for i in range(len(tiles) - 1) if tiles[i][0] == tiles[i + 1][0]], key=lambda x: x[0])
horizontals = sorted([(tiles[i][1], min(tiles[i][0], tiles[i + 1][0]), max(tiles[i][0], tiles[i + 1][0])) for i in range(len(tiles) - 1) if tiles[i][1] == tiles[i + 1][1]], key=lambda x: x[0])
outside_verticals = [(vertical[0] + (1 if sum([1 for v in verticals[i + 1:] if v[1] <= (vertical[1] + vertical[2]) // 2 < v[2]]) % 2 == 0 else -1), vertical[1] + 1, vertical[2] - 1) for i, vertical in enumerate(verticals)]
outside_horizontals = [(horizontal[0] + (1 if sum([1 for v in horizontals[i + 1:] if v[1] <= (horizontal[1] + horizontal[2]) // 2 < v[2]]) % 2 == 0 else -1), horizontal[1] + 1, horizontal[2] - 1) for i, horizontal in enumerate(horizontals)]
area = 0
for i, tile1 in enumerate(tiles):
    for tile2 in tiles[i + 1:]:
        area_ = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        if area_ > area:
            for vertical in outside_verticals:
                if min(tile1[0], tile2[0]) <= vertical[0] <= max(tile1[0], tile2[0]) and min(tile1[1], tile2[1]) <= vertical[2] and vertical[1] <= max(tile1[1], tile2[1]):
                    break
            else:
                for horizontal in outside_horizontals:
                    if min(tile1[1], tile2[1]) <= horizontal[0] <= max(tile1[1], tile2[1]) and min(tile1[0], tile2[0]) <= horizontal[2] and horizontal[1] <= max(tile1[0], tile2[0]):
                        break
                else:
                    area = area_
print(area)
