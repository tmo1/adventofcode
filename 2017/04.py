# https://adventofcode.com/2017/day/4#part2

import sys

print(len([1 for line in sys.stdin if len(line.split()) == len(set(line.split()))]))
