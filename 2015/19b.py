# https://adventofcode.com/2015/day/19#part2
# needed help from https://eddmann.com/posts/advent-of-code-2015-day-19-medicine-for-rudolph/

import sys

replacements = []
for line in sys.stdin:
    if line == "\n":
        break
    words = line.split()
    replacements.append((words[0], words[2]))
molecules = {sys.stdin.readline().strip(): 0}
steps = 0
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
                    print(molecules[molecule] + 1)
                    exit()
                molecules[new_molecule] = molecules[molecule] + 1
    molecules.pop(molecule)
