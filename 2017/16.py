# https://adventofcode.com/2017/day/16

programs = [chr(x) for x in range(97, 113)]
for dance_move in open(0).readline().strip().split(','):
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
print(''.join(programs))
