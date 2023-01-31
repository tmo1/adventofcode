# https://adventofcode.com/2017/day/6

import sys

banks, states, redistributions = [int(x) for x in sys.stdin.readline().split()], set(), 0
while True:
    state = tuple(banks)
    if state in states:
        print(redistributions)
        quit()
    states.add(state)
    i = banks.index(max(banks))
    n = banks[i]
    banks[i] = 0
    for j in range(i + 1, i + 1 + n):
        banks[j % 16] += 1
    redistributions += 1
