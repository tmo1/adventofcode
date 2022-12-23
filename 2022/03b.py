# https://adventofcode.com/2022/day/3#part2

import sys

priorities = 0
while True:
    one = sys.stdin.readline().strip()
    if not one:
        break
    two = sys.stdin.readline().strip()
    three = sys.stdin.readline().strip()
    item = ord(({*one} & {*two} & {*three}).pop()) - 38
    if item > 52:
        item -= 58
    priorities += item
print(priorities)
