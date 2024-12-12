# https://adventofcode.com/2024/day/12

garden, regions = [list(line.strip()) for line in open(0)], []
for y, row in enumerate(garden):
    for x, plant in enumerate(row):
        if plant != '*':
            regions.append([set(), 0])
            new_plots = {(x, y)}
            while new_plots:
                x1, y1 = new_plots.pop()
                for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
                    if 0 <= x2 < len(garden) and 0 <= y2 < len(garden):
                        if garden[y2][x2] == plant:
                            if (x2, y2) not in regions[-1][0]: new_plots.add((x2, y2))
                        elif garden[y2][x2] != '*' or (x2, y2) not in regions[-1][0]: regions[-1][1] += 1
                    else: regions[-1][1] += 1
                regions[-1][0].add((x1, y1))
                garden[y1][x1] = '*'
print(sum([len(region[0]) * region[1] for region in regions]))
