# https://adventofcode.com/2022/day/18

import sys

cubes = []
for line in sys.stdin:
    cubes.append([int(n) for n in line.split(',')])
total = 6 * len(cubes)
for i in range(len(cubes)):
    cube1 = cubes[i]
    for j in range(i + 1, len(cubes)):
        cube2 = cubes[j]
        same = sum(1 for k in range(3) if cube1[k] == cube2[k])
        one_apart = sum(1 for k in range(3) if abs(cube1[k] - cube2[k]) == 1)
        if same == 2 and one_apart == 1:
            total -= 2
print(total)

