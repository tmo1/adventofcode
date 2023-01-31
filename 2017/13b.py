# https://adventofcode.com/2017/day/13#part2

import sys

zeros, n = set(), 0
for line in sys.stdin:
    line = line.split(': ')
    zeros.add((int(line[0]), 2 * (int(line[1]) - 1)))
while True:
    for zero in zeros:
        if (n + zero[0]) % zero[1] == 0:
            break
    else:
        print(n)
        quit()
    n += 1
