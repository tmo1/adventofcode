# https://adventofcode.com/2015/day/19#part2
# needed help from https://eddmann.com/posts/advent-of-code-2015-day-19-medicine-for-rudolph/
# this is an optimized version of 19b.py - see this thread for background:
# https://old.reddit.com/r/adventofcode/comments/13lfxxq/2015_day_19_part_1_2_python_deterministic_solution/

import sys

replacements = []
for line in sys.stdin:
    if line == "\n":
        break
    words = line.split()
    replacements.append((words[0], words[2]))
molecules = {sys.stdin.readline().strip()}
molecules_seen = set()
steps = 1
while True:
    molecule = min(molecules, key=len)
    for replacement in replacements:
        for i in range(len(molecule)):
            for j in range(len(replacement[1])):
                if (i + j == len(molecule)) or (not molecule[i + j] == replacement[1][j]):
                    break
            else:
                new_molecule = molecule[:i] + replacement[0] + molecule[i + len(replacement[1]):]
                if new_molecule == 'e':
                    print(steps)
                    exit()
                if molecule not in molecules_seen:
                    molecules.add(new_molecule)
    molecules.remove(molecule)
    molecules_seen.add(molecule)
    steps += 1
