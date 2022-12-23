# https://adventofcode.com/2022/day/17

import copy
import sys

jets = sys.stdin.readline().strip()
rocks = [[[2, 0], [3, 0], [4, 0], [5, 0]], [[2, 1], [3, 1], [3, 2], [3, 0], [4, 1]],
         [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]], [[2, 0], [2, 1], [2, 2], [2, 3]], [[2, 0], [3, 0], [2, 1], [3, 1]]]
chamber = {(x, 0) for x in range(7)}
highest = 0
jet = 0
for i in range(2022):
    rock = copy.deepcopy(rocks[i % 5])
    adjustment = highest + 4
    for n in rock:
        n[1] += adjustment
    rest = False
    while not rest:
        new_rock = []
        if jets[jet] == '<':
            if rock[0][0] > 0:
                for n in rock:
                    if (n[0] - 1, n[1]) in chamber:
                        break
                    new_rock.append([n[0] - 1, n[1]])
                else:
                    rock = new_rock
        else:
            if rock[-1][0] < 6:
                for n in rock:
                    if (n[0] + 1, n[1]) in chamber:
                        break
                    new_rock.append([n[0] + 1, n[1]])
                else:
                    rock = new_rock
        jet = (jet + 1) % len(jets)
        new_rock = []
        for n in rock:
            if (n[0], n[1] - 1) in chamber:
                for m in rock:
                    chamber.add((m[0], m[1]))
                rest = True
                highest = max([o[1] for o in rock] + [highest])
                break
            else:
                new_rock.append([n[0], n[1] - 1])
        else:
            rock = new_rock
print(highest)
