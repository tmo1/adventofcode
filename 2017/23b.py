# https://adventofcode.com/2017/day/23#part2
# This solution makes assumptions about the nature of the input program.
# It works for my input, but may or may not work for other input.

from math import sqrt

program, i, registers, total = [x.split() for x in open(0)], 0, {chr(x): 0 for x in range(97, 105)}, 0
prog_len, registers['a'] = len(program), 1
while i < 8:
    arg1 = registers[program[i][1]] if program[i][1].isalpha() else int(program[i][1])
    if len(program[i]) == 3:
        arg2 = registers[program[i][2]] if program[i][2].isalpha() else int(program[i][2])
    match program[i][0]:
        case 'set':
            registers[program[i][1]] = arg2
        case 'sub':
            registers[program[i][1]] -= arg2
        case 'mul':
            registers[program[i][1]] *= arg2
            total += 1
        case 'jnz':
            if arg1 != 0:
                i += arg2 - 1
    i += 1
for i in range(registers['b'], registers['c'] + 1, 17):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            registers['h'] += 1
            break
print(registers['h'])
