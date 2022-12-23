#! /usr/bin/python3

# https://adventofcode.com/2021/day/13#part2

import sys

dots = set()
for line in sys.stdin:
	if line == '\n':
		break
	(x, y) = line.split(',')
	(x, y) = int(x), int(y)
	dots.add((x, y))

for line in sys.stdin:
	instruction = line.split('=')
	(axis, fold) = instruction[0][-1], int(instruction[1])
	dots2 = set()
	if axis == 'y':
		for dot in dots:
			dots2.add((dot[0], (2 * fold) - dot[1]) if dot[1] > fold else dot)
	else:
		for dot in dots:
			dots2.add(((2 * fold) - dot[0], dot[1]) if dot[0] > fold else dot)
	dots = dots2
	
grid = [['.' for x in range(50)] for y in range(50)]
for dot in dots:
	grid[dot[1]][dot[0]] = '#'

for y in range(50):
	for x in range(50):
		print(grid[y][x], end='')
	print()

