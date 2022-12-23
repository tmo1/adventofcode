# https://adventofcode.com/2015/day/19

import sys

replacements = []
new_molecules = set()
for line in sys.stdin:
    if line == "\n":
        break
    words = line.split()
    replacements.append((words[0], words[2]))
molecule = sys.stdin.readline().strip()
for replacement in replacements:
    for i in range(len(molecule)):
        for j in range(len(replacement[0])):
            if (i + j == len(molecule)) or (not molecule[i + j] == replacement[0][j]):
                break
        else:
            new_molecules.add(molecule[:i] + replacement[1] + molecule[i + len(replacement[0]):])
print(len(new_molecules))
