#! /usr/bin/python3

# https://adventofcode.com/2021/day/9#part2

import sys
import copy
			
def extend(x, y, grid):
	grid[x][y] = -1
	for i in range(-1, 2):
		if x + i < 0 or x + i >= len(grid):
			continue
		for j in range(-1, 2):
			if i != 0 and j != 0:
				continue
			if y + j < 0 or y + j >= len(grid[0]):
				continue
			if grid[x + i][y + j] == 9 or grid[x + i][y + j] == -1:
				continue
			extend(x + i, y + j, grid)

total = 0
vents = []
basins = []
for line in sys.stdin:
	points = list(line.strip())
	nums = []
	for point in points:
		nums.append(int(point))
	vents.append(nums)
for i in range(len(vents)):
	for j in range(len(vents[0])):
		low = 1
		for k in range(-1, 2):
			if i + k < 0 or i + k >= len(vents):
				continue
			for l in range (-1, 2):
				if j + l < 0 or j + l >= len(vents[0]):
					continue
				if k == 0 and l == 0:
					continue
				if vents[i + k][j + l] < vents[i][j]:
					low = 0
					break
		if low == 1:
			grid = copy.deepcopy(vents)
			extend(i, j, grid)
			size = 0
			for line in grid:
				for point in line:
					if point == -1:
						size += 1
			basins.append(size)

basins.sort(reverse=True)
n = 1
for basin in basins[:3]:
	n *= basin
print(n)
