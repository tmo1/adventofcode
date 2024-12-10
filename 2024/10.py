# https://adventofcode.com/2024/day/10

def hike(x1, y1):
    if guide[y1][x1] == 9:
        nines.add((x1, y1))
        return
    for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
        if 0 <= x2 < len(guide) and 0 <= y2 < len(guide) and guide[y2][x2] == guide[y1][x1] + 1: hike(x2, y2)

guide, total = [[int(c) for c in line.strip()] for line in open(0)], 0
for y, line in enumerate(guide):
    for x, c in enumerate(line):
        if c == 0:
            nines = set()
            hike(x, y)
            total += len(nines)
print(total)
