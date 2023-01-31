# https://adventofcode.com/2017/day/8#part2

import sys
from collections import defaultdict

registers, highest = defaultdict(lambda: 0), 0
for line in sys.stdin:
    line = line.split()
    match line[5]:
        case '>':
            if not registers[line[4]] > int(line[6]):
                continue
        case '<':
            if not registers[line[4]] < int(line[6]):
                continue
        case '>=':
            if not registers[line[4]] >= int(line[6]):
                continue
        case '<=':
            if not registers[line[4]] <= int(line[6]):
                continue
        case '==':
            if not registers[line[4]] == int(line[6]):
                continue
        case '!=':
            if not registers[line[4]] != int(line[6]):
                continue
    registers[line[0]] += int(line[2]) if line[1] == 'inc' else -int(line[2])
    highest = max(highest, registers[line[0]])
print(highest)
