# https://adventofcode.com/2025/day/6

from math import prod
lines = [line.split() for line in open(0)]
print(sum([sum([int(lines[j][column]) for j in range(len(lines) - 1)]) if lines[-1][column] == '+' else prod([int(lines[j][column]) for j in range(len(lines) - 1)]) for column in range(len(lines[0]))]))
