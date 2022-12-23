# https://adventofcode.com/2015/day/16#part2

import sys

tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
for line in sys.stdin:
    words = [(x.strip(',')) for x in line.split()]
    for i in range(2, 7, 2):
        word = words[i].strip(':')
        if word == 'cats' or word == 'trees':
            if not tape[word] < int(words[i + 1]):
                break
        elif word == 'pomeranians' or word == 'goldfish':
            if not tape[word] > int(words[i + 1]):
                break
        else:
            if not tape[word] == int(words[i + 1]):
                break
    else:
        print(words[1].strip(':'))
