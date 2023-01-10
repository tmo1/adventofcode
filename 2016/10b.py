# https://adventofcode.com/2016/day/10

import sys


def give(v, b):
    if b in bots:
        bots[b].add(v)
    else:
        bots[b] = {v}


def output(v, o):
    n = int(o)
    if n < 3 and outputs[n] is None:
        outputs[n] = v
        total = 1
        for x in outputs:
            if x is None:
                return
            total *= x
        print(total)
        quit()


bots, outputs = {}, [None for i in range(3)]
lines = [line.split() for line in sys.stdin]
i = 0
while True:
    line = lines[i]
    if line[0] == 'value':
        give(int(line[1]), line[5])
        lines.pop(i)
    else:
        bot, dest1, dest2 = line[1], line[6], line[11]
        if bot in bots and len(bots[bot]) == 2:
            low, high = min(bots[bot]), max(bots[bot])
            if line[5] == 'bot':
                give(low, dest1)
            else:
                output(low, dest1)
            if line[10] == 'bot':
                give(high, dest2)
            else:
                output(high, dest2)
        i = (i + 1) % len(lines)
