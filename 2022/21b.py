# https://adventofcode.com/2022/day/21#part2
# This solution assumes that all monkey numbers can be easily reduced to the algebraic form 'a + bx', where 'x' is
# 'humn's number (which is the case for my input).

import sys

monkeys = {}
for line in sys.stdin:
    line = line.split()
    monkeys[line[0][:-1]] = [[int(x), 0] if x.isdigit() else x for x in line[1:]]
monkeys['humn'] = [[0, 1]]
monkeys['root'][1] = '-'


def number(monkey):
    n = monkeys[monkey]
    if len(n) == 1:
        return n[0]
    a = number(n[0]) if isinstance(n[0], str) else n[0]
    b = number(n[2]) if isinstance(n[2], str) else n[2]
    match n[1]:
        case '+':
            n = [a[0] + b[0], a[1] + b[1]]
        case '-':
            n = [a[0] - b[0], a[1] - b[1]]
        case '*':
            if a[1] != 0 and b[1] != 0:
                print('error: higher order polynomial in \'humn\' found!')
                quit()
            n = [a[0] * b[0], a[1] * b[0] + a[0] * b[1]]
        case '/':
            if b[1] != 0:
                print('error: division by \'humn\'!')
                quit()
            n = [a[0] / b[0], a[1] / b[0]]
    return n

root = number('root')
print(round(-root[0] / root[1]))
