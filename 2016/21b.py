# https://adventofcode.com/2016/day/21#part2

import sys

letters, p, operations = set(list('abcdefgh')), list('fbgdceah'), [line.split() for line in sys.stdin]


def passwords(password, remaining):
    if remaining:
        for letter in remaining:
            passwords(password + [letter], remaining - {letter})
        return
    unscrambled = [letter for letter in password]
    for operation in operations:
        match operation[0]:
            case 'swap':
                if operation[1] == 'position':
                    x, y = int(operation[2]), int(operation[5])
                else:
                    x, y = password.index(operation[2]), password.index(operation[5])
                password[x], password[y] = password[y], password[x]
            case 'rotate':
                match operation[1]:
                    case 'right':
                        password = password[-int(operation[2]):] + password[:-int(operation[2])]
                    case 'left':
                        password = password[int(operation[2]):] + password[:int(operation[2])]
                    case other:
                        n = password.index(operation[6]) + 1
                        if n > 4:
                            n += 1
                        n %= len(password)
                        password = password[-n:] + password[:-n]
            case 'reverse':
                password = password[:int(operation[2])] + list(reversed(password[int(operation[2]):int(operation[4]) + 1])) + password[int(operation[4]) + 1:]
            case 'move':
                x = password.pop(int(operation[2]))
                password.insert(int(operation[5]), x)
    if password == p:
        print(''.join(unscrambled))
        quit()


passwords([], letters)
