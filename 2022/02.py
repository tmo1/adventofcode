# https://adventofcode.com/2022/day/2

import sys

outcomes = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6, ('C', 'X'): 6,
            ('C', 'Y'): 0, ('C', 'Z'): 3}
shapes = {'X': 1, 'Y': 2, 'Z': 3}
score = 0
for line in sys.stdin:
    signs = line.split()
    score += outcomes[(signs[0], signs[1])] + shapes[signs[1]]
print(score)
