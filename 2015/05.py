# https://adventofcode.com/2015/day/5

import sys
nice = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
bad = {'ab', 'cd', 'pq', 'xy'}
for line in sys.stdin:
    v = 0
    prev = ''
    double = False
    b = False
    for letter in line:
        if (prev + letter) in bad:
            b = True
            break
        if letter in vowels:
            v += 1
        if letter == prev:
            double = True
        prev = letter
    if v > 2 and double and not b:
        nice += 1
print(nice)
