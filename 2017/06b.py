# https://adventofcode.com/2017/day/6#part2

import sys

banks, states, redistributions = [int(x) for x in sys.stdin.readline().split()], {}, 0
while True:
    state = tuple(banks)
    if state in states:
        print(redistributions - states[state])
        quit()
    states[state] = redistributions
    i = banks.index(max(banks))
    n = banks[i]
    banks[i] = 0
    for j in range(i + 1, i + 1 + n):
        banks[j % 16] += 1
    redistributions += 1
