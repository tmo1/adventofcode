# https://adventofcode.com/2016/day/7#part2

import sys

n = 0


def ssl():
    global n
    for x in sequences['aba']:
        for y in sequences['bab']:
            if x[0] == y[1] and x[1] == y[0]:
                n += 1
                return


for line in sys.stdin:
    prev, net, sequences = [], 'aba', {'aba': set(), 'bab': set()}
    for char in line.strip():
        match char:
            case '[':
                prev = []
                net = 'bab'
            case ']':
                prev = []
                net = 'aba'
            case other:
                prev.append(char)
                if len(prev) == 4:
                    prev.pop(0)
                if len(prev) == 3 and prev[0] == char and prev[0] != prev[1]:
                    sequences[net].add(''.join(prev))
    ssl()
print(n)
