# https://adventofcode.com/2022/day/21

import sys

monkeys = {}
for line in sys.stdin:
    line = line.split()
    monkeys[line[0][:-1]] = int(line[1]) if len(line) == 2 else line[1:]


def number(monkey):
    n = monkeys[monkey]
    if isinstance(n, int):
        return n
    a, b, = number(n[0]), number(n[2])
    match n[1]:
        case '+':
            n = a + b
        case '-':
            n = a - b
        case '*':
            n = a * b
        case '/':
            n = a // b
    monkeys[monkey] = n
    return n


print(number('root'))
