# https://adventofcode.com/2015/day/23

import sys

program = []
for line in sys.stdin:
    program.append(line.split())
registers = {'a': 0, 'b': 0}
i = 0
while i < len(program):
    if program[i][0] == 'hlf':
        registers[program[i][1]] //= 2
        i += 1
    elif program[i][0] == 'tpl':
        registers[program[i][1]] *= 3
        i += 1
    elif program[i][0] == 'inc':
        registers[program[i][1]] += 1
        i += 1
    elif program[i][0] == 'jmp':
        i += int(program[i][1])
    elif program[i][0] == 'jie':
        if registers[program[i][1][0]] % 2 == 0:
            i += int(program[i][2])
        else:
            i += 1
    else:
        if registers[program[i][1][0]] == 1:
            i += int(program[i][2])
        else:
            i += 1
print(registers['b'])
