# https://adventofcode.com/2024/day/3#part2

import re

program = open(0).read()
control = {n.start(): True if n.group()[2] == '(' else False for n in re.finditer(r"do(n't)?\(\)", program)} | {
    -1: True}
print(sum([int(match[1]) * int(match[2]) for match in re.finditer(r"mul\((\d+),(\d+)\)", program) if
           control[max([c for c in control.keys() if c < match.start()])]]))
