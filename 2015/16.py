# https://adventofcode.com/2015/day/16

import sys

tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
for line in sys.stdin:
    words = [(x.strip(',')) for x in line.split()]
    for i in range(2, 7, 2):
        if not tape[words[i].strip(':')] == int(words[i + 1]):
            break
    else:
        print(words[1].strip(':'))
