# https://adventofcode.com/2015/day/7#part2

import sys
rules = []
for line in sys.stdin:
    tokens = line.split()
    for i in range(len(tokens)):
        if tokens[i].isnumeric():
            tokens[i] = int(tokens[i])
    rules.append(list(tokens))
signals = {'b': 16076}


def signal(x):
    if x in signals:
        return signals[x]
    for rule in rules:
        if rule[-1] == x:
            if len(rule) == 3:
                result = rule[0] if isinstance(rule[0], int) else signal(rule[0])
                signals[rule[-1]] = result
                return result
            if len(rule) == 4:
                result = ~signal(rule[1]) & 65535
                signals[rule[-1]] = result
                return result
            op1 = rule[0] if isinstance(rule[0], int) else signal(rule[0])
            op2 = rule[2] if isinstance(rule[2], int) else signal(rule[2])
            if rule[1] == 'AND':
                result = op1 & op2
                signals[rule[-1]] = result
                return result
            if rule[1] == 'OR':
                result = op1 | op2
                signals[rule[-1]] = result
                return result
            if rule[1] == 'LSHIFT':
                result = (op1 << op2) & 65535
                signals[rule[-1]] = result
                return result
            if rule[1] == 'RSHIFT':
                result = op1 >> op2
                signals[rule[-1]] = result
                return result


print(signal('a'))
