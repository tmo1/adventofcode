# https://adventofcode.com/2022/day/17#part2
# I couldn't figure this one out, and it took me a while even after reading
# https://www.reddit.com/r/adventofcode/comments/znykq2/2022_day_17_solutions/
# I finally coded the following solution based on this post:
# https://old.reddit.com/r/adventofcode/comments/znykq2/2022_day_17_solutions/j0wglja/

import copy
import sys

jets = sys.stdin.readline().strip()
rocks = [[[2, 0], [3, 0], [4, 0], [5, 0]], [[2, 1], [3, 1], [3, 2], [3, 0], [4, 1]],
         [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]], [[2, 0], [2, 1], [2, 2], [2, 3]], [[2, 0], [3, 0], [2, 1], [3, 1]]]
chamber = {(x, 0) for x in range(7)}
highest = 0
jet = 0
states = {}
total_rocks = 0
r = 0
cycle_found = False
while total_rocks < 1000000000000:
    rock = copy.deepcopy(rocks[r])
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
    total_rocks += 1
    if not cycle_found:
        state = []
        for i in range(7):
            state.append(max([x[1] for x in chamber if x[0] == i]))
        lowest = min(state)
        state = [x - lowest for x in state]
        state += [r, jet]
        state = tuple(state)
        if state in states:
            height_gain_in_cycle = highest - states[state][0]
            rocks_in_cycle = total_rocks - states[state][1]
            skipped_cycles = (1000000000000 - total_rocks) // rocks_in_cycle
            total_rocks += skipped_cycles * rocks_in_cycle
            cycle_found = True
        else:
            states[state] = [highest, total_rocks]
    r = (r + 1) % 5
print(highest + (skipped_cycles * height_gain_in_cycle))
