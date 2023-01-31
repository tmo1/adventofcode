# https://adventofcode.com/2017/day/16#part2

programs = [chr(x) for x in range(97, 113)]
initial_state, n, found_cycle = tuple(programs), 0, False
puzzle = open(0)
moves = [move for move in puzzle.readline().strip().split(',')]
while n < 1000000000:
    for dance_move in moves:
        move, dancers = dance_move[0], dance_move[1:]
        match move:
            case 's':
                programs = programs[-int(dancers):] + programs[:16 - int(dancers)]
            case 'x':
                dancers = dancers.split('/')
                a, b = int(dancers[0]), int(dancers[1])
                programs[a], programs[b] = programs[b], programs[a]
            case 'p':
                a, b = programs.index(dancers[0]), programs.index(dancers[2])
                programs[a], programs[b] = programs[b], programs[a]
    n += 1
    if not found_cycle and tuple(programs) == initial_state:
        found_cycle, n = True, 1000000000 - (1000000000 % n)
print(''.join(programs))
