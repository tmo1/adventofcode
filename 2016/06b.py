# https://adventofcode.com/2016/day/6#part2

import sys

letters = [{chr(n): 0 for n in range(97, 123)} for i in range(8)]
for line in sys.stdin:
    for count, char in enumerate(line.strip()):
        letters[count][char] += 1
letters = [{k: v for k, v in letters[i].items() if v > 0} for i in range(8)]
print(''.join([min(letters[n], key=letters[n].get) for n in range(8)]))
