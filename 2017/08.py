# https://adventofcode.com/2017/day/8

import sys
from collections import defaultdict

registers = defaultdict(lambda: 0)
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
print(max(registers.values()))
