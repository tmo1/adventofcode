# https://adventofcode.com/2024/day/12#part2

from collections import defaultdict

garden, regions = [list(line.strip()) for line in open(0)], []
for y, row in enumerate(garden):
    for x, plant in enumerate(row):
        if plant != '*':
            regions.append([set(), 0])
            new_plots, vertical_sides, horizontal_sides = {(x, y)}, defaultdict(list), defaultdict(list)
            while new_plots:
                x1, y1 = new_plots.pop()
                for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
                    if (not (0 <= x2 < len(garden) and 0 <= y2 < len(garden))) or (garden[y2][x2] != plant and (garden[y2][x2] != '*' or (x2, y2) not in regions[-1][0])):
                        if x2 != x1: vertical_sides[(x1, x2)].append(y1)
                        else: horizontal_sides[(y1, y2)].append(x1)
                    elif garden[y2][x2] == plant and (x2, y2) not in regions[-1][0]: new_plots.add((x2, y2))
                regions[-1][0].add((x1, y1))
                garden[y1][x1] = '*'
            for k in list(vertical_sides.values()) + list(horizontal_sides.values()):
                k.sort()
                regions[-1][1] += sum([1 for i in range(len(k) - 1) if k[i + 1] - k[i] > 1]) + 1
print(sum([len(region[0]) * region[1] for region in regions]))
