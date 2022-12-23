# https://adventofcode.com/2015/day/25

import sys

words = sys.stdin.readline().split()
row = int(words[15].strip(','))
column = int(words[17].strip('.'))
n = ((row + column - 2) * (row + column - 1) // 2) + column - 1
code = 20151125
for i in range(n):
    code = (code * 252533) % 33554393
print(code)
