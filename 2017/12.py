# https://adventofcode.com/2017/day/12

import sys

programs = {}
for line in sys.stdin:
    line = line.split()
    programs[line[0]] = {x.strip(',') for x in line[2:]}
done = False
while not done:
    done, new_programs = True, {}
    for program, connected_programs in programs.items():
        new_programs[program] = {x for x in connected_programs}
        for connected_program in connected_programs:
            if len(programs[connected_program] - connected_programs) != 0:
                new_programs[program] |= programs[connected_program]
                done = False
    programs = new_programs
print(len(programs['0']))
