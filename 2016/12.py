# https://adventofcode.com/2016/day/12
# both parts - see comment below
# this takes a bit over 15s for part 2 for my input on my W550s

import sys

registers = [0 for i in range(26)]
# comment out the following line for part 1, leave uncommented for part 2
registers[2] = 1
program, i = [line.split() for line in sys.stdin], 0
while i < len(program):
    line = program[i]
    match line[0]:
        case 'cpy':
            registers[ord(line[2]) - 97] = int(line[1]) if line[1][0].isdigit() else registers[ord(line[1]) - 97]
        case 'inc':
            registers[ord(line[1]) - 97] += 1
        case 'dec':
            registers[ord(line[1]) - 97] -= 1
        case 'jnz':
            if (int(line[1]) if line[1][0].isdigit() else registers[ord(line[1]) - 97]) != 0:
                i += int(line[2]) - 1
    i += 1
print(registers[0])
