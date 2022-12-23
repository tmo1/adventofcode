#! /usr/bin/python3

# https://adventofcode.com/2021/day/15
# this takes 25 seconds on my W550s for my puzzle input, so it must not
# be quite an optimum solution, according to:
# https://adventofcode.com/2021/about

import sys

grid = []
for line in sys.stdin:
	grid.append([int(c) for c in line[:-1]])
side = len(grid)

risks = {}
def calc_risk(x1, y1, x2, y2):
	global risks
	if ((x1, y1), (x2, y2)) in risks:
		return risks[((x1, y1), (x2, y2))]
	if x1 == x2:
		s = sum(grid[y][x1] for y in range(y1 + 1, y2 + 1))
		risks[(x1, y1), (x2, y2)] = s
		return s
	if y1 == y2:
		s = sum(grid[y1][x] for x in range(x1 + 1, x2 + 1))	
		risks[(x1, y1), (x2, y2)] = s
		return s
	x3 = x1 + ((x2 - x1) // 2)
	low = 1000000
	for y in range(y1, y2 + 1):
		r = calc_risk(x1, y1, x3, y) + calc_risk(x3 + 1, y, x2, y2) + grid[y][x3 + 1]
		if r < low:
			low = r
	risks[(x1, y1), (x2, y2)] = low
	return low
			
print(calc_risk(0, 0, side - 1, side - 1))
