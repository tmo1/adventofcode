#! /usr/bin/python3

# https://adventofcode.com/2021/day/5

import sys

points = {}
for line in sys.stdin:
	(a,b) = line.split('->')
	(x1, y1) = a.split(',')
	(x2, y2) = b.split(',')
	(x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
	if (x1 == x2):
		if y1 > y2:
			y1, y2 = y2, y1
		for y in range(y1, y2 + 1):
			if (x1, y) in points:
				points[(x1, y)] += 1
			else:
				points[(x1, y)] = 1
	if (y1 == y2):
		if x1 > x2:
			x1, x2 = x2, x1
		for x in range(x1, x2 + 1):
			if (x, y1) in points:
				points[(x, y1)] += 1
			else:
				points[(x, y1)] = 1

print(sum(1 for key in points.keys() if points[key] > 1))

