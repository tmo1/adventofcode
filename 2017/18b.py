# https://adventofcode.com/2017/day/18#part2

from collections import deque

program, i0, i1, registers0, registers1, deque0, deque1, running0, running1, total = [x.split() for x in open(0)], 0, 0, {chr(x): 0 for x in range(97, 123)}, {chr(x): 0 for x in range(97, 123)}, deque(), deque(), True, True, 0
registers1['p'], program_length = 1, len(program)


def do_instruction(i, registers, local_queue, remote_queue, prog_id):
    global total
    arg1 = registers[program[i][1]] if program[i][1].isalpha() else int(program[i][1])
    if len(program[i]) == 3:
        arg2 = registers[program[i][2]] if program[i][2].isalpha() else int(program[i][2])
    match program[i][0]:
        case 'snd':
            remote_queue.append(arg1)
            if prog_id == 1:
                total += 1
        case 'set':
            registers[program[i][1]] = arg2
        case 'add':
            registers[program[i][1]] += arg2
        case 'mul':
            registers[program[i][1]] *= arg2
        case 'mod':
            registers[program[i][1]] %= arg2
        case 'rcv':
            if local_queue:
                registers[program[i][1]] = local_queue.popleft()
            else:
                return i
        case 'jgz':
            if arg1 > 0:
                i += arg2 - 1
    i += 1
    return i


while running0 or running1:
    blocked = False
    if running0:
        new_i = do_instruction(i0, registers0, deque0, deque1, 0)
        if new_i < 0 or new_i >= program_length:
            running0 = False
        else:
            if new_i == i0:
                blocked = True
            else:
                i0 = new_i
    if running1:
        new_i = do_instruction(i1, registers1, deque1, deque0, 1)
        if new_i < 0 or new_i >= program_length:
            running1 = False
        else:
            if new_i == i0 and blocked is True:
                break
            i1 = new_i
print(total)
