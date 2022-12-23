# https://adventofcode.com/2022/day/23

import sys

elves = set()
for i, line in enumerate(sys.stdin):
    elves |= set([(count, i) for count, char in enumerate(line.strip()) if char == '#'])


def look(ex, ey, d):
    match d:
        case 0:
            return (ex, ey - 1) if len({(ex - 1, ey - 1), (ex, ey - 1), (ex + 1, ey - 1)} & elves) == 0 else None
        case 1:
            return (ex, ey + 1) if len({(ex - 1, ey + 1), (ex, ey + 1), (ex + 1, ey + 1)} & elves) == 0 else None
        case 2:
            return (ex - 1, ey) if len({(ex - 1, ey - 1), (ex - 1, ey), (ex - 1, ey + 1)} & elves) == 0 else None
        case 3:
            return (ex + 1, ey) if len({(ex + 1, ey + 1), (ex + 1, ey), (ex + 1, ey - 1)} & elves) == 0 else None


direction = 0
for r in range(10):
    proposals = {}
    for elf in elves:
        x, y = elf[0], elf[1]
        neighbors = set()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                neighbors.add((x + i, y + j))
        neighbors.remove((x, y))
        if len(neighbors & elves) > 0:
            for i in range(4):
                proposal = look(elf[0], elf[1], (direction + i) % 4)
                if proposal is not None:
                    proposals[elf] = proposal
                    break
    for elf, proposal in proposals.items():
        if sum([1 for v in proposals.values() if v == proposal]) == 1:
            elves.remove(elf)
            elves.add(proposal)
    direction = (direction + 1) % 4
x1 = min([elf[0] for elf in elves])
x2 = max([elf[0] for elf in elves])
y1 = min([elf[1] for elf in elves])
y2 = max([elf[1] for elf in elves])
print((x2 - x1 + 1) * (y2 - y1 + 1) - len(elves))
