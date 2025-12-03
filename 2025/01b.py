# https://adventofcode.com/2025/day/1#part2
from itertools import combinations

position, combination = 50, 0
for line in open(0):
    n = int(line[1:])
    if line[0] == 'R': position, combination = (position + n) % 100, combination + (position + n) // 100
    else: position, combination = (position - n) % 100, combination + abs(position - n) // 100 + (1 if position > 0 else 0) if position - n <= 0 else combination
print(combination)
