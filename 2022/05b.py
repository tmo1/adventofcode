# https://adventofcode.com/2022/day/5#part2

import sys

stacks = [[] for i in range(100)]
while True:
    line = sys.stdin.readline()
    if line[1] == '1':
        break
    for i in range(100):
        if i * 4 >= len(line):
            break
        if line[i * 4] != '[':
            continue
        stacks[i].append(line[((i * 4) + 1)])
line = sys.stdin.readline()
for stack in stacks:
    stack.reverse()
for line in sys.stdin:
    line = line.split()
    crates = stacks[int(line[3]) - 1][-int(line[1]):]
    stacks[int(line[3]) - 1] = stacks[int(line[3]) - 1][:-int(line[1])]
    stacks[int(line[5]) - 1] += crates
print(''.join([stacks[i][-1] for i in range(100) if len(stacks[i]) > 0]))
