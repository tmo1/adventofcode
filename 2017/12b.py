# https://adventofcode.com/2017/day/12#part2

import sys

programs, groups, done = {}, set(), False
for line in sys.stdin:
    line = line.split()
    programs[line[0]] = {x.strip(',') for x in line[2:]}
while not done:
    done, new_programs = True, {}
    for program, connected_programs in programs.items():
        new_programs[program] = {x for x in connected_programs}
        for connected_program in connected_programs:
            if len(programs[connected_program] - connected_programs) != 0:
                new_programs[program] |= programs[connected_program]
                done = False
    programs = new_programs
for program, connected_programs in programs.items():
    for group in groups:
        if connected_programs == programs[group]:
            break
    else:
        groups.add(program)
print(len(groups))
