# https://adventofcode.com/2015/day/8

import sys
mem = code = 0
for line in sys.stdin:
    c = 0
    i = 1
    while not line[i] == '"':
        if line[i] == '\\':
            if line[i + 1] == 'x':
                i += 4
            else:
                i += 2
        else:
            i += 1
        c += 1
    mem += c
    code += len(line) - 1
print(code - mem)
