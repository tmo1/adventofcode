# https://adventofcode.com/2016/day/4

import functools
import sys

n = 0
for line in sys.stdin:
    letters = {chr(x): 0 for x in range(97, 123)}
    line = line.split('-')
    for word in line[:-1]:
        for letter in word:
            letters[letter] += 1
    if ''.join(sorted(letters, key=functools.cmp_to_key(
            lambda a, b: 1 if (letters[a] > letters[b]) or (letters[a] == letters[b] and a < b) else -1), reverse=True)[
               :5]) == line[-1][-7:-2]:
        n += int(line[-1][:3])
print(n)
