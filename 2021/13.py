#! /usr/bin/python3

# https://adventofcode.com/2021/day/13

import sys

dots = set()
for line in sys.stdin:
	if line == '\n':
		break
	(x, y) = line.split(',')
	(x, y) = int(x), int(y)
	dots.add((x, y))

line = sys.stdin.readline().split('=')
(axis, fold) = line[0][-1], int(line[1])
dots2 = set()

if axis == 'y':
	for dot in dots:
		dots2.add((dot[0], (2 * fold) - dot[1]) if dot[1] > fold else dot)
else:
	for dot in dots:
		dots2.add(((2 * fold) - dot[0], dot[1]) if dot[0] > fold else dot)

print(len(dots2))

	
