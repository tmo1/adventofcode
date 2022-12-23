# https://adventofcode.com/2022/day/18#part2
# this takes 23 seconds for my input on my W550s

import sys

cubes = []
for line in sys.stdin:
    cubes.append([int(n) for n in line.split(',')])
x1 = min(cube[0] for cube in cubes) - 1
x2 = max(cube[0] for cube in cubes) + 1
y1 = min(cube[1] for cube in cubes) - 1
y2 = max(cube[1] for cube in cubes) + 1
z1 = min(cube[2] for cube in cubes) - 1
z2 = max(cube[2] for cube in cubes) + 1
steam = {(x1, y1, z1)}
total = 0


def new_steam(x, y, z):
    global total
    if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2 and (x, y, z) not in steam and (x, y, z) not in steam2 and [x, y, z] not in cubes:
        for cube in cubes:
            same = sum(1 for i in range(3) if cube[i] == (x, y, z)[i])
            one_apart = sum(1 for i in range(3) if abs(cube[i] - (x, y, z)[i]) == 1)
            if same == 2 and one_apart == 1:
                total += 1
        return True
    return False


possibilities = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
while True:
    steam2 = set()
    for s in steam:
        for possibility in possibilities:
            if new_steam(s[0] + possibility[0], s[1] + possibility[1], s[2] + possibility[2]):
                steam2.add((s[0] + possibility[0], s[1] + possibility[1], s[2] + possibility[2]))
    if not steam2:
        print(total)
        quit()
    steam |= steam2
