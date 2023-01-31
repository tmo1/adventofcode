# https://adventofcode.com/2017/day/4#part2

import sys
from collections import defaultdict

valid = 0
for line in sys.stdin:
    line, prev_letters, invalid = line.split(), [], False
    for word in line:
        letters = defaultdict(lambda: 0)
        for letter in word:
            letters[letter] += 1
        for prev in prev_letters:
            if letters == prev:
                invalid = True
                break
        if invalid:
            break
        prev_letters.append(letters)
    else:
        valid += 1
print(valid)
