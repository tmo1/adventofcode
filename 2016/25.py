# https://adventofcode.com/2016/day/25

# This code could conceivably yield a false positive if the input contains 'tgl' instructions (my input does not),
# since the state tuples only include the registers and instruction pointer, not the program code itself.
# Additionally, it could fail to terminate at all if a correct clock sequence is encountered without a return to a
# previous program state (e.g., if one of the registers is incremented for each clock tick).
# Furthermore, it only tracks the state of registers a-d (the only ones utilized in at least my input).

import sys

registers, program, states, n = [0 for i in range(26)], [line.split() for line in sys.stdin], {}, 0
while True:
    i, output, registers[0] = 0, [], n
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
            case 'out':
                output.append(registers[ord(line[1]) - 97] if line[1].isalpha() else int(line[1]))
                if output[-1] != (len(output) - 1) % 2:
                    break
                state = (registers[0], registers[1], registers[2], registers[3], i)
                if states.get(state, -1) == output[-1]:
                    print(n)
                    quit()
                states[state] = output[-1]
            case 'tgl':
                x = (registers[ord(line[1]) - 97] if line[1].isalpha() else int(line[1])) + i
                if 0 <= x < len(program):
                    if len(program[x]) == 2:
                        program[x][0] = 'dec' if program[x][0] == 'inc' else 'inc'
                    else:
                        program[x][0] = 'cpy' if program[x][0] == 'jnz' else 'jnz'
        i += 1
    n += 1
