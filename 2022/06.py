# https://adventofcode.com/2022/day/6

import sys

data = sys.stdin.readline()
for i in range(3, len(data)):
    if len(set(data[i - 3:i + 1])) == 4:
        print(i + 1)
        break
