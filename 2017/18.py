# https://adventofcode.com/2017/day/18

program, i, last_freq, registers = [x.split() for x in open(0)], 0, 0, {chr(x): 0 for x in range(97, 123)}
while True:
    arg1 = registers[program[i][1]] if program[i][1].isalpha() else int(program[i][1])
    if len(program[i]) == 3:
        arg2 = registers[program[i][2]] if program[i][2].isalpha() else int(program[i][2])
    match program[i][0]:
        case 'snd':
            last_freq = arg1
        case 'set':
            registers[program[i][1]] = arg2
        case 'add':
            registers[program[i][1]] += arg2
        case 'mul':
            registers[program[i][1]] *= arg2
        case 'mod':
            registers[program[i][1]] %= arg2
        case 'rcv':
            if arg1 != 0:
                print(last_freq)
                quit()
        case 'jgz':
            if arg1 > 0:
                i += arg2 - 1
    i += 1
