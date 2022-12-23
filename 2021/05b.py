#! /usr/bin/python3

# https://adventofcode.com/2021/day/5#part2

import sys

points = {}
for line in sys.stdin:
	(a,b) = line.split('->')
	(x1, y1) = a.split(',')
	(x2, y2) = b.split(',')
	(x1, y1, x2, y2) = (int(x1), int(y1), int(x2), int(y2))
	if x2 > x1:
		xstep = 1
	elif x1 > x2:
		xstep = -1
	else:
		xstep = 0
	if y2 > y1:
		ystep = 1
	elif y1 > y2:
		ystep = -1
	else:
		ystep = 0
	while 1:
		if (x1, y1) in points:
			points[(x1, y1)] += 1
		else:
			points[(x1, y1)] = 1
		if x1 == x2 and y1 == y2:
			break
		x1 += xstep
		y1 += ystep
			
print(sum(1 for key in points.keys() if points[key] > 1))

