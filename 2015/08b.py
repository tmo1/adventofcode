# https://adventofcode.com/2015/day/8#part2

import sys
enc = code = 0
for line in sys.stdin:
    c = 2
    for x in line.strip():
        if x == '\\' or x == '"':
            c += 2
        else:
            c += 1
    enc += c
    code += len(line) - 1
print(enc - code)
