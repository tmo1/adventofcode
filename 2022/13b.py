# https://adventofcode.com/2022/day/13#part2

import sys
from functools import cmp_to_key

def parse(tokens):
    packets = []
    while tokens:
        token = tokens.pop()
        if token == ']':
            return packets
        if token != '':
            packets.append(parse(tokens) if token == '[' else int(token))


lines = []


while True:
    line = sys.stdin.readline()
    if not line:
        break
    if line == '\n':
        continue
    line = line.strip()
    i = 0
    while i < len(line):
        if line[i] == '[':
            line = line[:i + 1] + ',' + line[i + 1:]
            i += 1
        if line[i] == ']':
            line = line[:i] + ',' + line [i:]
            i += 1
        i += 1
    line = line.split(',')[1:]
    line.reverse()
    lines.append(parse(line))
lines.append([[2]])
lines.append([[6]])


def compare(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            return 0 if a == b else 1 if a < b else -1
        else:
            return compare([a], b)
    else:
        if isinstance(b, int):
            return compare(a, [b])
    j = 0
    while True:
        if j == len(a):
            return 0 if j == len(b) else 1
        if j == len(b):
            return -1
        c = compare(a[j], b[j])
        if c != 0:
            return c
        j += 1


lines.sort(key=cmp_to_key(compare), reverse=True)
decoder = 1
for i in range(len(lines)):
    if lines[i] == [[6]] or lines[i] == [[2]]:
        decoder *= i + 1
print(decoder)
