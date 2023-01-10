# https://adventofcode.com/2016/day/10

import sys


def give(v, b):
    if b in bots:
        if bots[b] | {v} == {61, 17}:
            print(b)
            quit()
        bots[b].add(v)
    else:
        bots[b] = {v}


bots = {}
lines = [line.split() for line in sys.stdin]
i = 0
while True:
    line = lines[i]
    if line[0] == 'value':
        give(int(line[1]), line[5])
        lines.pop(i)
    else:
        bot = line[1]
        if bot in bots and len(bots[bot]) == 2:
            if line[5] == 'bot':
                give(min(bots[bot]), line[6])
            if line[10] == 'bot':
                give(max(bots[bot]), line[11])
        i = (i + 1) % len(lines)
