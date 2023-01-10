# https://adventofcode.com/2016/day/21

import sys

password = list('abcdefgh')
for line in sys.stdin:
    line = line.split()
    match line[0]:
        case 'swap':
            if line[1] == 'position':
                x, y = int(line[2]), int(line[5])
            else:
                x, y = password.index(line[2]), password.index(line[5])
            password[x], password[y] = password[y], password[x]
        case 'rotate':
            match line[1]:
                case 'right':
                    password = password[-int(line[2]):] + password[:-int(line[2])]
                case 'left':
                    password = password[int(line[2]):] + password[:int(line[2])]
                case other:
                    n = password.index(line[6]) + 1
                    if n > 4:
                        n += 1
                    n %= len(password)
                    password = password[-n:] + password[:-n]
        case 'reverse':
            password = password[:int(line[2])] + list(reversed(password[int(line[2]):int(line[4]) + 1])) + password[int(line[4]) + 1:]
        case 'move':
            x = password.pop(int(line[2]))
            password.insert(int(line[5]), x)
print(''.join(password))
