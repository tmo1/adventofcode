# https://adventofcode.com/2016/day/23

import sys

registers = [0 for i in range(26)]
registers[0] = 7
program, i = [line.split() for line in sys.stdin], 0
while i < len(program):
    line = program[i]
    match line[0]:
        case 'cpy':
            if not line[2].isdigit():
                registers[ord(line[2]) - 97] = registers[ord(line[1]) - 97] if line[1].isalpha() else int(line[1])
        case 'inc':
            registers[ord(line[1]) - 97] += 1
        case 'dec':
            registers[ord(line[1]) - 97] -= 1
        case 'jnz':
            if (registers[ord(line[1]) - 97] if line[1].isalpha() else int(line[1])) != 0:
                i += (registers[ord(line[2]) - 97] if line[2].isalpha() else int(line[2])) - 1
        case 'tgl':
            x = (registers[ord(line[1]) - 97] if line[1].isalpha() else int(line[1])) + i
            if 0 <= x < len(program):
                if len(program[x]) == 2:
                    program[x][0] = 'dec' if program[x][0] == 'inc' else 'inc'
                else:
                    program[x][0] = 'cpy' if program[x][0] == 'jnz' else 'jnz'
    i += 1
print(registers[0])
