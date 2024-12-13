# https://adventofcode.com/2024/day/10#part2

def hike(x1, y1):
    global total
    if guide[y1][x1] == 9:
        total += 1
        return
    for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
        if 0 <= x2 < len(guide) and 0 <= y2 < len(guide) and guide[y2][x2] == guide[y1][x1] + 1: hike(x2, y2)

guide, total = [[int(c) for c in line.strip()] for line in open(0)], 0
# Alternate version:
# for z in filter(lambda z: guide[z[1]][z[0]] == 0, ((x, y, c) for y, line in enumerate(guide) for x, c in enumerate(line))): hike(z[0], z[1])
for y, line in enumerate(guide):
    for x, c in enumerate(line):
        if c == 0: hike(x, y)
print(total)
