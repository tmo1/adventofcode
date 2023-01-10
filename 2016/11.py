# https://adventofcode.com/2016/day/11
# BFS - takes about 1m46s for my input on my W550s

import sys

floors, states = [set() for i in range(4)], {}
for count, line in enumerate(sys.stdin):
    line = line.split()
    i = 0
    if line[4] == 'nothing':
        continue
    while line[i] != 'a':
        i += 1
    while i < len(line):
        if line[i] == 'and':
            i += 1
        if line[i + 2][:3] == 'mic':
            material = line[i + 1][:-11]
            floors[count].add((material, 'm'))
        else:
            material = line[i + 1]
            floors[count].add((material, 'g'))
        i += 3
total = len([item for x in floors for item in x])


def safe(f, first_floor):
    for j in [first_floor, first_floor + 1]:
        for item in f[j]:
            if item[1] == 'm' and (item[0], 'g') not in f[j] and sum([1 for x in f[j] if x[1] == 'g']) > 0:
                return False
    return True


def elevator(f, e, turns, min_floor):
    if turns == 0:
        if len(f[3]) == total:
            print(i)
            quit()
        return
    if turns == 1 and e == 0:
        return
    global states
    state = tuple([tuple(sorted(x)) for x in f] + [e])
    states[state] = turns
    for x in f[e]:
        for y in f[e]:
            cargo = {x, y}
            floors[e] -= cargo
            if e < 3:
                floors[e + 1] |= cargo
                t = tuple([tuple(sorted(x)) for x in floors] + [e + 1])
                if safe(floors, e) and (t not in states or states[t] < turns - 1):
                    elevator(floors, e + 1, turns - 1,
                             min_floor + 1 if e == min_floor and len(floors[e]) == 0 else min_floor)
                floors[e + 1] -= cargo
            if e > 0 and e > min_floor:
                floors[e - 1] |= cargo
                t = tuple([tuple(sorted(x)) for x in floors] + [e - 1])
                if safe(floors, e - 1) and (t not in states or states[t] < turns - 1):
                    elevator(floors, e - 1, turns - 1, min_floor)
                floors[e - 1] -= cargo
            floors[e] |= cargo


i = 3
while True:
    print(i)
    elevator(floors, 0, i, 0)
    i += 2
