# https://adventofcode.com/2022/day/6#part2

import sys

data = sys.stdin.readline()
for i in range(13, len(data)):
    if len(set(data[i - 13:i + 1])) == 14:
        print(i + 1)
        break
