# https://adventofcode.com/2022/day/2#part2

import sys

outcomes = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6, ('C', 'X'): 6,
            ('C', 'Y'): 0, ('C', 'Z'): 3}
shapes = {'X': 1, 'Y': 2, 'Z': 3}
win = {'A': 'Z', 'C': 'Y', 'B': 'X'}
lose = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
score = 0
for line in sys.stdin:
    signs = line.split()
    if signs[1] == 'X':
        play = win[signs[0]]
    elif signs[1] == 'Y':
        play = draw[signs[0]]
    else:
        play = lose[signs[0]]
    score += outcomes[(signs[0], play)] + shapes[play]
print(score)
