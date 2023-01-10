# https://adventofcode.com/2016/day/23#part2

import sys

registers = [0 for i in range(26)]
registers[0] = 12
program, i = [line.split() for line in sys.stdin], 0
while i < len(program):
    if i < len(program) - 2 and program[i + 2][0] == 'jnz' and program[i + 2][2] == '-2' and (
            program[i][0] == 'inc' or program[i][0] == 'dec') and (
            program[i + 1][0] == 'inc' or program[i + 1][0] == 'dec'):
        # unroll addition loop
        loop_counter = program[i + 2][1]
        loop_iterations = abs(registers[ord(loop_counter) - 97])
        registers[ord(loop_counter) - 97] = 0
        for j in [i, i + 1]:
            if program[j][1] != loop_counter:
                registers[ord(program[j][1]) - 97] += loop_iterations if program[j][0] == 'inc' else - loop_iterations
        i += 3
        continue
    if i < len(program) - 5 and program[i][0] == 'cpy' and program[i][2] == program[i + 3][1] and program[i + 3][
        0] == 'jnz' and program[i + 3][2] == '-2' and (program[i + 1][0] == 'inc' or program[i + 1][0] == 'dec') and (
            program[i + 2][0] == 'inc' or program[i + 2][0] == 'dec') and (
            program[i + 4][0] == 'inc' or program[i + 4][0] == 'dec') and program[i + 4][1] == program[i + 5][1]:
        # unroll multiplication loop
        inner_loop_counter = program[i + 3][1]
        inner_loop_iterations = abs(registers[ord(program[i][1]) - 97] if program[i][1].isalpha() else int(program[i][1]))
        outer_loop_counter = program[i + 5][1]
        outer_loop_iterations = abs(registers[ord(program[i + 5][1]) - 97])
        n = inner_loop_iterations * outer_loop_iterations
        registers[ord(inner_loop_counter) - 97] = 0
        registers[ord(outer_loop_counter) - 97] = 0
        for j in [i + 1, i + 2]:
            if program[j][1] != inner_loop_counter:
                registers[ord(program[j][1]) - 97] += n if program[j][0] == 'inc' else -n
        i += 6
        continue
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
